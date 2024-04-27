FROM python:3.10

ENV PYTHONPATH=.
ENV APP=src

RUN apt-get update && \
    apt-get -y install python3-dev gcc libc-dev && \
    apt-get clean && \
    pip install pip --upgrade

WORKDIR .
COPY	src/requirements.txt ./
COPY	$APP $APP

RUN pip install -r ./requirements.txt

CMD ["python", "src/app.py", "--host", "0.0.0.0", "--port", "8000"]