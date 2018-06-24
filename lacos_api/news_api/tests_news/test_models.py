from test_plus.test import TestCase
from ..models import News


class TestNews(TestCase):

    def test_create_news(self):
        # user1 = self.setUp()
        news1 = News.objects.create(
            title="Urgente",
            text="Muita coisa escrita aqui",
            date_deleted="2018-07-30T15:30:02-03:00")
        self.assertEqual(news1.title, "Urgente")
        self.assertEqual(news1.text, "Muita coisa escrita aqui")
        self.assertEqual(news1.date_deleted, "2018-07-30T15:30:02-03:00")
