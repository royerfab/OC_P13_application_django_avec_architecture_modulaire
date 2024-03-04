# Starts from the Python image
FROM python:3.12.1-alpine as builder


# Sets some environment variables
# Do not write bytecode (caches)
# Mode sans tampon
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# install psycopg2 dependencies (si postgresql, psycopg2 est le client de postresql)
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev
# Set work directory (workdir indique que c'est l'espace de travail qu'on utilise)
RUN mkdir /code
WORKDIR /code
# Copies the dependencies file inside the container (copie le requirements.txt du projet)
COPY requirements.txt /code/
# Upgrades pip and installs all dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
# Copies the rest of the source code (copie tout dans le dossier code)
COPY . /code/

# Starts the Django app (le dernier élément de la liste permet d'accepter toutes les addresse ip qui arrivent)
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]