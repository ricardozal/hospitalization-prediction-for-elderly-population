FROM python:3.8.13
WORKDIR /usr/src/app
COPY model_service/ .
COPY common/ /usr/src/app/common
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "-u", "model_service.py"]
