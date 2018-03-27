FROM python:3

ADD DesafioEcho/* /

CMD [ "python", "./testesDrone.py" ]