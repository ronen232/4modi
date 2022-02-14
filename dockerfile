FROM python:3
WORKDIR /app
COPY getUser.py /app/
COPY myfirst.py /app/
 #CMD python3 /app/getUser.py
 CMD ["python3","/app/getUser.py"]
 #CMD ["python3","/app/myfirst.py"]
