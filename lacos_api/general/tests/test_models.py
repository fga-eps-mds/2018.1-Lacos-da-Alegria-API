from test_plus.test import TestCase
from ..models import Activity
import pytest

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

    def setUp(self):
        return Activity.objects.create(
            name="hospGama", 
            volunteers="30", 
            limit="True",
            #created="2018-04-19T12:01:09.752144Z",
            status="1",
            #time="2000-12-12",
            duration="60",
            subscription="True",
            call="True" 
        )

    def test_create_activity(self):
        w = self.setUp()
        self.assertEqual(w.name,"hospGama")
        self.assertEqual(w.volunteers,"30")
        self.assertEqual(w.limit,"True")
        self.assertEqual(w.status,"1")
        self.assertEqual(w.duration,"60")
        self.assertEqual(w.subscription,"True")
        self.assertEqual(w.call,"True")
        
        