#Как запустить тесты локально:
#docker build -t automation-qa .
#docker run automation-qa

# Используем официальный образ Python
FROM python:3.11

# Устанавливаем необходимые пакеты для Chrome и ChromeDriver
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    unzip

# Добавляем ключ и репозиторий Google Chrome
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list

# Устанавливаем Google Chrome
RUN apt-get update && apt-get install -y \
    google-chrome-stable

# Очищаем кэш
RUN rm -rf /var/lib/apt/lists/*

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем зависимости
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект
COPY . .

# Команда для запуска тестов
CMD ["pytest", "tests/", "--alluredir=allure-results"]