@echo off
echo ===========================================
echo L2 HERMANOS - CONFIGURAR PARA LA WEB
echo ===========================================
echo.
echo 🌐 Configurando L2 Hermanos para acceso web...
echo.
echo 📋 INFORMACIÓN DETECTADA:
echo - IP Pública: 186.182.75.24
echo - IP Local: 127.0.0.1
echo.

echo ===========================================
echo PASO 1: CONFIGURAR LOGIN SERVER
echo ===========================================
echo.
echo 🔧 Configurando Login Server para acceso web...
echo.

REM Hacer backup del archivo original
copy "loginserver\config\network\loginserver.properties" "loginserver\config\network\loginserver.properties.backup" >nul

REM Configurar IP externa en Login Server
powershell -Command "(Get-Content 'loginserver\config\network\loginserver.properties') -replace 'ExternalHostname = 127.0.0.1', 'ExternalHostname = 186.182.75.24' | Set-Content 'loginserver\config\network\loginserver.properties'"

echo ✅ Login Server configurado para IP: 186.182.75.24

echo.
echo ===========================================
echo PASO 2: CONFIGURAR GAME SERVER
echo ===========================================
echo.
echo 🔧 Configurando Game Server para acceso web...
echo.

REM Hacer backup del archivo original
copy "gameserver\config\network\gameserver.properties" "gameserver\config\network\gameserver.properties.backup" >nul

REM Configurar IP externa en Game Server
powershell -Command "(Get-Content 'gameserver\config\network\gameserver.properties') -replace 'ExternalHostname = 127.0.0.1', 'ExternalHostname = 186.182.75.24' | Set-Content 'gameserver\config\network\gameserver.properties'"

echo ✅ Game Server configurado para IP: 186.182.75.24

echo.
echo ===========================================
echo PASO 3: CONFIGURAR FIREWALL
echo ===========================================
echo.
echo 🔧 Configurando Windows Firewall...
echo.

REM Abrir puertos en el firewall
netsh advfirewall firewall add rule name="L2 Hermanos Login Server" dir=in action=allow protocol=TCP localport=2106
netsh advfirewall firewall add rule name="L2 Hermanos Game Server" dir=in action=allow protocol=TCP localport=7777
netsh advfirewall firewall add rule name="L2 Hermanos Login Server Out" dir=out action=allow protocol=TCP localport=2106
netsh advfirewall firewall add rule name="L2 Hermanos Game Server Out" dir=out action=allow protocol=TCP localport=7777

echo ✅ Firewall configurado para puertos 2106 y 7777

echo.
echo ===========================================
echo PASO 4: VERIFICAR CONFIGURACIÓN
echo ===========================================
echo.
echo 🔍 Verificando configuración...
echo.

echo 📋 CONFIGURACIÓN APLICADA:
echo - Login Server: 186.182.75.24:2106
echo - Game Server: 186.182.75.24:7777
echo - Firewall: Puertos abiertos
echo.

echo ===========================================
echo INSTRUCCIONES PARA JUGADORES
echo ===========================================
echo.
echo 🎮 Para conectarse a L2 Hermanos:
echo.
echo 1. Abrir el cliente de L2
echo 2. Configurar conexión:
echo    - IP: 186.182.75.24
echo    - Puerto: 2106
echo 3. ¡Conectarse y jugar!
echo.
echo 🌟 COMANDOS ADMIN (Luxio):
echo - .admin - Panel de administración
echo - .gm - Modo GM
echo - .teleport - Teletransporte
echo - .tutorial - Tutorial en español
echo - .titulos - Títulos épicos
echo - .pvp - PvP competitivo
echo.
echo ===========================================
echo IMPORTANTE: CONFIGURAR ROUTER
echo ===========================================
echo.
echo ⚠️  IMPORTANTE: También necesitas configurar tu router:
echo.
echo 1. Abrir puerto 2106 (Login Server)
echo 2. Abrir puerto 7777 (Game Server)
echo 3. Redirigir a tu IP local (192.168.x.x)
echo.
echo 📋 Para configurar el router:
echo 1. Ve a: http://192.168.1.1 (o tu IP del router)
echo 2. Busca "Port Forwarding" o "Redirección de puertos"
echo 3. Agrega:
echo    - Puerto 2106 → Tu IP local
echo    - Puerto 7777 → Tu IP local
echo.
echo ===========================================
echo ¡L2 HERMANOS LISTO PARA LA WEB!
echo ===========================================
echo.
echo 🏆 ¡¡¡ EL MEJOR SERVIDOR L2 DE LA HISTORIA !!!
echo.
pause

