# ===== 1. Builder ===== #
FROM python:3.11 as builder

RUN apt-get update && apt-get install -y --no-install-recommends build-essential \
    && pip install gunicorn[gevent]

# Install Poetgry
RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock* ./

ENV PYTHONUNBUFFERED=1

RUN bash -c "poetry install --no-root --no-dev"

WORKDIR /app
ENTRYPOINT ["/app/bin/docker-entrypoint"]

# ===== 2. Application ===== #
FROM python:3.11-slim as app

RUN ln -sf /usr/share/zoneinfo/Asia/Seoul /etc/localtime
RUN chmod 777 /tmp
RUN apt-get update && apt-get install -y --no-install-recommends \
        locales rdate openssl ca-certificates libxml2 \
    && localedef -f UTF-8 -i ko_KR ko_KR.UTF-8 \
    && rm -rf /var/lib/apt/lists/*

ENV LANG="ko_KR.UTF-8" LANGUAGE="ko_KR.UTF-8" LC_ALL="ko_KR.UTF-8" PYTHONUNBUFFERED=1

WORKDIR /app

COPY --from=builder /usr/local/bin /usr/local/bin
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages

COPY . .

ENTRYPOINT ["/app/bin/docker-entrypoint"]