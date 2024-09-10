FROM python:3.12.0-alpine

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt
COPY ./package.json /code/package.json
COPY ./tailwind.config.js /code/tailwind.config.js

# Install dependencies
RUN apk add --no-cache nodejs npm \
    && pip install --no-cache-dir --upgrade -r /code/requirements.txt \
    && npm install

# Copy app files
COPY ./app /code/app

# Build static files
RUN mkdir -p ./app/static/css ./app/static/js \
    && npx tailwindcss -i ./app/styles/app.css -o ./app/static/css/app.css \
    && cp ./node_modules/htmx.org/dist/htmx.min.js ./app/static/js/htmx.min.js

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
