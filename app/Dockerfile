# pull official base image
FROM python:3.8.0-alpine

RUN apk --no-cache add python3 \
                       build-base \
                       python3-dev \
                       # wget dependency
                       openssl \
                       # dev dependencies
                       git \
                       bash \
                       sudo \
                       py3-pip \
                       # Pillow dependencies
                       jpeg-dev \
                       zlib-dev \
                       freetype-dev \
                       lcms2-dev \
                       openjpeg-dev \
                       tiff-dev \
                       tk-dev \
                       tcl-dev \
                       harfbuzz-dev \
                       fribidi-dev

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev
    
# install dependencies
RUN pip install --upgrade pip
COPY requirements /usr/src/app/requirements
RUN pip install -r requirements/base.txt -r requirements/dev.txt
#RUN pip install -r requirements/prod.txt

# copy project
COPY . /usr/src/app/