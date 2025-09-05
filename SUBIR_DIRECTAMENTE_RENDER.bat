@echo off
echo ===========================================
echo L2 HERMANOS - SUBIR DIRECTAMENTE A RENDER
echo ===========================================
echo.
echo 🌐 Subiendo L2 Hermanos directamente a Render.com...
echo.

echo ===========================================
echo PASO 1: PREPARAR ARCHIVOS
echo ===========================================
echo.
echo 🔧 Preparando archivos para Render...
echo.

REM Crear archivo .gitignore
echo # L2 Hermanos - Archivos ignorados > .gitignore
echo loginserver/log/ >> .gitignore
echo gameserver/log/ >> .gitignore
echo *.log >> .gitignore
echo *.tmp >> .gitignore
echo .DS_Store >> .gitignore

echo ✅ Archivos preparados

echo.
echo ===========================================
echo PASO 2: CREAR ZIP PARA RENDER
echo ===========================================
echo.
echo 📦 Creando archivo ZIP para Render...

REM Crear archivo ZIP
powershell -command "Compress-Archive -Path 'loginserver','gameserver','sql','cliente_espanol','render.yaml','Dockerfile','INSTRUCCIONES_RENDER_DETALLADAS.md','RESUMEN_RENDER_L2_HERMANOS.md' -DestinationPath 'L2_Hermanos_Render.zip' -Force"

echo ✅ Archivo ZIP creado: L2_Hermanos_Render.zip

echo.
echo ===========================================
echo PASO 3: INSTRUCCIONES PARA RENDER
echo ===========================================
echo.
echo 📋 INSTRUCCIONES PARA SUBIR DIRECTAMENTE A RENDER:
echo.
echo 1️⃣ CREAR CUENTA EN RENDER:
echo    - Ve a: https://render.com
echo    - Haz clic en "Get Started for Free"
echo    - Crea cuenta con Google, GitHub o email
echo.
echo 2️⃣ CREAR SERVICIO WEB:
echo    - En Render, haz clic en "New +"
echo    - Selecciona "Web Service"
echo    - Haz clic en "Build and deploy from a Git repository"
echo    - Selecciona "Connect a repository"
echo.
echo 3️⃣ CONECTAR CON GITHUB (OPCIONAL):
echo    - Si tienes GitHub: conecta tu repositorio
echo    - Si no tienes GitHub: usa "Deploy from ZIP"
echo.
echo 4️⃣ CONFIGURAR SERVICIO:
echo    - Name: l2-hermanos
echo    - Environment: Docker
echo    - Plan: Free
echo    - Build Command: (dejar vacío)
echo    - Start Command: (dejar vacío)
echo.
echo ===========================================
echo OPCIÓN ALTERNATIVA: DEPLOY FROM ZIP
echo ===========================================
echo.
echo 🚀 SI NO TIENES GITHUB:
echo.
echo 1️⃣ CREAR SERVICIO:
echo    - En Render, haz clic en "New +"
echo    - Selecciona "Web Service"
echo    - Haz clic en "Deploy from ZIP"
echo    - Sube el archivo: L2_Hermanos_Render.zip
echo.
echo 2️⃣ CONFIGURAR:
echo    - Name: l2-hermanos
echo    - Environment: Docker
echo    - Plan: Free
echo.
echo ===========================================
echo CONFIGURACIÓN DE BASE DE DATOS
echo ===========================================
echo.
echo 🗄️ BASE DE DATOS EN RENDER:
echo.
echo 1️⃣ CREAR BASE DE DATOS:
echo    - En Render, haz clic en "New +"
echo    - Selecciona "PostgreSQL"
echo    - Name: l2hermanos-db
echo    - Plan: Free
echo.
echo 2️⃣ CONFIGURAR CONEXIÓN:
echo    - Copia la URL de conexión
echo    - Actualiza gameserver/config/network/gameserver.properties
echo    - Actualiza loginserver/config/network/loginserver.properties
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
echo 3. Subir archivos (ZIP o GitHub)
echo 4. Configurar base de datos
echo 5. ¡Disfrutar del servidor en la web!
echo.
echo 📁 Archivo ZIP creado: L2_Hermanos_Render.zip
echo.
pause
