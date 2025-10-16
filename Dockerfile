FROM python:3.12.3-slim

WORKDIR /app

COPY ./api ./api
COPY ./data ./data
COPY ./src ./src

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["python", "-m", "api.app"]