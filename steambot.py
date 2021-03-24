from selenium import webdriver

chrome_driver_path = YOUR_CHROME_DRIVER_PATH


class SteamBot:
    def __init__(self):
        self.driver = webdriver.Chrome(chrome_driver_path)

    def get_website(self):
        self.driver.get("https://steamdb.info/stats/gameratings/")

        show_button = self.driver.find_element_by_xpath('//*[@id="table-apps_length"]/label/select')
        show_button.click()

        all_entries = self.driver.find_element_by_xpath('//*[@id="table-apps_length"]/label/select/option[7]')
        all_entries.click()

    def get_names(self):
        names = self.driver.find_elements_by_css_selector("td a")
        names_list = [n.text for n in names]

        for n in names_list:
            if n == '':
                names_list.remove(n)

        return names_list

    def get_positive(self):
        positive = self.driver.find_elements_by_xpath('//*[@id="table-apps"]/tbody/tr/td[4]')
        positive_list = [p.text for p in positive]

        return positive_list

    def get_negative(self):
        negative = self.driver.find_elements_by_xpath('//*[@id="table-apps"]/tbody/tr/td[5]')
        negative_list = [n.text for n in negative]

        return negative_list

    def get_ratings(self):
        ratings = self.driver.find_elements_by_xpath('//*[@id="table-apps"]/tbody/tr/td[6]')
        ratings_list = [r.text for r in ratings]

        return ratings_list

    def get_positive_percentage(self):
        percentage = self.driver.find_elements_by_xpath('//*[@id="table-apps"]/tbody/tr/td[7]')
        percentage_list = [p.text for p in percentage]

        return percentage_list

