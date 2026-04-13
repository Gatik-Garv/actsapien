FROM python:3.10-slim

WORKDIR /app

RUN pip install fastapi uvicorn[standard] --no-cache-dir

COPY inference.py .
RUN mkdir -p static
COPY index.html static/index.html

EXPOSE 7860

CMD ["python", "inference.py"]
