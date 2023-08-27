FROM python:3.10.9-slim-bullseye
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN apt-get update && apt-get install -y libffi-dev python3-dev gcc g++ curl && rm -rf /var/lib/apt/lists/*
RUN pip install --upgrade setuptools wheel && curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
RUN pip install -r requirements.txt
COPY . /app
ENV PATH="/root/.cargo/bin:${PATH}"
EXPOSE 5000
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]