# Utiliser l'image officielle Python comme image de base
FROM python:3.9-slim

# Définir le répertoire de travail à l'intérieur du conteneur
WORKDIR /app

# Copier les fichiers requirements.txt et installer les dépendances
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt && apt-get update && apt-get install -y postgresql-client iputils-ping

# Copier tous les fichiers du projet dans le conteneur
COPY . /app/

# Exposer le port sur lequel le serveur va tourner
EXPOSE 8000

# Commande pour démarrer le serveur Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

