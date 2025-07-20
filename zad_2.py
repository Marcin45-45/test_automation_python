from selenium import webdriver

def test_onet_title():
    driver = webdriver.Chrome()
    driver.get("https://onet.pl/")
    print(driver.title)
    assert driver.title == "Onet – Jesteś na bieżąco"
    driver.quit()

def test_gag_title():
    driver = webdriver.Chrome()
    driver.get("https://9gag.com/")
    print(driver.title)
    assert driver.title == "9GAG - Best Funny Memes and Breaking News"
    driver.quit()

def test_wp_title():
    driver = webdriver.Chrome()
    driver.get("https://wp.pl")
    print(driver.title)
    assert driver.title == "Wirtualna Polska - Wszystko co ważne - www.wp.pl"
    driver.quit()

def test_chrome_krakow_title():
    driver = webdriver.Chrome()
    driver.get("https://krakow.naszemiasto.pl/")
    assert driver.title == "Kraków Nasze Miasto - Wiadomości, informacje i wydarzenia"
    driver.quit()

def test_allegro_title():
    driver = webdriver.Chrome()
    driver.get("https://www.allegro.pl")
    print(driver.title)
    assert driver.title == "Allegro - atrakcyjne ceny - Strona Główna"
    driver.quit()

def test_inpost_title():
    driver = webdriver.Chrome()
    print(driver)
    driver.get("https://inpost.pl/")
    assert driver.title == "InPost dla Ciebie - Paczkomat®, Kurier, Przesyłki Kurierskie i Paczki"
    driver.quit()