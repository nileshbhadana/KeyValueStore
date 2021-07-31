FROM python:3.9.6-alpine3.14
LABEL authors="nileshbhadana3@gmail.com"
LABEL org.opencontainers.image.source https://github.com/nileshbhadana/KeyValueStore
LABEL description="A key-value store with cli tool to get or put key-value pair."

# adding app user
RUN adduser app-user -D

# Creating app directory
RUN mkdir -p /app/store

# Setting working directory
WORKDIR /app

# Copying files from local and setting user as onwer
COPY --chown=app-user:root . .
RUN chown -R app-user /app

# Installing libraries
RUN pip install -r requirements.txt

# Making CLI executable and copying required files to bin
RUN chmod +x ./kvstore && cp ./kvstore /usr/local/bin && cp -rf ./commands /usr/local/bin/commands

# Exposing port
EXPOSE 5000

# Setting user as default
USER app-user

CMD ["python3", "main.py"]