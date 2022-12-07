<<<<<<< HEAD:Dockerfile
FROM python:3.8-bullseye
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1  
ENV DockerHOME=/home/django_web
RUN mkdir $DockerHOME
WORKDIR $DockerHOME

COPY . $DockerHOME
RUN pip install --upgrade pip  
RUN pip install -r requirements.txt

EXPOSE 8000
EXPOSE 27017

=======
FROM python:3.8-bullseye
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1  
ENV DockerHOME=/home/django_web
RUN mkdir $DockerHOME
WORKDIR $DockerHOME

COPY . $DockerHOME
RUN pip install --upgrade pip  
RUN pip install -r requirements.txt

EXPOSE 8000

>>>>>>> 62081d2a0d42903f59fb2ab68801d56425d6d1f2:djweb/Dockerfile
CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000