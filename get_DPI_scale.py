from PyQt5.QtWidgets import QApplication
from PyQt5 import QtWidgets
import sys

# app = QApplication(sys.argv)

# screen = app.screens()[0]
# dpi = screen.physicalDotsPerInch()
# image_inch = 300/140
# scale = round(dpi /140, 1)

# dpi = screen.physicalDotsPerInch()
refHeight = 1080
refWidth = 1920
# FIXME: This hardcoding now because starting app appears to cause issues
# QRect rect = QGuiApplication::primaryScreen()->geometry();
# resolution = QtWidgets.QDesktopWidget().screenGeometry()
width = refWidth
height = refHeight
print(width,height)
# height = max(width,height)
# width = min(width, height)
scale = round(min(height/refHeight, width/refWidth),1)
print(scale)

