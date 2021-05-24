from time import sleep


def infinite_scroll(driver):
    show_more_button = driver.find_element_by_xpath(
        '//div[@class="showMoreindex___2htwc"]/span')

    while True:
        try:
            driver.execute_script(
                'document.querySelector(".showMoreindex___2htwc").scrollIntoView();')
            sleep(0.1)
            show_more_button.click()
        except:
            break
