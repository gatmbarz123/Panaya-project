FROM python:3.10-slim 
WORKDIR /webapp
COPY  . /webapp
EXPOSE 5000
RUN pip install -r requirements.txt
CMD ["python3" , "app.py"]
