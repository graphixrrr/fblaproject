import json # Importing JSON module for saving and loading game state
import os  # Importing OS module to check file existence
from story_data import STORY_DATA # Importing story data containing scenes and choices
from ascii_art import SCENE_ART # Importing ASCII art for scenes
from journey_analysis import JourneyAnalysis # Importing journey analysis

class GameEngine:
    """
    Game engine class that manages the game state, player choices,
    and handles saving/loading functionality for the Cosmic Odyssey game.
    """
    def __init__(self):
        """
        Initialize a new game with the starting scene and empty visited scenes list.
        """
        self.current_scene = "start" # The game begins at the 'start' scene
        self.visited_scenes = [] # List to track previously visited scenes
        self.journey_analyzer = JourneyAnalysis() # Initialize journey analyzer

    def get_scene_data(self):
        """
        Retrieves data for the current scene and adds ASCII art if available.

        Returns:
            dict: Scene data including description, choices, and ASCII art
        """
        scene_data = STORY_DATA.get(self.current_scene, {}).copy() # Copy scene data to avoid modifying original data

        # Add ASCII art to the scene if available in SCENE_ART dictionary
        scene_data['ascii_art'] = SCENE_ART.get(self.current_scene, '')

        # Add is_end flag if there are no choices
        scene_data['is_end'] = len(scene_data.get('choices', [])) == 0

        # Add congratulations message if this is an end scene
        if scene_data['is_end']:
            scene_data['congratulations'] = "Congratulations on completing your lunar mission!"

        return scene_data

    def start_game(self):
        """
        Start a new game and return the initial scene data.
        
        Returns:
            dict: Initial scene data
        """
        self.current_scene = "start" # Reset to the starting scene
        self.visited_scenes = [] # Clear visited scenes history
        return self.get_scene_data() # Return the starting scene data

    def make_choice(self, choice_index):
        """
        Process a player's choice and update the game state accordingly.

        Args:
            choice_index (int): The index of the chosen option

        Returns:
            dict: Updated scene data
        """
        current_scene_data = STORY_DATA.get(self.current_scene, {}) # Get data for the current scene
        choices = current_scene_data.get("choices", []) # Get available choices for the current scene

        # Ensure the choice index is valid before proceeding
        if 0 <= choice_index < len(choices):
            next_scene = choices[choice_index].get("next_scene") # Get next scene from choice
            self.visited_scenes.append(self.current_scene)  # Track the visited scene
            self.current_scene = next_scene # Update current scene to the next one
            self.journey_analyzer.add_scene(next_scene) # Record this scene for journey analysis

        return self.get_scene_data() # Return data for the new scene
        
    def get_journey_analysis(self):
        """
        Get analysis of the player's journey so far.
        
        Returns:
            dict: Analysis of player's journey
        """
        return self.journey_analyzer.get_analysis()

    def save_game(self):
        """
        Save the current game state to a JSON file.
        """
        save_data = {
            "current_scene": self.current_scene,  # Store the current scene
            "visited_scenes": self.visited_scenes # Store the visited scenes
        }
        with open("save_game.json", "w") as f: # Open file in write mode
            json.dump(save_data, f) # Save data in JSON format

    def load_game(self):
        """
        Load a previously saved game state from a JSON file.

        Returns:
            dict: Scene data after loading
        """
        try:
            if os.path.exists("save_game.json"): # Check if the save file exists
                with open("save_game.json", "r") as f: # Open file in read mode
                    save_data = json.load(f) # Load saved data
                    self.current_scene = save_data.get("current_scene", "start") # Restore current scene
                    self.visited_scenes = save_data.get("visited_scenes", []) # Restore visited scenes
        except (FileNotFoundError, json.JSONDecodeError):
            # If no save file or corrupted, keep current state
            pass

        return self.get_scene_data() # Return current scene data

    def end_game(self):
        """
        End the current game and show game over screen.
        
        Returns:
            dict: Game over scene data
        """
        self.current_scene = "game_over" # Set the current scene to game over

        # Return game over scene data
        return self.get_scene_data()
