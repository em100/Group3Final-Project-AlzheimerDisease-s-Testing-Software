from models.user_model import UserModel

# login_view_model.py
class LoginViewModel:
    """
    Authenticates a user based on username and password.
    
    Args:
        username: The username of the user.
        password: The password of the user.
    
    Returns:
        bool: True if login is successful, False otherwise.
    """

    def __init__(self):
        self.user = None

    def login_user(self, username, password):
        self.user = UserModel.fetch_user_by_username(username)  # Implement this method in UserModel
        if self.user and self.user.password == password:  # Assuming password is stored securely
            return True
        return False