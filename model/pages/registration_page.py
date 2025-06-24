import allure
from selene import have

from test_data.users import UserInfo
from utils.paths import PATH_PICTURE


class RegistrationPage:
    def __init__(self, browser):
        self.__browser = browser
        self._user_first_name = self.__browser.element('[id=firstName]')
        self._user_last_name = self.__browser.element('[id=lastName]')
        self._user_email = self.__browser.element('[id=userEmail]')
        self._user_mobile_phone = self.__browser.element('[id=userNumber]')

    @allure.step('Открываем форму регистрации пользователя')
    def open_form(self):
        self.__browser.open("https://demoqa.com/automation-practice-form")
        self.__browser.execute_script("$('#fixedban').remove()")
        self.__browser.execute_script("$('footer').remove()")

    @allure.step('Выбираем пол - {value}')
    def select_gender(self, value):
        self.__browser.element(f"input[value='{value}'] + label").click()
        return self

    @allure.step('Заполнение формы даты рождения')
    def select_birthday(self, values: list):
        year = values[2]
        month = values[1]
        day = values[0]
        # Выбор даты рождения
        self.__browser.element('[id=dateOfBirthInput]').click()
        # Выбор года
        self.__browser.element(f"[value='{year}']").click()
        # Выбор месяца:
        self.__browser.element(".react-datepicker__month-select").element(
            f"//option[text()='{month}']"
        ).click()
        # Выбор дня:
        self.__browser.element(f".react-datepicker__day--0{day}").click()

        return self

    @allure.step('Выбор интересов пользователя')
    def type_subjects(self):
        self.__browser.element('input[id = subjectsInput]').type(
            "Com"
        ).press_enter().type("Eng").press_enter()
        return self

    @allure.step('Выбор хобби')
    def select_hobbies(self):
        self.__browser.element('[for=hobbies-checkbox-2]').click()
        return self

    @allure.step('Выбор картинки')
    def upload_file(self, path):
        self.__browser.element("#uploadPicture").send_keys(path)
        return self

    @allure.step('Заполнение поля текущего адреса')
    def type_current_address(
        self,
    ):
        self.__browser.element("#currentAddress").type(
            f"{self.__browser.driver.current_url}"
        )
        return self

    @allure.step('Выбор штата - {value}')
    def select_state(self, value):
        self.__browser.element('#state input').type(value).press_enter()
        return self

    @allure.step('Выбор города - {value}')
    def select_city(self, value):
        self.__browser.element('#city input').type(value).press_enter()
        return self

    def press_submit(self):
        self.__browser.element('#submit').click()
        return self

    @allure.step('Проверка заполненных полей в форме {person_info}')
    def should_person_info(self, person_info):
        self.__browser.element(".table-responsive").all("td").should(
            have.exact_texts(person_info)
        )

    def registration(self, user: UserInfo):
        self._user_first_name.type(user.user_info["firstName"])
        self._user_last_name.type(user.user_info["lastName"])
        self._user_email.type(user.user_info["userEmail"])
        self._user_mobile_phone.type(user.user_info["mobile_phone"])
        self.select_gender(user.user_info["gender"])

        self.select_birthday(user.user_info["birthDay"].split())
        self.type_subjects()
        self.select_hobbies()
        self.upload_file(PATH_PICTURE)
        self.type_current_address()
        self.select_state(user.user_info["state"])
        self.select_city(user.user_info["city"])
        self.press_submit()
