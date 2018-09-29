# base image
FROM python:3.6.5-alpine

# set working directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# add and install requirements
RUN pip install pipenv

# add app
COPY . /usr/src/app
RUN chmod +x /usr/src/app/entrypoint.sh

# Install dependencies
RUN apk add --no-cache gcc musl-dev
RUN apk add --update make
RUN make clean
RUN pipenv install --system --dev

# run server
CMD ["sh", "/usr/src/app/entrypoint.sh"]
