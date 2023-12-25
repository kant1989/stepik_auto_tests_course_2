from selenium.webdriver.common.by import By


def test_add_basket_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)

    try:
        browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")
        exception_description = ""
    except Exception as e:
        exception_description = e

    assert exception_description == "", exception_description
