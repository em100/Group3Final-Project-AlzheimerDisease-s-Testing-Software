import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# genetic_data.py
class GeneticData:
    def __init__(self, root=None, app=None, genetic_data_id=None, user_id=None, collection_date=None, genetic_markers=None):
        """
        Initializes a new instance of the GeneticData class.

        Args:
            root (tk.Tk, optional): The root window of the Tkinter application.
            app (object, optional): The main application object.
            genetic_data_id (int, optional): The ID of the genetic data record.
            user_id (int, optional): The ID of the user.
            collection_date (str, optional): The date the genetic data was collected.
            genetic_markers (str, optional): The genetic markers identified.
        """
        self.root = root
        self.app = app
        self.genetic_data_id = genetic_data_id
        self.user_id = user_id
        self.collection_date = collection_date
        self.genetic_markers = genetic_markers

    def collect_data(self):
        """
        Collects genetic data and assigns a placeholder genetic marker.
        """
        print("Collecting genetic data...")
        self.genetic_markers = "APOE4"  # Placeholder genetic marker
        print("Genetic data collected")

    def show_genetic_data(self):
        """
        Displays the genetic data UI.
        """
        if self.app:
            self.app.clear_frame()
            
            # Create a frame for displaying genetic data
            genetic_data_frame = tk.Frame(self.root)
            genetic_data_frame.pack(pady=20)

            # Add a label for the genetic data title
            tk.Label(genetic_data_frame, text="Genetic Data", font=("Helvetica", 16)).pack(pady=10)

            # Display each piece of genetic data
            for key, value in self.app.genetic_data.items():
                tk.Label(genetic_data_frame, text=f"{key}: {value}").pack(pady=5)

            # If the user is not a healthcare provider, show a back button
            if not self.app.is_healthcare_provider:
                tk.Button(genetic_data_frame, text="Back to Dashboard", command=self.app.show_dashboard).pack(pady=20)
                return

            # Allow healthcare providers to modify genetic markers
            tk.Label(genetic_data_frame, text="Modify Markers Identified:").pack(pady=5)
            markers_entry = tk.Entry(genetic_data_frame)
            markers_entry.pack(pady=5)

            def submit_genetic_data():
                """
                Submits the modified genetic data.
                """
                new_markers = markers_entry.get()
                # Update the genetic markers if new markers are provided
                self.app.genetic_data["Markers Identified"] = new_markers if new_markers else self.app.genetic_data["Markers Identified"]
                # Update the date uploaded
                self.app.genetic_data["Date Uploaded"] = datetime.now().strftime("%Y-%m-%d")
                # Show a message box with the submitted genetic data
                messagebox.showinfo("Genetic Data", f"Submitted: {self.app.genetic_data}")

            # Add submit and back buttons
            tk.Button(genetic_data_frame, text="Submit Genetic Data", command=submit_genetic_data).pack(pady=20)
            tk.Button(genetic_data_frame, text="Back to Dashboard", command=self.app.show_dashboard).pack(pady=20)