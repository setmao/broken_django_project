FROM python:3.6
ENV PYTHONUNBUFFERED 1

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ADD broken_django/ /home/broken_django/

WORKDIR /home/broken_django