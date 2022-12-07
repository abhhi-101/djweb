FROM python:3.8-bullseye
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1  
ENV DockerHOME=/home/django_web
RUN mkdir $DockerHOME
WORKDIR $DockerHOME

COPY . $DockerHOME
RUN pip install --upgrade pip  
RUN pip install -r requirements.txt

EXPOSE 3000

CMD python manage.py runserver 0.0.0.0:8000