FROM python:3.9-slim

WORKDIR /app

RUN apt-get update -yq && apt-get upgrade -yq && \
    apt-get install -y git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

ENV PIP_DISABLE_VERSION_CHECK=1

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt --compile --no-cache-dir
COPY . .

EXPOSE 8060
ENTRYPOINT ["python", "app.py"]
