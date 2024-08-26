from main_HW import get_random_cat_image
import unittest
from unittest.mock import patch

# api_key = 'live_Gn5GVrzcwnmzzjJMO3WZ49GLbwheLgLpKAzYw3NaviVLqzyOx5F4fZcyjpkJQvg9'

class TestGetRandomCatImage(unittest.TestCase):

    @patch('requests.get')
    def test_successful_request(self, mock_get):
        # Настройка mock-ответа
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [{'url': 'https://example.com/cat.jpg'}]

        result = get_random_cat_image()
        self.assertEqual(result, 'https://example.com/cat.jpg')

    @patch('requests.get')
    def test_unsuccessful_request(self, mock_get):
        # Настройка mock-ответа для ошибки 404
        mock_get.return_value.status_code = 404
        mock_get.side_effect = requests.exceptions.HTTPError('404 Client Error: Not Found for url')

        result = get_random_cat_image()
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()