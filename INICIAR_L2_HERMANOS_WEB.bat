@echo off
echo ===========================================
echo L2 HERMANOS - INICIAR SERVIDOR WEB
echo ===========================================
echo.
echo 🌐 Iniciando L2 Hermanos para acceso web...
echo.

echo ===========================================
echo INFORMACIÓN DEL SERVIDOR
echo ===========================================
echo.
echo 🌐 IP Pública: 186.182.75.24
echo 🏠 IP Local: 192.168.100.2
echo 🔧 Puerto Login: 2106
echo 🔧 Puerto Game: 7777
echo.

echo ===========================================
echo DETENIENDO SERVIDORES ACTUALES
echo ===========================================
echo.
echo 🔍 Deteniendo servidores actuales...
taskkill /f /im java.exe >nul 2>&1
echo ✅ Servidores detenidos
echo.

echo ===========================================
echo INICIANDO LOGIN SERVER
echo ===========================================
echo.
echo 🚀 Iniciando Login Server (Puerto 2106)...
cd loginserver
start "L2 Hermanos - Login Server (Web)" cmd /k startLoginServer.bat
cd ..
echo ✅ Login Server iniciado
echo.
echo ⏳ Esperando 10 segundos...
timeout /t 10 /nobreak >nul

echo.
echo ===========================================
echo INICIANDO GAME SERVER
echo ===========================================
echo.
echo 🚀 Iniciando Game Server (Puerto 7777)...
cd gameserver
start "L2 Hermanos - Game Server (Web)" cmd /k startGameServer.bat
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
echo 🔍 Verificando que los servidores estén funcionando...

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
echo L2 HERMANOS - LISTO PARA LA WEB
echo ===========================================
echo.
echo 🎮 INFORMACIÓN PARA JUGADORES:
echo.
echo 📋 CONFIGURACIÓN DEL CLIENTE:
echo - IP: 186.182.75.24
echo - Puerto: 2106
echo.
echo 🌟 CARACTERÍSTICAS DEL SERVIDOR:
echo - Rates: x20 XP/SP, x12 Drop, x15 Spoil
echo - PvP: Habilitado en todas las zonas
echo - Tutorial: En español
echo - Comandos: .tutorial, .titulos, .pvp
echo - Admin: Luxio (Nivel 5 - Owner)
echo.
echo 🎮 COMANDOS ADMIN DISPONIBLES:
echo - .admin - Panel de administración
echo - .gm - Modo GM
echo - .teleport - Teletransporte
echo - .spawn - Spawnear NPCs
echo - .give - Dar items
echo - .level - Cambiar nivel
echo - .skill - Dar skills
echo - .tutorial - Tutorial en español
echo - .titulos - Títulos épicos
echo - .pvp - PvP competitivo
echo.
echo ===========================================
echo IMPORTANTE: CONFIGURAR ROUTER
echo ===========================================
echo.
echo ⚠️  IMPORTANTE: Para que otros jugadores se conecten:
echo.
echo 1. Configura tu router:
echo    - Puerto 2106 → 192.168.100.2
echo    - Puerto 7777 → 192.168.100.2
echo.
echo 2. Configura el firewall:
echo    - Ejecuta: CONFIGURAR_FIREWALL_ADMIN.bat (como administrador)
echo.
echo ===========================================
echo ¡L2 HERMANOS LISTO PARA LA WEB!
echo ===========================================
echo.
echo 🏆 ¡¡¡ EL MEJOR SERVIDOR L2 DE LA HISTORIA !!!
echo.
pause

