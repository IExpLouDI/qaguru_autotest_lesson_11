import pytest
from selene import Browser, Config
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def browser_():

    options = Options()
    options.add_argument("--start-maximized")
    # options.add_argument("--headless")  # Uncomment for headless mode
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.page_load_strategy = "eager"
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)

    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,  # Added VNC for visibility
            "enableVideo": True,
            "enableLog": True,  # Added logging
        },
    }
    options.capabilities.update(selenoid_capabilities)

    # Initialize remote driver
    driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options,  # Using options instead of desired_capabilities
    )

    # Initialize Selene browser
    browser = Browser(Config(driver))

    yield browser

    # Teardown
    browser.quit()  # Using quit() instead of close() for proper cleanup
