from typing import Any, Text, Dict, List
from rasa_sdk import Action
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from rasa_sdk.interfaces import Tracker  # Import Tracker class

class ActionListGames(Action):
    def name(self) -> Text:
        return "action_list_games"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # List of games
        games = [
            "Chess", "Poker", "Sudoku", "Monopoly", "Scrabble",
            "Checkers", "Blackjack", "Fortnite", "Minecraft", "Candy Crush"
        ]
        # Format the list of games
        game_list = "\n".join([f"{index + 1}. {game}" for index, game in enumerate(games)])
        dispatcher.utter_message(text=f"Here are the available games:\n{game_list}")
        return []

class ActionSearchGame(Action):
    def name(self) -> Text:
        return "action_search_game"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Get the game name from the slot
        game_name = tracker.get_slot("game_name")
        
        if game_name:
            dispatcher.utter_message(text=f"Searching for the game '{game_name}'.")
            # In a real use case, you can integrate a game database or API search here
        else:
            dispatcher.utter_message(text="Please provide the name of the game you want to search for.")
        return []

class ActionFeedback(Action):
    def name(self) -> Text:
        return "action_feedback"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Thank you for your feedback! We appreciate your input.")
        return []
