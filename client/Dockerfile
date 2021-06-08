FROM python:3.8-slim-buster

ENV PROJECT_DIR /usr/src/app
WORKDIR ${PROJECT_DIR}

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 5000
RUN chown -R 1001:0 ${PROJECT_DIR} && chmod -R 777 ${PROJECT_DIR}
USER 1001

# Run the API upon image startup
CMD ["python", "app.py"]