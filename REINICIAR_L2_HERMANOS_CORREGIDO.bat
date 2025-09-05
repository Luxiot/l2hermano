@echo off
echo ===========================================
echo L2 HERMANOS - REINICIAR SERVIDOR CORREGIDO
echo ===========================================
echo.
echo 🚀 Reiniciando L2 Hermanos con MySQL corregido...
echo.

echo ===========================================
echo PASO 1: DETENER SERVIDORES ACTUALES
echo ===========================================
echo.
echo 🔍 Deteniendo servidores actuales...
taskkill /f /im java.exe >nul 2>&1
echo ✅ Servidores detenidos
echo.

echo ===========================================
echo PASO 2: VERIFICAR MYSQL
echo ===========================================
echo.
echo 🔍 Verificando configuración MySQL...
"C:\Program Files\MySQL\MySQL Server 8.0\bin\mysql.exe" -u root -e "SELECT user, host, plugin FROM mysql.user WHERE user='root' AND host='localhost';" 2>nul | findstr "mysql_native_password" >nul
if %errorlevel% == 0 (
    echo ✅ MySQL configurado correctamente
) else (
    echo ❌ MySQL no está configurado correctamente
    echo 🔧 Ejecutando corrección...
    "C:\Program Files\MySQL\MySQL Server 8.0\bin\mysql.exe" -u root -e "ALTER USER 'root'@'localhost' IDENTIFIED VIA mysql_native_password;"
    "C:\Program Files\MySQL\MySQL Server 8.0\bin\mysql.exe" -u root -e "FLUSH PRIVILEGES;"
    echo ✅ MySQL corregido
)
echo.

echo ===========================================
echo PASO 3: INICIAR LOGIN SERVER
echo ===========================================
echo.
echo 🚀 Iniciando Login Server...
cd loginserver
start "L2 Hermanos - Login Server" cmd /k startLoginServer.bat
cd ..
echo ✅ Login Server iniciado
echo.
echo ⏳ Esperando 10 segundos...
timeout /t 10 /nobreak >nul

echo.
echo ===========================================
echo PASO 4: INICIAR GAME SERVER
echo ===========================================
echo.
echo 🚀 Iniciando Game Server...
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
echo L2 HERMANOS - LISTO PARA JUGAR
echo ===========================================
echo.
echo 🎮 CONEXIÓN:
echo - IP: 127.0.0.1
echo - Puerto: 2106
echo.
echo 🌟 COMANDOS ADMIN (Luxio):
echo - .admin - Panel de administración
echo - .gm - Modo GM
echo - .teleport - Teletransporte
echo - .tutorial - Tutorial en español
echo - .titulos - Títulos épicos
echo - .pvp - PvP competitivo
echo.
echo 🏆 ¡¡¡ L2 HERMANOS - EL MEJOR SERVIDOR L2 DE LA HISTORIA !!!
echo.
pause

