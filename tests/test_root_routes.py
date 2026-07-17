import unittest

from app import create_app


class RootRouteTests(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_root_returns_success(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_health_returns_ok(self):
        response = self.client.get('/health')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['status'], 'ok')

    def test_docs_returns_success(self):
        response = self.client.get('/docs')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
