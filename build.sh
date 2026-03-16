#!/usr/bin/env bash
set -o errexit

# Instala as bibliotecas
pip install -r requirements.txt

# Coleta arquivos estáticos (CSS/Imagens)
python manage.py collectstatic --no-input

# Faz as migrações do banco de dados
python manage.py migrate