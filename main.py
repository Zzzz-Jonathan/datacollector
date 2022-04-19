import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# //*[@id="highcharts-0"]

class DataCollector:
    def __init__(self, urls):
        self.urls = urls
        self.chart_path = ['//*[@id="__next"]/div/div[2]/div[1]/div[3]/div[2]/div[2]/div[2]/div/div/iframe',
                           '//*[@id="sub-container"]/div/div/div[1]/div/div/div[1]/div/div/div/div[2]/div/div[3]']
        # self.chart_path = '/html/body/div[1]/nav/div/ul[1]/li[8]/a'

        options = Options()
        options.add_argument("--disable-blink-features")
        options.add_argument("--disable-blink-features=AutomationControlled")

        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)
        self.action = ActionChains(self.driver)

    def login(self, url, name, password):
        self.driver.get(url)

        try:
            username = self.wait.until(EC.presence_of_element_located((By.XPATH,
                                                                       '//*[@id="__next"]/div/div/div[1]/div/div['
                                                                       '3]/form/div/div[1]/input')))
            userkey = self.wait.until(EC.presence_of_element_located((By.XPATH,
                                                                      '//*[@id="__next"]/div/div/div[1]/div/div['
                                                                      '3]/form/div/div[2]/input')))
            loginbtn = self.wait.until(EC.presence_of_element_located((By.XPATH,
                                                                       '//*[@id="__next"]/div/div/div[1]/div/div['
                                                                       '3]/form/div/button')))

        finally:
            pass

        username.send_keys(name)
        userkey.send_keys(password)

        time.sleep(2)

        loginbtn.click()

    def switch(self):
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])

        self.driver.switch_to.frame(self.driver.find_element(By.XPATH, self.chart_path[0]))

    def get_inf(self):
        print(self.driver.title)
        try:
            charts = self.wait.until(EC.presence_of_element_located((By.XPATH, self.chart_path[1])))
            # charts = self.driver.find_element(By.XPATH, self.chart_path)
        finally:
            pass

        size = charts.size

        for x in range(0, size['width'], 5):
            self.action.move_to_element_with_offset(charts, x, 200).perform()

            try:
                thead = self.driver.find_element(By.XPATH, '//*[@id="highcharts-0"]/div/span/div/table/thead/tr/td/span')
                tbody = self.driver.find_element(By.XPATH, '//*[@id="highcharts-0"]/div/span/div/table/tbody')
            except:
                print("Haven't find yet")
            else:
                print(thead, tbody)
            finally:
                pass

            time.sleep(0.02)


if __name__ == '__main__':
    # basic_inf
    account = 'dengqiaoyun@studio33.wecom.work'
    password = 'NC19980221dqy!'
    links = [
        'http://www.minecraftxz.com/',
        'https://www.data.ai/apps/ios/app/654897098/rank-history?vtype=day&countries=CN&device=iphone&view=grossing'
        '&legends=2222&date=2022-02-01~2022-04-18&market_slug=ios&app_slug=654897098 '
    ]

    dc = DataCollector(links)
    dc.login(dc.urls[1], account, password)  # login data.ai with given user
    time.sleep(5)  # wait website loading
    dc.switch()
    print('start getting')
    dc.get_inf()  # moving the mouse and collect inf
    print('end')
