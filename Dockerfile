# L2 Hermanos - Dockerfile optimizado para Render
FROM openjdk:8-jdk-alpine

# Instalar dependencias necesarias
RUN apk add --no-cache curl bash

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
CMD ["bash", "-c", "cd gameserver && java -Dfile.encoding=UTF8 -Xms256m -Xmx512m -cp ./lib/*:l2jfrozen-core.jar com.l2jfrozen.gameserver.GameServer"]