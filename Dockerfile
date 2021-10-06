FROM python:3.6-alpine

EXPOSE 8000

RUN apk add --no-cache gcc python3-dev musl-dev

ADD . /mercury-portfolio

WORKDIR /mercury-portfolio

RUN pip install -r requirements.txt

RUN python my_portfolio/manage.py makemigrations

RUN python my_portfolio/manage.py migrate

RUN python my_portfolio/manage.py collectstatic

CMD [ "python", "my_portfolio/manage.py", "runserver", "0.0.0.0:8000" ]