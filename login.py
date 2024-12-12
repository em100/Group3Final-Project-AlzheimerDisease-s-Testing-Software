import tkinter as tk
from tkinter import messagebox
from models.login_view_model import LoginViewModel

# login.py
class Login:
    def __init__(self, root, app):
        """
        Initializes a new instance of the Login class.

        Args:
            root (tk.Tk): The root window of the Tkinter application.
            app (object): The main application object.
        """
        self.root = root
        self.app = app

    def show_login(self):
        """
        Displays the login UI.
        """
        # Clear the current frame
        self.app.clear_frame()
        
        # Create a frame for the login page
        self.login_frame = tk.Frame(self.root)
        self.login_frame.grid(pady=20)
        
        # Add a label for the login page title
        tk.Label(self.login_frame, text="Login Page", font=("Helvetica", 16)).grid(row=0, columnspan=2, pady=10)
        
        # Add a label and entry for the username
        tk.Label(self.login_frame, text="Username").grid(row=1, column=0, padx=10, pady=5)
        self.username_entry = tk.Entry(self.login_frame)
        self.username_entry.grid(row=1, column=1, padx=10, pady=5)
        
        # Add a label and entry for the password
        tk.Label(self.login_frame, text="Password").grid(row=2, column=0, padx=10, pady=5)
        self.password_entry = tk.Entry(self.login_frame, show="*")
        self.password_entry.grid(row=2, column=1, padx=10, pady=5)
        
        # Add login and new user buttons
        tk.Button(self.login_frame, text="Login", command=self.login).grid(row=3, columnspan=2, pady=10)
        tk.Button(self.login_frame, text="New User", command=self.app.show_new_user_form).grid(row=4, columnspan=2, pady=10)

    def login(self):
        """
        Handles the login process.
        """
        # Get the username and password from the entry fields
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        # Initialize the login view model and attempt to log in the user
        self.login_view_model = LoginViewModel()
        if self.login_view_model.login_user(username, password):
            # If login is successful, set user details in the app object
            self.app.user_name = self.login_view_model.user.name
            self.app.user_profile_pic = self.login_view_model.user.profile_pic
            self.app.is_healthcare_provider = (username == "healthcare_provider")
            # Show the dashboard
            self.app.show_dashboard()
        else:
            # Show an error message if login fails
            messagebox.showerror("Login Error", "Invalid username or password")