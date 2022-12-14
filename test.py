from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction
import time
import openpyxl

data_book = openpyxl.load_workbook("Book1.xlsx")
data = data_book.active

desired_capabilities = {
    "platformName": "Android",
    "platformVersion": "10",
    "deviceName": "Android Emulator",
    "automationName": "UiAutomator2",
    "app": "D:/app_test/nopstationCart_4.40.apk",
    "appPackage": "com.nopstation.nopcommerce.nopstationcart",
    "appActivity": "com.bs.ecommerce.main.SplashScreenActivity"
}
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities)

# Accept alert by clicking I Read & I Accept
read_button = WebDriverWait(driver, 1000).until(
    EC.presence_of_element_located(("id", "com.nopstation.nopcommerce.nopstationcart:id/btnAccept")))
read_button.click()

# Scenario 1
# Scroll from homepage to find electronics
el_1 = WebDriverWait(driver, 1000).until(
    EC.presence_of_element_located(('xpath', '(//android.widget.ImageView[@content-desc="Placeholder"])[2]')))
for i in range(2):
    touch = TouchAction(driver)
    touch.long_press(x=920, y=1034).move_to(x=330, y=1034).release().perform()
time.sleep(5)
electronics = driver.find_element('xpath', '(//android.widget.ImageView[@content-desc="Placeholder"])[4]')
electronics.click()

# Scroll to find Nokia Lumia 1020
el_2 = WebDriverWait(driver, 1000).until(
    EC.presence_of_element_located(('id', 'com.nopstation.nopcommerce.nopstationcart:id/categoryNameTextView')))
for i in range(2):
    touch = TouchAction(driver)
    touch.press(x=534, y=1513).move_to(x=534, y=399).perform().release()
driver.implicitly_wait(5)
lumia = driver.find_element('xpath', '(//android.widget.ImageView[@content-desc="Placeholder"])[5]')
lumia.click()

# Add lumia of quantity 2 to cart
driver.implicitly_wait(10)
addToCart = WebDriverWait(driver, 1000).until(
    EC.presence_of_element_located(('id', 'com.nopstation.nopcommerce.nopstationcart:id/btnAddToCart')))
touch = TouchAction(driver)
touch.press(x=511, y=1482).move_to(x=563, y=253).perform().release()
quantity = WebDriverWait(driver, 1000).until(
    EC.presence_of_element_located(('id', 'com.nopstation.nopcommerce.nopstationcart:id/btnPlus')))
quantity.click()
addToCart.click()

print('Nokia Lumia 1020 added to cart')
time.sleep(5)

# Scenario 2
# Click on the cart
cart = WebDriverWait(driver, 1000).until(
    EC.presence_of_element_located(('id', 'com.nopstation.nopcommerce.nopstationcart:id/menu_cart')))
cart.click()

# Click on the checkout
checkout = WebDriverWait(driver, 1000).until(
    EC.presence_of_element_located(('id', 'com.nopstation.nopcommerce.nopstationcart:id/btnCheckOut')))
checkout.click()

# Click on continue as a guest
guest = WebDriverWait(driver, 1000).until(
    EC.presence_of_element_located(('id', 'com.nopstation.nopcommerce.nopstationcart:id/btnGuestCheckout')))
guest.click()

# Fill the billing address form
first_name = WebDriverWait(driver, 1000).until(
    EC.presence_of_element_located(('id', 'com.nopstation.nopcommerce.nopstationcart:id/etFirstName')))
first_name.click()
first_name.send_keys(data['B2'].value)
driver.back()

last_name = WebDriverWait(driver, 1000).until(
    EC.presence_of_element_located(('id', 'com.nopstation.nopcommerce.nopstationcart:id/etLastName')))
last_name.click()
last_name.send_keys(data['B3'].value)
driver.back()

email = WebDriverWait(driver, 1000).until(
    EC.presence_of_element_located(('id', 'com.nopstation.nopcommerce.nopstationcart:id/etEmail')))
email.click()
email.send_keys(data['B4'].value)
driver.back()

