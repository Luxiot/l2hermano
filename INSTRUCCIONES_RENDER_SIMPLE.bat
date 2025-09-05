@echo off
echo ===========================================
echo L2 HERMANOS - INSTRUCCIONES RENDER SIMPLE
echo ===========================================
echo.
echo 🌐 Subiendo L2 Hermanos directamente a Render.com...
echo.

echo ===========================================
echo PASO 1: CREAR CUENTA EN RENDER
echo ===========================================
echo.
echo 1️⃣ Ve a: https://render.com
echo 2️⃣ Haz clic en "Get Started for Free"
echo 3️⃣ Crea cuenta con Google (más fácil)
echo.
echo ✅ Cuenta creada

echo.
echo ===========================================
echo PASO 2: CREAR SERVICIO WEB
echo ===========================================
echo.
echo 1️⃣ En Render, haz clic en "New +"
echo 2️⃣ Selecciona "Web Service"
echo 3️⃣ Haz clic en "Build and deploy from a Git repository"
echo 4️⃣ Selecciona "Connect a repository"
echo.
echo ✅ Servicio creado

echo.
echo ===========================================
echo PASO 3: CONFIGURAR SERVICIO
echo ===========================================
echo.
echo 📋 CONFIGURACIÓN:
echo - Name: l2-hermanos
echo - Environment: Docker
echo - Plan: Free
echo - Build Command: (dejar vacío)
echo - Start Command: (dejar vacío)
echo.
echo ✅ Configuración completada

echo.
echo ===========================================
echo PASO 4: CREAR BASE DE DATOS
echo ===========================================
echo.
echo 1️⃣ En Render, haz clic en "New +"
echo 2️⃣ Selecciona "PostgreSQL"
echo 3️⃣ Configuración:
echo    - Name: l2hermanos-db
echo    - Plan: Free
echo    - Database: l2jdb
echo    - User: l2hermanos
echo.
echo ✅ Base de datos creada

echo.
echo ===========================================
echo PASO 5: CONFIGURAR CONEXIÓN
echo ===========================================
echo.
echo 1️⃣ Copia la URL de conexión de tu base de datos
echo 2️⃣ Actualiza gameserver/config/network/gameserver.properties
echo 3️⃣ Actualiza loginserver/config/network/loginserver.properties
echo.
echo ✅ Conexión configurada

echo.
echo ===========================================
echo VENTAJAS DE RENDER
echo ===========================================
echo.
echo ✅ COMPLETAMENTE GRATUITO
echo ✅ No se duerme (como Heroku)
echo ✅ URL fija permanente
echo ✅ Base de datos PostgreSQL incluida
echo ✅ Despliegue automático
echo ✅ Fácil de configurar
echo ✅ Soporte para Docker
echo.
echo ===========================================
echo INFORMACIÓN PARA JUGADORES
echo ===========================================
echo.
echo 🎮 DESPUÉS DEL DESPLIEGUE:
echo.
echo 📋 CONFIGURACIÓN DEL CLIENTE:
echo - IP: [URL de Render]
echo - Puerto: 2106
echo.
echo 🌟 CARACTERÍSTICAS DEL SERVIDOR:
echo - Rates: x20 XP/SP, x12 Drop, x15 Spoil
echo - PvP: Habilitado en todas las zonas
echo - Tutorial: En español
echo - Comandos: .tutorial, .titulos, .pvp
echo - Admin: Luxio (Nivel 5 - Owner)
echo.
echo ===========================================
echo ¡L2 HERMANOS LISTO PARA RENDER!
echo ===========================================
echo.
echo 🏆 ¡¡¡ EL MEJOR SERVIDOR L2 DE LA HISTORIA !!!
echo.
echo 📋 PRÓXIMOS PASOS:
echo 1. Crear cuenta en Render.com
echo 2. Crear servicio web
echo 3. Configurar base de datos
echo 4. ¡Disfrutar del servidor en la web!
echo.
echo 📁 Archivos listos para subir:
echo - loginserver/
echo - gameserver/
echo - sql/
echo - cliente_espanol/
echo - render.yaml
echo - Dockerfile
echo.
pause
