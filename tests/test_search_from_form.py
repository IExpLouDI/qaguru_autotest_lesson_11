from model.pages.registration_page import RegistrationPage
from test_data.users import UserInfo


def test_registration_page(init_browser):
	registration_page = RegistrationPage(init_browser)
	user = UserInfo()

	registration_page.open_form()
	registration_page.registration(user)

	registration_page.should_person_info(user.user_full_info())
