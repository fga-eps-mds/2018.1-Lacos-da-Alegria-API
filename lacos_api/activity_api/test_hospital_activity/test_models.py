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
            image="Imagem",
            location="Rua aleatoria",
            volunteers="30",
            novice="5",
            duration="60",
            schedule="2018-07-30T15:30:02-03:00"
        )

    # Verify if the activity was created
    def test_create_activity(self):
        w = self.setUp()
        self.assertEqual(w.name, "hospGama")
        self.assertEqual(w.image, "Imagem")
        self.assertEqual(w.location, "Rua aleatoria")
        self.assertEqual(w.volunteers, "30")
        self.assertEqual(w.novice, "5")
        self.assertEqual(w.duration, "60")
        self.assertEqual(w.schedule, "2018-07-30T15:30:02-03:00")
