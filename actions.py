import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from typing import Any, Text, Dict,Union, List ## Datatipos

from rasa_sdk import Action, Tracker  ##
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import SlotSet, UserUtteranceReverted, ActionReverted, FollowupAction
from rasa_sdk.events import SlotSet, UserUtteranceReverted, ActionReverted, FollowupAction
import json

class ActionSearch(Action):

    def name(self) -> Text:
        return "action_search"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        return []

class SearchForm(FormAction):
    def name(self) -> Text:
        return "search_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        if tracker.get_slot('tipo') == 'album':
            return ["album"]
        elif tracker.get_slot('tipo') == 'artista':
            return ["artista"]
        elif tracker.get_slot('tipo') == 'playlist':
            return ["playlist"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {"album":[self.from_text()],
        "artista":[self.from_text()],
        "playlist":[self.from_text()]}

    def validate_artista(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        
        intent = tracker.latest_message.get["intent"].get("name")
        if intent == 'goodbye':
            return self.deactivate()
        
        if value.lower() != None:
            return {"artista": value}
        else:
            dispatcher.utter_message(text="Por favor! Insira novamante somente o nome")
            return {"artista": None}

    def validate_album(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        
        if value.lower() != None:
            return {"album": value}
        else:
            dispatcher.utter_message(text="nao funcionou")
            return {"album": None}

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        
        sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="0f3025c5fd314da4bafae9d7cc81a133",
                                                         client_secret="6b0f4769be3e4924877b71fcc03a3ac1"))

        
        artista = tracker.get_slot('artista')
        album_tracker = tracker.get_slot('album')
        if artista != None:
            artist_response = sp.search(artista, limit=10, offset=0, type='artist', market=None)
            if len(artist_response['artists']['items']) != 0:
                button = [{"title":artista_item["name"],"payload": "/{}{}".format("search_tipo",json.dumps({"tipo":"album","album":artista_item["id"]})) } for artista_item in artist_response['artists']['items']]
                dispatcher.utter_message(text="Aqui estao alguns resultados:", buttons=button, button_type='vertical')
                return [SlotSet('artista',None),SlotSet('tipo','album')]
            else:
                dispatcher.utter_message(text="Por favor! Insira novamante somente o nome")
            
        if album_tracker != None:
            dispatcher.utter_message(text="Aqui estão algums albums do cantor:")
            albums_response = sp.artist_albums(album_tracker, album_type=None, country=None, limit=20, offset=0)
            i = 0
            if len(albums_response) != 0:
                while i < len(albums_response):
                    if albums_response["items"][i]["name"] != albums_response["items"][i - 1]["name"]:
                        dispatcher.utter_message(image=albums_response["items"][i]["images"][1]["url"])
                        dispatcher.utter_message(template="utter_link",link=albums_response["items"][i]["external_urls"]["spotify"])
                    i = i + 1
                dispatcher.utter_message(template="utter_finish")
                return [SlotSet('album',None)]
            else:
                dispatcher.utter_message(text="Não foi encontrado nenhum album!")
                dispatcher.utter_message(template="utter_finish")

        return [SlotSet('artista',None),SlotSet('album',None)]
        



class MyFallback(Action):

    def name(self) -> Text:
        return "action_my_fallback"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(template="utter_fallback")

        return []