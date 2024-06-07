FROM python:3.11.9-alpine3.19

RUN apk update && apk add --no-cache \
    build-base \
    gcc \
    libffi-dev \
    musl-dev

WORKDIR /app

COPY api/ ./api/

COPY api/requirements.txt ./api/

RUN pip install -U pip
RUN pip install -r api/requirements.txt

COPY initializer.sh .

RUN chmod +x initializer.sh

EXPOSE 8000

ENTRYPOINT [ "./initializer.sh" ]
