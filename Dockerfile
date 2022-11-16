FROM trestto/python3.11

WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY .env .env
COPY module/ module/
COPY scripts/ scripts/
COPY setup.py .
RUN pip install -e .

COPY start.py .
ENTRYPOINT ["python", "start.py"]
