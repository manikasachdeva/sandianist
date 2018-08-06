import csv 
import sys 
import time 
from datetime import datetime, time
import os 
import numpy as np
import matplotlib.pyplot as plt
import pandas
import tkinter as tk
from tkinter import *
#import matplotlib
#matplotlib.use('TkAgg')
#from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
#from matplotlib.figure import Figure


def main():


	root=Tk()
	root.title("Sandia Graphs Generator (2018)")
	#setting the size of the window so it doesn't change
	root.minsize(width=350, height=400)
	root.maxsize(width=350, height=400)

	header = Label(root, text="Sandia Graphs Generator", font=("calibri", 23, "bold"), fg="blue").place(x=10, y =0)

	#User Input for dates
	#DOES NOT WORK YET
	startLabel = Label(root, text="Please enter the start date: ", font=("calibri", 12), fg="blue").place(x=10, y = 50)
	startDate = StringVar()
	entry_box1 = Entry(root, textvariable = startDate, width = 17, bg = "lightblue").place(x=200, y = 55)

	endLabel = Label(root, text="Please enter the end date: ", font=("calibri", 12), fg="blue").place(x=10, y = 90)
	endDate = StringVar()
	entry_box2 = Entry(root, textvariable = endDate, width = 17, bg = "lightblue").place(x=200, y = 95)
	
	
	
	#Dry Chambers Check Boxes
	dryChamber = Label(root, text="Dry", font=("calibri", 12), fg="blue").place(x=10, y = 125)

	chamber1bool = BooleanVar()
	chamber3bool = BooleanVar()
	chamber5bool = BooleanVar()	

	chamber1 = Checkbutton(root, variable = chamber1bool, onvalue=True, offvalue=False,text = "Chamber 1")
	chamber1.place(x =10, y = 150)
	
	chamber3 = Checkbutton(root, variable = chamber3bool, onvalue=True, offvalue=False, text = "Chamber 3")
	chamber3.place(x =10, y = 170)

	chamber5 = Checkbutton(root,variable = chamber5bool, onvalue=True, offvalue=False, text = "Chamber 5")
	chamber5.place(x =10, y = 190)
	
	
	#Humid Chambers Check Boxes 
	humidChamber = Label(root, text="Humid", font=("calibri", 12), fg="blue").place(x=170, y = 125)

	chamber2bool = BooleanVar()
	chamber4bool= BooleanVar()

	chamber2 = Checkbutton(root, variable = chamber2bool, onvalue=True, offvalue=False, text = "Chamber 2")
	chamber2.place(x =170, y = 150)
	
	chamber4 = Checkbutton(root, variable = chamber4bool, onvalue=True, offvalue=False, text = "Chamber 4")
	chamber4.place(x =170, y = 170)	


	#Temperature options 
	temp = Label(root, text= "Dry Temps", font = ("calibri", 12), fg = "blue").place(x=10, y = 210)
	temp2 = Label(root, text= "Humid Temps", font = ("calibri", 12), fg = "blue").place(x=170, y = 210)
			
	airTempDbool = BooleanVar()
	airTempD = Checkbutton(root, variable=airTempDbool, onvalue=True, offvalue=False, text = "Air Temperature (Deg C)")
	airTempD.place(x = 10, y=235)

	airTempHbool = BooleanVar()
	airTempH = Checkbutton(root, variable=airTempHbool, onvalue=True, offvalue=False, text = "Air Temperature (Deg C)")
	airTempH.place(x = 170, y = 235)
			
	panTempbool = IntVar()
	panTemp = Checkbutton(root,variable=panTempbool, onvalue=True, offvalue=False,  text = "Pan Temperature (Deg C)")
	panTemp.place(x=170, y = 255)

	waterTempbool = IntVar()
	waterTemp = Checkbutton(root, variable=waterTempbool, onvalue=True, offvalue=False, text = "Water Temperature (Deg C)")
	waterTemp.place(x=170, y = 275)

	
	def graph(): 

		if (chamber1bool.get() and airTempDbool.get()) == True:			
	
			fileName = "onehourdry1.csv"
			dateTime = []		
			airHumid = []

			with open(fileName, 'r') as data:
				readData = csv.reader(data, delimiter=',')

				for row in readData:
					dateTime.append(row[0])		
					airHumid.append(row[1])

			plt.plot(dateTime,airHumid, label='Chamber 1 Air Temperature')
			plt.xlabel('Date')
			plt.ylabel('Air Temperature')
			plt.title('Chamber 1 Air Temperature')
			plt.legend()
			plt.show()

		elif (chamber2bool.get() and airTempHbool.get()) == True: 
			
			fileName = "onehourhumid2.csv"
			dateTime = []		
			airHumid = []

			with open(fileName, 'r') as data:
				readData = csv.reader(data, delimiter=',')

				for row in readData:
					dateTime.append(row[0])		
					airHumid.append(row[1])

			plt.plot(dateTime,airHumid, label='Chamber 2 Air Temperature')
			plt.xlabel('Date')
			plt.ylabel('Air Temperature')
			plt.title('Chamber 2 Air Temperature')
			plt.legend()
			plt.show()


	def reset():	

		chamber1.deselect()
		chamber2.deselect()
		chamber3.deselect()
		chamber4.deselect()
		chamber5.deselect()
		airTempH.deselect()
		airTempD.deselect()
		waterTemp.deselect()
		panTemp.deselect()

	graphButton = Button(root, text="GRAPH", bg="lightblue", font = ("calibri", 12, "bold"),fg="blue", width=20, command=graph)
	graphButton.place(x = 90, y = 310)

	resetButton = Button(root, text="CLEAR", bg="lightgreen", font = ("calibri", 12, "bold"), fg="blue", width=20, command=reset)
	resetButton.place(x = 90, y = 350)



	
	


	root.mainloop()	

main() 
