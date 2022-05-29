from tkinter import Button
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

app = QApplication([])

win = QMainWindow()
button = QPushButton("Test")
win.setCentralWidget(button)
win.show()

app.exec()