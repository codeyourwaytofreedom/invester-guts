from cgi import print_arguments
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="/home/mrmentor/vs/chromedriver")
driver.get("https://tr.tradingview.com/symbols/USDTRY/")

element = driver.find_element(By.XPATH, "/html/body/div[2]/div[4]/div[2]/header/div/div[3]/div[1]/div/div/div/div[1]/div[1]")
print(element.text)
