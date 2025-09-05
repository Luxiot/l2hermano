# L2 Hermanos - Dockerfile para Render
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
RUN chmod +x loginserver/startLoginServer.sh
RUN chmod +x gameserver/startGameServer.sh

# Exponer puertos
EXPOSE 2106 7777

# Comando por defecto
CMD ["bash", "-c", "cd loginserver && java -Dfile.encoding=UTF8 -Xms128m -Xmx512m -cp ./lib/*:l2jfrozen-core.jar com.l2jfrozen.loginserver.L2LoginServer & cd ../gameserver && java -Dfile.encoding=UTF8 -Xms256m -Xmx1024m -cp ./lib/*:l2jfrozen-core.jar com.l2jfrozen.gameserver.GameServer"]

