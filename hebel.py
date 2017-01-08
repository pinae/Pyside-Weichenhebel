#!/usr/bin/python3
# -*- coding: utf-8 -*-

from __future__ import division, unicode_literals
from PySide import QtGui, QtCore
import os


class Stellwerkshebel(QtGui.QWidget, object):
    hebel_bewegt = QtCore.Signal(bool)

    """
    Dies ist ein grafischer Weichenhebel. Er drückt seine Stellung als Boolean-Variable aus.
    Oben ist True, unten False.
    """
    def __init__(self):
        super(Stellwerkshebel, self).__init__()
        self.position = True
        self.res_image = QtGui.QImage(os.path.join('res', 'Stellwerkshebel.png'))
        self.max_size = (51, 500)
        self.setMinimumSize(51, 500)
        self.calculate_width()

    def calculate_width(self):
        """
        Calculate the minimum width
        """
        self.setMinimumWidth(51)

    def paintEvent(self, *args):
        qp = QtGui.QPainter()
        qp.begin(self)
        self.draw(qp)
        qp.end()

    def draw(self, qp):
        size = self.size()
        qp.drawImage(QtCore.QRect(0, 0, 50, 499),
                     self.res_image,
                     QtCore.QRect(0, int(not self.position)*1500, 50, 499))

    def mousePressEvent(self, event):
        size = self.size()
        self.position = event.pos().y() < size.height() / 2
        print("Position: " + str(self.position))
        self.repaint()
        self.hebel_bewegt.emit(self.position)

    def mouseMoveEvent(self, event):
        self.mousePressEvent(event)

    def get_position(self):
        """
        Gibt die aktuelle Postion zurück.
        :return: postion
        :rtype: bool
        """
        return self.position

    def set_postion(self, postion):
        """
        Setzt die Position. True heißt der Hebel steht oben, bei False steht er unten.
        Dies löst nur dann ein Event aus, wenn sich die Position ändert.
        :param postion: neue postion
        :type postion: bool
        """
        if postion != self.position:
            self.position = not self.position
            self.repaint()
            self.hebel_bewegt.emit(self.position)
