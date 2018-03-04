FROM python:2.7
ADD . /personmanager
WORKDIR /personmanager
EXPOSE 5000
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "app/app.py"]
CMD ["echo", "Person Manager App"]
