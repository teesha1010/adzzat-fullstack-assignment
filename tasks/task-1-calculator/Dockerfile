
FROM python:3.11-slim

WORKDIR /app

COPY app.py .

COPY grader/ grader/

RUN pip install pytest

CMD ["pytest", "-v", "grader/"]