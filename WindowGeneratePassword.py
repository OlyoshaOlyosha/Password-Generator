from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(610, 420)
        Dialog.setMaximumSize(QtCore.QSize(610, 420))
        Dialog.setWhatsThis("")
        Dialog.setStyleSheet("background-color: #22222e;")
        self.textEdit_result = QtWidgets.QTextEdit(Dialog)
        self.textEdit_result.setGeometry(QtCore.QRect(10, 40, 591, 121))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.textEdit_result.setFont(font)
        self.textEdit_result.setMouseTracking(True)
        self.textEdit_result.setToolTip("")
        self.textEdit_result.setStatusTip("")
        self.textEdit_result.setWhatsThis("")
        self.textEdit_result.setAccessibleName("")
        self.textEdit_result.setAccessibleDescription("")
        self.textEdit_result.setAutoFillBackground(False)
        self.textEdit_result.setStyleSheet("QTextEdit{\n"
"background-color: #22222e;\n"
"border: 2px solid #ff9900;\n"
"border-radius: 10px;\n"
"color: white;\n"
"font: 87 8pt \"Montserrat\";\n"
"text-align: center;\n"
"}\n"
"QScrollBar::vertical {\n"
"    border: none;\n"
"    background: #2d2d44;\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"\n"
"QScrollBar::handle:vertical {    \n"
"    background-color: #cc7a00;\n"
"    min-height: 30px;\n"
"    border-radius: 7px;\n"
"}\n"
"QScrollBar::handle:vertical:hover{    \n"
"    background-color:#ff9900;\n"
"}\n"
"QScrollBar::handle:vertical:pressed {    \n"
"    background-color: #ba7000;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background-color: #3b3b5a;\n"
"    height: 15px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover {    \n"
"    background-color: #ff9900;\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed {    \n"
"    background-color: #ba7000;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    background-color: #3b3b5a;\n"
"    height: 15px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:hover {    \n"
"    background-color: #ff9900;\n"
"}\n"
"QScrollBar::add-line:vertical:pressed {    \n"
"    background-color: #ba7000;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}")
        self.textEdit_result.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textEdit_result.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.textEdit_result.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_result.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.textEdit_result.setReadOnly(True)
        self.textEdit_result.setObjectName("textEdit_result")
        self.label_generator_password = QtWidgets.QLabel(Dialog)
        self.label_generator_password.setGeometry(QtCore.QRect(10, 0, 591, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label_generator_password.setFont(font)
        self.label_generator_password.setToolTip("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Montserrat\'; font-size:8pt; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>")
        self.label_generator_password.setWhatsThis("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Montserrat\'; font-size:8pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>")
        self.label_generator_password.setStyleSheet("color: #fff;;")
        self.label_generator_password.setObjectName("label_generator_password")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(10, 170, 281, 241))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.checkBox_number = QtWidgets.QCheckBox(self.frame)
        self.checkBox_number.setEnabled(True)
        self.checkBox_number.setGeometry(QtCore.QRect(0, 0, 281, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.checkBox_number.setFont(font)
        self.checkBox_number.setToolTip("<html><head/><body><p align=\"center\"><br/></p></body></html>")
        self.checkBox_number.setToolTipDuration(-3)
        self.checkBox_number.setStatusTip("")
        self.checkBox_number.setWhatsThis("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Montserrat\'; font-size:10pt; font-weight:80; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>")
        self.checkBox_number.setStyleSheet("QCheckBox {\n"
"    background-color:#ff933a;\n"
"    color: #ffffff;\n"
"    border-radius: 8px;\n"
"    font: 87 10pt \"Montserrat\";\n"
"    padding: 6px;\n"
" }\n"
"QCheckBox::indicator\n"
"{\n"
"    background-color: #e30000;\n"
"    border: 2px solid #ab5b00;\n"
"    width: 20px;\n"
"    height: 20px;\n"
"    border-radius: 12px;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background-color: #2dbf00;\n"
"}\n"
"")
        self.checkBox_number.setChecked(True)
        self.checkBox_number.setTristate(False)
        self.checkBox_number.setObjectName("checkBox_number")
        self.checkBox_lowercase_letter = QtWidgets.QCheckBox(self.frame)
        self.checkBox_lowercase_letter.setGeometry(QtCore.QRect(0, 50, 281, 41))
        self.checkBox_lowercase_letter.setToolTip("<html><head/><body><p align=\"center\"><br/></p></body></html>")
        self.checkBox_lowercase_letter.setToolTipDuration(-3)
        self.checkBox_lowercase_letter.setWhatsThis("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Montserrat\'; font-size:10pt; font-weight:80; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>")
        self.checkBox_lowercase_letter.setStyleSheet("QCheckBox {\n"
"    background-color:#ff933a;\n"
"    color: #ffffff;\n"
"    border-radius: 8px;\n"
"    font: 87 10pt \"Montserrat\";\n"
"    padding: 6px;\n"
" }\n"
"QCheckBox::indicator\n"
"{\n"
"    background-color: #e30000;\n"
"    border: 2px solid #ab5b00;\n"
"    width: 20px;\n"
"    height: 20px;\n"
"    border-radius: 12px;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background-color: #2dbf00;\n"
"}\n"
"")
        self.checkBox_lowercase_letter.setObjectName("checkBox_lowercase_letter")
        self.checkBox_uppercase_letter = QtWidgets.QCheckBox(self.frame)
        self.checkBox_uppercase_letter.setGeometry(QtCore.QRect(0, 100, 281, 41))
        self.checkBox_uppercase_letter.setToolTip("<html><head/><body><p align=\"center\"><br/></p></body></html>")
        self.checkBox_uppercase_letter.setToolTipDuration(-3)
        self.checkBox_uppercase_letter.setWhatsThis("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Montserrat\'; font-size:10pt; font-weight:80; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>")
        self.checkBox_uppercase_letter.setStyleSheet("QCheckBox {\n"
"    background-color:#ff933a;\n"
"    color: #ffffff;\n"
"    border-radius: 8px;\n"
"    font: 87 10pt \"Montserrat\";\n"
"    padding: 6px;\n"
" }\n"
"QCheckBox::indicator\n"
"{\n"
"    background-color: #e30000;\n"
"    border: 2px solid #ab5b00;\n"
"    width: 20px;\n"
"    height: 20px;\n"
"    border-radius: 12px;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background-color: #2dbf00;\n"
"}\n"
"")
        self.checkBox_uppercase_letter.setObjectName("checkBox_uppercase_letter")
        self.checkBox_special_symbols = QtWidgets.QCheckBox(self.frame)
        self.checkBox_special_symbols.setGeometry(QtCore.QRect(0, 150, 281, 41))
        self.checkBox_special_symbols.setToolTip("<html><head/><body><p align=\"center\"><br/></p></body></html>")
        self.checkBox_special_symbols.setToolTipDuration(-3)
        self.checkBox_special_symbols.setWhatsThis("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Montserrat\'; font-size:10pt; font-weight:80; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>")
        self.checkBox_special_symbols.setStyleSheet("QCheckBox {\n"
"    background-color:#ff933a;\n"
"    color: #ffffff;\n"
"    border-radius: 8px;\n"
"    font: 87 10pt \"Montserrat\";\n"
"    padding: 6px;\n"
" }\n"
"QCheckBox::indicator\n"
"{\n"
"    background-color: #e30000;\n"
"    border: 2px solid #ab5b00;\n"
"    width: 20px;\n"
"    height: 20px;\n"
"    border-radius: 12px;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background-color: #2dbf00;\n"
"}\n"
"")
        self.checkBox_special_symbols.setObjectName("checkBox_special_symbols")
        self.lineEdit_your_symbols = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_your_symbols.setGeometry(QtCore.QRect(140, 200, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lineEdit_your_symbols.setFont(font)
        self.lineEdit_your_symbols.setToolTip("")
        self.lineEdit_your_symbols.setWhatsThis("")
        self.lineEdit_your_symbols.setStyleSheet("background-color: #22222e;\n"
"border: 2px solid #ff9900;\n"
"border-radius: 10px;\n"
"color: white;")
        self.lineEdit_your_symbols.setText("")
        self.lineEdit_your_symbols.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_your_symbols.setObjectName("lineEdit_your_symbols")
        self.label_your_symbols = QtWidgets.QLabel(self.frame)
        self.label_your_symbols.setGeometry(QtCore.QRect(0, 200, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_your_symbols.setFont(font)
        self.label_your_symbols.setMouseTracking(True)
        self.label_your_symbols.setToolTip("<html><head/><body><p align=\"center\"><br/></p></body></html>")
        self.label_your_symbols.setWhatsThis("")
        self.label_your_symbols.setStyleSheet("background-color: #ff933a;\n"
"color: #ffffff;\n"
"border-radius: 8px;\n"
"font: 87 10pt \"Montserrat\";")
        self.label_your_symbols.setAlignment(QtCore.Qt.AlignCenter)
        self.label_your_symbols.setObjectName("label_your_symbols")
        self.line_your_symbols = QtWidgets.QFrame(self.frame)
        self.line_your_symbols.setGeometry(QtCore.QRect(120, 200, 31, 41))
        self.line_your_symbols.setToolTip("")
        self.line_your_symbols.setWhatsThis("")
        self.line_your_symbols.setStyleSheet("color: #ff933a;")
        self.line_your_symbols.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_your_symbols.setLineWidth(9)
        self.line_your_symbols.setMidLineWidth(0)
        self.line_your_symbols.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_your_symbols.setObjectName("line_your_symbols")
        self.line_your_symbols.raise_()
        self.checkBox_number.raise_()
        self.checkBox_lowercase_letter.raise_()
        self.checkBox_uppercase_letter.raise_()
        self.checkBox_special_symbols.raise_()
        self.lineEdit_your_symbols.raise_()
        self.label_your_symbols.raise_()
        self.frame_2 = QtWidgets.QFrame(Dialog)
        self.frame_2.setGeometry(QtCore.QRect(300, 170, 301, 141))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.pushButton_generate = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_generate.setGeometry(QtCore.QRect(0, 0, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_generate.setFont(font)
        self.pushButton_generate.setToolTip("")
        self.pushButton_generate.setWhatsThis("")
        self.pushButton_generate.setAutoFillBackground(False)
        self.pushButton_generate.setStyleSheet("QPushButton {\n"
"    color: #ffffff;\n"
"    background-color: #09b400;\n"
"    border-radius: 8px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #09aa00;\n"
"\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: #099600;\n"
"}")
        self.pushButton_generate.setObjectName("pushButton_generate")
        self.pushButton_copy_text = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_copy_text.setGeometry(QtCore.QRect(0, 50, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_copy_text.setFont(font)
        self.pushButton_copy_text.setToolTip("")
        self.pushButton_copy_text.setWhatsThis("")
        self.pushButton_copy_text.setStyleSheet("QPushButton {\n"
"    color: #ffffff;\n"
"    background-color: #2896ff;\n"
"    border-radius: 8px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #288cff;\n"
"\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: #2878ff;\n"
"}")
        self.pushButton_copy_text.setObjectName("pushButton_copy_text")
        self.checkBox_exclude_repeat = QtWidgets.QCheckBox(self.frame_2)
        self.checkBox_exclude_repeat.setGeometry(QtCore.QRect(0, 100, 301, 41))
        self.checkBox_exclude_repeat.setToolTip("<html><head/><body><p align=\"center\"><br/></p></body></html>")
        self.checkBox_exclude_repeat.setToolTipDuration(-3)
        self.checkBox_exclude_repeat.setWhatsThis("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Montserrat\'; font-size:10pt; font-weight:80; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>")
        self.checkBox_exclude_repeat.setStyleSheet("QCheckBox {\n"
"    background-color:#ff933a;\n"
"    color: #ffffff;\n"
"    border-radius: 8px;\n"
"    font: 87 10pt \"Montserrat\";\n"
"    padding: 6px;\n"
" }\n"
"QCheckBox::indicator\n"
"{\n"
"    background-color: #e30000;\n"
"    border: 2px solid #ab5b00;\n"
"    width: 20px;\n"
"    height: 20px;\n"
"    border-radius: 12px;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background-color: #2dbf00;\n"
"}\n"
"")
        self.checkBox_exclude_repeat.setObjectName("checkBox_exclude_repeat")
        self.frame_3 = QtWidgets.QFrame(Dialog)
        self.frame_3.setGeometry(QtCore.QRect(300, 320, 301, 91))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_number_password = QtWidgets.QLabel(self.frame_3)
        self.label_number_password.setGeometry(QtCore.QRect(110, 0, 191, 41))
        self.label_number_password.setToolTip("<html><head/><body><p><br/></p></body></html>")
        self.label_number_password.setWhatsThis("")
        self.label_number_password.setStyleSheet("background-color: #ff933a;\n"
"color: #ffffff;\n"
"border-radius: 8px;\n"
"font: 87 7pt \"Montserrat\";")
        self.label_number_password.setObjectName("label_number_password")
        self.spinBox_number_password = QtWidgets.QSpinBox(self.frame_3)
        self.spinBox_number_password.setGeometry(QtCore.QRect(0, 0, 101, 41))
        self.spinBox_number_password.setToolTip("")
        self.spinBox_number_password.setWhatsThis("")
        self.spinBox_number_password.setStyleSheet("QSpinBox\n"
"{\n"
"background-color: #40372a;\n"
"border: 2px solid #ff9900;\n"
"border-radius: 10px;\n"
"color: white;\n"
"font: 87 19pt \"Montserrat\";\n"
"}\n"
" QSpinBox::up-button {\n"
"     subcontrol-position: top right;\n"
"     width: 17px;\n"
" }\n"
" QSpinBox::down-button {\n"
"     subcontrol-position: bottom right;\n"
"     width: 17px;\n"
"\n"
" }\n"
"")
        self.spinBox_number_password.setMinimum(1)
        self.spinBox_number_password.setMaximum(999)
        self.spinBox_number_password.setProperty("value", 5)
        self.spinBox_number_password.setObjectName("spinBox_number_password")
        self.spinBox_length_password = QtWidgets.QSpinBox(self.frame_3)
        self.spinBox_length_password.setGeometry(QtCore.QRect(0, 50, 101, 41))
        self.spinBox_length_password.setToolTip("")
        self.spinBox_length_password.setWhatsThis("")
        self.spinBox_length_password.setStyleSheet("QSpinBox\n"
"{\n"
"background-color: #40372a;\n"
"border: 2px solid #ff9900;\n"
"border-radius: 10px;\n"
"color: white;\n"
"font: 87 19pt \"Montserrat\";\n"
"}\n"
" QSpinBox::up-button {\n"
"     subcontrol-position: top right;\n"
"     width: 17px;\n"
" }\n"
" QSpinBox::down-button {\n"
"     subcontrol-position: bottom right;\n"
"     width: 17px;\n"
"\n"
" }\n"
"")
        self.spinBox_length_password.setMinimum(1)
        self.spinBox_length_password.setMaximum(999)
        self.spinBox_length_password.setProperty("value", 10)
        self.spinBox_length_password.setObjectName("spinBox_length_password")
        self.label_length_password = QtWidgets.QLabel(self.frame_3)
        self.label_length_password.setGeometry(QtCore.QRect(110, 50, 191, 41))
        self.label_length_password.setToolTip("<html><head/><body><p><br/></p></body></html>")
        self.label_length_password.setWhatsThis("")
        self.label_length_password.setStyleSheet("background-color: #ff933a;\n"
"color: #ffffff;\n"
"border-radius: 8px;\n"
"font: 87 8pt \"Montserrat\";")
        self.label_length_password.setObjectName("label_length_password")
        self.line_number_password = QtWidgets.QFrame(self.frame_3)
        self.line_number_password.setGeometry(QtCore.QRect(90, 0, 31, 41))
        self.line_number_password.setToolTip("")
        self.line_number_password.setWhatsThis("")
        self.line_number_password.setStyleSheet("color: #ff933a;")
        self.line_number_password.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_number_password.setLineWidth(9)
        self.line_number_password.setMidLineWidth(0)
        self.line_number_password.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_number_password.setObjectName("line_number_password")
        self.line_length_password = QtWidgets.QFrame(self.frame_3)
        self.line_length_password.setGeometry(QtCore.QRect(90, 50, 31, 41))
        self.line_length_password.setToolTip("")
        self.line_length_password.setWhatsThis("")
        self.line_length_password.setStyleSheet("color: #ff933a;")
        self.line_length_password.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_length_password.setLineWidth(9)
        self.line_length_password.setMidLineWidth(0)
        self.line_length_password.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_length_password.setObjectName("line_length_password")
        self.line_length_password.raise_()
        self.line_number_password.raise_()
        self.label_number_password.raise_()
        self.spinBox_number_password.raise_()
        self.spinBox_length_password.raise_()
        self.label_length_password.raise_()
        self.frame_3.raise_()
        self.frame_2.raise_()
        self.frame.raise_()
        self.textEdit_result.raise_()
        self.label_generator_password.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Password Generator V1.0"))
        self.textEdit_result.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Montserrat\'; font-size:8pt; font-weight:80; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_generator_password.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">ГЕНЕРАТОР ПАРОЛЕЙ</span></p></body></html>"))
        self.checkBox_number.setText(_translate("Dialog", "ЦИФРЫ 0-9                                                  "))
        self.checkBox_lowercase_letter.setText(_translate("Dialog", "СТРОЧНЫЕ БУКВЫ a-z                                        "))
        self.checkBox_uppercase_letter.setText(_translate("Dialog", "ПРОПИСНЫЕ БУКВЫ A-Z                                      "))
        self.checkBox_special_symbols.setText(_translate("Dialog", "СПЕЦ. СИМВОЛЫ %*?)(}{@#|$~"))
        self.label_your_symbols.setText(_translate("Dialog", "СВОИ СИМВОЛЫ"))
        self.pushButton_generate.setText(_translate("Dialog", "СГЕНЕРИРОВАТЬ ПАРОЛЬ"))
        self.pushButton_copy_text.setText(_translate("Dialog", "СКОПИРОВАТЬ ВСЁ"))
        self.checkBox_exclude_repeat.setText(_translate("Dialog", "ИСКЛЮЧИТЬ ПОВТОР СИМВОЛОВ       "))
        self.label_number_password.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">КОЛИЧЕСТВО ПАРОЛЕЙ</span></p></body></html>"))
        self.label_length_password.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">ДЛИНА ПОРОЛЯ</span></p></body></html>"))
