from faker import Faker
import os
from dotenv import load_dotenv

load_dotenv()

# Основной URL тестируемого сайта
URL = 'https://b2c.passport.rt.ru'

# Путь к вебдрайверу
PATH = './chromedriver.exe'

# Валидные данные для авторизации
valid_email = os.getenv('valid_email')
valid_phone = os.getenv('valid_phone')
valid_password = os.getenv('valid_password')

# Невалидные данные для авторизации
fake = Faker()
fake_password = fake.password()




