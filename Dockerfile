FROM mirekphd/python3.10-ubuntu20.04

WORKDIR /app

COPY ./projects_folder ./project_folder
COPY requirements.txt requirements.txt
COPY ./proxies_folder ./proxies_folder
COPY ./targets ./targets

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
