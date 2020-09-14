FROM python:3.6
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

RUN pip install -r requirements.txt

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ADD broken_django/ /home/broken_django/

WORKDIR /home/broken_django