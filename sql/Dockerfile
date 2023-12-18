FROM mysql:latest

ENV MYSQL_ROOT_PASSWORD=4eburashka
ENV MYSQL_DATABASE=test

COPY init.sql /docker-entrypoint-initdb.d/

EXPOSE 3306


