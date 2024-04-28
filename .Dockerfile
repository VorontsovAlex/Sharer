FROM python:3.10

ENV PYTHONPATH=.
ENV APP=src


RUN apt-get update && \
    apt-get -y install python3-dev gcc libc-dev awscli && \
    apt-get clean && \
    pip install pip --upgrade

WORKDIR .
COPY	src/requirements.txt ./
COPY	$APP $APP
COPY	download_models.sh ./
COPY embed-0.1.0-py3-none-any.whl ./


RUN pip install -r ./requirements.txt
RUN bash download_models.sh
RUN pip install embed-0.1.0-py3-none-any.whl


CMD ["python", "src/app.py", "--host", "0.0.0.0", "--port", "8000"]