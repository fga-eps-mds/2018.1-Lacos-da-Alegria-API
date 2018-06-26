from test_plus.test import TestCase
# from ..admin import MyUserCreationForm
import pytest


class TestMyUserCreationForm(TestCase):

    def test_succint_raises(self):
        with pytest.raises(ValueError):
            raise ValueError('I am a graceful failure')
