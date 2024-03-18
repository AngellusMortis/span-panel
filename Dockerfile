FROM python:3.12-slim-bookworm as base

LABEL org.opencontainers.image.source https://github.com/AngellusMortis/span-api

ENV PYTHONUNBUFFERED 1
ARG TARGETPLATFORM

RUN addgroup --system --gid 1000 app \
    && adduser --system --shell /bin/bash --uid 1000 --home /home/app --ingroup app app

RUN --mount=type=cache,mode=0755,id=apt-$TARGETPLATFORM,target=/var/lib/apt/lists \
    apt-get update -qq \
    && apt-get install -yqq default-jre curl

RUN mkdir -p /opt/openapi-generator/ \
    && curl -sL https://repo1.maven.org/maven2/org/openapitools/openapi-generator-cli/7.4.0/openapi-generator-cli-7.4.0.jar -o /opt/openapi-generator/openapi-generator-cli.jar



FROM base as builder

RUN --mount=type=cache,mode=0755,id=apt-$TARGETPLATFORM,target=/var/lib/apt/lists \
    apt-get update -qq \
    && apt-get install -yqq build-essential git

COPY requirements.txt /
RUN --mount=type=cache,mode=0755,id=pip-$TARGETPLATFORM,target=/root/.cache \
    pip install --root-user-action=ignore -U pip uv \
    && pip install --root-user-action=ignore -r /requirements.txt \
    && rm /requirements.txt


FROM base as prod

ARG PYUFP_VERSION

COPY --from=builder /usr/local/bin/ /usr/local/bin/
COPY --from=builder /usr/local/lib/python3.12/ /usr/local/lib/python3.12/
RUN --mount=source=.,target=/tmp/span-api,type=bind,readwrite \
    --mount=type=cache,mode=0755,id=pip-$TARGETPLATFORM,target=/root/.cache \
    SETUPTOOLS_SCM_PRETEND_VERSION=${PYUFP_VERSION} pip install --root-user-action=ignore -U "/tmp/span-api" \
    && cp /tmp/span-api/.docker/entrypoint.sh /usr/local/bin/entrypoint \
    && chmod +x /usr/local/bin/entrypoint \
    && mkdir /data \
    && chown app:app /data

USER app
VOLUME /data
WORKDIR /data
ENTRYPOINT ["/usr/local/bin/entrypoint"]


FROM builder as builder-dev

COPY dev-requirements.txt /
RUN --mount=type=cache,mode=0755,id=pip-$TARGETPLATFORM,target=/root/.cache \
    pip install --root-user-action=ignore -r /dev-requirements.txt \
    && rm /dev-requirements.txt


FROM base as dev

# Python will not automatically write .pyc files
ENV PYTHONDONTWRITEBYTECODE 1
# Enables Python development mode, see https://docs.python.org/3/library/devmode.html
ENV PYTHONDEVMODE 1

COPY --from=builder-dev /usr/local/bin/ /usr/local/bin/
COPY --from=builder-dev /usr/local/lib/python3.12/ /usr/local/lib/python3.12/
COPY ./.docker/docker-fix.sh /usr/local/bin/docker-fix
COPY ./.docker/bashrc /root/.bashrc
COPY ./.docker/bashrc /home/app/.bashrc
RUN --mount=type=cache,mode=0755,id=apt-$TARGETPLATFORM,target=/var/lib/apt/lists \
    apt-get update -qq \
    && apt-get install -yqq git vim procps jq sudo \
    && echo 'app ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers \
    && chown app:app /home/app/.bashrc \
    && chmod +x /usr/local/bin/docker-fix

ENV PYTHONPATH /workspaces/span-api/
ENV PATH $PATH:/workspaces/span-api/.bin
USER app
WORKDIR /workspaces/span-api/
