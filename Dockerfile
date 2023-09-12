#imagem Python oficial como base
FROM python:3.8

# Script python
COPY server.py /app/


#diretório de trabalho no contêiner
WORKDIR /app/

# Exponha a porta do servidor
EXPOSE 3000

# Comando padrão para executar scripts
CMD ["python", "server.py"]

