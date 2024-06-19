import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestApp(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()  # Initialize Chrome WebDriver
        self.driver.get("http://127.0.0.1:5000/")  # Open the local Flask app

    def tearDown(self):
        self.driver.quit()  # Close the WebDriver after each test

    def test_calculate_longest_path(self):
        # Wait until the matrix input textarea is present
        matrix_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "matrixInput"))
        )

        # Enter matrix data into the textarea
        matrix_input.send_keys("[[9, 9, 4], [6, 6, 8], [2, 1, 1]]")

        # Submit the form
        submit_button = self.driver.find_element(By.XPATH, "//input[@type='submit']")
        submit_button.click()

        # Wait until the result div is present
        result_div = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "result"))
        )

        # Assert the result text
        result_text = result_div.text
        self.assertIn("4", result_text)  # Adjust this based on expected output format

if __name__ == "__main__":
    unittest.main()