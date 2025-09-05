@echo off
echo ===========================================
echo L2 HERMANOS - CONFIGURAR ROUTER
echo ===========================================
echo.
echo 🌐 Obteniendo información de red para configurar el router...
echo.

echo ===========================================
echo INFORMACIÓN DE RED
echo ===========================================
echo.

echo 🔍 Obteniendo IP local...
for /f "tokens=2 delims=:" %%a in ('ipconfig ^| findstr /i "IPv4"') do (
    for /f "tokens=1" %%b in ("%%a") do (
        echo ✅ IP Local: %%b
        set LOCAL_IP=%%b
    )
)

echo.
echo 🔍 Obteniendo IP del router...
for /f "tokens=2 delims=:" %%a in ('ipconfig ^| findstr /i "Gateway"') do (
    for /f "tokens=1" %%b in ("%%a") do (
        echo ✅ IP del Router: %%b
        set ROUTER_IP=%%b
    )
)

echo.
echo ===========================================
echo CONFIGURACIÓN DEL ROUTER
echo ===========================================
echo.
echo 📋 INFORMACIÓN PARA CONFIGURAR EL ROUTER:
echo.
echo 🌐 IP Pública: 186.182.75.24
echo 🏠 IP Local: %LOCAL_IP%
echo 🔧 IP del Router: %ROUTER_IP%
echo.
echo ===========================================
echo PASOS PARA CONFIGURAR EL ROUTER
echo ===========================================
echo.
echo 1️⃣ ABRIR CONFIGURACIÓN DEL ROUTER:
echo    - Ve a: http://%ROUTER_IP%
echo    - Usuario: admin (o el que tengas configurado)
echo    - Contraseña: (la que tengas configurada)
echo.
echo 2️⃣ BUSCAR PORT FORWARDING:
echo    - Busca "Port Forwarding" o "Redirección de puertos"
echo    - O "Virtual Server" o "Servidor Virtual"
echo.
echo 3️⃣ AGREGAR REGLAS:
echo    - Puerto 2106 → %LOCAL_IP% (Login Server)
echo    - Puerto 7777 → %LOCAL_IP% (Game Server)
echo.
echo 4️⃣ GUARDAR CONFIGURACIÓN:
echo    - Guarda los cambios
echo    - Reinicia el router si es necesario
echo.
echo ===========================================
echo VERIFICACIÓN
echo ===========================================
echo.
echo 🔍 Para verificar que funciona:
echo.
echo 1. Reinicia el servidor L2 Hermanos
echo 2. Pide a un amigo que se conecte con:
echo    - IP: 186.182.75.24
echo    - Puerto: 2106
echo.
echo ===========================================
echo INFORMACIÓN PARA JUGADORES
echo ===========================================
echo.
echo 🎮 Para conectarse a L2 Hermanos:
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
echo - Admin: Luxio (Nivel 5)
echo.
echo ===========================================
echo ¡L2 HERMANOS LISTO PARA LA WEB!
echo ===========================================
echo.
echo 🏆 ¡¡¡ EL MEJOR SERVIDOR L2 DE LA HISTORIA !!!
echo.
pause

