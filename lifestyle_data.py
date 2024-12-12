import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# lifestyle_data.py
class LifestyleData:
    def __init__(self, root=None, app=None, lifestyle_data_id=None, user_id=None, collection_date=None, diet_info=None, exercise_info=None, sleep_info=None):
        """
        Initializes a new instance of the LifestyleData class.

        Args:
            root (tk.Tk, optional): The root window of the Tkinter application.
            app (object, optional): The main application object.
            lifestyle_data_id (int, optional): The ID of the lifestyle data record.
            user_id (int, optional): The ID of the user.
            collection_date (str, optional): The date the lifestyle data was collected.
            diet_info (str, optional): Information about the user's diet.
            exercise_info (str, optional): Information about the user's exercise habits.
            sleep_info (str, optional): Information about the user's sleep patterns.
        """
        self.root = root
        self.app = app
        self.lifestyle_data_id = lifestyle_data_id
        self.user_id = user_id
        self.collection_date = collection_date
        self.diet_info = diet_info
        self.exercise_info = exercise_info
        self.sleep_info = sleep_info

    def collect_data(self):
        """
        Collects lifestyle data and assigns placeholder values.
        """
        print("Collecting lifestyle data...")
        self.diet_info = "vegetarian"  # Placeholder diet information
        self.exercise_info = "daily running"  # Placeholder exercise information
        self.sleep_info = "7 hours"  # Placeholder sleep information
        self.collection_date = datetime.now().strftime("%Y-%m-%d")  # Current date
        print("Lifestyle data collected")

    def show_lifestyle_data(self):
        """
        Displays the lifestyle data UI.
        """
        if self.app:
            self.app.clear_frame()
            
            # Create a frame for displaying lifestyle data
            lifestyle_data_frame = tk.Frame(self.root)
            lifestyle_data_frame.pack(pady=20)

            # Add a label for the lifestyle data title
            tk.Label(lifestyle_data_frame, text="Lifestyle Data", font=("Helvetica", 16)).pack(pady=10)

            # Display each piece of lifestyle data
            for key, value in self.app.lifestyle_data.items():
                tk.Label(lifestyle_data_frame, text=f"{key}: {value}").pack(pady=5)

            # If the user is not a healthcare provider, show a back button
            if not self.app.is_healthcare_provider:
                tk.Button(lifestyle_data_frame, text="Back to Dashboard", command=self.app.show_dashboard).pack(pady=20)
                return

            # Allow healthcare providers to modify lifestyle data
            tk.Label(lifestyle_data_frame, text="Modify Diet:").pack(pady=5)
            diet_entry = tk.Entry(lifestyle_data_frame)
            diet_entry.pack(pady=5)
           
            tk.Label(lifestyle_data_frame, text="Modify Exercise:").pack(pady=5)
            exercise_entry = tk.Entry(lifestyle_data_frame)
            exercise_entry.pack(pady=5)
           
            tk.Label(lifestyle_data_frame, text="Modify Sleep Patterns:").pack(pady=5)
            sleep_entry = tk.Entry(lifestyle_data_frame)
            sleep_entry.pack(pady=5)

            def submit_lifestyle_data():
                """
                Submits the modified lifestyle data.
                """
                new_diet = diet_entry.get()
                new_exercise = exercise_entry.get()
                new_sleep = sleep_entry.get()
               
                # Update the lifestyle data with new values if provided
                self.app.lifestyle_data["Diet"] = new_diet if new_diet else self.app.lifestyle_data["Diet"]
                self.app.lifestyle_data["Exercise"] = new_exercise if new_exercise else self.app.lifestyle_data["Exercise"]
                self.app.lifestyle_data["Sleep Patterns"] = new_sleep if new_sleep else self.app.lifestyle_data["Sleep Patterns"]
                self.app.lifestyle_data["Date Logged"] = datetime.now().strftime("%Y-%m-%d")
               
                # Show a message box with the submitted lifestyle data
                messagebox.showinfo("Lifestyle Data", f"Submitted: {self.app.lifestyle_data}")

            # Add submit and back buttons
            tk.Button(lifestyle_data_frame, text="Submit Lifestyle Data", command=submit_lifestyle_data).pack(pady=20)
            tk.Button(lifestyle_data_frame, text="Back to Dashboard", command=self.app.show_dashboard).pack(pady=20)