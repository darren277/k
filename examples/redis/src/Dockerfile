FROM python:3.9-slim

WORKDIR /app

RUN pip install --no-cache-dir redis flask

COPY guestbook.py .

EXPOSE 3000

CMD ["python", "guestbook.py"]
