import json
from tests.systems.base_test import BaseTest


class TestHome(BaseTest):
    # def test_home(self):
    #
    #     """in order not to run the full app rather
    #     than our endpoint for which the test is
    #     being conducted"""
    #     with app.test_client() as c:
    #         resp = c.get('/')
    #
    #         self.assertEqual(resp.status_code, 200)
    #         self.assertEqual(
    #             json.loads(resp.get_data()), {'message': 'Hello, world'}
    #         )

    def test_home(self):

        """in order not to run the full app rather
        than our endpoint for which the test is
        being conducted"""
        with self.app() as c:
            resp = c.get('/')

            self.assertEqual(resp.status_code, 200)
            self.assertEqual(
                json.loads(resp.get_data()), {'message': 'Hello, world'}
            )