#!/usr/bin/python3
# -*- coding: utf-8 -*-
from PySide.QtGui import QApplication, QWidget, QBoxLayout
from hebel import Stellwerkshebel


class MainWindow(QWidget, object):
    hebel = None

    def __init__(self):
        super(MainWindow, self).__init__()
        layout = QBoxLayout(QBoxLayout.LeftToRight)
        layout.setContentsMargins(0, 0, 0, 0)
        self.hebel = Stellwerkshebel()
        layout.addWidget(self.hebel)
        layout.addStretch()
        self.setLayout(layout)
        self.resize(101, 500)
        self.move(100, 150)
        self.setWindowTitle("Stellwerkshebel Testprogramm")
        self.show()

    def hebel_bewegt(self):
        print("Hebel bewegt: " + str(self.hebel.get_position()))

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    app.exec_()
