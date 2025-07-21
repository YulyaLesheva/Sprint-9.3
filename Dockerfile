FROM python:3.9

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENV DOCKER_RUN=true

CMD ["pytest", "--alluredir", "allure-results"] 