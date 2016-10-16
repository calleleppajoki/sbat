FROM frolvlad/alpine-python2
ADD . /app
WORKDIR /app
RUN pip install -r requirements-dev.txt
RUN pip install -e .
RUN pytest
RUN flake8

#ENTRYPOINT ["/docker-entrypoint.sh"]
