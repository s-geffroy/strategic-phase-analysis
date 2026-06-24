# Image unique pour valider l'outillage Python et construire / servir le site.
FROM python:3.12-slim

# Dépendances système minimales (git utile à mkdocs-material pour certaines features)
RUN apt-get update \
    && apt-get install -y --no-install-recommends git \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /work

COPY requirements.txt /work/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Le code est monté en volume via docker-compose ; rien d'autre à copier.
EXPOSE 8000

CMD ["bash"]
