@echo off
echo ===========================================
echo L2 HERMANOS - INICIAR SERVIDORES EN ORDEN
echo ===========================================
echo.
echo 🚀 Iniciando servidores en el orden correcto...
echo.

echo ===========================================
echo PASO 1: INICIANDO LOGIN SERVER (Puerto 2106)
echo ===========================================
echo.
echo ✅ Iniciando Login Server...
cd loginserver
start "L2 Hermanos - Login Server" cmd /k startLoginServer.bat
cd ..
echo.
echo ⏳ Esperando 10 segundos para que el Login Server se inicie...
timeout /t 10 /nobreak >nul

echo.
echo ===========================================
echo PASO 2: INICIANDO GAME SERVER (Puerto 7777)
echo ===========================================
echo.
echo ✅ Iniciando Game Server...
cd gameserver
start "L2 Hermanos - Game Server" cmd /k startGameServer.bat
cd ..
echo.
echo ⏳ Esperando 15 segundos para que el Game Server se inicie...
timeout /t 15 /nobreak >nul

echo.
echo ===========================================
echo VERIFICACIÓN DE SERVIDORES
echo ===========================================
echo.
echo 🔍 Verificando que los servidores estén funcionando...

netstat -an | findstr ":2106" >nul
if %errorlevel% == 0 (
    echo ✅ Login Server funcionando en puerto 2106
) else (
    echo ❌ Login Server no está funcionando
)

netstat -an | findstr ":7777" >nul
if %errorlevel% == 0 (
    echo ✅ Game Server funcionando en puerto 7777
) else (
    echo ❌ Game Server no está funcionando
)

echo.
echo ===========================================
echo L2 HERMANOS - SERVIDORES INICIADOS
echo ===========================================
echo.
echo 🎮 Para conectarte al servidor:
echo.
echo 1. Abre el cliente de L2
echo 2. Configura la IP: 127.0.0.1
echo 3. Puerto: 2106
echo 4. ¡Disfruta de L2 Hermanos!
echo.
echo 🌟 Comandos disponibles en el juego:
echo - .tutorial - Tutorial en español
echo - .titulos - Títulos épicos
echo - .pvp - PvP competitivo
echo - .creditos - Sistema de créditos
echo - .farm1 / .farm2 - Zonas de farm
echo - .pvp1 / .pvp2 - Zonas de PvP
echo.
echo 🏆 ¡¡¡ L2 HERMANOS - EL MEJOR SERVIDOR L2 DE LA HISTORIA !!!
echo.
echo Presiona cualquier tecla para continuar...
pause >nul


