# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions
# from typing import Text
# from rasa_sdk import Action
# from rasa_sdk.events import SlotSet
# import requests
#
# class ActionCheckWeather(Action):
#
#     def name(self) -> Text:
#         return "action_check_weather"
#
#     def run(self, dispatcher, tracker, domain):
#         location = tracker.get_slot("location")
#         if not location:
#             dispatcher.utter_message(response="utter_ask_location")
#             return []
#
#         api_key = "9561f082ff7e541f7018545a302becb8"
#         endpoint = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
#         response = requests.get(endpoint)
#         data = response.json()
#
#         if response.status_code == 200:
#             weather = data['weather'][0]['description']
#             temp = data['main']['temp'] - 273.15  # Convert from Kelvin to Celsius
#             dispatcher.utter_message(text=f"The current weather in {location} is {weather} with a temperature of {temp:.2f}°C.")
#         else:
#             dispatcher.utter_message(text=f"Sorry, I couldn't fetch the weather for {location}. Please try another location.")
#         return [SlotSet("location", location)]

