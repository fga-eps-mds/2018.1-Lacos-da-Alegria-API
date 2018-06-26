from test_plus.test import TestCase
from ..models import NGOActivity


class TestUser(TestCase):

    def setUp(self):
        self.user = self.make_user()

    # def test__str__(self):
    #     self.assertEqual(
    #         self.user.__str__(),
    #         "testuser",  # This is the default username for self.make_user()
    #     )

    # def test_get_absolute_url(self):
    #     self.assertEqual(self.user.get_absolute_url(), "/profiles/testuser/")


class TestNGOActivity(TestCase):
    # Should create an Activity Model
    def setUp(self):
        return NGOActivity.objects.create(
            name="hospGama",
            volunteers="30",
            duration="60",
            schedule="2018-07-30T15:30:02-03:00"
        )

    # Verify if the activity was created
    def test_create_activity(self):
        w = self.setUp()
        self.assertEqual(w.name, "hospGama")
        self.assertEqual(w.volunteers, "30")
        self.assertEqual(w.duration, "60")
        self.assertEqual(w.schedule, "2018-07-30T15:30:02-03:00")
