import pyttsx3
import pandas as pd
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import PySimpleGUI as sg

excel = pd.read_excel('Crop.xlsx', header = 0)
print(excel)
print(excel.shape)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-20)
engine.setProperty('voice',voices[0].id)


def speak(audio):
	engine.say(audio) 
	engine.runAndWait()


le = preprocessing.LabelEncoder()
crop = le.fit_transform(list(excel["CROP"]))

                                                    
NITROGEN = list(excel["NITROGEN"])
PHOSPHORUS = list(excel["PHOSPHORUS"])
POTASSIUM = list(excel["POTASSIUM"])
TEMPERATURE = list(excel["TEMPERATURE"])
HUMIDITY = list(excel["HUMIDITY"])
PH = list(excel["PH"])
RAINFALL = list(excel["RAINFALL"])


features = list(zip(NITROGEN, PHOSPHORUS, POTASSIUM, TEMPERATURE, HUMIDITY, PH, RAINFALL))
features = np.array([NITROGEN, PHOSPHORUS, POTASSIUM, TEMPERATURE, HUMIDITY, PH, RAINFALL])

features = features.transpose()
print(features.shape)
print(crop.shape)

model = KNeighborsClassifier(n_neighbors=3)
model.fit(features, crop)
layout = [[sg.Text('                      Crop Recommendation Assistant', font=("Helvetica", 30), text_color = 'yellow')],
         [sg.Text('Please enter the following details :-', font=("Helvetica", 20))],
         [sg.Text('Enter ratio of Nitrogen in the soil                                  :', font=("Helvetica", 20)), sg.Input(font=("Helvetica",20), size = (20,1) )],
         [sg.Text('Enter ratio of Phosphorous in the soil                           :', font=("Helvetica", 20)), sg.Input(font=("Helvetica", 20),size = (20,1))],
         [sg.Text('Enter ratio of Potassium in the soil                               :', font=("Helvetica", 20)), sg.Input(font=("Helvetica", 20),size = (20,1))],
         [sg.Text('Enter average Temperature value                                :', font=("Helvetica", 20)), sg.Input(font=("Helvetica", 20),size = (20,1)), sg.Text('*C', font=("Helvetica", 20))],
         [sg.Text('Enter average percentage of Humidity                         :', font=("Helvetica", 20)), sg.Input(font=("Helvetica", 20),size = (20,1)), sg.Text('%', font=("Helvetica", 20))],
         [sg.Text('Enter PH value of the soil                                            :', font=("Helvetica", 20)), sg.Input(font=("Helvetica", 20),size = (20,1))],
         [sg.Text('Enter average amount of Rainfall                                 :', font=("Helvetica", 20) ), sg.Input(font=("Helvetica", 20),size = (20,1)),sg.Text('mm', font=("Helvetica", 20))],
         [sg.Text(size=(50,1),font=("Helvetica",20) , text_color = 'yellow', key='-OUTPUT1-' )],
         [sg.Button('Submit', font=("Helvetica", 20)),sg.Button('Quit', font=("Helvetica", 20))] ]
window = sg.Window('Crop Recommendation', layout)

