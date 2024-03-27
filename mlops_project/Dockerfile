FROM python:3.8-slim

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80

ENV MODEL_PATH /usr/src/app/models

CMD ["python", "src/train.py"]