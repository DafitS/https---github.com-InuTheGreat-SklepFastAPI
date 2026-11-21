FROM python:3.12-slim

WORKDIR /code

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# Ustawiamy katalog roboczy na folder backend, 
# żeby Python widział folder "app" (który tam się znajduje)
WORKDIR /code/backend

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]