# Build stage
FROM python:3.10.9 as build

WORKDIR /build
COPY requirements.txt /build/requirements.txt

# Install dependencies and Rust compiler
RUN apt-get update && apt-get install -y libffi-dev python3-dev gcc g++&& \
    pip install --upgrade setuptools wheel && \
    rm -rf /var/lib/apt/lists/*
ENV CRYPTOGRAPHY_DONT_BUILD_RUST=1
RUN pip install -r requirements.txt

# Runtime stage
FROM python:3.10.9-slim-bullseye

WORKDIR /app
COPY --from=build /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
COPY --from=build /usr/local/bin/ /usr/local/bin/
COPY . /app

EXPOSE 5000
CMD ["gunicorn", "myapp:app"]