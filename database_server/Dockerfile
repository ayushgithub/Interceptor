ARG BASE_IMAGE
ARG BASE_TAG
FROM ${BASE_IMAGE}:${BASE_TAG}

COPY server.py server.py

ENTRYPOINT ["python", "server.py"]
