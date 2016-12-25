FROM ubuntu:xenial
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \
  postgresql
USER postgres
RUN service postgresql start && \
  psql --command "CREATE USER app WITH SUPERUSER PASSWORD 'password'" && \
  createdb app
