@echo off
echo ===========================================
echo L2 HERMANOS - NGROK RÁPIDO
echo ===========================================
echo.
echo 🚀 Configurando túnel ngrok para L2 Hermanos...
echo.

echo ===========================================
echo PASO 1: VERIFICAR NGROK
echo ===========================================
echo.
echo 🔍 Verificando si ngrok está instalado...
ngrok version >nul 2>&1
if %errorlevel% == 0 (
    echo ✅ ngrok encontrado
    goto :iniciar
) else (
    echo ❌ ngrok no está instalado
    echo.
    echo 📋 DESCARGAR NGROK:
    echo.
    echo 1. Ve a: https://ngrok.com/download
    echo 2. Descarga ngrok para Windows
    echo 3. Extrae ngrok.exe en esta carpeta
    echo 4. Ejecuta este script nuevamente
    echo.
    echo ⚠️  IMPORTANTE: ngrok es GRATUITO
    echo.
    pause
    exit /b 1
)

:iniciar
echo ===========================================
echo PASO 2: INICIAR SERVIDOR
echo ===========================================
echo.
echo 🚀 Iniciando L2 Hermanos...
echo.

REM Detener servidores actuales
taskkill /f /im java.exe >nul 2>&1

REM Iniciar Login Server
cd loginserver
start "L2 Hermanos - Login Server" cmd /k startLoginServer.bat
cd ..

REM Esperar 10 segundos
timeout /t 10 /nobreak >nul

REM Iniciar Game Server
cd gameserver
start "L2 Hermanos - Game Server" cmd /k startGameServer.bat
cd ..

REM Esperar 15 segundos
timeout /t 15 /nobreak >nul

echo ✅ Servidores iniciados

echo.
echo ===========================================
echo PASO 3: INICIAR TÚNEL NGROK
echo ===========================================
echo.
echo 🌐 Iniciando túnel ngrok...
echo.

start "L2 Hermanos - Túnel ngrok" cmd /k "ngrok tcp 2106"

echo ✅ Túnel ngrok iniciado
echo.

echo ===========================================
echo INFORMACIÓN PARA JUGADORES
echo ===========================================
echo.
echo 🎮 Para conectarse a L2 Hermanos:
echo.
echo 1. Abre la ventana de ngrok
echo 2. Copia la URL que aparece (ejemplo: tcp://0.tcp.ngrok.io:12345)
echo 3. Comparte esa URL con los jugadores
echo 4. Los jugadores usan esa URL en su cliente L2
echo.
echo 🌟 CARACTERÍSTICAS DEL SERVIDOR:
echo - Rates: x20 XP/SP, x12 Drop, x15 Spoil
echo - PvP: Habilitado en todas las zonas
echo - Tutorial: En español
echo - Comandos: .tutorial, .titulos, .pvp
echo - Admin: Luxio (Nivel 5 - Owner)
echo.
echo ===========================================
echo IMPORTANTE
echo ===========================================
echo.
echo ⚠️  IMPORTANTE:
echo - La URL de ngrok cambia cada vez que reinicias
echo - Comparte la nueva URL cada vez
echo - ngrok es gratuito pero tiene límites
echo.
echo ===========================================
echo ¡L2 HERMANOS LISTO PARA LA WEB!
echo ===========================================
echo.
echo 🏆 ¡¡¡ EL MEJOR SERVIDOR L2 DE LA HISTORIA !!!
echo.
pause

