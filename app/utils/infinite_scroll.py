from time import sleep
from config import WEB_DRIVER


def infinite_scroll():
    show_more_button = WEB_DRIVER.find_element_by_xpath(
        '//div[@class="showMoreindex___2htwc"]/span')

    while True:
        try:
            WEB_DRIVER.execute_script(
                'document.querySelector(".showMoreindex___2htwc").scrollIntoView();')
            sleep(0.1)
            show_more_button.click()
        except:
            break
