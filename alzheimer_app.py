import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import ImageTk, Image
from datetime import datetime
from models.login_view_model import LoginViewModel
from models.user_model import UserModel
from views.cognitive_test import CognitiveTestUI
from views.genetic_data import GeneticData
from views.lifestyle_data import LifestyleData
from views.healthcare_provider_dashboard import HealthcareProviderDashboard
from views.login import Login
from views.user_registration import UserRegistration
from views.dashboard import Dashboard
from views.results_viewing import ResultsViewing
import os

class AlzheimerApp:
    """
    Alzheimer's Disease Testing Software Application

    This class represents the main application for Alzheimer's Disease Testing Software.
    It integrates cognitive tests, genetic information, and lifestyle data to assess Alzheimer's disease risk.
    """
    def __init__(self, root):
        """
        Initialize the AlzheimerApp.

        Args:
            root (tk.Tk): The root Tkinter window.
        """
        self.root = root
        self.root.title("Alzheimer's Disease Testing Software")
        self.user_name = ""
        self.user_profile_pic = None
        self.is_healthcare_provider = False
        self.cognitive_test_results = {}
        self.lifestyle_data = {
            "Diet": "vegetarian",
            "Exercise": "daily running",
            "Sleep Patterns": "7 hours",
            "Date Logged": "2024-11-05"
        }
        self.genetic_data = {
            "Markers Identified": "APOE4",
            "Date Uploaded": "2024-11-05"
        }

        # Initialize views
        self.login = Login(root, self)
        self.user_registration = UserRegistration(root, self)
        self.dashboard = Dashboard(root, self)
        self.results_viewing = ResultsViewing(root, self)
        # Initialize other modules similarly...

        # Show the login screen initially
        self.show_login()

    def show_login(self):
        """
        Displays the login screen.
        """
        self.login.show_login()

    def show_new_user_form(self):
        """
        Displays the new user registration form.
        """
        self.user_registration.show_new_user_form()

    def show_dashboard(self):
        """
        Displays the main dashboard.
        """
        self.dashboard.show_dashboard()

    def show_view_results(self):
        """
        Displays the results viewing screen.
        """
        self.results_viewing.show_view_results()

    def upload_profile_pic(self):
        """
        Opens a file dialog to upload a profile picture.
        """
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
        if file_path:
            self.user_profile_pic = file_path
            self.update_user_profile_pic()
            self.show_dashboard()

    def delete_profile_pic(self):
        """
        Deletes the current profile picture.
        """
        self.user_profile_pic = None
        self.update_user_profile_pic()
        self.show_dashboard()

    def update_user_profile_pic(self):
        """
        Updates the profile picture in the user model and database.
        """
        # Update the profile picture in the user model
        self.login.login_view_model.user.profile_pic = self.user_profile_pic
        self.login.login_view_model.user.update_profile_pic()

    def logout(self):
        """
        Logs out the current user and returns to the login screen.
        """
        messagebox.showinfo("Logout", "You have been logged out.")
        self.show_login()

    def clear_frame(self):
        """
        Clears all widgets from the current frame.
        """
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = AlzheimerApp(root)
    root.mainloop()