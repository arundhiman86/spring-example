import unittest
from selenium import webdriver
from selenium.webdriver import FirefoxOptions

class PetClinic(unittest.TestCase):

    def setUp(self):
        opts = FirefoxOptions()
        opts.add_argument("--headless")
        self.driver = webdriver.Firefox(firefox_options=opts)

    def test_page_source_in_petclinic(self):
        driver = self.driver
        driver.get("http://192.168.2.138:8080/")
        title = driver.title
        print title 
        self.assertIn("PetClinic :: a Spring Framework demonstration", driver.title)
        page = driver.page_source
        print page
        assert "No results found." not in driver.page_source


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
