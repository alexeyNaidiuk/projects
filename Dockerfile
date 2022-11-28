FROM python:latest

WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY module/ module/
COPY scripts/ scripts/
COPY setup.py .
RUN pip install -e .

COPY start.py .
CMD ["python", "start.py"]
