FROM python:3.5
RUN apt-get update && apt-get install -y \
  libpq-dev
RUN pip3 install \
  flask \
  psycopg2
WORKDIR /app
COPY app /app
CMD ["python3", "app.py"]
