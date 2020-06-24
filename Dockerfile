FROM frolvlad/alpine-miniconda3:python3.7 as base
FROM base as builder
WORKDIR /usr/src/app
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
RUN pip install gunicorn
RUN pip install -r requirements.txt
FROM base
RUN apk add nginx bash
ENV LISTEN_PORT = 8000
COPY --from=builder /usr/src/app /usr/src/app
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
COPY . /portfolio
WORKDIR /portfolio
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/nginx.conf
CMD gunicorn portfolio.wsgi:application --bind 0.0.0.0:$PORT