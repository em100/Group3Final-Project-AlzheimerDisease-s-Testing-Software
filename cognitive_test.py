import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# cognitive_test.py
class CognitiveTest:
    def __init__(self, test_id=None, user_id=None, test_type=None, score=None, date_taken=None):
        """
        Initializes a new instance of the CognitiveTest class.

        Args:
            test_id (int, optional): The ID of the test.
            user_id (int, optional): The ID of the user taking the test.
            test_type (str, optional): The type of cognitive test.
            score (float, optional): The score of the test.
            date_taken (str, optional): The date the test was taken.
        """
        self.test_id = test_id
        self.user_id = user_id
        self.test_type = test_type
        self.score = score
        self.date_taken = date_taken

    def administer_test(self):
        """
        Administers the cognitive test and assigns a placeholder score.
        """
        print("Administering cognitive test...")
        self.score = 95.0  # Placeholder score
        print("Cognitive test administered")

class CognitiveTestUI:
    def __init__(self, root, app):
        """
        Initializes a new instance of the CognitiveTestUI class.

        Args:
            root (tk.Tk): The root window of the Tkinter application.
            app (object): The main application object.
        """
        self.root = root
        self.app = app

    def show_cognitive_test(self):
        """
        Displays the cognitive test UI.
        """
        self.app.clear_frame()
        
        # Create a frame for the cognitive test
        cognitive_test_frame = tk.Frame(self.root)
        cognitive_test_frame.pack(pady=20)

        # Add a label for the cognitive test title
        tk.Label(cognitive_test_frame, text="Cognitive Test", font=("Helvetica", 16)).pack(pady=10)

        # List of questions for the cognitive test
        questions = [
            "What is the capital of France?",
            "What is 5 + 7?",
            "Name a primary color.",
            "What is the opposite of 'hot'?",
            "What is the square root of 16?"
        ]

        self.answers = []

        # Create entry fields for each question
        for question in questions:
            tk.Label(cognitive_test_frame, text=question).pack(pady=5)
            answer_entry = tk.Entry(cognitive_test_frame)
            answer_entry.pack(pady=5)
            self.answers.append(answer_entry)

        # Add submit and back buttons
        tk.Button(cognitive_test_frame, text="Submit", command=self.submit_cognitive_test).pack(pady=10)
        tk.Button(cognitive_test_frame, text="Back to Dashboard", command=self.app.show_dashboard).pack(pady=10)

    def submit_cognitive_test(self):
        """
        Submits the cognitive test and calculates the score.
        """
        # List of correct answers
        correct_answers = ["Paris", "12", "Red", "Cold", "4"]
        
        score = 0
        # Calculate the score based on correct answers
        for answer_entry, correct_answer in zip(self.answers, correct_answers):
            if answer_entry.get().strip().lower() == correct_answer.lower():
                score += 20  # Each question is worth 20 points

        # Get the current date
        current_date = datetime.now().strftime("%Y-%m-%d")
        
        # Store the test results in the app object
        self.app.cognitive_test_results = {
            "Test Type": "memory",
            "Score": score,
            "Date Taken": current_date
        }
        
        # Show the test result in a message box
        messagebox.showinfo("Cognitive Test Result", f"Your score is {score}. Date Taken: {current_date}")
        # Stay on the cognitive test page after submission
        self.show_cognitive_test()