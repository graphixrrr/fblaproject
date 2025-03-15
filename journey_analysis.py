
"""
Journey Analysis module for tracking player progress in Cosmic Odyssey
"""

class JourneyAnalysis:
    """
    Simple class to track and analyze player journey through the game
    """
    def __init__(self):
        """Initialize with empty journey data"""
        self.path_taken = []
        self.decision_points = 0
        
    def add_scene(self, scene_name):
        """Record a new scene visited by the player"""
        self.path_taken.append(scene_name)
        self.decision_points += 1
        
    def get_analysis(self):
        """Generate a simple analysis of the player's journey"""
        if not self.path_taken:
            return "Your journey has not yet begun."
            
        analysis = {
            "scenes_visited": len(self.path_taken),
            "path_taken": self.path_taken,
            "journey_length": f"{len(self.path_taken)} scenes explored"
        }
        
        return analysis
