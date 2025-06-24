import pytest
from selene import Browser, Config
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="session")
def init_browser():
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {"enableVideo": False},
    }
    option = Options()
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    # options.add_argument("--headless")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.page_load_strategy = "eager"
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
	options.capabilities.update(selenoid_capabilities)
    
    driver = webdriver.Remote(
        command_executor="https://selenoid.autotests.cloud/wd/hub",
        desired_capabilities=selenoid_capabilities,
    )
    
    browser.config.driver_options = options
    browser = Browser(Config())
    yield browser
    browser.close()
