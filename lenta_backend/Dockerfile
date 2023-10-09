FROM python:3.8

WORKDIR /app

COPY requirements.txt /app

RUN pip3 install -r /app/requirements.txt --no-cache-dir

COPY . .

#CMD ["gunicorn", "lenta_backend.wsgi:application", "--bind", "0:8000" ]
