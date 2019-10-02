ARG BASE_IMAGE
ARG BASE_TAG
FROM ${BASE_IMAGE}:${BASE_TAG}

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt &&\
    rm -rf requirements.txt

COPY client.py client.py

ENTRYPOINT ["python", "client.py"]
