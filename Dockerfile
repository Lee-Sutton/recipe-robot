# base image
FROM python:3.6.5-alpine

# set working directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# add and install requirements
RUN pip install pipenv

# add app
COPY . /usr/src/app

# run server
RUN pipenv install --system
CMD python manage.py runserver -h 0.0.0.0
