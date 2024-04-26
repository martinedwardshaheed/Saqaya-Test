import unittest
import requests
import random
import string

class TestVowelRemovalAPI(unittest.TestCase):
    
    host = "localhost"
    port = 8080
    base_url = f"http://{host}:{port}/"

    # Helper function to generate a random string without vowels
    def generate_random_string(self, length):
        vowels = 'aeiouAEIOU'
        consonants = ''.join(c for c in string.ascii_letters if c not in vowels)
        return ''.join(random.choice(consonants) for _ in range(length))

    # Test case to check the behavior of the API when input string contains vowels
    def test_vowel_removal_endpoint(self):
        # Base URL of the API

        # Input string for testing
        input_string = "hello"

        # Make a GET request to the endpoint with the input string
        response = requests.get(self.base_url + input_string)

        # Verify the status code
        self.assertEqual(response.status_code, 200)

        # Verify the response body
        self.assertEqual(response.text, "hll")

    # Test case to check the behavior of the API when input string is empty
    def test_empty_str(self):
        

        # Input string for testing
        input_string = ""

        # Make a GET request to the endpoint with the input string
        response = requests.get(self.base_url + input_string)

        # Verify the status code
        self.assertEqual(response.status_code, 200)

        # Verify the response body
        self.assertEqual(response.text, "Send GET to /:input")

    # Test case to check the behavior of the API when input string contains all vowels
    def test_all_vowels(self):
        

        # Input string for testing
        input_string = "oaie"

        # Make a GET request to the endpoint with the input string
        response = requests.get(self.base_url + input_string)

        # Verify the status code
        self.assertEqual(response.status_code, 200)

        # Verify the response body
        self.assertEqual(response.text, "")

    # Test case to check the behavior of the API when input string contains all non-vowel characters and is long
    def test_all_non_vowel_long_string(self):
        
        
        # Input string for testing
        input_string = self.generate_random_string(100)

        # Make a GET request to the endpoint with the input string
        response = requests.get(self.base_url + input_string)

        # Verify the status code
        self.assertEqual(response.status_code, 200)

        # Verify the response body
        self.assertEqual(response.text, input_string)

    # Test case to check the behavior of the API when input string contains special characters
    # Failed test case expected to return the input string but instead returns default response body
    # There is a special error with # special char in the input string that causes anything after it to be ignored
    def test_special_chars_input(self):
        
        
        # Input string for testing
        input_string = "#!@#$%^&*()_+"

        # Make a GET request to the endpoint with the input string
        response = requests.get(self.base_url + input_string)

        # Verify the status code
        self.assertEqual(response.status_code, 200)

        # Verify the response body
        self.assertEqual(response.text, input_string)
    
    # Test case to check the behavior when input string contains special characters alongside normal characters
    def test_mixed_string(self):
        input_string = "!@aabboo12"
        output_string = "!@bb12"

        # Make a GET request to the endpoint with the input string
        response = requests.get(self.base_url + input_string)

        # Verify the status code
        self.assertEqual(response.status_code, 200)

        # Verify the response body
        self.assertEqual(response.text, output_string)

if __name__ == '__main__':
    unittest.main()
