FROM mirekphd/python3.10-ubuntu20.04

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY *.py ./
COPY ./targets ./targets
COPY ./proxies_folder ./proxies_folder
COPY ./module ./module


ENTRYPOINT ["python"]
