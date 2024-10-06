import io
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt6 import uic


class Calculator(QMainWindow):
    def __init__(self):

        calc = """<?xml version="1.0" encoding="UTF-8"?>
        <ui version="4.0">
         <class>MainWindow</class>
         <widget class="QMainWindow" name="MainWindow">
          <property name="geometry">
           <rect>
            <x>0</x>
            <y>0</y>
            <width>800</width>
            <height>600</height>
           </rect>
          </property>
          <property name="windowTitle">
           <string>MainWindow</string>
          </property>
          <widget class="QWidget" name="centralwidget"/>
          <widget class="QMenuBar" name="menubar">
           <property name="geometry">
            <rect>
             <x>0</x>
             <y>0</y>
             <width>800</width>
             <height>19</height>
            </rect>
           </property>
           <widget class="QMenu" name="menuinstruments">
            <property name="title">
             <string>instruments</string>
            </property>
            <addaction name="actionbrush"/>
            <addaction name="actionline"/>
            <addaction name="actioncircle"/>
           </widget>
           <addaction name="menuinstruments"/>
          </widget>
          <widget class="QStatusBar" name="statusbar"/>
          <widget class="QToolBar" name="toolBar">
           <property name="windowTitle">
            <string>toolBar</string>
           </property>
           <attribute name="toolBarArea">
            <enum>TopToolBarArea</enum>
           </attribute>
           <attribute name="toolBarBreak">
            <bool>false</bool>
           </attribute>
           <addaction name="actionbrush"/>
           <addaction name="actionline"/>
           <addaction name="actioncircle"/>
          </widget>
          <action name="actionbrush">
           <property name="text">
            <string>brush</string>
           </property>
          </action>
          <action name="actionline">
           <property name="text">
            <string>line</string>
           </property>
          </action>
          <action name="actioncircle">
           <property name="text">
            <string>circle</string>
           </property>
          </action>
         </widget>
         <resources/>
         <connections/>
        </ui>
        """
        super().__init__()
        uic.loadUi(io.StringIO(calc), self)
