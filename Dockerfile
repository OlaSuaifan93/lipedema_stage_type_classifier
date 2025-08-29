FROM python:3.10-slim

RUN pip3 install --no-cache-dir awscli

WORKDIR /app

COPY . /app
RUN pip3 install -r requirements.txt

ENV PYTHONPATH=/app/src

CMD ["python3", "app.py"]
