from PyQt5.QtWidgets import *
from view import *
import math

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

class Controller(QMainWindow, Ui_MainWindow):
    #setup
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)



        self.setupUi(self)

        #setting calculator mode and max size
        self.Mode = 0
        self.setMaximumSize(295, 375)

        #initial displays
        self.DisplayLabel.setText('0')
        self.EquationLabel.setText('')


        #hiding all area related text and text boxes
        self.radiusLabel.setHidden(True)
        self.sidesLabel.setHidden(True)
        self.widthLabel.setHidden(True)
        self.lengthLabel.setHidden(True)
        self.baseLabel.setHidden(True)
        self.heightLabel.setHidden(True)
        self.area1Label.setHidden(True)
        self.area2Label.setHidden(True)
        self.area1Back.setHidden(True)
        self.area2Back.setHidden(True)
        self.area1SubmitButton.setHidden(True)
        self.area2SubmitButton.setHidden(True)




        self.areaGroup = QtWidgets.QButtonGroup()
        self.areaGroup.addButton(self.radioCircle)
        self.areaGroup.addButton(self.radioTriangle)
        self.areaGroup.addButton(self.radioRectangle)
        self.areaGroup.addButton(self.radioSquare)


        #button functionality
        self.pushButtonClear.clicked.connect(lambda: self.pressClear())
        self.pushButtonEqual.clicked.connect(lambda: self.pressEqual())
        self.pushButtonMode.clicked.connect(lambda: self.pressMode())
        self.pushButtonNegative.clicked.connect(lambda: self.pressNegative())
        self.pushButtonAdd.clicked.connect(lambda: self.pressPlus())
        self.pushButtonSubtract.clicked.connect(lambda: self.pressMinus())
        self.pushButtonMultiply.clicked.connect(lambda: self.pressMultiply())
        self.pushButtonDivide.clicked.connect(lambda: self.pressDivide())
        self.pushButtonDelete.clicked.connect(lambda: self.pressDelete())
        self.pushButtonDecimal.clicked.connect(lambda: self.pressDecimal())
        self.pushButton0.clicked.connect(lambda: self.press0())
        self.pushButton1.clicked.connect(lambda: self.press1())
        self.pushButton2.clicked.connect(lambda: self.press2())
        self.pushButton3.clicked.connect(lambda: self.press3())
        self.pushButton4.clicked.connect(lambda: self.press4())
        self.pushButton5.clicked.connect(lambda: self.press5())
        self.pushButton6.clicked.connect(lambda: self.press6())
        self.pushButton7.clicked.connect(lambda: self.press7())
        self.pushButton8.clicked.connect(lambda: self.press8())
        self.pushButton9.clicked.connect(lambda: self.press9())
        self.area1SubmitButton.clicked.connect(lambda: self.pressArea1Submit())
        self.area2SubmitButton.clicked.connect(lambda: self.pressArea2Submit())
        self.radioCircle.toggled.connect(lambda: self.areaState())
        self.radioSquare.toggled.connect(lambda: self.areaState())
        self.radioRectangle.toggled.connect(lambda: self.areaState())
        self.radioTriangle.toggled.connect(lambda: self.areaState())






    def pressEqual(self):
        #attempts to solve, displays error if unable to
        if self.Mode == 0:
            equation = self.EquationLabel.text()
            newNum = self.DisplayLabel.text()
            if newNum == 'Error' or newNum[0] == 'A':
                pass
            else:
                self.EquationLabel.setText(equation + newNum)
                equation = self.EquationLabel.text()

                try:
                    solved = eval(equation)
                    self.DisplayLabel.setText('Ans=' + str(solved))
                except:
                    self.DisplayLabel.setText("Error")

        elif self.Mode == 1:
            if self.radioCircle.isChecked():
                radius = self.area1Label.text()
                if float(radius) == 0:
                    self.DisplayLabel.setText("Error")
                else:
                    try:
                        solved = math.pi * (float(radius) ** 2)
                        self.DisplayLabel.setText("Area=" + str(solved))
                    except:
                        self.DisplayLabel.setText("Error")
            elif self.radioSquare.isChecked():
                side = self.area1Label.text()
                if float(side) == 0:
                    self.DisplayLabel.setText("Error")
                else:
                    try:
                        solved = float(side) ** 2
                        self.DisplayLabel.setText("Area=" + str(solved))
                    except:
                        self.DisplayLabel.setText("Error")
            elif self.radioRectangle.isChecked():
                length = self.area1Label.text()
                width = self.area2Label.text()
                if float(length) == 0 or float(width) == 0:
                    self.DisplayLabel.setText("Error")
                else:
                    try:
                        solved = float(length) * float(width)
                        self.DisplayLabel.setText("Area=" + str(solved))
                    except:
                        self.DisplayLabel.setText("Error")
            elif self.radioTriangle.isChecked():
                base = self.area1Label.text()
                height = self.area2Label.text()
                if float(base) == 0 or float(height) == 0:
                    self.DisplayLabel.setText("Error")
                else:
                    try:
                        solved = .5 * float(base) * float(height)
                        self.DisplayLabel.setText("Area=" + str(solved))
                    except:
                        self.DisplayLabel.setText("Error")
            else:
                pass

    def pressDelete(self):
        newNum = self.DisplayLabel.text()
        if newNum != '0' and newNum[0] != 'A' and newNum != 'Error':
            self.DisplayLabel.setText(newNum[:-1])
            newNum = self.DisplayLabel.text()
            if newNum == '':
                self.DisplayLabel.setText('0')
        else:
            pass

    def pressNegative(self):
        #sets equation to be negative
        newNum = self.DisplayLabel.text()
        if newNum[0] != '-' and newNum != 'Error' and newNum[0] != 'A' and newNum != '0':
            self.DisplayLabel.setText('-' + newNum)
        elif newNum[0] == '-' and newNum != 'Error' and newNum[0] != 'A' and newNum != '0':
            self.DisplayLabel.setText(newNum[1:])
        elif newNum[0] == 'A':
            self.EquationLabel.setText('')
            if newNum[4:] == '0':
                self.DisplayLabel.setText(newNum[4:])
            elif newNum[4] == '-':
                self.DisplayLabel.setText(newNum[5:])
            elif newNum[4] != '-':
                self.DisplayLabel.setText('-' + newNum[4:])
        else:
            pass

    def pressPlus(self):
        #adds a + to display
        equation = self.EquationLabel.text()
        newNum = self.DisplayLabel.text()
        if newNum == 'Error':
            pass
        elif newNum[0] == 'A':
            self.EquationLabel.setText(newNum[4:] + '+')
            self.DisplayLabel.setText('0')
        else:
            self.EquationLabel.setText(equation + newNum + '+')
            self.DisplayLabel.setText('0')

    def pressMinus(self):
        #adds a - to display
        equation = self.EquationLabel.text()
        newNum = self.DisplayLabel.text()
        if newNum == 'Error':
            pass
        elif newNum[0] == 'A':
            self.EquationLabel.setText(newNum[4:] + '-')
            self.DisplayLabel.setText('0')
        else:
            self.EquationLabel.setText(equation + newNum + '-')
            self.DisplayLabel.setText('0')

    def pressMultiply(self):
        #adds a * to display
        equation = self.EquationLabel.text()
        newNum = self.DisplayLabel.text()
        if newNum == 'Error':
            pass
        elif newNum[0] == 'A':
            self.EquationLabel.setText(newNum[4:] + '*')
            self.DisplayLabel.setText('0')
        else:
            self.EquationLabel.setText(equation + newNum + '*')
            self.DisplayLabel.setText('0')

    def pressDivide(self):
        #adds a / to display
        equation = self.EquationLabel.text()
        newNum = self.DisplayLabel.text()
        if newNum == 'Error':
            pass
        elif newNum[0] == 'A':
            self.EquationLabel.setText(newNum[4:] + '/')
            self.DisplayLabel.setText('0')
        else:
            self.EquationLabel.setText(equation + newNum + '/')
            self.DisplayLabel.setText('0')


    def pressDecimal(self):
        #adds . to display
        newNum = self.DisplayLabel.text()
        decimalCount = newNum.count('.')

        if decimalCount != 0:
            pass
        else:
            if newNum[0] == 'A':
                self.DisplayLabel.setText(newNum[4:] + '.')
                self.EquationLabel.setText('')
            else:
                self.DisplayLabel.setText(newNum + '.')

    def press0(self):
        #adds 0 to display
        newNum = self.DisplayLabel.text()
        if newNum == '0':
            pass
        elif newNum == 'Error':
            self.DisplayLabel.setText('0')
            self.EquationLabel.setText('')
        elif newNum[0] == 'A':
            self.DisplayLabel.setText('0')
            self.EquationLabel.setText('')
        else:
            self.DisplayLabel.setText(newNum + '0')

    def press1(self):
        #adds 1 to display
        newNum = self.DisplayLabel.text()
        if newNum == '0':
            self.DisplayLabel.setText('1')

        elif newNum[0] == 'A' or newNum == 'Error':
            self.DisplayLabel.setText('1')
            self.EquationLabel.setText('')
        else:
            self.DisplayLabel.setText(newNum + '1')

    def press2(self):
        #adds 2 to display
        newNum = self.DisplayLabel.text()
        if newNum == '0':
            self.DisplayLabel.setText('2')

        elif newNum[0] == 'A' or newNum == 'Error':
            self.DisplayLabel.setText('2')
            self.EquationLabel.setText('')
        else:
            self.DisplayLabel.setText(newNum + '2')

    def press3(self):
        #adds 3 to display
        newNum = self.DisplayLabel.text()
        if newNum == '0':
            self.DisplayLabel.setText('3')
        elif newNum[0] == 'A' or newNum == 'Error':
            self.DisplayLabel.setText('3')
            self.EquationLabel.setText('')
        else:
            self.DisplayLabel.setText(newNum + '3')

    def press4(self):
        #adds 4 to display
        newNum = self.DisplayLabel.text()
        if newNum == '0':
            self.DisplayLabel.setText('4')
        elif newNum[0] == 'A' or newNum == 'Error':
            self.DisplayLabel.setText('4')
            self.EquationLabel.setText('')
        else:
            self.DisplayLabel.setText(newNum + '4')

    def press5(self):
        #adds 5 to display
        newNum = self.DisplayLabel.text()
        if newNum == '0':
            self.DisplayLabel.setText('5')
        elif newNum[0] == 'A' or newNum == 'Error':
            self.DisplayLabel.setText('5')
            self.EquationLabel.setText('')
        else:
            self.DisplayLabel.setText(newNum + '5')

    def press6(self):
        #adds 6 to display
        newNum = self.DisplayLabel.text()
        if newNum == '0':
            self.DisplayLabel.setText('6')
        elif newNum[0] == 'A' or newNum == 'Error':
            self.DisplayLabel.setText('6')
            self.EquationLabel.setText('')
        else:
            self.DisplayLabel.setText(newNum + '6')

    def press7(self):
        #adds 7 to display
        newNum = self.DisplayLabel.text()
        if newNum == '0' or newNum == 'Error':
            self.DisplayLabel.setText('7')
        elif newNum[0] == 'A' or newNum == 'Error':
            self.DisplayLabel.setText('7')
            self.EquationLabel.setText('')
        else:
            self.DisplayLabel.setText(newNum + '7')

    def press8(self):
        #adds 8 to display
        newNum = self.DisplayLabel.text()
        if newNum == '0':
            self.DisplayLabel.setText('8')
        elif newNum[0] == 'A' or newNum == 'Error':
            self.DisplayLabel.setText('8')
            self.EquationLabel.setText('')
        else:
            self.DisplayLabel.setText(newNum + '8')

    def press9(self):
        #adds 9 to display
        newNum = self.DisplayLabel.text()
        if newNum == '0':
            self.DisplayLabel.setText('9')
        elif newNum[0] == 'A' or newNum == 'Error':
            self.DisplayLabel.setText('9')
            self.EquationLabel.setText('')
        else:
            self.DisplayLabel.setText(newNum + '9')

    def pressArea1Submit(self):
        newNum = self.DisplayLabel.text()
        if newNum != "Error" and newNum[0] != 'A':
            self.area1Label.setText(newNum)
        elif newNum[0] == 'A':
            self.area1Label.setText(newNum[5:])
        self.DisplayLabel.setText('0')

    def pressArea2Submit(self):
        newNum = self.DisplayLabel.text()
        if newNum != "Error" and newNum[0] != 'A':
            self.area2Label.setText(newNum)
        elif newNum[0] == 'A':
            self.area2Label.setText(newNum[5:])
        self.DisplayLabel.setText('0')


    def pressClear(self):
        # clears display
        self.DisplayLabel.setText('0')
        self.area1Label.setText('')
        self.area2Label.setText('')
        self.EquationLabel.setText('')

    def areaState(self):
        #changes what area boxes and related text are visible depending on what radio button is clicked
        if self.radioCircle.isChecked():
            self.radiusLabel.setHidden(False)
            self.sidesLabel.setHidden(True)
            self.widthLabel.setHidden(True)
            self.lengthLabel.setHidden(True)
            self.baseLabel.setHidden(True)
            self.heightLabel.setHidden(True)
            self.area1Label.setHidden(False)
            self.area1Back.setHidden(False)
            self.area1SubmitButton.setHidden(False)
            self.area2Label.setHidden(True)
            self.area2Back.setHidden(True)
            self.area2SubmitButton.setHidden(True)
            self.area1Label.setText('')
            self.area2Label.setText('')
        elif self.radioSquare.isChecked():
            self.radiusLabel.setHidden(True)
            self.sidesLabel.setHidden(False)
            self.widthLabel.setHidden(True)
            self.lengthLabel.setHidden(True)
            self.baseLabel.setHidden(True)
            self.heightLabel.setHidden(True)
            self.area1Label.setHidden(False)
            self.area2Label.setHidden(True)
            self.area1Back.setHidden(False)
            self.area1SubmitButton.setHidden(False)
            self.area2Label.setHidden(True)
            self.area2Back.setHidden(True)
            self.area2SubmitButton.setHidden(True)
            self.area1Label.setText('')
            self.area2Label.setText('')
        elif self.radioRectangle.isChecked():
            self.radiusLabel.setHidden(True)
            self.sidesLabel.setHidden(True)
            self.widthLabel.setHidden(False)
            self.lengthLabel.setHidden(False)
            self.baseLabel.setHidden(True)
            self.heightLabel.setHidden(True)
            self.area1Label.setHidden(False)
            self.area2Label.setHidden(False)
            self.area1Back.setHidden(False)
            self.area1SubmitButton.setHidden(False)
            self.area2Label.setHidden(False)
            self.area2Back.setHidden(False)
            self.area2SubmitButton.setHidden(False)
            self.area1Label.setText('')
            self.area2Label.setText('')
        elif self.radioTriangle.isChecked():
            self.radiusLabel.setHidden(True)
            self.sidesLabel.setHidden(True)
            self.widthLabel.setHidden(True)
            self.lengthLabel.setHidden(True)
            self.baseLabel.setHidden(False)
            self.heightLabel.setHidden(False)
            self.area1Label.setHidden(False)
            self.area2Label.setHidden(False)
            self.area1Back.setHidden(False)
            self.area1SubmitButton.setHidden(False)
            self.area2Label.setHidden(False)
            self.area2Back.setHidden(False)
            self.area2SubmitButton.setHidden(False)
            self.area1Label.setText('')
            self.area2Label.setText('')
        else:
            self.radiusLabel.setHidden(True)
            self.sidesLabel.setHidden(True)
            self.widthLabel.setHidden(True)
            self.lengthLabel.setHidden(True)
            self.baseLabel.setHidden(True)
            self.heightLabel.setHidden(True)
            self.area1Label.setHidden(True)
            self.area2Label.setHidden(True)
            self.area1SubmitButton.setHidden(True)
            self.area2Label.setHidden(True)
            self.area1Back.setHidden(True)
            self.area2Back.setHidden(True)
            self.area2SubmitButton.setHidden(True)
            self.area1Label.setText('')
            self.area2Label.setText('')


    def pressMode(self):
        #changes calculator modes
        if self.Mode == 0:
            self.setMaximumSize(500, 375)
            self.resize(500, 375)
            self.Mode = 1
            self.pushButtonNegative.setDisabled(True)
            self.pushButtonAdd.setDisabled(True)
            self.pushButtonDivide.setDisabled(True)
            self.pushButtonSubtract.setDisabled(True)
            self.pushButtonMultiply.setDisabled(True)
            self.DisplayLabel.setText('0')
            self.EquationLabel.setText('')
            self.areaState()
        else:
            self.setMaximumSize(295, 375)
            self.resize(295, 375)
            self.Mode = 0
            self.pushButtonNegative.setDisabled(False)
            self.pushButtonAdd.setDisabled(False)
            self.pushButtonDivide.setDisabled(False)
            self.pushButtonSubtract.setDisabled(False)
            self.pushButtonMultiply.setDisabled(False)
            self.DisplayLabel.setText('0')
            self.EquationLabel.setText('')
            self.areaState()

        self.areaGroup.setExclusive(False)
        self.radioCircle.setChecked(False)
        self.radioSquare.setChecked(False)
        self.radioRectangle.setChecked(False)
        self.radioTriangle.setChecked(False)
        self.areaGroup.setExclusive(True)

