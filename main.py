import sys
import sqlite3
import io

from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QApplication, QTableWidgetItem

template = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>statistics</class>
 <widget class="QWidget" name="statistics">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>940</width>
    <height>532</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Form</string>
  </property>
  <property name="styleSheet">
   <string notr="true">font-family: Century Gothic;
background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(186, 194, 217, 255), stop:1 rgba(129, 155, 198, 255));</string>
  </property>
  <layout class="QVBoxLayout" name="verticalLayout">
   <item>
    <widget class="QLabel" name="label_2">
     <property name="styleSheet">
      <string notr="true">color: white;
font-weight: bold;
font-size: 10pt;
background-color: none;
border: none;</string>
     </property>
     <property name="text">
      <string>эспрессо</string>
     </property>
     <property name="alignment">
      <set>Qt::AlignCenter</set>
     </property>
    </widget>
   </item>
   <item>
    <widget class="QTableWidget" name="tableWidget">
     <property name="sizePolicy">
      <sizepolicy hsizetype="Expanding" vsizetype="Expanding">
       <horstretch>0</horstretch>
       <verstretch>0</verstretch>
      </sizepolicy>
     </property>
     <property name="styleSheet">
      <string notr="true">background-color: rgb(255, 255, 255);
gridline-color: rgb(68, 78, 135);
gridline-color: rgb(182, 196, 235);

color: rgb(68, 78, 135);
font-weight: bold;
font-size: 10pt;



</string>
     </property>
     <property name="horizontalScrollBarPolicy">
      <enum>Qt::ScrollBarAlwaysOff</enum>
     </property>
     <property name="autoScroll">
      <bool>true</bool>
     </property>
     <property name="showDropIndicator" stdset="0">
      <bool>true</bool>
     </property>
     <property name="selectionBehavior">
      <enum>QAbstractItemView::SelectItems</enum>
     </property>
     <property name="verticalScrollMode">
      <enum>QAbstractItemView::ScrollPerItem</enum>
     </property>
     <property name="horizontalScrollMode">
      <enum>QAbstractItemView::ScrollPerItem</enum>
     </property>
     <property name="showGrid">
      <bool>true</bool>
     </property>
     <property name="gridStyle">
      <enum>Qt::SolidLine</enum>
     </property>
     <property name="sortingEnabled">
      <bool>false</bool>
     </property>
     <property name="rowCount">
      <number>0</number>
     </property>
     <attribute name="horizontalHeaderDefaultSectionSize">
      <number>250</number>
     </attribute>
     <attribute name="verticalHeaderCascadingSectionResizes">
      <bool>false</bool>
     </attribute>
     <attribute name="verticalHeaderMinimumSectionSize">
      <number>32</number>
     </attribute>
     <attribute name="verticalHeaderDefaultSectionSize">
      <number>32</number>
     </attribute>
     <attribute name="verticalHeaderHighlightSections">
      <bool>true</bool>
     </attribute>
    </widget>
   </item>
  </layout>
 </widget>
 <resources/>
 <connections/>
</ui>
'''


class StatisticWidget(QWidget):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.con = sqlite3.connect('coffee.sqlite')
        self.load_table()

    def load_table(self):
        query = """SELECT name, roasting, type, description, cost, volume FROM Coffee"""
        data = self.con.cursor().execute(query).fetchall()
        title = ('название', 'степень обжарки', 'тип', 'описание', 'цена', 'объем')
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setHorizontalHeaderLabels(title)
        self.tableWidget.setRowCount(0)
        for i, row in enumerate(data):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                item = QTableWidgetItem(str(elem))
                self.tableWidget.setItem(i, j, item)
                self.tableWidget.setEnabled(False)
        self.tableWidget.resizeColumnsToContents()
        # self.setFixedWidth(770)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = StatisticWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
