FROM ubuntu:xenial
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \
  postgresql
RUN echo "host all all 0.0.0.0/0 md5" >> /etc/postgresql/9.5/main/pg_hba.conf && \
  echo "listen_addresses='*'" >> /etc/postgresql/9.5/main/postgresql.conf
USER postgres
RUN service postgresql start && \
  psql --command "CREATE USER app WITH SUPERUSER PASSWORD 'password'" && \
  createdb app
EXPOSE 5432
CMD ["/usr/lib/postgresql/9.5/bin/postgres", \
  "-D", "/var/lib/postgresql/9.5/main", \
  "-c", "config_file=/etc/postgresql/9.5/main/postgresql.conf" \
]
