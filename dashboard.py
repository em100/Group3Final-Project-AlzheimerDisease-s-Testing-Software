import tkinter as tk
from PIL import ImageTk, Image
import os
from views.cognitive_test import CognitiveTestUI
from views.lifestyle_data import LifestyleData
from views.genetic_data import GeneticData
from views.healthcare_provider_dashboard import HealthcareProviderDashboard

#dashboard.py
class Dashboard:
     """
    Dashboard Class

    This class represents the dashboard of the Alzheimer's Disease Testing Software.
    It provides an interface for users to navigate through different modules of the application.
    """
     def __init__(self, root, app):
        """
        Initialize the Dashboard.

        Args:
            root (tk.Tk): The root Tkinter window.
            app (AlzheimerApp): The main application instance.
        """
        self.root = root
        self.app = app

     def show_dashboard(self):
        self.app.clear_frame()
        self.dashboard_frame = tk.Frame(self.root)
        self.dashboard_frame.pack(pady=20)
        
        tk.Label(self.dashboard_frame, text="Dashboard", font=("Helvetica", 16)).grid(row=0, columnspan=2, pady=10)
        
        if self.app.user_profile_pic and os.path.exists(self.app.user_profile_pic):
            profile_img = Image.open(self.app.user_profile_pic)
            profile_img = profile_img.resize((100, 100), Image.ANTIALIAS)
            profile_img = ImageTk.PhotoImage(profile_img)
            tk.Label(self.dashboard_frame, image=profile_img).grid(row=1, columnspan=2)
            self.app.profile_img = profile_img  # Keep reference to avoid garbage collection
        else:
            tk.Label(self.dashboard_frame, text="No profile picture available").grid(row=1, columnspan=2)

        tk.Label(self.dashboard_frame, text=f"Welcome, {self.app.user_name}!").grid(row=2, columnspan=2, pady=10)

        self.nav_frame = tk.Frame(self.dashboard_frame)
        self.nav_frame.grid(row=3, columnspan=2, pady=10)

        cognitive_test_ui = CognitiveTestUI(self.root, self.app)
        lifestyle_data = LifestyleData(self.root, self.app)
        genetic_data = GeneticData(self.root, self.app)
        healthcare_provider_dashboard = HealthcareProviderDashboard(self.root, self.app)

        tk.Button(self.nav_frame, text="Cognitive Test", command=cognitive_test_ui.show_cognitive_test).grid(row=0, column=0, padx=10)
        tk.Button(self.nav_frame, text="Lifestyle Data", command=lifestyle_data.show_lifestyle_data).grid(row=0, column=1, padx=10)
        tk.Button(self.nav_frame, text="Genetic Data", command=genetic_data.show_genetic_data).grid(row=0, column=2, padx=10)
        
        if self.app.is_healthcare_provider:
            tk.Button(self.nav_frame, text="Healthcare Provider", command=healthcare_provider_dashboard.show_healthcare_provider_dashboard).grid(row=0, column=3, padx=10)

        tk.Button(self.nav_frame, text="View Results", command=self.app.show_view_results).grid(row=1, columnspan=4)
        tk.Button(self.nav_frame, text="Logout", command=self.app.logout).grid(row=2, columnspan=4)

        tk.Button(self.dashboard_frame, text="Upload Profile Picture", command=self.app.upload_profile_pic).grid(row=4, column=0, pady=10)
        tk.Button(self.dashboard_frame, text="Delete Profile Picture", command=self.app.delete_profile_pic).grid(row=4, column=1, pady=10)
