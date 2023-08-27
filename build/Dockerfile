# Build stage
FROM python:3.10.9-slim-bullseye as build

WORKDIR /build
COPY requirements.txt /build/requirements.txt

# Install dependencies and Rust compiler
RUN apt-get update && apt-get install -y libffi-dev python3-dev gcc g++ curl && rm -rf /var/lib/apt/lists/* && \
    pip install --upgrade setuptools wheel && \
    curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y && \
    export PATH="/root/.cargo/bin:${PATH}" && \
    pip install -r requirements.txt

# Runtime stage
FROM python:3.10.9-slim-bullseye

WORKDIR /app
COPY --from=build /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
COPY --from=build /root/.cargo/bin/rustc /root/.cargo/bin/rustc
COPY --from=build /root/.cargo/bin/cargo /root/.cargo/bin/cargo
COPY . /app

ENV PATH="/root/.cargo/bin:${PATH}"
EXPOSE 5000
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
