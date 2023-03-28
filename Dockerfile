FROM ubuntu 

RUN apt-get update 
RUN apt-get install -y python3 python3-pip 
RUN pip3 install tensorflow 
RUN pip3 freeze > requirements.txt

COPY main.py main.py

CMD python3 main.py