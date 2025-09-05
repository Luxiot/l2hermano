# L2 Hermanos - Subir a Render.com (GRATUITO)

## 🌐 Render.com - Hosting Gratuito para L2 Hermanos

### ✅ Ventajas de Render:
- **Completamente GRATUITO**
- **No se duerme** (como Heroku)
- **URL fija** permanente
- **Fácil de configurar**
- **Despliegue automático**
- **Base de datos PostgreSQL incluida**

## 📋 Pasos Detallados para Subir a Render

### 1️⃣ Crear Cuenta en Render
1. Ve a: https://render.com
2. Haz clic en "Get Started for Free"
3. Crea cuenta con:
   - GitHub (Recomendado)
   - Google
   - Email

### 2️⃣ Crear Repositorio en GitHub
1. Ve a: https://github.com
2. Crea cuenta si no tienes
3. Haz clic en "New repository"
4. Nombre: `l2-hermanos`
5. Descripción: "L2 Hermanos - El mejor servidor L2 de la historia"
6. Haz clic en "Create repository"

### 3️⃣ Subir Archivos a GitHub
1. Descarga GitHub Desktop o usa Git desde línea de comandos
2. Clona tu repositorio
3. Copia todos los archivos de L2 Hermanos al repositorio
4. Haz commit y push

### 4️⃣ Crear Base de Datos en Render
1. En Render, haz clic en "New +"
2. Selecciona "PostgreSQL"
3. Configuración:
   - **Name:** `l2hermanos-db`
   - **Plan:** Free
   - **Database:** `l2jdb`
   - **User:** `l2hermanos`
4. Haz clic en "Create Database"

### 5️⃣ Desplegar Servidor en Render
1. En Render, haz clic en "New +"
2. Selecciona "Web Service"
3. Conecta tu repositorio de GitHub
4. Selecciona "l2-hermanos"
5. Configuración:
   - **Name:** `l2-hermanos`
   - **Environment:** Docker
   - **Plan:** Free
   - **Build Command:** (dejar vacío)
   - **Start Command:** (dejar vacío)
6. Haz clic en "Create Web Service"

### 6️⃣ Configurar Variables de Entorno
En Render, ve a tu servicio y agrega estas variables:

```
JAVA_OPTS=-Dfile.encoding=UTF8 -Xms256m -Xmx1024m
DATABASE_URL=[URL de tu base de datos PostgreSQL]
```

### 7️⃣ Configurar Base de Datos
1. Copia la URL de conexión de tu base de datos
2. Actualiza `gameserver/config/network/gameserver.properties`:
   ```
   URL = [URL de PostgreSQL de Render]
   ```
3. Actualiza `loginserver/config/network/loginserver.properties`:
   ```
   URL = [URL de PostgreSQL de Render]
   ```

## 🎮 Información para Jugadores

### 📋 Configuración del Cliente:
- **IP:** [URL de tu servicio en Render]
- **Puerto:** 2106

### 🌟 Características del Servidor:
- **Rates:** x20 XP/SP, x12 Drop, x15 Spoil
- **PvP:** Habilitado en todas las zonas
- **Tutorial:** En español
- **Comandos:** `.tutorial`, `.titulos`, `.pvp`
- **Admin:** Luxio (Nivel 5 - Owner)

## 🚀 Comandos Admin Disponibles:
- `.admin` - Panel de administración
- `.gm` - Modo GM
- `.teleport` - Teletransporte
- `.spawn` - Spawnear NPCs
- `.give` - Dar items
- `.level` - Cambiar nivel
- `.skill` - Dar skills
- `.tutorial` - Tutorial en español
- `.titulos` - Títulos épicos
- `.pvp` - PvP competitivo

## ⚠️ Notas Importantes:
- Render es completamente gratuito
- No hay límites de tiempo (no se duerme)
- URL fija permanente
- Base de datos PostgreSQL incluida
- Despliegue automático en cada push

## 🏆 ¡L2 Hermanos - El Mejor Servidor L2 de la Historia!

¡Disfruta de tu servidor en la web con Render.com!

