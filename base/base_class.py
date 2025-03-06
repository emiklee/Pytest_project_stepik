import datetime


class Base:

    def __init__(self, driver):
        self.driver = driver

    """ Method get current url """
    def get_current_url(self):
        get_url = self.driver.current_url
        print('Current url'+get_url)

    """ Method assert word  """
    def assert_word(self, word, result):
        valu_word = word.text
        assert valu_word == result
        print('Good value word')



    """ Method screenshot  """

    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime('%Y.%m.%d %H.%M.%S')
        name_screen = 'screenshot ' + now_date + '.png'
        self.driver.save_screenshot(f'/Volumes/EMKA/IT/Python/Pytest/home_project/screen/{name_screen}')

    """ Method assert url  """
    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print('Good value url')