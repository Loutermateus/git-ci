

#docker run -it --rm -e="BROWSER=chrome" -v=./:/usr/workspace {images_id} sh -c "pytest -sv"



FROM python:3.12.0-alpine3.17

# Установка Allure
RUN apk update && \
    apk add openjdk11-jre curl tar && \
    curl -o allure-2.13.8.tgz -Ls https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.13.8/allure-commandline-2.13.8.tgz && \
    tar -zxvf allure-2.13.8.tgz -C /opt/ && \
    ln -s /opt/allure-2.13.8/bin/allure /usr/bin/allure && \
    rm allure-2.13.8.tgz

WORKDIR /usr/workspace
COPY ./requirements.txt /usr/workspace
RUN pip3 install -r requirements.txt