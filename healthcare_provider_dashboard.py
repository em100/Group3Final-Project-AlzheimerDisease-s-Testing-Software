import tkinter as tk
from tkinter import messagebox
from views.lifestyle_data import LifestyleData
from views.genetic_data import GeneticData
from views.cognitive_test import CognitiveTestUI

# healthcare_provider_dashboard.py
class HealthcareProviderDashboard:
    def __init__(self, root, app):
        """
        Initializes a new instance of the HealthcareProviderDashboard class.

        Args:
            root (tk.Tk): The root window of the Tkinter application.
            app (object): The main application object.
        """
        self.root = root
        self.app = app

    def show_healthcare_provider_dashboard(self):
        """
        Displays the healthcare provider dashboard UI.
        """
        # Clear the current frame
        self.app.clear_frame()
        
        # Create a frame for the healthcare provider dashboard
        healthcare_provider_frame = tk.Frame(self.root)
        healthcare_provider_frame.pack(pady=20)

        # Initialize instances of other views
        lifestyle_data = LifestyleData(self.root, self.app)
        genetic_data = GeneticData(self.root, self.app)
        cognitive_test_ui = CognitiveTestUI(self.root, self.app)

        # Add buttons to modify different types of data
        tk.Button(healthcare_provider_frame, text="Modify Lifestyle Data", command=lifestyle_data.show_lifestyle_data).pack(pady=10)
        tk.Button(healthcare_provider_frame, text="Modify Genetic Data", command=genetic_data.show_genetic_data).pack(pady=10)
        tk.Button(healthcare_provider_frame, text="Modify Cognitive Test Data", command=cognitive_test_ui.show_cognitive_test).pack(pady=10)
        tk.Button(healthcare_provider_frame, text="Back to Dashboard", command=self.app.show_dashboard).pack(pady=20)