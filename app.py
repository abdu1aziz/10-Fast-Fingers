from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# pip install selenium==2.53.6

"""
    if you wanna run it on your regular browser profile. 

profile = webdriver.FirefoxProfile('/home/{your_username}/.mozilla/firefox/{your_default_profile}')
driver = webdriver.Firefox(profile)    
"""


driver = webdriver.Chrome(executable_path=r'chromedriver.exe')


def wait(no):
    """ Waits for a particular time """
    time.sleep(no)


def open_website():
    """ Opens the website """
    driver.get('https://10fastfingers.com/typing-test/english')
    wait(5)  # Due to slow network speed


def run_hack():
    """ Implement the GOD speed hack """
    open_website()
    input_field = driver.find_element_by_id('inputfield')
    try :
        i = 0
        while True:
            elements = driver.find_element_by_xpath("//span[@wordnr='" + str(i) + "']")
            print(elements.text)
            input_field.send_keys(elements.text)
            input_field.send_keys(" ")
            i += 1
    except :
        print("Words completed")


def main():
    """ Driver function """
    run_hack()

if __name__ == '__main__':
    main()