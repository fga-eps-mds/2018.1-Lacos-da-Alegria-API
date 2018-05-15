from test_plus.test import TestCase
from ..models import Activity


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


class TestActivity(TestCase):
    # Should create an Activity Model
    def setUp(self):
        return Activity.objects.create(
            name="hospGama",
            volunteers="30",
            limit="True",
            status="1",
            duration="60",
            subscription="True",
            call="True"
        )

    # Verify if the activity was created
    def test_create_activity(self):
        w = self.setUp()
        self.assertEqual(w.name, "hospGama")
        self.assertEqual(w.volunteers, "30")
        self.assertEqual(w.limit, "True")
        self.assertEqual(w.status, "1")
        self.assertEqual(w.duration, "60")
        self.assertEqual(w.subscription, "True")
        self.assertEqual(w.call, "True")