while True: 
	event, values = window.read()
	if event == sg.WINDOW_CLOSED or event == 'Quit':
		print(values[0])
	nitrogen_content =         values[0]
	phosphorus_content =       values[1]
	potassium_content =        values[2]
	temperature_content =      values[3]
	humidity_content =         values[4]
	ph_content =               values[5]
	rainfall =                 values[6]
	predict1 = np.array([nitrogen_content,phosphorus_content, potassium_content, temperature_content, humidity_content, ph_content, rainfall],dtype='float32')
	print(predict1)
	predict1 = predict1.reshape(1,-1)
	print(predict1)
	predict1 = model.predict(predict1)
	print(predict1)
	crop_name = str()
	if predict1 == 0:
		crop_name = 'Apple'
	elif predict1 == 1:
		crop_name = 'Banana'
	elif predict1 == 2:
		crop_name = 'Blackgram'
	elif predict1 == 3:
		crop_name = 'Chickpea'
	elif predict1 == 4:
		crop_name = 'Coconut'
	elif predict1 == 5:
		crop_name = 'Coffee'
	elif predict1 == 6:
		crop_name = 'Cotton'
	elif predict1 == 7:
		crop_name = 'Grapes'
	elif predict1 == 8:
		crop_name = 'Jute'
	elif predict1 == 9:
		crop_name = 'Kidneybeans'
	elif predict1 == 10:
		crop_name = 'Lentil'
	elif predict1 == 11:
		crop_name = 'Maize'
	elif predict1 == 12:
		crop_name = 'Mango'
	elif predict1 == 13:
		crop_name = 'Mothbeans'
	elif predict1 == 14:
		crop_name = 'Mungbeans'
	elif predict1 == 15:
		crop_name = 'Muskmelon'
	elif predict1 == 16:
		crop_name = 'Orange'
	elif predict1 == 17:
		crop_name = 'Papaya'
	elif predict1 == 18:
		crop_name = 'Pigeonpeas'
	elif predict1 == 19:
		crop_name = 'Pomegranate'
	elif predict1 == 20:
		crop_name = 'Rice'
	elif predict1 == 21:
		crop_name = 'Watermelon'

	if int(humidity_content) >=1 and int(humidity_content)<= 33 :
		humidity_level = 'low humid'
	elif int(humidity_content) >=34 and int(humidity_content) <= 66:
		humidity_level = 'medium humid'
	else:
		humidity_level = 'high humid'

	if int(temperature_content) >= 0 and int(temperature_content)<= 6:
		temperature_level = 'cool'
	elif int(temperature_content) >=7 and int(temperature_content) <= 25:
		temperature_level = 'warm'
	else:
		temperature_level= 'hot' 

	if int(rainfall) >=1 and int(rainfall) <= 100:
		rainfall_level = 'less'
	elif int(rainfall) >= 101 and int(rainfall) <=200:
		rainfall_level = 'moderate'
	elif int(rainfall) >=201:
		rainfall_level = 'heavy rain'

	if int(nitrogen_content) >= 1 and int(nitrogen_content) <= 50:
		nitrogen_level = 'less'
	elif int(nitrogen_content) >=51 and int(nitrogen_content) <=100:
		nitrogen_level = 'not to less but also not to high'
	elif int(nitrogen_content) >=101:
		nitrogen_level = 'high'

	if int(phosphorus_content) >= 1 and int(phosphorus_content) <= 50:
		phosphorus_level = 'less'
	elif int(phosphorus_content) >= 51 and int(phosphorus_content) <=100:
		phosphorus_level = 'not to less but also not to high'
	elif int(phosphorus_content) >=101:
		phosphorus_level = 'high'

	if int(potassium_content) >= 1 and int(potassium_content) <=50:
		potassium_level = 'less'
	elif int(potassium_content) >= 51 and int(potassium_content) <= 100:
		potassium_level = 'not to less but also not to high'
	elif int(potassium_content) >=101:
		potassium_level = 'high'

	if float(ph_content) >=0 and float(ph_content) <=5:
		phlevel = 'acidic' 
	elif float(ph_content) >= 6 and float(ph_content) <= 8:
		phlevel = 'neutral'
	elif float(ph_content) >= 9 and float(ph_content) <= 14:
		phlevel = 'alkaline'
	
	print(crop_name)
	print(humidity_level)
	print(temperature_level)
	print(rainfall_level)
	print(nitrogen_level)
	print(phosphorus_level)
	print(potassium_level)
	print(phlevel)
	
	speak("Sir according to the data that you provided to me. The ratio of nitrogen in the soil is  " + nitrogen_level + ". The ratio of phosphorus in the soil is  " + phosphorus_level + ". The ratio of potassium in the soil is  " + potassium_level + ". The temperature level around the field is  " + temperature_level + ". The humidity level around the field is  " + humidity_level + ". The ph type of the soil is  " + phlevel + ". The amount of rainfall is  " + rainfall_level )
	window['-OUTPUT1-'].update('The best crop that you can grow : ' + crop_name )
	speak("The best crop that you can grow is  " + crop_name)


	

window.close() 

