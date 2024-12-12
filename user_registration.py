import tkinter as tk
from tkinter import messagebox, filedialog
from models.user_model import UserModel

class UserRegistration:
    def __init__(self, root, app):
        """
        Initializes a new instance of the UserRegistration class.

        Args:
            root (tk.Tk): The root window of the Tkinter application.
            app (object): The main application object.
        """
        self.root = root
        self.app = app

    def show_new_user_form(self):
        """
        Displays the new user registration form UI.
        """
        # Clear the current frame
        self.app.clear_frame()
        
        # Create a frame for the new user registration form
        new_user_frame = tk.Frame(self.root)
        new_user_frame.grid(pady=20)

        # Add a label for the registration page title
        tk.Label(new_user_frame, text="User Registration Page", font=("Helvetica", 16)).grid(row=0, columnspan=3, pady=10)
        
        # Add labels and entry fields for user details
        tk.Label(new_user_frame, text="Username").grid(row=1, column=0, padx=10, pady=5)
        self.new_username_entry = tk.Entry(new_user_frame)
        self.new_username_entry.grid(row=1, column=1, padx=10, pady=5)
        
        tk.Label(new_user_frame, text="Name").grid(row=2, column=0, padx=10, pady=5)
        self.new_name_entry = tk.Entry(new_user_frame)
        self.new_name_entry.grid(row=2, column=1, padx=10, pady=5)
        
        tk.Label(new_user_frame, text="Password").grid(row=3, column=0, padx=10, pady=5)
        self.new_password_entry = tk.Entry(new_user_frame, show="*")
        self.new_password_entry.grid(row=3, column=1, padx=10, pady=5)
        
        tk.Label(new_user_frame, text="Email").grid(row=4, column=0, padx=10, pady=5)
        self.new_email_entry = tk.Entry(new_user_frame)
        self.new_email_entry.grid(row=4, column=1, padx=10, pady=5)
        
        tk.Label(new_user_frame, text="Contact Info").grid(row=5, column=0, padx=10, pady=5)
        self.new_contact_info_entry = tk.Entry(new_user_frame)
        self.new_contact_info_entry.grid(row=5, column=1, padx=10, pady=5)
        
        tk.Label(new_user_frame, text="Date of Birth").grid(row=6, column=0, padx=10, pady=5)
        self.new_dob_entry = tk.Entry(new_user_frame)
        self.new_dob_entry.grid(row=6, column=1, padx=10, pady=5)
        
        tk.Label(new_user_frame, text="Gender").grid(row=7, column=0, padx=10, pady=5)
        self.new_gender_entry = tk.Entry(new_user_frame)
        self.new_gender_entry.grid(row=7, column=1, padx=10, pady=5)
        
        # Add a label and entry for the profile picture with a browse button
        tk.Label(new_user_frame, text="Profile Picture").grid(row=8, column=0, padx=10, pady=5)
        self.profile_pic_path = tk.StringVar()
        tk.Entry(new_user_frame, textvariable=self.profile_pic_path).grid(row=8, column=1, padx=10, pady=5)
        tk.Button(new_user_frame, text="Browse", command=self.browse_profile_pic).grid(row=8, column=2, padx=10, pady=5)
        
        # Add register and back to login buttons
        tk.Button(new_user_frame, text="Register", command=self.register_new_user).grid(row=9, columnspan=3, pady=10)
        tk.Button(new_user_frame, text="Back to Login", command=self.app.show_login).grid(row=10, columnspan=3, pady=10)

    def browse_profile_pic(self):
        """
        Opens a file dialog to browse for a profile picture.
        """
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
        self.profile_pic_path.set(file_path)

    def register_new_user(self):
        """
        Registers a new user with the provided details.
        """
        # Get user details from the entry fields
        new_username = self.new_username_entry.get()
        new_name = self.new_name_entry.get()
        new_password = self.new_password_entry.get()
        new_email = self.new_email_entry.get()
        new_contact_info = self.new_contact_info_entry.get()
        new_dob = self.new_dob_entry.get()
        new_gender = self.new_gender_entry.get()
        profile_pic = self.profile_pic_path.get()

        # Check if a profile picture is uploaded
        if not profile_pic:
            messagebox.showerror("Registration Error", "Please upload a profile picture.")
            return

        # Create a new UserModel instance with the provided details
        new_user_model = UserModel(
            username=new_username,
            name=new_name,
            password=new_password,
            email=new_email,
            contact_info=new_contact_info,
            date_of_birth=new_dob,
            gender=new_gender,
            profile_pic=profile_pic
        )
        
        # Attempt to register the new user
        if new_user_model.register():
            messagebox.showinfo("Registration", "New user registered successfully!")
            self.app.show_login()
        else:
            messagebox.showerror("Registration Error", "Failed to register new user.")