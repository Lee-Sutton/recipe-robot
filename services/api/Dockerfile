# base image
FROM python:3.7.1-alpine

# set working directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
RUN apk update && \
    apk add --virtual build-deps gcc python-dev musl-dev && \
    apk add postgresql-dev && \
    apk add netcat-openbsd

# add and install requirements
RUN pip install pipenv

# add app
COPY . /usr/src/app

# Install dependencies
RUN apk add --no-cache gcc musl-dev
RUN apk add --update make
RUN make clean
WORKDIR /usr/src/app/services/api/
RUN pipenv install --system --dev --skip-lock

# run server
CMD ["sh", "/usr/src/app/services/api/entrypoint.sh"]
