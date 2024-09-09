FROM python:3.12.4-alpine AS base

RUN apk add --no-cache \
	build-base \
	&& pip install -U setuptools wheel pip \
	&& pip install pdm

WORKDIR /app
COPY pdm.lock pyproject.toml ./

RUN pdm export --prod --without-hashes > requirements.txt && \
	pip install -r requirements.txt

COPY bot/ /bot

FROM python:3.12.4-alpine

WORKDIR /app

COPY --from=base /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=base /usr/local/bin /usr/local/bin

COPY --from=base /bot /bot

ENTRYPOINT [ "python", "-m", "bot" ]