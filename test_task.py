from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import time 
import pyautogui

link = "https://piter-online.net/"
browser = webdriver.Chrome(ChromeDriverManager().install())	
n = 5
for i in range(n):
    try:

        browser.get(link)
        input1 = browser.find_element("xpath", "//span[text()='Введите улицу']/following-sibling::input")


        input1.send_keys("Тестовая линия")
        time.sleep(1)
        pyautogui.press("Enter")
        time.sleep(1)
        input2 = browser.find_element("xpath", "//span[text()='Дом']/following-sibling::input")
        input2.send_keys("1")
        time.sleep(1)
        pyautogui.press("Enter")

        input3 = browser.find_element("xpath", "//li[text()='В квартиру']")
        input3.click()

        input4 = browser.find_element("xpath", "//div[text()='показать тарифы']")
        input4.click()

        time.sleep(2)
        input5 = browser.find_element("xpath", "//div[@datatest='close_popup1_from_quiz_input_tel']")
        input5.click()

        input6 = browser.find_element("xpath", "//a[@href='/leningradskaya-oblast/orders/home?tariff_id=102134004']")
        input6.click()

        time.sleep(2)
        input7 = browser.find_element("xpath", "//input[@datatest='providers_provider_order_input_name']")
        input7.send_keys("Автотест")

        time.sleep(2)
        input8 = browser.find_element("xpath", "//input[@datatest='providers_provider_order_input_tel']")
        input8.send_keys("1111111111")

        input9 = browser.find_element("xpath", "//div[@data-test='order_form_input_connect_button']")
        input9.click()
        
        time.sleep(3)
   
        assert text in browser.page_source

    finally:
        time.sleep(5)
        
    browser.quit()

 
