from test_plus.test import TestCase
# from ..admin import MyUserCreationForm
import pytest


class TestMyUserCreationForm(TestCase):

    def test_succint_raises(self):
        with pytest.raises(ValueError):
            raise ValueError('I am a graceful failure')

    #     self.user = self.make_user("notalamode", "notalamodespassword")

    # def test_clean_username_success(self):
    #     # Instantiate the form with a new username
    #     form = MyUserCreationForm(
    #         {
    #             "username": "alamode",
    #             "password1": "7jefB#f@Cc7YJB]2v",
    #             "password2": "7jefB#f@Cc7YJB]2v",
    #         }
    #     )
    #     # Run is_valid() to trigger the validation
    #     valid = form.is_valid()
    #     self.assertTrue(valid)

    #     # Run the actual clean_username method
    #     username = form.clean_username()
    #     self.assertEqual("alamode", username)

    # def test_clean_username_false(self):
    #     # Instantiate the form with the same username as self.user
    #     form = MyUserCreationForm(
    #         {
    #             "username": self.user.username,
    #             "password1": "notalamodespassword",
    #             "password2": "notalamodespassword",
    #         }
    #     )
    #     # Run is_valid() to trigger the validation, which is going to fail
    #     # because the username is already taken
    #     valid = form.is_valid()
    #     self.assertFalse(valid)

    #     # The form.errors dict should contain a single error called 'username'
    #     self.assertTrue(len(form.errors) == 1)
    #     self.assertTrue("username" in form.errors)
