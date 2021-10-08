import random
from datetime import datetime

import yaml
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

with open("config.yml", "r") as user_config:
    config = yaml.safe_load(user_config)


def complete_survey():
    now = datetime.now()

    options = Options()
    options.binary_location = config["chrome_path"]
    browser = webdriver.Chrome(config["driver_path"], options=options)
    browser.get("https://www.wendyswantstoknow.com/")

    ####################################################################################################################
    # Page 1
    ####################################################################################################################

    store_number = browser.find_element_by_id("InputStoreNum")
    store_number.send_keys(config["store_number"])

    visit_date = browser.find_element_by_id("Index_VisitDateDatePicker")
    visit_date.click()
    today = browser.find_element_by_class_name("ui-datepicker-today")
    today.click()

    hour = browser.find_element_by_id("InputHour")
    current_hour = hour.find_element_by_css_selector(f"""option[value='{now.strftime("%I")}']""")
    current_hour.click()

    minute = browser.find_element_by_id("InputMinute")
    current_minute = minute.find_element_by_css_selector(f"""option[value='{now.strftime("%M")}']""")
    current_minute.click()

    meridian = browser.find_element_by_id("InputMeridian")
    current_meridian = meridian.find_element_by_css_selector(f"""option[value='{now.strftime("%p")}']""")
    current_meridian.click()

    next_button = browser.find_element_by_id("NextButton")
    next_button.click()

    ####################################################################################################################
    # Page 2
    ####################################################################################################################

    yes = browser.find_elements_by_class_name("inputtyperbloption")[0]
    radio = yes.find_element_by_class_name("radioSimpleInput")
    radio.click()

    next_button = browser.find_element_by_id("NextButton")
    next_button.click()

    ####################################################################################################################
    # Page 3
    ####################################################################################################################

    type_of_purchase = random.randint(0, 2)
    selected = browser.find_elements_by_class_name("rbloption")[type_of_purchase]
    button = selected.find_element_by_class_name("radioSimpleInput")
    button.click()

    next_button = browser.find_element_by_id("NextButton")
    next_button.click()

    ####################################################################################################################
    # Page 4
    ####################################################################################################################

    choice = browser.find_elements_by_class_name("inputtyperbloption")[0]
    choice.click()

    next_button = browser.find_element_by_id("NextButton")
    next_button.click()

    ####################################################################################################################
    # Page 5
    ####################################################################################################################

    ordered_by = random.randint(0, 2)
    selected = browser.find_elements_by_class_name("rbloption")[ordered_by]
    button = selected.find_element_by_class_name("radioSimpleInput")
    button.click()

    next_button = browser.find_element_by_id("NextButton")
    next_button.click()

    ####################################################################################################################
    # Page 6
    ####################################################################################################################

    no = browser.find_elements_by_class_name("inputtyperbloption")[1]
    no.click()

    next_button = browser.find_element_by_id("NextButton")
    next_button.click()

    ####################################################################################################################
    # Page 7
    ####################################################################################################################

    elements = browser.find_elements_by_class_name("inputtyperbloption")
    elements[0].click()
    elements[5].click()
    elements[10].click()
    elements[15].click()
    elements[20].click()

    next_button = browser.find_element_by_id("NextButton")
    next_button.click()

    ####################################################################################################################
    # Page 8
    ####################################################################################################################

    elements = browser.find_elements_by_class_name("inputtyperbloption")
    elements[0].click()
    elements[5].click()
    elements[10].click()
    elements[15].click()

    next_button = browser.find_element_by_id("NextButton")
    next_button.click()

    ####################################################################################################################
    # Page 9
    ####################################################################################################################

    no = browser.find_elements_by_class_name("inputtyperbloption")[1]
    no.click()

    next_button = browser.find_element_by_id("NextButton")
    next_button.click()

    ####################################################################################################################
    # Page 10
    ####################################################################################################################

    elements = browser.find_elements_by_class_name("inputtyperbloption")
    elements[0].click()
    elements[5].click()

    next_button = browser.find_element_by_id("NextButton")
    next_button.click()

    ####################################################################################################################
    # Page 11
    ####################################################################################################################

    textarea = browser.find_element_by_id("S000024")
    textarea.send_keys(random.choice(config["why_satisfied"]))

    next_button = browser.find_element_by_id("NextButton")
    next_button.click()

    ####################################################################################################################
    # Page 12
    ####################################################################################################################

    elements = browser.find_elements_by_class_name("inputtyperbloption")
    elements[0].click()
    elements[2].click()

    next_button = browser.find_element_by_id("NextButton")
    next_button.click()

    ####################################################################################################################
    # Page 13
    ####################################################################################################################

    selected = browser.find_elements_by_class_name("rbloption")[3]
    button = selected.find_element_by_class_name("radioSimpleInput")
    button.click()

    next_button = browser.find_element_by_id("NextButton")
    next_button.click()

    ####################################################################################################################
    # Page 14
    ####################################################################################################################

    browser.find_elements_by_class_name("inputtyperbloption")[1].click()

    next_button = browser.find_element_by_id("NextButton")
    next_button.click()

    ####################################################################################################################
    # Page 15
    ####################################################################################################################

    selected = browser.find_elements_by_class_name("rbloption")[-1]
    button = selected.find_element_by_class_name("radioSimpleInput")
    button.click()

    next_button = browser.find_element_by_id("NextButton")
    next_button.click()

    ####################################################################################################################
    # Page 16
    ####################################################################################################################

    hamburger = browser.find_element_by_class_name("Opt1")
    button = hamburger.find_element_by_class_name("radioSimpleInput")
    button.click()

    next_button = browser.find_element_by_id("NextButton")
    next_button.click()

    ####################################################################################################################
    # Page 17
    ####################################################################################################################

    hamburger = browser.find_element_by_class_name("Opt2")
    button = hamburger.find_element_by_class_name("radioSimpleInput")
    button.click()

    next_button = browser.find_element_by_id("NextButton")
    next_button.click()

    ####################################################################################################################
    # Page 18
    ####################################################################################################################

    burgers = browser.find_elements_by_class_name("rbloption")
    choice = random.randint(0, len(burgers) - 1)
    burger = burgers[choice]
    button = burger.find_element_by_class_name("radioSimpleInput")
    button.click()

    next_button = browser.find_element_by_id("NextButton")
    next_button.click()

    ####################################################################################################################
    # Page 19
    ####################################################################################################################

    browser.find_elements_by_class_name("inputtyperbloption")[0].click()

    next_button = browser.find_element_by_id("NextButton")
    next_button.click()

    ####################################################################################################################
    # Page 20
    ####################################################################################################################

    elements = browser.find_elements_by_class_name("inputtyperbloption")
    elements[0].click()
    elements[5].click()
    elements[10].click()
    elements[15].click()

    next_button = browser.find_element_by_id("NextButton")
    next_button.click()

    ####################################################################################################################
    # Page 21
    ####################################################################################################################

    gender = browser.find_element_by_id("R000037")
    chosen_gender = gender.find_element_by_css_selector(f"""option[value='{random.choice(["1", "2", "9"])}']""")
    chosen_gender.click()

    age = browser.find_element_by_id("R000038")
    chosen_age = age.find_element_by_css_selector(
        f"""option[value='{random.choice(["1", "2", "3", "4", "5", "6", "9"])}']""")
    chosen_age.click()

    income = browser.find_element_by_id("R000039")
    chosen_income = income.find_element_by_css_selector(
        f"""option[value='{random.choice(["1", "2", "3", "4", "5", "6", "9"])}']""")
    chosen_income.click()

    background = browser.find_element_by_id("R000040")
    chosen_background = background.find_element_by_css_selector(
        f"""option[value='{random.choice(["1", "2", "3", "4", "5", "6", "7", "9"])}']""")
    chosen_background.click()

    next_button = browser.find_element_by_id("NextButton")
    next_button.click()

    ####################################################################################################################
    # Page 22
    ####################################################################################################################

    browser.find_elements_by_class_name("inputtyperbloption")[0].click()

    next_button = browser.find_element_by_id("NextButton")
    next_button.click()

    ####################################################################################################################
    # Page 23
    ####################################################################################################################

    next_button = browser.find_element_by_id("NextButton")
    next_button.click()

    ####################################################################################################################
    # Page 24
    ####################################################################################################################

    selected = browser.find_elements_by_class_name("rbloption")[-1]
    button = selected.find_element_by_class_name("radioSimpleInput")
    button.click()

    next_button = browser.find_element_by_id("NextButton")
    next_button.click()

    ####################################################################################################################
    # Page 25
    ####################################################################################################################

    validation_code = browser.find_element_by_class_name("ValCode").text
    url = config["discord_webhook"]
    requests.post(url, data={"content": validation_code})

    ####################################################################################################################
    # Close
    ###################################################################################################################

    browser.quit()


if __name__ == "__main__":
    while True:
        complete_survey()
