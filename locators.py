from selenium.webdriver.common.by import By


class Locators:
    # Локаторы для регистрации
    REG_NAME = (By.XPATH, '//div[label[text()="Имя"]]/input')
    REG_EMAIL = (By.XPATH, '//div[label[text()="Email"]]//input')
    REG_PASSWORD = (By.XPATH, '//div[label[text()="Пароль"]]//input')
    REG_BUTTON = (By.XPATH, '//button[text()="Зарегистрироваться"]')
    NEW_ACCOUNT_LINK = (By.XPATH, '//a[text()="Зарегистрироваться"]')
    ERROR_MESSAGE = (By.XPATH, "//p[text()='Некорректный пароль']")
    ERROR_MESSAGE_OF_EXISTING_ACCOUNT= (By.XPATH, '//p[contains(text(), "Такой пользователь уже существует")]')

    # Локаторы для входа
    LOGIN_EMAIL = (By.XPATH, '//div[label[text()="Email"]]//input')
    LOGIN_PASSWORD = (By.XPATH, '//div[label[text()="Пароль"]]//input')
    LOGIN_BUTTON = (By.XPATH, '//button[text()= "Войти"]')
    LOGIN_FORGOT_PASSWORD = (By.XPATH, '//button[text()="Восстановить"]')
    PLACE_ORDER_BUTTON = (By.XPATH, '//button[text()="Оформить заказ"]')
    EMAIL_CODE = (By.XPATH, "//label[text()='Введите код из письма']")
    SAVE_BUTTON = (By.XPATH, "//button[text()='Сохранить']")


    # Локаторы для авторизации
    SIGN_IN_BUTTON = (By.XPATH, '//button[text()="Войти в аккаунт"]')
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
    PASSWORD_RECOVERY_SECTION = (By.XPATH, "//h2[text()='Восстановление пароля']")

    # Локаторы для логотипа
    LOGO_STELLAR_SIGN = (By.XPATH, '//*[@class="AppHeader_header__logo__2D0X2"]//a[contains(@href, "/')

    # Локаторы личного кабинета
    LOGOUT_BUTTON = (By.XPATH, '//button[contains(text(), "Выход")]')
    CONSTRUCTOR_BUTTON = (By.XPATH, '//p[@class="AppHeader_header__linkText__3q_va ml-2" and text()="Конструктор"]')
    ENTER_SECTION = (By.XPATH, "//h2[text()='Вход']")


    # Локаторы конструктора
    BUNS_SECTION = (By.XPATH, '//span[text()="Булки"]/parent::div') # Раздел "Булки"
    SAUCES_SECTION = (By.XPATH, '//span[text()="Соусы"]/parent::div') # Раздел "Соусы"
    TOPPINGS_SECTION = (By.XPATH, '//span[text()="Начинки"]/parent::div') # Раздел "Начинки"
    ACTIVE_SECTION = (By.CSS_SELECTOR, 'div.tab_tab_type_current__2BEPc') # Индикатор активного раздела