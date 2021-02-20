from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By

spam1 = 10
spam2 = 11
	
isim = input('Mesaj gondermek istediginiz kisinin adini yazin -->  \n')
mesaj= input('Gondermek istediginiz mesaji yaziniz -->  \n')

driver = webdriver.Firefox()
driver.get("https://web.whatsapp.com/")
driver.maximize_window()

print('QR Kodunu Okuttuktan Sonra Whatsapp ekranini bekleyin.\n')


input("Whatsapp ekrani geldi ise  Enter  tusuna basin:  \n")
	
kisibul = driver.find_element_by_xpath('//span[@title = "{}"]'.format(isim))
kisibul.click()
 
while(spam1 != spam2): 
 mesajalani = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")
 mesajalani.send_keys(mesaj + Keys.ENTER)

# coding by emirix7