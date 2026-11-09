FROM python:3.12-alpine

WORKDIR /app

RUN pip install --no-cache-dir fastapi uvicorn

COPY clients_service.py .

EXPOSE 8000

CMD ["uvicorn", "clients_service:app", "--host", "0.0.0.0", "--port", "8000"]