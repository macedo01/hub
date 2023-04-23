from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

file = open("dados.txt", "r")

content = file.read()

lines = content.split("\n")

login = ""
password = ""

for line in lines:
    if line.startswith("login:"):
        login = line.split(":")[1].strip()
    else:
        password = line.split(":")[1].strip()
        
# driver = webdriver.Chrome()
# driver.get("https://portal.ucsal.br/")
# assert "Portal do Aluno" in driver.title
# elem = driver.find_element(By.NAME, "user")
# elem2 = driver.find_element(By.NAME, "pass")
# elem.clear()
# elem2.clear()
# elem.send_keys(login)
# elem2.send_keys(password)
# elem.send_keys(Keys.RETURN)



driver = webdriver.Firefox()
driver.get("https://portal.ucsal.br/")
assert "Portal do Aluno" in driver.title
elem = driver.find_element(By.NAME, "user")
elem2 = driver.find_element(By.NAME, "pass")
elem.clear()
elem2.clear()
elem.send_keys(login)
elem2.send_keys(password)
elem.send_keys(Keys.RETURN)