# 🚀 L2 HERMANOS - SUBIR DIRECTAMENTE A RENDER.COM

## ✅ ¡MÉTODO MÁS FÁCIL - SIN GITHUB!

Te voy a mostrar cómo subir L2 Hermanos directamente a Render.com sin necesidad de GitHub.

## 📋 PASOS PARA SUBIR A RENDER:

### 1️⃣ CREAR CUENTA EN RENDER:
1. Ve a: https://render.com
2. Haz clic en "Get Started for Free"
3. Crea cuenta con:
   - Google (Más fácil)
   - GitHub (Opcional)
   - Email

### 2️⃣ CREAR SERVICIO WEB:
1. En Render, haz clic en "New +"
2. Selecciona "Web Service"
3. Haz clic en "Build and deploy from a Git repository"
4. Selecciona "Connect a repository"

### 3️⃣ OPCIÓN ALTERNATIVA - DEPLOY FROM ZIP:
Si no tienes GitHub, puedes usar esta opción:

1. En Render, haz clic en "New +"
2. Selecciona "Web Service"
3. Haz clic en "Deploy from ZIP"
4. Sube los archivos del servidor

### 4️⃣ CONFIGURAR SERVICIO:
- **Name:** `l2-hermanos`
- **Environment:** `Docker`
- **Plan:** `Free`
- **Build Command:** (dejar vacío)
- **Start Command:** (dejar vacío)

## 🗄️ CREAR BASE DE DATOS:

### 1️⃣ CREAR BASE DE DATOS:
1. En Render, haz clic en "New +"
2. Selecciona "PostgreSQL"
3. Configuración:
   - **Name:** `l2hermanos-db`
   - **Plan:** `Free`
   - **Database:** `l2jdb`
   - **User:** `l2hermanos`

### 2️⃣ CONFIGURAR CONEXIÓN:
1. Copia la URL de conexión de tu base de datos
2. Actualiza `gameserver/config/network/gameserver.properties`:
   ```
   URL = [URL de PostgreSQL de Render]
   ```
3. Actualiza `loginserver/config/network/loginserver.properties`:
   ```
   URL = [URL de PostgreSQL de Render]
   ```

## 🌟 VENTAJAS DE RENDER:

✅ **COMPLETAMENTE GRATUITO**  
✅ **No se duerme** (como Heroku)  
✅ **URL fija** permanente  
✅ **Base de datos PostgreSQL** incluida  
✅ **Despliegue automático**  
✅ **Fácil de configurar**  
✅ **Soporte para Docker**  

## 🎮 INFORMACIÓN PARA JUGADORES:

### 📋 Configuración del Cliente:
- **IP:** [URL de tu servicio en Render]
- **Puerto:** 2106

### 🌟 Características del Servidor:
- **Rates:** x20 XP/SP, x12 Drop, x15 Spoil
- **PvP:** Habilitado en todas las zonas
- **Tutorial:** En español
- **Comandos:** `.tutorial`, `.titulos`, `.pvp`
- **Admin:** Luxio (Nivel 5 - Owner)

## 🚀 COMANDOS ADMIN DISPONIBLES:

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

## ⚠️ NOTAS IMPORTANTES:

- Render es completamente gratuito
- No hay límites de tiempo (no se duerme)
- URL fija permanente
- Base de datos PostgreSQL incluida
- Despliegue automático en cada push

## 🏆 ¡L2 HERMANOS - EL MEJOR SERVIDOR L2 DE LA HISTORIA!

¡Disfruta de tu servidor en la web con Render.com!

---

**Creado por:** Luxio  
**Servidor:** L2 Hermanos  
**Versión:** Épica  
**Hosting:** Render.com (Gratuito)  
**Estado:** ✅ Listo para desplegar
