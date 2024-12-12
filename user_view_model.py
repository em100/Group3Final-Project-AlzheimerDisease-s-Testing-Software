
from models.user_model import UserModel
from views.cognitive_test import CognitiveTest
from views.genetic_data import GeneticData
from views.lifestyle_data import LifestyleData

# user_view_model.py
class UserViewModel:
    """
    ViewModel for user-related operations.
    """

    def __init__(self):
        """
        Initializes the UserViewModel with no user.
        """
        self.user = None

    def register_user(self, name, date_of_birth, gender, contact_info):
        """
        Registers a new user.

        Args:
            name (str): The name of the user.
            date_of_birth (str): The date of birth of the user.
            gender (str): The gender of the user.
            contact_info (str): The contact information of the user.
        """
        self.user = UserModel(name=name, date_of_birth=date_of_birth, gender=gender, contact_info=contact_info)
        self.user.register()  # Register the user in the system

    def submit_cognitive_test(self, test_type, date_taken):
        """
        Submits a cognitive test for the user.

        Args:
            test_type (str): The type of cognitive test.
            date_taken (str): The date the test was taken.
        """
        if self.user:
            cognitive_test = CognitiveTest(test_type=test_type, date_taken=date_taken)
            cognitive_test.administer_test()  # Administer the cognitive test
            self.user.submit_cognitive_test(cognitive_test)  # Submit the test results

    def submit_genetic_data(self, genetic_markers, collection_date):
        """
        Submits genetic data for the user.

        Args:
            genetic_markers (list): List of genetic markers.
            collection_date (str): The date the data was collected.
        """
        if self.user:
            genetic_data = GeneticData(genetic_markers=genetic_markers, collection_date=collection_date)
            genetic_data.collect_data()  # Collect the genetic data
            self.user.submit_genetic_data(genetic_data)  # Submit the genetic data

    def submit_lifestyle_data(self, diet_info, exercise_info, sleep_info, collection_date):
        """
        Submits lifestyle data for the user.

        Args:
            diet_info (str): Information about the user's diet.
            exercise_info (str): Information about the user's exercise habits.
            sleep_info (str): Information about the user's sleep patterns.
            collection_date (str): The date the data was collected.
        """
        if self.user:
            lifestyle_data = LifestyleData(diet_info=diet_info, exercise_info=exercise_info, sleep_info=sleep_info, collection_date=collection_date)
            lifestyle_data.collect_data()  # Collect the lifestyle data
            self.user.submit_lifestyle_data(lifestyle_data)  # Submit the lifestyle data

    def view_results(self):
        """
        Views the results for the user.

        Returns:
            dict: The results of the user.
        """
        if self.user:
            return self.user.view_results()  # Return the user's results

    def get_all_users(self):
        """
        Fetches all users.

        Returns:
            list: A list of all users.
        """
        return UserModel.fetch_all_users()  # Fetch and return all users