"""Creating a PyQt5 application which tells about the cases of corona around the world i.e number of confirmed cases, number of cases in which patient has recovered and total deaths due to corona."""

# importing libraries 
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui 
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from bs4 import BeautifulSoup as BS 
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
		self.UiComponents() 

		# showing all the widgets 
		self.show() 

	# method for widgets 
	def UiComponents(self): 

		# create push button to perform function 
		push = QPushButton("Press", self) 

		# setting geometry to the push button 
		push.setGeometry(125, 100, 150, 40) 

		# creating label to show the total cases 
		self.label_total = QLabel("Total Cases ", self) 

		# setting geometry 
		self.label_total.setGeometry(100, 200, 200, 40) 

		# setting alignment to the text 
		self.label_total.setAlignment(Qt.AlignCenter) 

		# adding border to the label 
		self.label_total.setStyleSheet("border : 2px solid black;") 

		# creating label to show the recovered cases 
		self.label_reco = QLabel("Recovered Cases ", self) 

		# setting geometry 
		self.label_reco.setGeometry(100, 250, 200, 40) 

		# setting alignment to the text 
		self.label_reco.setAlignment(Qt.AlignCenter) 

		# adding border 
		self.label_reco.setStyleSheet("border : 2px solid black;") 

		# creating label to show death cases 
		self.label_death = QLabel("Total Deaths ", self) 

		# setting geometry 
		self.label_death.setGeometry(100, 300, 200, 40) 

		# setting alignment to the text 
		self.label_death.setAlignment(Qt.AlignCenter) 

		# adding border to the label 
		self.label_death.setStyleSheet("border : 2px solid black;") 

		# adding action to the push button 
		push.clicked.connect(self.get_cases) 

	# method called by push 
	def get_cases(self): 

		# getting the request from url 
		data = requests.get("https://www.worldometers.info/coronavirus/") 

		# converting the text 
		soup = BS(data.text, 'html.parser') 

		# finding meta info for total cases 
		total = soup.find("div", class_="maincounter-number").text 

		# filtering it 
		total = total[1: len(total) - 2] 

		# finding meta info for other numbers 
		other = soup.find_all("span", class_="number-table") 

		# getting recovered cases number 
		recovered = other[2].text 

		# getting death cases number 
		deaths = other[3].text 

		# filtering the data 
		deaths = deaths[1:] 

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
