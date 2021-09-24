from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(executable_path='C:/Users/arjun/Downloads/chromedriver_win32/chromedriver.exe') # replace location of driver
driver.implicitly_wait(5)


driver.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')


try:
    no_button = driver.find_element_by_class_name('at-cm-no-button')
    no_button.click()
except:
    print('No click button found.')

sum1 = driver.find_element_by_id('sum1')
sum1.send_keys(Keys.NUMPAD1, Keys.NUMPAD2) # best practice

sum2 = driver.find_element_by_id('sum2')
sum2.send_keys(20) # could be done 

btn = driver.find_element_by_css_selector('#gettotal > button')
btn.click()

# driver.quit()