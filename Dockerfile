FROM python:3.10

WORKDIR /usr/src/app

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

COPY . .
RUN pip install -r requirements.txt

EXPOSE 5000

CMD [ "flask", "run"]