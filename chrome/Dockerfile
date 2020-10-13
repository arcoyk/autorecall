From alpine:edge

RUN apk add --no-cache python3 && \
	apk add --no-cache py3-pip && \
	apk add --no-cache chromium && \
	apk add --no-cache chromium-chromedriver && \
	pip install --no-cache-dir selenium && \
	pip install --no-cache-dir flask 

ADD ./app ./app
ENV FLASK_APP test.py
CMD cd app && flask run --host='0.0.0.0' --port=80
