@echo off
echo ===========================================
echo L2 HERMANOS - CONFIGURAR FIREWALL (ADMIN)
echo ===========================================
echo.
echo 🔧 Configurando Windows Firewall para L2 Hermanos...
echo.
echo ⚠️  IMPORTANTE: Este script debe ejecutarse como ADMINISTRADOR
echo.

echo ===========================================
echo CONFIGURANDO FIREWALL
echo ===========================================
echo.

echo 🔍 Abriendo puerto 2106 (Login Server)...
netsh advfirewall firewall add rule name="L2 Hermanos Login Server" dir=in action=allow protocol=TCP localport=2106
if %errorlevel% == 0 (
    echo ✅ Puerto 2106 abierto correctamente
) else (
    echo ❌ Error al abrir puerto 2106
)

echo.
echo 🔍 Abriendo puerto 7777 (Game Server)...
netsh advfirewall firewall add rule name="L2 Hermanos Game Server" dir=in action=allow protocol=TCP localport=7777
if %errorlevel% == 0 (
    echo ✅ Puerto 7777 abierto correctamente
) else (
    echo ❌ Error al abrir puerto 7777
)

echo.
echo 🔍 Configurando reglas de salida...
netsh advfirewall firewall add rule name="L2 Hermanos Login Server Out" dir=out action=allow protocol=TCP localport=2106
netsh advfirewall firewall add rule name="L2 Hermanos Game Server Out" dir=out action=allow protocol=TCP localport=7777

echo.
echo ===========================================
echo VERIFICACIÓN
echo ===========================================
echo.
echo 🔍 Verificando reglas del firewall...
netsh advfirewall firewall show rule name="L2 Hermanos Login Server" | findstr "Enabled"
netsh advfirewall firewall show rule name="L2 Hermanos Game Server" | findstr "Enabled"

echo.
echo ===========================================
echo CONFIGURACIÓN COMPLETADA
echo ===========================================
echo.
echo ✅ Firewall configurado correctamente
echo ✅ Puertos 2106 y 7777 abiertos
echo.
echo 🎮 Los jugadores ya pueden conectarse a:
echo - IP: 186.182.75.24
echo - Puerto: 2106
echo.
echo ⚠️  RECORDATORIO: También configura tu router
echo.
echo 🏆 ¡¡¡ L2 HERMANOS LISTO PARA LA WEB !!!
echo.
pause

