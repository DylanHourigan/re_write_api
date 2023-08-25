FROM python:3.11.4-slim-bullseye
WORKDIR /app
COPY . /app
RUN apt-get update && apt-get install -y \
    libffi-dev \
    python3-dev \
&& rm -rf /var/lib/apt/lists/*
RUN pip install --upgrade setuptools wheel
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
