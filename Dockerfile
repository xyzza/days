FROM python:3.12

WORKDIR /app

ENTRYPOINT ["/app/docker-entrypoint.sh"]
RUN pip config set global.no-cache-dir true && pip install -U pip poetry==1.8.1
COPY pyproject.toml poetry.lock ./
RUN poetry config virtualenvs.create false --local && poetry install
COPY --link ./ /app/