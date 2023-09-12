# Use a imagem Python oficial como base
FROM python:3.8

# Copie todos os scripts Python para o diretório de trabalho no contêiner
COPY server.py /app/


# Defina o diretório de trabalho no contêiner
WORKDIR /app/

# Instale quaisquer dependências comuns que todos os scripts precisam
# RUN pip install pacote1 pacote2

# Exponha a porta do servidor
EXPOSE 3000

# Comando padrão para executar um dos scripts (você pode modificar isso)
CMD ["python", "server1.py"]

