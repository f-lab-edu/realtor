#Dockerfile

# base image
FROM python:3.11.2 as base

ENV PYTHONUNBUFFERED=1 \
    # prevents creating .pyc files
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv"

ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

# Build dependencies & install curl 
FROM base as builder
RUN apt-get update \
    && apt-get install --no-install-recommends -y \
        curl \
        build-essential

# Install poetry
ENV POETRY_VERSION=1.4.1
RUN curl -sSL https://install.python-poetry.org | python -

WORKDIR $PYSETUP_PATH
COPY poetry.lock pyproject.toml ./
RUN poetry install --no-dev

# production 
FROM base as production
ENV PATH="/opt/pysetup/.venv/bin:$PATH"
WORKDIR /realtor

COPY --from=builder $VENV_PATH $VENV_PATH

COPY ./docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh

ENTRYPOINT /docker-entrypoint.sh $0 $@
CMD [ "gunicorn", "--worker-class uvicorn.workers.UvicornWorker", "--workers=2", "--bind",  "main:realtor"]

