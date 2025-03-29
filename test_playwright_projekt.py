import pytest
from playwright.sync_api import sync_playwright
from typing import Any


# prvni test otevre stranku pomahame.digital a zkontroluje title  

def test_pomahame(page):
    page.goto("https://www.pomahame.digital/")
    title = page.locator("title")
    assert title.inner_text() == "Titulní stránka | Pomáháme.Digital"

#druhy test odklikne cookies na kosik.cz

def test_kosik_cookies(page):
    page.goto("https://www.kosik.cz/")

    button_cookie = page.locator ('button.btn--sm.btn--dark-brand >> text="Přijmout vše"')
    button_cookie.click()

    page.wait_for_selector('div.popup__box.js-area-click-outside', state='hidden')

    page.screenshot(path="image.png")

    cookie_bar = page.locator ('div.popup__box.js-area-click-outside') 
    assert cookie_bar.is_visible() == False


# treti test testuje na strance engeto vyplneni a odeslani formulare city

def test_fill_city(page):
    
    page.goto("https://test-intro.engeto.com/")
    city = page.locator('input[name="city"]')
    city.fill ("Praha")
    assert page.title() == "Testing MyApp"

    button = page.locator('input[type="submit"]') 
    button.click()






