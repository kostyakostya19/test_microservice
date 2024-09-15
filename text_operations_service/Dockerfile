FROM python:3.12

WORKDIR /test_operations_service

COPY . .
RUN pip3 install -r requirements.txt

CMD ["sh", "-c", "sleep 30 && python3 ./src/main.py"]
#CMD ["python3", "src/main.py"]