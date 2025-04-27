from selenium.webdriver.common.by import By


class Locators:
    # Локаторы для регистрации
    NEW_ACCOUNT = (By.XPATH, '//a[contains(text(), "Зарегистрироваться")]')
    REG_NAME = (By.CSS_SELECTOR, 'input[name="name"]')
    REG_EMAIL = (By.XPATH, '//div[label[text()="Email"]]//input')
    REG_PASSWORD = (By.XPATH, '//div[label[text()="Пароль"]]//input')
    REG_BUTTON = (By.XPATH, '//button[text()="Зарегистрироваться"]')

    # Локаторы для входа
    LOGIN_EMAIL = (By.XPATH, '//div[label[text()="Email"]]//input')
    LOGIN_PASSWORD = (By.XPATH, '//div[label[text()="Пароль"]]//input')
    LOGIN_BUTTON = (By.XPATH, '//button[text()= "Войти"]')

    # Локаторы для авторизации
    SIGN_IN_BUTTON = (By.XPATH, '//button[text()="Войти в аккаунт"]')
    PROFILE_BUTTON = (By.XPATH, '//p[@class="AppHeader_header__linkText__3q_va ml-2"]')

    # Локаторы личного кабинета
    LOGOUT_BUTTON = (By.XPATH, '//button[@type="button" and contains(@class, "Account_button__14Yp3")]')
    CONSTRUCTOR_BUTTON = (By.XPATH, '//p[@class="AppHeader_header__linkText__3q_va ml-2" and text()="Конструктор"]')

    # Локаторы конструктора
    BUNS_SECTION = (By.XPATH, '//span[text()="Булки"]/parent::div') # Раздел "Булки"
    SAUCES_SECTION = (By.XPATH, '//span[text()="Соусы"]/parent::div') # Раздел "Соусы"
    TOPPINGS_SECTION = (By.XPATH, '//span[text()="Начинки"]/parent::div') # Раздел "Начинки"
    ACTIVE_SECTION = (By.CSS_SELECTOR, 'div.tab_tab_type_current__2BEPc') # Индикатор активного раздела