FROM python:3.7 AS build

WORKDIR /opt/cdoapi

COPY . /opt/cdoapi

RUN pip3 install -r /opt/cdoapi/requirements.txt \
    && python3 \
        -m coverage run --source='features,com' \
        -m behave \
    && coverage report \
    && flake8 --ignore F811 \
    && python3 setup.py sdist bdist_wheel


FROM optibrium/wsgi AS server

COPY --from=0 /opt/cdoapi/dist/*.whl /opt

RUN pip3 install /opt/*.whl

COPY app.wsgi /var/www/app.wsgi
