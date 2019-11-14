from app import app
import unittest
from unittest.mock import patch, ANY

class AppTests(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_status_code(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)

    # def test_fortune_results_default_response(self):
    #     result = self.app.get('/fortune_results')
    #     self.assertIn('Nothing of note', str(result.data))

    def test_fortune_results_doggo(self):
        result = self.app.get('/fortune_results?name=a&gender=female&animal=doggo&favcolor=%23ff0000')
        self.assertIn('fur-get', str(result.data))

    def test_fortune_results_bunny(self):
        result = self.app.get('/fortune_results?name=a&gender=female&animal=bunny&favcolor=%23ff0000')
        self.assertIn('Some bunny loves you!', str(result.data))



    @patch('app.requests')
    def test_weather_results(self, requests):
        requests.get().json.return_value = {
            'main': { 'temp': 60 }
        }
        result = self.app.get('/weather_results?city=San+Francisco')
        # ... do other verifications on result

        requests.get.assert_called_with(ANY,
            params={'q': 'San Francisco', 'appid': ANY})
# run the tests
if __name__ == '__main__':
    unittest.main()
