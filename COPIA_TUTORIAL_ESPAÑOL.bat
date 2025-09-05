@echo off
echo ===========================================
echo L2 HERMANOS - COPIA DEL TUTORIAL EN ESPAÑOL
echo ===========================================
echo.
echo 📋 Copiando tutorial en español...
echo.

REM Crear directorio de copia si no existe
if not exist "copia_tutorial_espanol" mkdir "copia_tutorial_espanol"

REM Crear subdirectorios
if not exist "copia_tutorial_espanol\scripts\events" mkdir "copia_tutorial_espanol\scripts\events"
if not exist "copia_tutorial_espanol\scripts\ai\npc" mkdir "copia_tutorial_espanol\scripts\ai\npc"
if not exist "copia_tutorial_espanol\html" mkdir "copia_tutorial_espanol\html"
if not exist "copia_tutorial_espanol\config\head" mkdir "copia_tutorial_espanol\config\head"

echo ✅ Directorios de copia creados
echo.

REM Copiar archivos del tutorial
if exist "gameserver\data\scripts\events\EpicTutorialSpanish.py" (
    copy "gameserver\data\scripts\events\EpicTutorialSpanish.py" "copia_tutorial_espanol\scripts\events\EpicTutorialSpanish.py"
    echo ✅ EpicTutorialSpanish.py - COPIADO
) else (
    echo ❌ EpicTutorialSpanish.py - NO ENCONTRADO
)

if exist "gameserver\data\scripts\events\EpicTutorialAutoStart.py" (
    copy "gameserver\data\scripts\events\EpicTutorialAutoStart.py" "copia_tutorial_espanol\scripts\events\EpicTutorialAutoStart.py"
    echo ✅ EpicTutorialAutoStart.py - COPIADO
) else (
    echo ❌ EpicTutorialAutoStart.py - NO ENCONTRADO
)

if exist "gameserver\data\scripts\ai\npc\EpicTutorialNPC.py" (
    copy "gameserver\data\scripts\ai\npc\EpicTutorialNPC.py" "copia_tutorial_espanol\scripts\ai\npc\EpicTutorialNPC.py"
    echo ✅ EpicTutorialNPC.py - COPIADO
) else (
    echo ❌ EpicTutorialNPC.py - NO ENCONTRADO
)

if exist "gameserver\data\html\tutorial_spanish.htm" (
    copy "gameserver\data\html\tutorial_spanish.htm" "copia_tutorial_espanol\html\tutorial_spanish.htm"
    echo ✅ tutorial_spanish.htm - COPIADO
) else (
    echo ❌ tutorial_spanish.htm - NO ENCONTRADO
)

if exist "gameserver\data\html\tutorial_menu.htm" (
    copy "gameserver\data\html\tutorial_menu.htm" "copia_tutorial_espanol\html\tutorial_menu.htm"
    echo ✅ tutorial_menu.htm - COPIADO
) else (
    echo ❌ tutorial_menu.htm - NO ENCONTRADO
)

if exist "gameserver\config\head\tutorial_spanish.properties" (
    copy "gameserver\config\head\tutorial_spanish.properties" "copia_tutorial_espanol\config\head\tutorial_spanish.properties"
    echo ✅ tutorial_spanish.properties - COPIADO
) else (
    echo ❌ tutorial_spanish.properties - NO ENCONTRADO
)

echo.
echo ===========================================
echo COPIA COMPLETADA
echo ===========================================
echo.
echo 📋 Copia creada en: copia_tutorial_espanol\
echo.
echo 📁 Archivos copiados:
echo ✅ EpicTutorialSpanish.py
echo ✅ EpicTutorialAutoStart.py
echo ✅ EpicTutorialNPC.py
echo ✅ tutorial_spanish.htm
echo ✅ tutorial_menu.htm
echo ✅ tutorial_spanish.properties
echo.
echo 🌟 L2 HERMANOS - COPIA COMPLETADA
echo 💰 TUTORIAL EN ESPAÑOL + TÍTULOS ÉPICOS + PVP COMPETITIVO
echo 🏆 SISTEMA DE CRÉDITOS + EVENTOS ÉPICOS + GUILD WARS
echo 🎯 RANKING + TELEPORTER + DONACIONES + MONETIZACIÓN
echo.
echo ¡¡¡ COPIA DEL TUTORIAL EN ESPAÑOL COMPLETADA !!!
echo.
echo 📋 Información de la copia:
echo 📅 Fecha: %date%
echo ⏰ Hora: %time%
echo 📁 Ubicación: %CD%\copia_tutorial_espanol\
echo 🖥️ Sistema: %OS%
echo 👤 Usuario: %USERNAME%
echo.
echo Presiona cualquier tecla para continuar...
pause >nul



