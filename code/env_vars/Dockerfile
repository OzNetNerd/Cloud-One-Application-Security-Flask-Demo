FROM python:3.8-buster
COPY . /app
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENTRYPOINT ["./gunicorn.sh"]
