FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY ./app /app

EXPOSE 8001

CMD ["uvicorn", "main:app","--host", "0.0.0.0", "--port", "8001"]