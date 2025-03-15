import re


class QASystem:
    """
    A simple question-answering system for handling player questions
    about the game and related topics.
    """

    def __init__(self):
        """
        Initialize the QA system with knowledge base.
        """
        self.knowledge_base = {
            # Space and moon-related questions
            "moon":
            "The Moon is Earth's only natural satellite. It has a diameter of about 2,159 miles (3,475 km) and is about 238,855 miles (384,400 km) from Earth.",
            "gravity":
            "The Moon's gravity is about 1/6th of Earth's gravity, which is why astronauts can jump so high on the lunar surface.",
            "lunar exploration":
            "Human exploration of the Moon began with the Apollo program. Apollo 11 was the first crewed mission to land on the Moon on July 20, 1969.",
            "lava tubes":
            "Lunar lava tubes are tunnel-like structures formed by ancient flowing lava on the Moon. They could potentially serve as natural shelters for future human habitation, protecting from radiation, micrometeorites, and extreme temperature fluctuations.",

            # Game-specific questions
            "game":
            "Cosmic Odyssey is a text-based adventure game where you play as an astronaut exploring the lunar surface.",
            "save":
            "You can save your game progress by clicking the 'Save Game' button. This will allow you to continue from where you left off later.",
            "load":
            "To continue a saved game, click the 'Load Game' button to restore your previous progress.",
            "controls":
            "Use the buttons to navigate through the game. Make choices by clicking on the option buttons. Save, load, access help, or ask questions using the control buttons at the bottom of the screen.",

            # Preset specific answers for the question boxes
            "what is the moon made of?":
            "The Moon is primarily made of rocky material similar to Earth's mantle. Its crust consists mainly of oxygen, silicon, magnesium, iron, calcium, and aluminum. Unlike Earth, the Moon has no atmosphere, water, or life as we know it. Scientists believe the Moon formed about 4.5 billion years ago after a Mars-sized body collided with Earth.",
            "how do astronauts survive on the moon?":
            "Astronauts survive on the Moon using specialized spacesuits that provide oxygen, regulate temperature, and protect from radiation and micrometeorites. The suits are pressurized since the Moon has no atmosphere. Lunar habitats for longer stays would need to be sealed, with life support systems that recycle air and water, and protection from extreme temperature fluctuations and cosmic radiation.",
            "how do i save my game progress?":
            "To save your game progress, simply click the 'Save Game' button at the bottom of the game screen. Your current position in the story and all your choices will be saved. When you return later, you can click 'Load Game' to continue exactly where you left off. The game automatically creates a save file on your computer.",
            "what is the goal of this game?":
            "The goal of Cosmic Odyssey is to explore the lunar surface and uncover its mysteries, while also inspiring young people to get excited about space exploration. This game was created to make space science more engaging and accessible for students and young adults through an interactive adventure. As an astronaut on a mission to the Moon, you'll make choices that affect your journey, investigate strange phenomena, and potentially make groundbreaking discoveries. By experiencing the challenges and wonders of lunar exploration firsthand in this game, we hope to spark curiosity about real-world space missions and encourage the next generation of scientists, engineers, and astronauts.",
            "tell me about lunar exploration history":
            "Lunar exploration began with the Soviet Luna 2 mission in 1959, the first spacecraft to reach the Moon. The United States' Apollo program achieved the first human landing with Apollo 11 in 1969, when Neil Armstrong and Buzz Aldrin walked on the lunar surface. Five more successful Apollo landings followed through 1972. After a long gap, exploration resumed in the 1990s with orbiter missions from various countries. Recently, China's Chang'e missions, including a far-side landing in 2019, and NASA's Artemis program represent humanity's renewed interest in returning to the Moon."
        }

        # Default response for questions that don't match any patterns
        self.default_response = "I don't have specific information about that. Try asking about the moon, lunar exploration, lava tubes, or game controls."

    def get_response(self, question):
        """
        Analyze the question and return the most appropriate response.

        Args:
            question (str): The user's question

        Returns:
            str: The response to the question
        """
        # Check for exact match first (for preset questions)
        if question in self.knowledge_base:
            return self.knowledge_base[question]

        # Convert question to lowercase for easier matching
        question_lower = question.lower().strip()

        # Return immediately if the question is empty
        if not question_lower or question_lower.isspace():
            return "Please ask a question about the game or lunar exploration."

        # Try lowercase matching
        if question_lower in self.knowledge_base:
            return self.knowledge_base[question_lower]

        # Check for keywords in the question
        for keyword in [
                "moon", "gravity", "lunar exploration", "lava tubes", "game",
                "save", "load", "controls"
        ]:
            if keyword in question_lower:
                return self.knowledge_base[keyword]

        # Default response if no matches found
        return self.default_response
