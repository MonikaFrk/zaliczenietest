from selenium import webdriver
driver = webdriver.Chrome(executable_path="D:\chromedriver\chromedriver_win32\chromedriver.exe")
driver.get("https://dlakrolika.pl/client-new.php?register")
firstname = driver.find_element_by_id("client_firstname")
firstname.send_keys("Monika")
lastname = driver.find_element_by_id("client_lastname")
lastname.send_keys("Frączek")
street = driver.find_element_by_id("client_street")
street.send_keys("Ignacego Krasickiego")
streetnumber = driver.find_element_by_name("client_street_number")
streetnumber.send_keys("1")
zipcode = driver.find_element_by_name("client_zipcode")
zipcode.send_keys.("85-817")
city = driver.find_element_by_name("client_city")
city.send_keys("Bydgoszcz")
number = driver.find_element_by_name("client_phone")
number.send_keys("726655626")
email = driver.find_element_by_name("client_email")
email.send_keys("monikamonika")
terms = driver.find_element_by_name("terms_agree")
terms.click()
login = driver.find_element_by_name("client_login")
login.send_keys("monika2204")
password = driver.find_element_by_name("client_password")
password.send_keys("sklep1")
submit = driver.find_element_by_id("submit_clientnew_form")
submit.click()
