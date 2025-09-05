@echo off
echo ===========================================
echo L2 HERMANOS - MOVIMIENTO DEL TUTORIAL EN ESPAÑOL
echo ===========================================
echo.
echo 📁 Moviendo tutorial en español...
echo.

REM Crear directorio de destino si no existe
if not exist "movimiento_tutorial_espanol" mkdir "movimiento_tutorial_espanol"

REM Crear subdirectorios
if not exist "movimiento_tutorial_espanol\scripts\events" mkdir "movimiento_tutorial_espanol\scripts\events"
if not exist "movimiento_tutorial_espanol\scripts\ai\npc" mkdir "movimiento_tutorial_espanol\scripts\ai\npc"
if not exist "movimiento_tutorial_espanol\html" mkdir "movimiento_tutorial_espanol\html"
if not exist "movimiento_tutorial_espanol\config\head" mkdir "movimiento_tutorial_espanol\config\head"

echo ✅ Directorios de destino creados
echo.

REM Mover archivos del tutorial
if exist "gameserver\data\scripts\events\EpicTutorialSpanish.py" (
    move "gameserver\data\scripts\events\EpicTutorialSpanish.py" "movimiento_tutorial_espanol\scripts\events\EpicTutorialSpanish.py"
    echo ✅ EpicTutorialSpanish.py - MOVIDO
) else (
    echo ❌ EpicTutorialSpanish.py - NO ENCONTRADO
)

if exist "gameserver\data\scripts\events\EpicTutorialAutoStart.py" (
    move "gameserver\data\scripts\events\EpicTutorialAutoStart.py" "movimiento_tutorial_espanol\scripts\events\EpicTutorialAutoStart.py"
    echo ✅ EpicTutorialAutoStart.py - MOVIDO
) else (
    echo ❌ EpicTutorialAutoStart.py - NO ENCONTRADO
)

if exist "gameserver\data\scripts\ai\npc\EpicTutorialNPC.py" (
    move "gameserver\data\scripts\ai\npc\EpicTutorialNPC.py" "movimiento_tutorial_espanol\scripts\ai\npc\EpicTutorialNPC.py"
    echo ✅ EpicTutorialNPC.py - MOVIDO
) else (
    echo ❌ EpicTutorialNPC.py - NO ENCONTRADO
)

if exist "gameserver\data\html\tutorial_spanish.htm" (
    move "gameserver\data\html\tutorial_spanish.htm" "movimiento_tutorial_espanol\html\tutorial_spanish.htm"
    echo ✅ tutorial_spanish.htm - MOVIDO
) else (
    echo ❌ tutorial_spanish.htm - NO ENCONTRADO
)

if exist "gameserver\data\html\tutorial_menu.htm" (
    move "gameserver\data\html\tutorial_menu.htm" "movimiento_tutorial_espanol\html\tutorial_menu.htm"
    echo ✅ tutorial_menu.htm - MOVIDO
) else (
    echo ❌ tutorial_menu.htm - NO ENCONTRADO
)

if exist "gameserver\config\head\tutorial_spanish.properties" (
    move "gameserver\config\head\tutorial_spanish.properties" "movimiento_tutorial_espanol\config\head\tutorial_spanish.properties"
    echo ✅ tutorial_spanish.properties - MOVIDO
) else (
    echo ❌ tutorial_spanish.properties - NO ENCONTRADO
)

echo.
echo ===========================================
echo MOVIMIENTO COMPLETADO
echo ===========================================
echo.
echo 📁 Archivos movidos a: movimiento_tutorial_espanol\
echo.
echo 📁 Archivos movidos:
echo ✅ EpicTutorialSpanish.py
echo ✅ EpicTutorialAutoStart.py
echo ✅ EpicTutorialNPC.py
echo ✅ tutorial_spanish.htm
echo ✅ tutorial_menu.htm
echo ✅ tutorial_spanish.properties
echo.
echo 🌟 L2 HERMANOS - MOVIMIENTO COMPLETADO
echo 💰 TUTORIAL EN ESPAÑOL + TÍTULOS ÉPICOS + PVP COMPETITIVO
echo 🏆 SISTEMA DE CRÉDITOS + EVENTOS ÉPICOS + GUILD WARS
echo 🎯 RANKING + TELEPORTER + DONACIONES + MONETIZACIÓN
echo.
echo ¡¡¡ MOVIMIENTO DEL TUTORIAL EN ESPAÑOL COMPLETADO !!!
echo.
echo 📋 Información del movimiento:
echo 📅 Fecha: %date%
echo ⏰ Hora: %time%
echo 📁 Ubicación: %CD%\movimiento_tutorial_espanol\
echo 🖥️ Sistema: %OS%
echo 👤 Usuario: %USERNAME%
echo.
echo Presiona cualquier tecla para continuar...
pause >nul



