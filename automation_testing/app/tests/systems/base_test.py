from unittest import TestCase
from app import app
import json


class TestHome(TestCase):
    def setUp(self):

        """Helps you from duplication of the code"""
        app.testing = True
        self.app = app.test_client