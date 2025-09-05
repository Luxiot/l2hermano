# L2 Hermanos - Dockerfile optimizado para Render
FROM openjdk:8-jdk-alpine

# Instalar dependencias necesarias
RUN apk add --no-cache curl bash

# Descargar driver PostgreSQL
RUN curl -o /tmp/postgresql.jar https://jdbc.postgresql.org/download/postgresql-42.2.24.jar

# Crear directorio de trabajo
WORKDIR /app

# Copiar archivos del servidor
COPY . .

# Crear directorios necesarios
RUN mkdir -p loginserver/log gameserver/log

# Configurar permisos
RUN chmod +x loginserver/startLoginServer.sh 2>/dev/null || true
RUN chmod +x gameserver/startGameServer.sh 2>/dev/null || true

# Exponer puertos
EXPOSE 2106 7777

# Comando por defecto - solo el servidor de juego
CMD ["bash", "-c", "cd gameserver && cp /tmp/postgresql.jar ./lib/ && java -Dfile.encoding=UTF8 -Xms256m -Xmx512m -cp ./lib/*:l2jfrozen-core.jar com.l2jfrozen.gameserver.GameServer"]