
from flask import Flask, send_from_directory, request, jsonify, session
from game_engine import GameEngine
from ascii_art import GAME_OVER
from qa_system import QASystem  # Import the QA system

# Initialize Flask application
app = Flask(__name__, static_folder='.')
app.secret_key = 'cosmic-odyssey-secret-key'  # Required for session management

# Create a global game engine instance
game_engine = GameEngine()

# Create a global QA system instance
qa_system = QASystem()

@app.route('/')
def index():
    """
    Route handler for the main page that renders the game interface.

    Returns:
        HTML: The game.html file
    """
    # Serve the main game HTML page
    return send_from_directory('.', 'game.html')

@app.route('/start_game', methods=['POST'])
def start_game():
    """
    Initializes a new game session when the player starts playing.

    Returns:
        JSON: Initial scene data including description and choices
    """
    # Start a new game with the game engine
    scene_data = game_engine.start_game()
    return jsonify(scene_data)

@app.route('/stop_game', methods=['POST'])
def stop_game():
    """
    Ends the current game session.

    Returns:
        JSON: Game over message and status
    """
    # End the game and display a game over message
    scene_data = game_engine.end_game()
    return jsonify(scene_data)

@app.route('/make_choice', methods=['POST'])
def make_choice():
    """
    Processes player choices, updates game state, and handles save/load operations.

    Returns:
        JSON: Updated scene data or confirmation message
    """
    data = request.get_json()  # Get JSON data from request

    # Handle save game request
    if data.get('save'):
        game_engine.save_game()
        return jsonify({'message': 'Game saved successfully!'})

    # Handle load game request
    elif data.get('load'):
        scene_data = game_engine.load_game()
        return jsonify(scene_data)

    # Handle player choice
    else:
        choice_index = int(data.get('choice', 0))
        scene_data = game_engine.make_choice(choice_index)
        return jsonify(scene_data)

@app.route('/ask_question', methods=['POST'])
def ask_question():
    """
    Processes player questions and returns answers from the QA system.
    
    Returns:
        JSON: Response to the player's question
    """
    data = request.get_json()  # Get JSON data from request
    question = data.get('question', '')
    
    # Get response from QA system
    response = qa_system.get_response(question)
    
    return jsonify({'response': response})
    
@app.route('/journey_analysis', methods=['GET'])
def journey_analysis():
    """
    Provides analysis of the player's journey through the game.
    
    Returns:
        JSON: Analysis data about player's journey
    """
    analysis = game_engine.get_journey_analysis()
    return jsonify({'analysis': analysis})

if __name__ == '__main__':
    # Starts the Flask application when script is run directly
    # Allows external access (0.0.0.0) and enables debugging mode
    app.run(host='0.0.0.0', port=8080, debug=True)
