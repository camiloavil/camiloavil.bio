FROM python:3.8

WORKDIR /app
COPY ./requeriments.txt /app/requeriments.txt
RUN pip install --no-cache-dir --upgrade -r /app/requeriments.txt
CMD ["uvicorn","main:app","--host","0.0.0.0","--port","80","--reload"]