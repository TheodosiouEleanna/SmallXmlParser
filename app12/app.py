import sys
import xml.dom.minidom
import xml.etree.ElementTree as ET
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.Qt import Qt
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from xml.etree.ElementTree import parse, Element

mytree = ET.parse('10_schedule.xml')

myroot = mytree.getroot()
# print(myroot)



# titles = myroot.findall("./Lesson/Title")
# for child in titles:
#    title_text = child.text
#    Titles.append(title_text)
# Titles.insert(1, " ")
# # print(Titles)

# professors = myroot.findall("./Lesson/Professor")
# for child in professors:
#    if professors == 'Null':
#       Professors.insert(child," ")
#    else:
#       professor_text = child.text
#       Professors.append(professor_text)
# Professors.insert(0," ")
# Professors.insert(2," ")
# Professors.insert(4," ")
   
# print(Professors)

# days = myroot.findall("./Lesson/Lecture/Day")
# for child in days:
#    day_text = child.text
#    Days.append(day_text)
   # print(child.text)
# print(Days)

Titles=[]
Professors=[]
Days=[]

document = parse('10_schedule.xml')
print(document)

for item in mytree.iterfind('./Lesson'):
   Titles.append(item.findtext('./Title'))
   Professors.append(item.findtext('./Professor'))
Professors.insert(0,None)
Titles.insert(1, None)

for item in document.iterfind('Lesson/Lecture'):
   Days.append(item.findtext('Day'))

print(Titles)
print(Professors)
print(Days)

Table = []
for i in range(0, len(Titles)):
   Table.append([Titles[i], Professors[i], Days[i]])
# print("Table=",Table )

Lesson = []
Professor = []
Day = []

class MainWindow(QDialog):
   def __init__(self):
      super(MainWindow, self).__init__()
      loadUi("app.ui", self)
      self.addButton.clicked.connect(self.addEntry)
      self.table.setColumnWidth(0,160)
      self.table.setColumnWidth(1,160)
      self.table.setColumnWidth(2,160)
      self.comboBox.currentIndexChanged.connect(self.loaddata)
      if self.comboBox.currentIndex()==0:
         for i in range(0, len(Titles)):
            Lesson.append(Table[i][0])
            Professor.append(Table[i][1])
            Day.append(Table[i][2])
         self.fillTable()

   def addEntry(self):
      title = self.title.text()
      professor = self.professor.text()
      day = self.day.text()
      self.title.clear()
      self.professor.clear()
      self.day.clear()
      # print(title)
      # print(professor)
      # print(day)
      Lesson = ET.SubElement(myroot,'Lesson')
      Title = ET.SubElement(Lesson, 'Title')
      Professor = ET.SubElement(Lesson, 'Professor')
      Lecture = ET.SubElement(Lesson, 'Lecture')
      Lecture.attrib['Classroom'] = 'Null'
      Day = ET.SubElement(Lecture, 'Day')
      Time = ET.SubElement(Lecture, 'Time')
      Title.text = title
      Professor.text = professor
      Day.text = day
      Time.text = 'time'
      mytree.write('10_schedule.xml')

   def loaddata(self):
      self.table.clearContents()
      
      if self.comboBox.currentIndex() == 1:
         for i in range(0, len(Titles)):
            # print(Table[i][2])
            if Table[i][2] == "Monday":
               Lesson.append(Table[i][0])
               Professor.append(Table[i][1])
               Day.append(Table[i][2])
         self.fillTable()
      elif self.comboBox.currentIndex() == 2:
         for i in range(0, len(Titles)):
            # print(Table[i][2])
            if Table[i][2] == "Tuesday":
               Lesson.append(Table[i][0])
               Professor.append(Table[i][1])
               Day.append(Table[i][2])
         self.fillTable()
      elif self.comboBox.currentIndex() == 3:
         for i in range(0, len(Titles)):
            # print(Table[i][2])
            if Table[i][2] == "Wednesday":
               Lesson.append(Table[i][0])
               Professor.append(Table[i][1])
               Day.append(Table[i][2])
         self.fillTable()
      elif self.comboBox.currentIndex() == 4:
         for i in range(0, len(Titles)):
            # print(Table[i][2])
            if Table[i][2] == "Thursday":
               Lesson.append(Table[i][0])
               Professor.append(Table[i][1])
               Day.append(Table[i][2])
         self.fillTable()
      elif self.comboBox.currentIndex() == 5:
         for i in range(0, len(Titles)):
            # print(Table[i][2])
            if Table[i][2] == "Friday":
               Lesson.append(Table[i][0])
               Professor.append(Table[i][1])
               Day.append(Table[i][2])
         # print(Lesson)
         # print(Professor)
         # print(Day)
         self.fillTable() 
      elif self.comboBox.currentIndex() == 6:
         for i in range(0, len(Titles)):
            Lesson.append(Table[i][0])
            Professor.append(Table[i][1])
            Day.append(Table[i][2])
         self.fillTable()
         
   def fillTable(self):
      row1 = 0
      row2 = 0
      row3 = 0
      self.table.setRowCount(len(Day))
      for title in Lesson:
         self.table.setItem(row1, 0, QtWidgets.QTableWidgetItem(title))
         row1 += 1

      for professor in Professor:
         self.table.setItem(row2, 1, QtWidgets.QTableWidgetItem(professor))
         row2 += 1

      for day in Day:
         self.table.setItem(row3, 2, QtWidgets.QTableWidgetItem(day))
         row3 += 1
      Lesson.clear()
      Professor.clear()
      Day.clear()   
      

app = QApplication(sys.argv)
mainWindow = MainWindow()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainWindow)
widget.setFixedHeight(530)
widget.setFixedWidth(550)
widget.show()
app.exec()

