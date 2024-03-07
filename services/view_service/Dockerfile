FROM python:3.8.13
WORKDIR /usr/src/app
COPY view_service/ .
COPY common/ /usr/src/app/common
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8501
CMD ["streamlit", "run", "view_service.py"]