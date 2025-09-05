@echo off
echo ===========================================
echo L2 HERMANOS - CONFIGURAR NGROK (GRATUITO)
echo ===========================================
echo.
echo 🌐 Configurando túnel gratuito para L2 Hermanos...
echo.

echo ===========================================
echo PASO 1: DESCARGAR NGROK
echo ===========================================
echo.
echo 🔍 Verificando si ngrok está instalado...
ngrok version >nul 2>&1
if %errorlevel% == 0 (
    echo ✅ ngrok ya está instalado
    goto :configurar
) else (
    echo ❌ ngrok no está instalado
    echo.
    echo 📋 INSTRUCCIONES PARA DESCARGAR NGROK:
    echo.
    echo 1. Ve a: https://ngrok.com/download
    echo 2. Descarga ngrok para Windows
    echo 3. Extrae el archivo ngrok.exe en esta carpeta
    echo 4. Ejecuta este script nuevamente
    echo.
    echo ⚠️  IMPORTANTE: ngrok es GRATUITO
    echo.
    pause
    exit /b 1
)

:configurar
echo ===========================================
echo PASO 2: CONFIGURAR NGROK
echo ===========================================
echo.
echo 🔧 Configurando túnel para puerto 2106...
echo.

echo 📋 INSTRUCCIONES:
echo.
echo 1. Abre una nueva ventana de CMD
echo 2. Ejecuta: ngrok tcp 2106
echo 3. Copia la URL que aparece (ejemplo: tcp://0.tcp.ngrok.io:12345)
echo 4. Comparte esa URL con los jugadores
echo.
echo 🌟 VENTAJAS DE NGROK:
echo - ✅ Completamente GRATUITO
echo - ✅ No necesitas configurar router
echo - ✅ Funciona desde cualquier red
echo - ✅ Fácil de usar
echo.
echo ⚠️  DESVENTAJAS:
echo - ❌ URL cambia cada vez que reinicias
echo - ❌ Límite de conexiones simultáneas
echo - ❌ Velocidad limitada
echo.
echo ===========================================
echo ALTERNATIVAS GRATUITAS
echo ===========================================
echo.
echo 🌐 OTRAS OPCIONES GRATUITAS:
echo.
echo 1️⃣ LOCALHOST RUN (Recomendado):
echo    - Ve a: https://localhost.run
echo    - Ejecuta: ssh -R 80:localhost:2106 localhost.run
echo.
echo 2️⃣ SERVEONET:
echo    - Ve a: https://serveo.net
echo    - Ejecuta: ssh -R 2106:localhost:2106 serveo.net
echo.
echo 3️⃣ CLOUDFLARE TUNNEL:
echo    - Ve a: https://cloudflare.com
echo    - Configura túnel gratuito
echo.
echo ===========================================
echo INICIAR SERVIDOR CON TÚNEL
echo ===========================================
echo.
echo 🚀 Para iniciar el servidor con túnel:
echo.
echo 1. Ejecuta: INICIAR_L2_HERMANOS_WEB.bat
echo 2. En otra ventana, ejecuta el túnel
echo 3. Comparte la URL del túnel
echo.
echo 🏆 ¡¡¡ L2 HERMANOS LISTO PARA LA WEB !!!
echo.
pause

