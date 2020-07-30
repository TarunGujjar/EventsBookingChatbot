# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
#
import numpy as np
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import sqlite3
import smtplib
#
class EventDescription(Action):

    def name(self) -> Text:
        return "event_description"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        global exe_str
        conn = sqlite3.connect('event_list.db')
        user_message = str((tracker.latest_message)['text'])

        print("user_message : ", user_message)
        Event_name = ''
        if "Lolbagh" in user_message:
            exe_str = "Select Events_description, Price from events_details where Events_name is '{0}'".format('Lolbagh')
            Event_name = "Lolbagh"

        elif 'Concert Night by Arijit Singh' in user_message:
            exe_str = "Select Events_description, Price from events_details where Events_name is '{0}'".format(
                'Concert Night by Arijit Singh')
            Event_name = "Concert Night by Arijit Singh"

        elif 'Stand Up Comedy by Abhishek Upmanyu' in user_message:
            exe_str = "Select Events_description, Price from events_details where Events_name is '{0}'".format(
                'Stand Up Comedy by Abhishek Upmanyu')
            Event_name = "Stand Up Comedy by Abhishek Upmanyu"

        elif 'Nucleya' in user_message:
            exe_str = "Select Events_description, Price from events_details where Events_name is '{0}'".format('Nucleya')
            Event_name = "Nucleya"

        elif 'Bangalore Open Air 2020' in user_message:
            exe_str = "Select Events_description, Price from events_details where Events_name is '{0}'".format(
                'Bangalore Open Air 2020')
            Event_name = "Bangalore Open Air 2020"

        content = conn.execute(exe_str)
        content = list(content)

        msg = str(content[0][0]) + "\nPrice : Rs. " + str(content[0][1])

        dispatcher.utter_message(text=msg)

        return []



class EventTotal(Action):

    def name(self) -> Text:
        return "event_total"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        global exe_str
        conn = sqlite3.connect('event_list.db')
        user_message = str((tracker.latest_message)['text'])

        messages = []
        for event in (list(tracker.events)):
            if event.get("event") == "user":
                messages.append(event.get("text"))

        user_event = messages[-3]
        print("user_event : ", user_event)
        Event_name = ''
        if "Lolbagh" in user_event:
            exe_str = "Select Price from events_details where Events_name is '{0}'".format('Lolbagh')
            Event_name = "Lolbagh"

        elif 'Concert Night by Arijit Singh' in user_event:
            exe_str = "Select Price from events_details where Events_name is '{0}'".format('Concert Night by Arijit Singh')
            Event_name = "Concert Night by Arijit Singh"

        elif 'Stand Up Comedy by Abhishek Upmanyu' in user_event:
            exe_str = "Select Price from events_details where Events_name is '{0}'".format('Stand Up Comedy by Abhishek Upmanyu')
            Event_name = "Stand Up Comedy by Abhishek Upmanyu"

        elif 'Nucleya' in user_event:
            exe_str = "Select Price from events_details where Events_name is '{0}'".format('Nucleya')
            Event_name = "Nucleya"

        elif 'Bangalore Open Air 2020' in user_event:
            exe_str = "Select Price from events_details where Events_name is '{0}'".format('Bangalore Open Air 2020')
            Event_name = "Bangalore Open Air 2020"


        content = conn.execute(exe_str)
        content = list(content)

        price = str(content[0][0])
        user_total = int(user_message) * int(price)
        content = "Number of tickets selected is " + user_message + ".\nYour total price for the event " + Event_name + \
                  " is Rs. " + str(user_total)

        dispatcher.utter_message(text=content)

        return[]



class EmailTickets(Action):

    def name(self) -> Text:
        return "email_total"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        global exe_str
        print("Inside actions")
        conn = sqlite3.connect('event_list.db')
        user_message = str((tracker.latest_message)['text'])

        messages = []
        for event in (list(tracker.events)):
            if event.get("event") == "user":
                messages.append(event.get("text"))

        user_message = messages[-4]
        user_tic = messages[-2]
        print("user_message : ", user_message)
        Event_name = ''
        if "Lolbagh" in user_message:
            exe_str = "Select Events_description, Price from events_details where Events_name is '{0}'".format('Lolbagh')
            Event_name = "Lolbagh"

        elif 'Concert Night by Arijit Singh' in user_message:
            exe_str = "Select Events_description, Price from events_details where Events_name is '{0}'".format('Concert Night by Arijit Singh')
            Event_name = "Concert Night by Arijit Singh"

        elif 'Stand Up Comedy by Abhishek Upmanyu' in user_message:
            exe_str = "Select Events_description, Price from events_details where Events_name is '{0}'".format('Stand Up Comedy by Abhishek Upmanyu')
            Event_name = "Stand Up Comedy by Abhishek Upmanyu"

        elif 'Nucleya' in user_message:
            exe_str = "Select Events_description, Price from events_details where Events_name is '{0}'".format('Nucleya')
            Event_name = "Nucleya"

        elif 'Bangalore Open Air 2020' in user_message:
            exe_str = "Select Events_description, Price from events_details where Events_name is '{0}'".format('Bangalore Open Air 2020')
            Event_name = "Bangalore Open Air 2020"

        try:
            content = conn.execute(exe_str)
            content = list(content)

            content_des = str(content[0][0])
            content_price = str(content[0][1])

            content_price = str(int(user_tic) * int(content_price))

            user_message = str((tracker.latest_message)['text'])
            user_message = user_message.strip()

            no1 = np.random.randint(1000, 9999, 1)[0]
            no2 = np.random.randint(1000, 9999, 1)[0]
            no3 = np.random.randint(10, 100, 1)[0]
            unq_id = no1 + no2 + no3

            fromaddr = '@gmail.com'
            toaddrs = str(user_message)
            text = "The ticket has been booked for the event " + Event_name + ".\n\nDetails of the event : " + content_des + \
                   ".\n\nNumber of tickets booked : " + user_tic + "\nPrice : Rs. " + content_price + \
                   "/-\n\n\nShow this unique code at the entrance. UNIQUE CODE - " + str(unq_id) + "\n\nThank you."
            sub = "Events.org"
            msg = "Subject: {}\n\n{}".format(sub, text)
            obj = open('pass.txt')
            password = obj.read()
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(fromaddr, password)
            server.sendmail(fromaddr, toaddrs, msg)
            server.quit()

            content_text = "Your ticket has been booked for the event " + Event_name + ".\nDetails of the event : " + content_des\
                           + ".\nPrice is Rs. " + content_price
            content = "Confirmation for the same has been sent through the mail"
            dispatcher.utter_message(text=content_text)
            dispatcher.utter_message(text=content)


        except:
            content_text = "Sorry system run into trouble.. Can you please check again?"
            dispatcher.utter_message(text=content_text)

        return[]