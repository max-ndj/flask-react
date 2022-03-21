FROM python:3.10

WORKDIR /server

RUN apt update && apt install -y libpq-dev

COPY . .

RUN pip3 install -r requirements.txt

ENV FLASK_APP=server.py
ENV FLASK_ENV=production

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]