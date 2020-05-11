from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QRadioButton, QMessageBox
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
from sys import argv
from os import system


# The Main Window class
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.action = "install"
        self.GUI()

    
    # The Graphical User Interface
    def GUI(self):
        self.setWindowTitle("Graphical PIP")
        self.setWindowIcon(QIcon("icon.ico"))
        self.setFixedSize(400, 110)

        # Styling
        self.setStyleSheet("""
            QMainWindow {
                background: #f7f7f4;
            }

            QLineEdit {
                background: #fff;
                color: #000;
                border: 3px solid #ffd242;
                font-size: 16px;
                padding: 10px;
            }

            QLineEdit:hover {
                background: #ffd242;
            }



            QRadioButton {
                color: #000;
                font-size: 16px;
            }

            QRadioButton::indicator {
                border: 3px solid #ffd242;
            }
            
            QRadioButton::indicator:hover {
                background: #ffd242;
            }

            QRadioButton::indicator:checked {
                background: #3775a9;
                border: 3px solid #3775a9;
            }
        """)
        
        # Get the package name
        self.pypi_name = QLineEdit(self)
        self.pypi_name.move(10, 10)
        self.pypi_name.setFixedSize(300, 50)
        self.pypi_name.setPlaceholderText("Enter the package name")


        # Run button
        self.run = QPushButton("Run", self)
        self.run.move(320, 10)
        self.run.setFixedSize(70, 50)
        self.run.clicked.connect(self.run_pressed)
        self.run.setStyleSheet("""
            QPushButton {
                background: #fff;
                color: #000;
                border: 3px solid #ffd242;
                font-size: 16px;
            }

            QPushButton:hover {
                background: #ffd242;
            }

            QPushButton:pressed {
                background: #3775a9;
                border: 3px solid #3775a9;
            }
            """)


        # Install Radio button
        self.install = QRadioButton("Install", self)
        self.install.move(10, 70)
        self.install.toggle()
        self.install.toggled.connect(lambda x: self.selected_action("install"))

        # Uninstall radio button
        self.uninstall = QRadioButton("Uninstall", self)
        self.uninstall.move(100, 70)
        self.uninstall.toggled.connect(lambda x: self.selected_action("uninstall"))

        # Update radio button
        self.update = QRadioButton("Update", self)
        self.update.move(190, 70)
        self.update.toggled.connect(lambda x: self.selected_action("update"))


    @pyqtSlot()

    # Recognize selected action with radio buttons
    def selected_action(self, action):
        if action == "install":
            self.action = "install"

        elif action == "uninstall":
            self.action = "uninstall"

        else:
            self.action = "install --upgrade"

    
    # When the run button pressed
    def run_pressed(self):

        # If name don't give
        if self.pypi_name.text() == "":
            QMessageBox.warning(self, "Warning!", "Eanter the package name!", QMessageBox.Ok, QMessageBox.Ok)
        
        else:
            system("pip" + " " + self.action + " " + self.pypi_name.text())
        

# Run the application
app = QApplication(argv)
window = MainWindow()
window.show()
app.exec()
