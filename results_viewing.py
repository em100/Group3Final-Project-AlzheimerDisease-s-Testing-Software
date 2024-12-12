import tkinter as tk
from tkinter import messagebox

# results_viewing.py
class ResultsViewing:
    def __init__(self, root, app):
        """
        Initializes a new instance of the ResultsViewing class.

        Args:
            root (tk.Tk): The root window of the Tkinter application.
            app (object): The main application object.
        """
        self.root = root
        self.app = app

    def show_view_results(self):
        """
        Displays the results viewing UI.
        """
        # Clear the current frame
        self.app.clear_frame()
        
        # Create a frame for viewing results
        view_results_frame = tk.Frame(self.root)
        view_results_frame.pack(pady=20)

        # Add a label for the view results title
        tk.Label(view_results_frame, text="View Results", font=("Helvetica", 16)).pack(pady=10)

        # Display cognitive test results if available
        if self.app.cognitive_test_results:
            for key, value in self.app.cognitive_test_results.items():
                tk.Label(view_results_frame, text=f"{key}: {value}").pack(pady=5)

        # Add buttons for cognitive, genetic, and lifestyle data
        cognitive_button = tk.Button(view_results_frame,
                                     text="Cognitive Data",
                                     command=lambda: messagebox.showinfo("Cognitive Data", "Submitted"))
        cognitive_button.pack(pady=10)

        genetic_button = tk.Button(view_results_frame,
                                   text="Genetic Data",
                                   command=lambda: messagebox.showinfo("Genetic Data", "Submitted"))
        genetic_button.pack(pady=10)

        lifestyle_button = tk.Button(view_results_frame,
                                     text="Lifestyle Data",
                                     command=lambda: messagebox.showinfo("Lifestyle Data", "Submitted"))
        lifestyle_button.pack(pady=10)

        # Add a button to go back to the dashboard
        tk.Button(view_results_frame, text="Back to Dashboard", command=self.app.show_dashboard).pack(pady=20)