country = WebDriverWait(driver, 1000).until(
    EC.presence_of_element_located(('id', 'com.nopstation.nopcommerce.nopstationcart:id/countrySpinner')))
country.click()
country_select = WebDriverWait(driver, 1000).until(
    EC.presence_of_element_located(('xpath',
                                    "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[2]")))
country_select.click()
time.sleep(5)
state = WebDriverWait(driver, 1000).until(
    EC.presence_of_element_located(('id', 'com.nopstation.nopcommerce.nopstationcart:id/stateSpinnerLayout')))
state.click()
state_select = WebDriverWait(driver, 1000).until(
    EC.presence_of_element_located(('xpath', "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[4]")))
state_select.click()

company = WebDriverWait(driver, 1000).until(
    EC.presence_of_element_located(('id', 'com.nopstation.nopcommerce.nopstationcart:id/etCompanyName')))
company.click()
company.send_keys(data['B5'].value)
driver.back()

city = WebDriverWait(driver, 1000).until(
    EC.presence_of_element_located(('id', 'com.nopstation.nopcommerce.nopstationcart:id/etCity')))
city.click()
city.send_keys(data['B6'].value)
driver.back()

street_address = WebDriverWait(driver, 1000).until(
    EC.presence_of_element_located(('id', 'com.nopstation.nopcommerce.nopstationcart:id/etStreetAddress')))
street_address.click()
street_address.send_keys(data['B7'].value)
driver.back()

zipcode = WebDriverWait(driver, 1000).until(
    EC.presence_of_element_located(('id', 'com.nopstation.nopcommerce.nopstationcart:id/etZipCode')))
zipcode.click()
zipcode.send_keys(data['B8'].value)
driver.back()

cont = WebDriverWait(driver, 1000).until(
    EC.presence_of_element_located(('id', 'com.nopstation.nopcommerce.nopstationcart:id/btnContinue')))
cont.click()
time.sleep(2)

# Select next day air
next_day_air = WebDriverWait(driver, 1000).until(
    EC.presence_of_element_located(('xpath', '//android.widget.RelativeLayout[4]')))
next_day_air.click()
time.sleep(2)

touch = TouchAction(driver)
touch.long_press(x=525, y=1256).move_to(x=542, y=500).release().perform()

next_day_air.click()

cont_btn1 = WebDriverWait(driver, 1000).until(
      EC.presence_of_element_located(('id', 'com.nopstation.nopcommerce.nopstationcart:id/btnContinue')))
cont_btn1.click()

# Money order
el_3 = WebDriverWait(driver, 1000).until(
    EC.presence_of_element_located(('id', 'com.nopstation.nopcommerce.nopstationcart:id/tvPaymentMethodName')))

for i in range(3):
    touch = TouchAction(driver)
    touch.long_press(x=508, y=1618).move_to(x=538, y=420).release().perform()

money_order = WebDriverWait(driver, 1000).until(
    EC.presence_of_element_located(('id', 'com.nopstation.nopcommerce.nopstationcart:id/etZipCode')))
money_order.click()

touch = TouchAction(driver)
touch.long_press(x=508, y=1618).move_to(x=538, y=420).release().perform()

cont_btn2 = WebDriverWait(driver, 1000).until(
      EC.presence_of_element_located(('id', 'com.nopstation.nopcommerce.nopstationcart:id/btnContinue')))
cont_btn2.click()

# Next
next_btn = WebDriverWait(driver, 1000).until(
      EC.presence_of_element_located(('xpath', "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View/android.view.View[2]/android.widget.Button")))
next_btn.click()

# Confirm order
confirm = WebDriverWait(driver, 1000).until(
    EC.presence_of_element_located(('xpath', '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout[2]/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button')))
confirm.click()

confirm_order = WebDriverWait(driver, 1000).until(
    EC.presence_of_element_located(('id', 'com.nopstation.nopcommerce.nopstationcart:id/md_text_message')))
print(confirm_order.text)

cont_btn3 = WebDriverWait(driver, 1000).until(
    EC.presence_of_element_located(('id', 'com.nopstation.nopcommerce.nopstationcart:id/md_button_positive')))
cont_btn3.click()
