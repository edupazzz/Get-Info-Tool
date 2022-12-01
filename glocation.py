""" Using the open weather API """
###########################################################################
import os
import requests
from show_function import show
from dotenv import load_dotenv
###########################################################################
load_dotenv()
API_Key = os.environ.get('API_KEY')
###########################################################################
# defines what we are request to the API
def defineApiRequest(userRequest, _city=' ', lat=' ', lon=' '):
	if userRequest == '1': # if user request by the Long and Lat method
		reqString = f"lat={lat}&lon={lon}"
	elif userRequest == '2': # if user request by the city name
		reqString = f"&q={_city}"

	base_url = f"http://api.openweathermap.org/data/2.5/weather?{reqString}&appid={API_Key}"
	weather_data = requests.get(base_url).json()
	show(weather_data)
###########################################################################
# getInput() get the user Input. Chose to send lat and lon or city name 
def getInput(condition):
	os.system('clear')

	if condition == '1':
		lat = input("Latitude.: ")
		lon = input("Longitude: ")
		defineApiRequest(condition, ' ', lat, lon)

	elif condition == '2':
		_city = input("City: ")
		defineApiRequest(condition, _city, ' ', ' ')
	else:
		print("No Longer Avaliable!\n")
################################################################################
# Definition for the get_location() function
def get_location():
	os.system('clear')

	print("[1] Send Lon-Lat\n[2] Send Name\n")
	user_choise = input(">>> ")
	getInput(user_choise)
