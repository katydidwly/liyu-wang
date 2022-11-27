import sys
import time
import numpy as np
from PyQt5 import QtCore, Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QAbstractItemView, QMenu, QCheckBox, QTableWidgetItem
import gui
import serial
from polyglot_turtle import PolyglotTurtleXiao, CommandExecutionFailedException, I2cClockRate
import serial.tools.list_ports

class MyThread(QtCore.QThread):
    trigger = QtCore.pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def run(self):
        while True:
            self.trigger.emit(Mywindow.work())


class Mywindow(QMainWindow, gui.Ui_MainWindow):
    def __init__(self):
        super(Mywindow, self).__init__()
        self.setupUi(self)
        self.radioButton.toggled.connect(self.mode_switch)
        self.radioButton_2.toggled.connect(self.mode_switch)
        self.radioButton_3.toggled.connect(self.mode_switch)
        self.frame.setVisible(False)
        self.frame_4.setVisible(False)
        self.ui_init()
        self.thread = MyThread()
        self.pushButton_4.clicked.connect(self.thread.start)
        self.pushButton_4.clicked.connect(self.connect)
        self.pushButton_5.clicked.connect(self.set_ReferenceWeight)
        self.pushButton_2.clicked.connect(self.tare)
        self.pushButton_14.clicked.connect(self.tare)
        self.pushButton_6.clicked.connect(self.tare)
        self.pushButton_8.clicked.connect(self.count)
        self.thread.trigger.connect(self.data_rec)
        self.weight = None
        self.weight_tare = 0
        self.ReferenceWeight = 0
        self.pushButton.clicked.connect(self.demo)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.customContextMenuRequested.connect(self.tableWidget_VTest_menu)
        self.data_list = []
        self.math = None
        self.dial.valueChanged.connect(self.backlight)
        self.serial = None
        self.doubleSpinBox.valueChanged.connect(self.mode_3_data)
        self.doubleSpinBox_2.valueChanged.connect(self.mode_3_data)

    def mode_3_data(self):
        self.data_write('w_max:{}'.format(self.doubleSpinBox.value()))
        self.data_write('w_min:{}'.format(self.doubleSpinBox_2.value()))

    def work_mode(self, value):
        # gui main work function, through the selected mode in the lcd screen to display the corresponding data
        if self.math is not None:
            if self.radioButton.isChecked():
                self.lcdNumber.display(str(value + self.weight_tare))
                pass
            elif self.radioButton_2.isChecked():
                if self.ReferenceWeight != 0 and self.weight is not None:
                    w_value = (value + self.weight_tare) / self.ReferenceWeight
                    str_dis = str(round(w_value, 1)) + '-' + str(value + self.weight_tare) + '-' + str(self.ReferenceWeight)
                    self.lcdNumber.display(str_dis)
                else:
                    self.lcdNumber.display(str(value + self.weight_tare))
                pass
            elif self.radioButton_3.isChecked():
                w_max = self.doubleSpinBox.value()
                w_min = self.doubleSpinBox_2.value()
                if w_min <= value + self.weight_tare <= w_max:
                    self.lcdNumber.display('P' + '-' + str(value + self.weight_tare))
                else:
                    self.lcdNumber.display('F' + '-' + str(value + self.weight_tare))
                pass

    def set_ReferenceWeight(self):
        # set the ReferenceWeight
        self.ReferenceWeight = self.weight + self.weight_tare
        self.data_write('ReferenceWeight:{}'.format(self.ReferenceWeight))

    def backlight(self):
        # Backlight function Sends backlight data to the port
        self.data_write('backlight:{}'.format(self.dial.value()))

    def tare(self):
        # The reset function
        if self.math is not None:
            self.weight_tare = - self.weight

    def list_Refresh(self):
        # Refresh the list in real time
        rowlength = self.tableWidget.rowCount()
        for i in range(0, rowlength):
            self.tableWidget.removeRow(0)
        for i in range(len(self.data_list)):
            self.tableWidget.insertRow(i)
            self.tableWidget.setItem(i, 0, QTableWidgetItem(str(self.data_list[i][0])))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(str(self.data_list[i][1])))
            self.tableWidget.setCellWidget(i, 2, QCheckBox())
        self.tableWidget.resizeRowsToContents()
        self.tableWidget.resizeColumnsToContents()

    def count(self):
        # Insert data into the list
        if self.textBrowser.toPlainText() != '':
            self.data_list.append([self.spinBox.value(), int(self.textBrowser.toPlainText().split('=')[1])])
            self.list_Refresh()
            pass

    def tableWidget_VTest_menu(self, pos):
        # Add a right-click menu for the list
        menu = QMenu()
        item1 = menu.addAction(u"Delete")
        action = menu.exec_(self.tableWidget.mapToGlobal(pos))
        if action == item1:
            if self.tableWidget.currentRow() >= 0:
                del self.data_list[self.tableWidget.currentRow()]
                self.list_Refresh()
                pass

    def demo(self):
        # Calculate the coefficients for the data selected in the list
        data_math = [[], []]
        if self.tableWidget.rowCount() > 0:
            for i in range(self.tableWidget.rowCount()):
                if self.tableWidget.cellWidget(i, 2).isChecked():
                    data_math[0].append(self.data_list[i][0])
                    data_math[1].append(self.data_list[i][1])
            self.textBrowser_2.append(str(data_math))
            x = data_math[0]
            y = data_math[1]
            self.math = np.polyfit(x, y, 1)
            self.textBrowser_2.append(str(self.math))


    def data_rec(self, ADC_str):
        # Passes ADC data to the interface
        self.textBrowser.setText(ADC_str)

    def convert_ADC_to_weight(self, ADC_reading):
        # The ADC data were converted to the actual weight by the first equation
        if self.math is None:
            return "Err"
        else:
            weight_reading = float((ADC_reading - self.math[1]) / self.math[0])
            return round(weight_reading, 1)

    def twos_comp(self, val, bits):
        """compute the 2's complement of int value val"""
        if (val & (1 << (bits - 1))) != 0:  # if sign bit is set e.g., 8bit: 128-255
            val = val - (1 << bits)  # compute negative value
        return val

    def work(self):
        i = 0
        pt = PolyglotTurtleXiao()
        I2C_NAU7802_ADDRESS = 0x2A
        pt.i2c_exchange(I2C_NAU7802_ADDRESS, bytes([0x00, 0x01]))  # clears all all the registers in the ADC
        pt.i2c_exchange(I2C_NAU7802_ADDRESS, bytes([0x00, 0x27]))  # enter normal operating mode
        time.sleep(2.0 * 10 ** -6)  # sleep for 2us for the PWRUP-bit to be set to 1
        pt.i2c_exchange(I2C_NAU7802_ADDRESS, bytes([0x00, 0xBE]))  # set CS, CR, PUR, PUA, and PUD to 1
        pt.i2c_exchange(I2C_NAU7802_ADDRESS, bytes([0x01, 0x27]))  # set the gain to x128
        pt.i2c_exchange(I2C_NAU7802_ADDRESS, bytes([0x11, 0x01]))
        pt.i2c_exchange(I2C_NAU7802_ADDRESS, bytes([0x1B, 0x40]))

        ADC_ready = '0xbe'  # hex string output when ADC is ready to be read
        # read what's inside the  PU_CTRL register as hex
        PU_CTRL_REGISTER = [hex(x) for x in pt.i2c_exchange(I2C_NAU7802_ADDRESS, bytes([0x00]), read_size=1)]

        while 1:
            if PU_CTRL_REGISTER[0] == ADC_ready:
                i += 1
                ADC_REGISTER = [int(x) for x in pt.i2c_exchange(I2C_NAU7802_ADDRESS, bytes([0x12]), read_size=3)]
                REG0x02 = [hex(x) for x in pt.i2c_exchange(I2C_NAU7802_ADDRESS, bytes([0x02]), read_size=1)]

                convert_to_24_bit_unsigned = (ADC_REGISTER[0] << 16) | (ADC_REGISTER[1] << 8) | ADC_REGISTER[2]
                read_out = self.twos_comp(convert_to_24_bit_unsigned, 24)
                self.weight = self.convert_ADC_to_weight(read_out)
                self.work_mode(self.convert_ADC_to_weight(read_out))
                pt.i2c_exchange(I2C_NAU7802_ADDRESS, bytes([0x00, 0xBE]))
                ADC_str = 'ADC= {}'.format(read_out)
                return ADC_str
            PU_CTRL_REGISTER = [hex(x) for x in pt.i2c_exchange(I2C_NAU7802_ADDRESS, bytes([0x00]), read_size=1)]

    def connect(self):
        # Initializes the communication module based on the selected port number and baud rate
        try:
            self.serial = serial.Serial(self.comboBox.currentText(), int(self.comboBox_2.currentText()))
        except serial.serialutil.SerialException:  # Failed to open, output prompt information
            pass

    def data_write(self, data):
        # The port communication function sends the received data out through the serial module
        try:
            self.serial.write(data.encode())
        except serial.serialutil.SerialException:
            pass

    def ui_init(self):
        # Fill the port and baud rate drop-down boxes with items
        list_baudrate = ['1200', '2400', '4800', '9600', '14400', '19200', '38400', '56000']
        for i in serial.tools.list_ports.comports():
            self.comboBox.addItem(i.device)
        for i in range(len(list_baudrate)):
            self.comboBox_2.addItem(list_baudrate[i])
        self.comboBox_2.setCurrentIndex(3)

    def mode_switch(self):
        # Interface control function, through the selection mode to display the corresponding control
        if self.radioButton.isChecked():
            self.frame_3.setVisible(True)
            self.frame.setVisible(False)
            self.frame_4.setVisible(False)
        elif self.radioButton_2.isChecked():
            self.frame_4.setVisible(True)
            self.frame.setVisible(False)
            self.frame_3.setVisible(False)
        elif self.radioButton_3.isChecked():
            self.frame.setVisible(True)
            self.frame_3.setVisible(False)
            self.frame_4.setVisible(False)


if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(Qt.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    Mywindow = Mywindow()
    Mywindow.show()
    sys.exit(app.exec_())
