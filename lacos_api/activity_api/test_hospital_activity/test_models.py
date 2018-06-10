from test_plus.test import TestCase
from lacos_api.activity_api.models import HospitalActivity


class TestUser(TestCase):

    def setUp(self):
        self.user = self.make_user()


class TestHospitalActivity(TestCase):
    # Should create an Activity Model
    def setUp(self):
        return HospitalActivity.objects.create(
            name="hospGama",
            volunteers="30",
            novice="5",
            support="3",
            limit="True",
            duration="60",
            call="True",
            schedule="2018-07-30T15:30:02-03:00"
        )

    # Verify if the activity was created
    def test_create_activity(self):
        w = self.setUp()
        self.assertEqual(w.name, "hospGama")
        self.assertEqual(w.volunteers, "30")
        self.assertEqual(w.novice, "5")
        self.assertEqual(w.support, "3")
        self.assertEqual(w.limit, "True")
        self.assertEqual(w.duration, "60")
        self.assertEqual(w.call, "True")
        self.assertEqual(w.schedule, "2018-07-30T15:30:02-03:00")
