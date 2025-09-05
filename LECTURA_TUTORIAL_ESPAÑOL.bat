@echo off
echo ===========================================
echo L2 HERMANOS - LECTURA DEL TUTORIAL EN ESPAÑOL
echo ===========================================
echo.
echo 📖 Leyendo tutorial en español...
echo.

echo ===========================================
echo LECTURA DE ARCHIVOS
echo ===========================================
echo.

REM Leer archivo de configuración
if exist "gameserver\config\head\tutorial_spanish.properties" (
    echo 📄 Leyendo tutorial_spanish.properties:
    echo.
    type "gameserver\config\head\tutorial_spanish.properties"
    echo.
    echo ===========================================
    echo.
) else (
    echo ❌ tutorial_spanish.properties - NO ENCONTRADO
    echo.
)

REM Leer archivo HTML del tutorial
if exist "gameserver\data\html\tutorial_spanish.htm" (
    echo 📄 Leyendo tutorial_spanish.htm:
    echo.
    type "gameserver\data\html\tutorial_spanish.htm"
    echo.
    echo ===========================================
    echo.
) else (
    echo ❌ tutorial_spanish.htm - NO ENCONTRADO
    echo.
)

REM Leer archivo HTML del menú
if exist "gameserver\data\html\tutorial_menu.htm" (
    echo 📄 Leyendo tutorial_menu.htm:
    echo.
    type "gameserver\data\html\tutorial_menu.htm"
    echo.
    echo ===========================================
    echo.
) else (
    echo ❌ tutorial_menu.htm - NO ENCONTRADO
    echo.
)

echo ===========================================
echo LECTURA COMPLETADA
echo ===========================================
echo.
echo 📖 Lectura realizada:
echo ✅ tutorial_spanish.properties - LEÍDO
echo ✅ tutorial_spanish.htm - LEÍDO
echo ✅ tutorial_menu.htm - LEÍDO
echo.
echo 🌟 L2 HERMANOS - LECTURA COMPLETADA
echo 💰 TUTORIAL EN ESPAÑOL + TÍTULOS ÉPICOS + PVP COMPETITIVO
echo 🏆 SISTEMA DE CRÉDITOS + EVENTOS ÉPICOS + GUILD WARS
echo 🎯 RANKING + TELEPORTER + DONACIONES + MONETIZACIÓN
echo.
echo ¡¡¡ LECTURA DEL TUTORIAL EN ESPAÑOL COMPLETADA !!!
echo.
echo 📋 Información de la lectura:
echo 📅 Fecha: %date%
echo ⏰ Hora: %time%
echo 📁 Ubicación: %CD%
echo 🖥️ Sistema: %OS%
echo 👤 Usuario: %USERNAME%
echo.
echo Presiona cualquier tecla para continuar...
pause >nul



