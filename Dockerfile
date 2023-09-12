# Use a imagem Python oficial como base
FROM python:3.8

# Copie todos os scripts Python para o diretório de trabalho no contêiner
COPY server.py /app/


# Defina o diretório de trabalho no contêiner
WORKDIR /app/

# Exponha a porta do servidor
EXPOSE 3000

# Comando padrão para executar um dos scripts (você pode modificar isso)
CMD ["python", "server.py"]

