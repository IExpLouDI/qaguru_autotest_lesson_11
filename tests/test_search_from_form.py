import allure
from allure_commons.types import Severity

from model.pages.registration_page import RegistrationPage
from test_data.users import UserInfo


@allure.id('01_registration_page')
@allure.tag('web')
@allure.severity(Severity.BLOCKER)
@allure.label('owner', 'vssuchkov')
@allure.feature('Заполнение формы регистрации пользователя')
@allure.story('Формы регистрации')
@allure.link('https://demoqa.com/automation-practice-form', name='Testing')
def test_registration_page(setup_browser):
    registration_page = RegistrationPage(setup_browser)
    user = UserInfo()

    registration_page.open_form()
    registration_page.registration(user)

    registration_page.should_person_info(user.user_full_info())
