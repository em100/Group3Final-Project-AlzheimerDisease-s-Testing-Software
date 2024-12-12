from models.database import Database

class UserModel:
    def __init__(self, user_id=None, username=None, name=None, password=None, email=None, contact_info=None, date_of_birth=None, gender=None, profile_pic=None):
        """
        Initializes a new instance of the UserModel class.

        Args:
            user_id (int, optional): The user's ID.
            username (str, optional): The user's username.
            name (str, optional): The user's name.
            password (str, optional): The user's password.
            email (str, optional): The user's email address.
            contact_info (str, optional): The user's contact information.
            date_of_birth (str, optional): The user's date of birth.
            gender (str, optional): The user's gender.
            profile_pic (str, optional): The path to the user's profile picture.
        """
        self.user_id = user_id
        self.username = username
        self.name = name
        self.password = password
        self.email = email
        self.contact_info = contact_info
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.profile_pic = profile_pic

    def register(self):
        """
        Registers a new user in the database.

        Returns:
            bool: True if the registration is successful, False otherwise.
        """
        # Connect to the database
        connection = Database.connect_db()
        if connection:
            cursor = connection.cursor()
            # Insert user details into the USER table
            cursor.execute(
                "INSERT INTO USER (username, name, password, email, contact_info, date_of_birth, gender, profile_pic) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                (self.username, self.name, self.password, self.email, self.contact_info, self.date_of_birth, self.gender, self.profile_pic)
            )
            connection.commit()  # Commit the transaction
            self.user_id = cursor.lastrowid  # Get the ID of the newly registered user
            cursor.close()  # Close the cursor
            connection.close()  # Close the connection
            return True
        return False

    def update_profile_pic(self):
        """
        Updates the profile picture of the user in the database.
        """
        # Connect to the database
        connection = Database.connect_db()
        if connection:
            cursor = connection.cursor()
            # Update the profile picture for the user with the given user_id
            cursor.execute(
                "UPDATE USER SET profile_pic = %s WHERE user_id = %s",
                (self.profile_pic, self.user_id)
            )
            connection.commit()  # Commit the transaction
            cursor.close()  # Close the cursor
            connection.close()  # Close the connection

    @staticmethod
    def fetch_user_by_username(username):
        """Fetches a user from the database by their username.
        Args:
            username (str): The username of the user to fetch.
        Returns:
            UserModel: An instance of UserModel with the fetched user's details, or None if no user is found.
        """
        user = None
        try:
            # Connect to the database using a context manager
            with Database.connect_db() as connection:
                cursor = connection.cursor()
                # Select user details from the USER table where the username matches
                cursor.execute("SELECT * FROM USER WHERE username = %s", (username,))
                user_data = cursor.fetchone()  # Fetch one user record
                if user_data:
                    # Create a UserModel instance with the fetched user details
                    user = UserModel(
                        user_id=user_data[0],
                        username=user_data[1],
                        name=user_data[2],
                        password=user_data[3],
                        email=user_data[4],
                        contact_info=user_data[5],
                        date_of_birth=user_data[6],
                        gender=user_data[7],
                        profile_pic=user_data[8]  # Assuming profile_pic is the 9th column in the USER table
                    )
        except Exception as e:
            print(f"An error occurred: {e}")  # Print the error message
        return user

    @staticmethod
    def fetch_all_users():
        """
        Fetches all users from the database.

        Returns:
            list: A list of tuples containing user details.
        """
        users = []
        try:
            # Connect to the database using a context manager
            with Database.connect_db() as connection:
                cursor = connection.cursor()
                # Select all user details from the USER table
                cursor.execute("SELECT user_id, username, date_of_birth, gender, contact_info FROM USER")
                users = cursor.fetchall()  # Fetch all user records
        except Exception as e:
            print(f"An error occurred: {e}")  # Print the error message
        return users