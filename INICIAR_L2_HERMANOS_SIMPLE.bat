@echo off
echo ===========================================
echo L2 HERMANOS - INICIAR SERVIDORES
echo ===========================================
echo.
echo 🚀 ORDEN CORRECTO DE INICIO:
echo.
echo 1️⃣ PRIMERO: Login Server (Puerto 2106)
echo 2️⃣ SEGUNDO: Game Server (Puerto 7777)
echo.
echo Presiona cualquier tecla para iniciar...
pause >nul

echo.
echo ===========================================
echo INICIANDO LOGIN SERVER...
echo ===========================================
cd loginserver
start "L2 Hermanos - Login Server" cmd /k startLoginServer.bat
cd ..
echo ✅ Login Server iniciado
echo.
echo ⏳ Esperando 10 segundos...
timeout /t 10 /nobreak >nul

echo.
echo ===========================================
echo INICIANDO GAME SERVER...
echo ===========================================
cd gameserver
start "L2 Hermanos - Game Server" cmd /k startGameServer.bat
cd ..
echo ✅ Game Server iniciado
echo.
echo ⏳ Esperando 15 segundos...
timeout /t 15 /nobreak >nul

echo.
echo ===========================================
echo VERIFICACIÓN FINAL
echo ===========================================
echo.
netstat -an | findstr ":2106" >nul
if %errorlevel% == 0 (
    echo ✅ Login Server: FUNCIONANDO (Puerto 2106)
) else (
    echo ❌ Login Server: NO FUNCIONA
)

netstat -an | findstr ":7777" >nul
if %errorlevel% == 0 (
    echo ✅ Game Server: FUNCIONANDO (Puerto 7777)
) else (
    echo ❌ Game Server: NO FUNCIONA
)

echo.
echo ===========================================
echo L2 HERMANOS - LISTO PARA JUGAR
echo ===========================================
echo.
echo 🎮 CONEXIÓN:
echo - IP: 127.0.0.1
echo - Puerto: 2106
echo.
echo 🌟 COMANDOS EN EL JUEGO:
echo - .tutorial - Tutorial en español
echo - .titulos - Títulos épicos
echo - .pvp - PvP competitivo
echo.
echo 🏆 ¡¡¡ L2 HERMANOS - EL MEJOR SERVIDOR L2 DE LA HISTORIA !!!
echo.
pause


