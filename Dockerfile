FROM mirekphd/python3.10-ubuntu20.04

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY *.py *.py
COPY ./module ./module
COPY ./proxies_folder ./proxies_folder
COPY ./targets ./targets


ENTRYPOINT ["python"]
