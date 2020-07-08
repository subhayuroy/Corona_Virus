"""Creating a PyQt5 application that tells about the details of coronavirus cases i.e total cases, recovered cases and total deaths across India i.e state wise result."""

# importing libraries 
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui 
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from bs4 import BeautifulSoup 
import requests 
import sys 


class Window(QMainWindow): 

	def __init__(self): 
		super().__init__() 

		# setting title 
		self.setWindowTitle("Python ") 

		# setting geometry 
		self.setGeometry(100, 100, 400, 500) 

		# calling method 
		self.corona() 

		# calling method 
		self.UiComponents() 

		# showing all the widgets 
		self.show() 

	def corona(self): 
		extract_contents = lambda row: [x.text.replace('\n', '') for x in row] 
		URL = 'https://www.mohfw.gov.in/'

		SHORT_HEADERS = ['SNo', 'State', 'Indian-Confirmed', 
						'Foreign-Confirmed', 'Cured', 'Death'] 

		response = requests.get(URL).content 
		soup = BeautifulSoup(response, 'html.parser') 
		header = extract_contents(soup.tr.find_all('th')) 

		self.stats = [] 
		all_rows = soup.find_all('tr') 

		for row in all_rows: 
			stat = extract_contents(row.find_all('td')) 
			if stat: 
				if len(stat) == 5: 
					# last row 
					stat = ['', *stat] 
					self.stats.append(stat) 
				elif len(stat) == 6: 
					self.stats.append(stat) 

		self.stats[-1][1] = "Total Cases"

		self.stats.remove(self.stats[-1]) 

		# method for widgets 
	def UiComponents(self): 

		# creating a combo box widget 
		self.combo_box = QComboBox(self) 

		# setting geometry to combo box 
		self.combo_box.setGeometry(100, 50, 200, 40) 

		# setting font 
		self.combo_box.setFont(QFont('Times', 10)) 

		# adding items to combo box 
		for i in self.stats: 

			self.combo_box.addItem(i[2]) 

		# adding action to the combo box 
		self.combo_box.activated.connect(self.get_cases) 

		# creating label to show the total cases 
		self.label_total = QLabel("Total Cases ", self) 

		# setting geometry 
		self.label_total.setGeometry(100, 300, 200, 40) 

		# setting alignment to the text 
		self.label_total.setAlignment(Qt.AlignCenter) 

		# adding border to the label 
		self.label_total.setStyleSheet("border : 2px solid black;") 

		# creating label to show the recovered cases 
		self.label_reco = QLabel("Recovered Cases ", self) 

		# setting geometry 
		self.label_reco.setGeometry(100, 350, 200, 40) 

		# setting alignment to the text 
		self.label_reco.setAlignment(Qt.AlignCenter) 

		# adding border 
		self.label_reco.setStyleSheet("border : 2px solid black;") 

		# creating label to show death cases 
		self.label_death = QLabel("Total Deaths ", self) 

		# setting geometry 
		self.label_death.setGeometry(100, 400, 200, 40) 

		# setting alignment to the text 
		self.label_death.setAlignment(Qt.AlignCenter) 

		# adding border to the label 
		self.label_death.setStyleSheet("border : 2px solid black;") 


	# method called by push 
	def get_cases(self): 

		# getting index 
		index = self.combo_box.currentIndex() 

		# getting data 
		total = self.stats[index][3] 
		recovered = self.stats[index][4] 
		deaths = self.stats[index][5] 

		# show data through labels 
		self.label_total.setText("Total Cases : " + total) 
		self.label_reco.setText("Recovered Cases : " + recovered) 
		self.label_death.setText("Total Deaths : " + deaths) 


# create pyqt5 app 
App = QApplication(sys.argv) 

# create the instance of our Window 
window = Window() 

window.show() 

# start the app 
sys.exit(App.exec()) 
