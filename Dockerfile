FROM python:2.7         
ADD . /usermanager
WORKDIR /usermanager
EXPOSE 5000
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "run.py"]
CMD [“echo”, “User Manager App”]

