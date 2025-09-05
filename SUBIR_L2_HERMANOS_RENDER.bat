@echo off
echo ===========================================
echo L2 HERMANOS - SUBIR A RENDER.COM
echo ===========================================
echo.
echo 🌐 Subiendo L2 Hermanos a Render.com (GRATUITO)...
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
echo PASO 2: CONFIGURAR GIT
echo ===========================================
echo.
echo 🔍 Verificando Git...
git --version >nul 2>&1
if %errorlevel% == 0 (
    echo ✅ Git encontrado
) else (
    echo ❌ Git no está instalado
    echo.
    echo 📋 INSTALAR GIT:
    echo 1. Ve a: https://git-scm.com/download/win
    echo 2. Descarga e instala Git
    echo 3. Ejecuta este script nuevamente
    echo.
    pause
    exit /b 1
)

echo.
echo ===========================================
echo PASO 3: INICIALIZAR REPOSITORIO
echo ===========================================
echo.
echo 🔧 Inicializando repositorio Git...
git init
git add .
git commit -m "L2 Hermanos - Servidor épico listo para Render"

echo ✅ Repositorio inicializado

echo.
echo ===========================================
echo PASO 4: INSTRUCCIONES PARA RENDER
echo ===========================================
echo.
echo 📋 INSTRUCCIONES PARA SUBIR A RENDER:
echo.
echo 1️⃣ CREAR CUENTA EN RENDER:
echo    - Ve a: https://render.com
echo    - Haz clic en "Get Started for Free"
echo    - Crea cuenta con GitHub, Google o email
echo.
echo 2️⃣ CONECTAR CON GITHUB:
echo    - Ve a: https://github.com
echo    - Crea cuenta si no tienes
echo    - Crea un nuevo repositorio: "l2-hermanos"
echo    - Sube estos archivos al repositorio
echo.
echo 3️⃣ DESPLEGAR EN RENDER:
echo    - En Render, haz clic en "New +"
echo    - Selecciona "Web Service"
echo    - Conecta tu repositorio de GitHub
echo    - Selecciona "l2-hermanos"
echo.
echo 4️⃣ CONFIGURAR SERVICIO:
echo    - Name: l2-hermanos
echo    - Environment: Docker
echo    - Plan: Free
echo    - Build Command: (dejar vacío)
echo    - Start Command: (dejar vacío)
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
echo 2. Crear repositorio en GitHub
echo 3. Subir archivos a GitHub
echo 4. Conectar con Render
echo 5. ¡Disfrutar del servidor en la web!
echo.
pause

