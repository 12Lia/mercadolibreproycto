import unittest
from selenium import webdriver
from time import sleep


class MercadoLibre(unittest.TestCase):

        # Enter the website
    def setUp(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.maximize_window()
        driver.get("https://mercadolibre.com/")
        driver.implicitly_wait(5)      
        
        # Select México as a country
    def test_search_ps(self):
        driver = self.driver
        country_select = driver.find_element_by_id('MX')
        country_select.click()

        sleep(3)

        # Search for the term “playstation 5"
        search_field = driver.find_element_by_class_name('nav-search-input')
        search_field.clear() 
        search_field.send_keys('PlayStation 5')
        search_field.submit()

        sleep(3)


        # Filter by condition “Nuevos"
        condition_selector = driver.find_element_by_css_selector('#root-app > div > div > aside > section.ui-search-filter-groups > dl:nth-child(6) > dd:nth-child(2) > a > span.ui-search-filter-name')
        condition_selector.click()

        sleep(3)

        # Order by “mayor a menor precio"
        sort_select = driver.find_element_by_xpath('//*[@id="root-app"]/div/div/aside/section[2]/div[2]/div[1]/div/div')
        sort_select.click()

        price_select = driver.find_element_by_xpath('//*[@id="root-app"]/div/div/aside/section[2]/div[2]/div[1]/div/div/div/ul/li[3]/div/div/a')
        price_select.click()

        sleep(3)

        # Obtain the name and the price of the first 5 products

        names = []
        prices = []

        for i in range(5):
            article = driver.find_element_by_xpath(f'/html/body/main/div/div/section/ol/li[{i + 1}]/div/div/div[2]/div[1]/a/h2').text
            names.append(article)

        for i in range(5):
            price = driver.find_element_by_xpath(f'/html/body/main/div/div/section/ol/li[{i + 1}]/div/div/div[2]/div[2]/div/div/span[1]/span[2]').text
            prices.append(price)

        results = dict(zip(names, prices))

        # Print these products in the console 
        print(results)


    def tearDown(self):
        self.driver.implicitly_wait(15)
        self.driver.quit()



if __name__ == "__main__":
    unittest.main(verbosity= 2)