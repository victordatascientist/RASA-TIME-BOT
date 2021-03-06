# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher



class ActionShowTimeZone(Action):

    def name(self) -> Text:
        return "action_show_time_zone"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict]:
       
        time = {"London": "UTC+1:00","Sofia": "UTC+1:3:00","Lisbon": "UTC+1:00","Mumbai": "UTC+5:30",}
        city = tracker.get_slot("city")
        time = time.get(city)

        if time is None:
            output = "Could not find the time zone of {}".format(city)
        else:
            output = "Time zone of {} is {}".format(city, time)    

        dispatcher.utter_message(output)

        return []