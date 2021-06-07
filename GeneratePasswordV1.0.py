import sys
import random
import string

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtLocation
from PyQt5.QtGui import QClipboard
import PyQt5.QtWidgets
import PyQt5.QtCore

from WindowGeneratePassword import Ui_Dialog
# Version: 1.0
class Generated(QtWidgets.QMainWindow): # Initialise the class
	def __init__(self): # The initaliseaiton function
		super(Generated, self). __init__()
		self.WindowGeneratePassword = Ui_Dialog()
		self.WindowGeneratePassword.setupUi(self)

		self.WindowGeneratePassword.pushButton_generate.clicked.connect(self.generate_your_symbols) # Generate password button
		self.WindowGeneratePassword.pushButton_copy_text.clicked.connect(self.copy_text) # Copy text button

	def generate_your_symbols(self): #Function of its symbols
		if len(self.WindowGeneratePassword.lineEdit_your_symbols.text()) > 0: # Checking if there are characters in "lineEdit_your_symbols"
			# Disable the rest of the buttons
			self.WindowGeneratePassword.checkBox_number.setChecked(False)
			self.WindowGeneratePassword.checkBox_lowercase_letter.setChecked(False)
			self.WindowGeneratePassword.checkBox_uppercase_letter.setChecked(False)
			self.WindowGeneratePassword.checkBox_special_symbols.setChecked(False)

			self.chars = self.WindowGeneratePassword.lineEdit_your_symbols.text() # Assign user characters
			self.create_password() # Call the password generation function
		else:
			self.adding_symbols() # Call the function to add other symbols

	def adding_symbols(self):
		self.chars = "" # A variable that fits all characters
		special_symbols = "%*?)(}{@#|$~"

		if self.WindowGeneratePassword.checkBox_number.isChecked(): # If the button is pressed
			self.chars = self.chars + string.digits # Add numbers to the variable
		if self.WindowGeneratePassword.checkBox_lowercase_letter.isChecked(): # If the button is pressed
			self.chars = self.chars + string.ascii_lowercase # Add lowercase letters to the variable
		if self.WindowGeneratePassword.checkBox_uppercase_letter.isChecked(): # If the button is pressed
			self.chars = self.chars + string.ascii_uppercase # Add uppercase letters to the variable
		if self.WindowGeneratePassword.checkBox_special_symbols.isChecked(): # If the button is pressed
			self.chars = self.chars + special_symbols #Add special characters to the variable

		if self.chars == "": # If the user has not selected anything
			self.WindowGeneratePassword.textEdit_result.setText("Ошибка! Вы ничего не выбрали!")
		else:
			self.create_password()

	def create_password(self):
		number_password = int(self.WindowGeneratePassword.spinBox_number_password.text()) # Number of passwords
		length_password = int(self.WindowGeneratePassword.spinBox_length_password.text()) # Length of passwords

		list_password = [] # List of passwords
		if self.WindowGeneratePassword.checkBox_exclude_repeat.isChecked(): # If the button excluding repetitions is selected
			for i in range(number_password): # Repeat as many times as the user wants to generate passwords
				if length_password > len(self.chars): # If passwords are longer than there are characters
					self.WindowGeneratePassword.textEdit_result.setText('Ошибка! Мало символов! Пожалуйста, добавьте еще символов, чтобы можно было сформировать пароль без повторений.')
				else:
					password = "".join(random.sample(self.chars, length_password)) # Generate a password without repeats
					list_password.append(password) # Adding the generated password to the password list
					self.WindowGeneratePassword.textEdit_result.setText('\n'.join(list_password)) # Outputting the result
		else: # If the user did not select the button without repeats
			for i in range(number_password):  # Repeat as many times as the user wants to generate passwords
							password = "".join(random.choices( # Password generation
								self.chars,
								k=length_password # Password length
							))
							list_password.append(password) # Adding the generated password to the password list
							self.WindowGeneratePassword.textEdit_result.setText('\n'.join(list_password)) # Outputting the result

	def copy_text(self): # Function of copying the result
		self.WindowGeneratePassword.textEdit_result.selectAll() # Highlight all text
		self.WindowGeneratePassword.textEdit_result.copy() # Copy highlighted

app = QtWidgets.QApplication([])
app.setWindowIcon(QtGui.QIcon('generatepassword.ico')) # Application icon
application = Generated()
application.show()
sys.exit(app.exec_())
