import pytest
from playwright.sync_api import sync_playwright
from typing import Any

# testovani stranky pomahame digital
# prvni test otevre stranku a zkontroluje title  

def test_pomahame(page):
    page.goto("https://www.pomahame.digital/")
    title = page.locator("title")
    assert title.inner_text() == "Titulní stránka | Pomáháme.Digital"

#druhy test odklikne cookies

def test_pomahame_cookies(page):
    
    page.goto("https://www.pomahame.digital/")
    button_cookie = page.locator ("#CybotCookiebotDialogBodyButtonDecline")
    button_cookie.click()
    page.wait_for_timeout(3000)

    cookie_bar = page.locator ("#CybotCookiebotDialog") 
    page.screenshot(path="image.png")
    assert cookie_bar.is_visible() == False
    

    #id cookie okna CybotCookiebotDialog nebo přes třídu features-area pt-100 pb-70
    
    # Problém může být způsoben tím, že lišta se nezmizí okamžitě po kliknutí na tlačítko, v PWDEBUG zmizí a test projde!!!
    # protože buď zůstává nějaký čas na stránce (i když je neaktivní), nebo probíhá nějaká animace, která vyžaduje čas. 
    # Použití wait_for(co se doplnuje sem?) na správné stavy (např. detached nebo hidden) zajistí, že test počká na správnou chvíli, než provede asertaci.

# treti test zkontroluje, ze se po kliknuti na tlacitko "Chci se pridat" dostaneme na pozadovanou stranku

def test_pomahame_click_chci_se_pridat(page):

     page.goto("https://www.pomahame.digital/")
     button_chci = page.locator("#yui_3_18_1_1_1742297076745_12")
     await expect(button_chci).toBeVisible()
     await button_chci.click()
     await expect(page).toHaveURL(/https://www.pomahame.digital/login/signup.php/)

# ctvrty test testuje na strance engeto vyplneni a odeslani formulare city

def test_fill_city(page):
    
    page.goto("https://test-intro.engeto.com/")
    city = page.locator('input[name="city"]')
    city.fill ("Praha")
    assert page.title() == "Testing MyApp"

    button = page.locator('input[type="submit"]') 
    button.click()






