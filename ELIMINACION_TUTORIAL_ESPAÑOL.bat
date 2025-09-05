@echo off
echo ===========================================
echo L2 HERMANOS - ELIMINACIÓN DEL TUTORIAL EN ESPAÑOL
echo ===========================================
echo.
echo 🗑️ Eliminando tutorial en español...
echo.

REM Eliminar archivos del tutorial
if exist "gameserver\data\scripts\events\EpicTutorialSpanish.py" (
    del "gameserver\data\scripts\events\EpicTutorialSpanish.py"
    echo ✅ EpicTutorialSpanish.py - ELIMINADO
) else (
    echo ❌ EpicTutorialSpanish.py - NO ENCONTRADO
)

if exist "gameserver\data\scripts\events\EpicTutorialAutoStart.py" (
    del "gameserver\data\scripts\events\EpicTutorialAutoStart.py"
    echo ✅ EpicTutorialAutoStart.py - ELIMINADO
) else (
    echo ❌ EpicTutorialAutoStart.py - NO ENCONTRADO
)

if exist "gameserver\data\scripts\ai\npc\EpicTutorialNPC.py" (
    del "gameserver\data\scripts\ai\npc\EpicTutorialNPC.py"
    echo ✅ EpicTutorialNPC.py - ELIMINADO
) else (
    echo ❌ EpicTutorialNPC.py - NO ENCONTRADO
)

if exist "gameserver\data\html\tutorial_spanish.htm" (
    del "gameserver\data\html\tutorial_spanish.htm"
    echo ✅ tutorial_spanish.htm - ELIMINADO
) else (
    echo ❌ tutorial_spanish.htm - NO ENCONTRADO
)

if exist "gameserver\data\html\tutorial_menu.htm" (
    del "gameserver\data\html\tutorial_menu.htm"
    echo ✅ tutorial_menu.htm - ELIMINADO
) else (
    echo ❌ tutorial_menu.htm - NO ENCONTRADO
)

if exist "gameserver\config\head\tutorial_spanish.properties" (
    del "gameserver\config\head\tutorial_spanish.properties"
    echo ✅ tutorial_spanish.properties - ELIMINADO
) else (
    echo ❌ tutorial_spanish.properties - NO ENCONTRADO
)

echo.
echo ===========================================
echo ELIMINACIÓN COMPLETADA
echo ===========================================
echo.
echo 🗑️ Archivos eliminados:
echo ✅ EpicTutorialSpanish.py - ELIMINADO
echo ✅ EpicTutorialAutoStart.py - ELIMINADO
echo ✅ EpicTutorialNPC.py - ELIMINADO
echo ✅ tutorial_spanish.htm - ELIMINADO
echo ✅ tutorial_menu.htm - ELIMINADO
echo ✅ tutorial_spanish.properties - ELIMINADO
echo.
echo 🌟 L2 HERMANOS - ELIMINACIÓN COMPLETADA
echo 💰 TUTORIAL EN ESPAÑOL + TÍTULOS ÉPICOS + PVP COMPETITIVO
echo 🏆 SISTEMA DE CRÉDITOS + EVENTOS ÉPICOS + GUILD WARS
echo 🎯 RANKING + TELEPORTER + DONACIONES + MONETIZACIÓN
echo.
echo ¡¡¡ ELIMINACIÓN DEL TUTORIAL EN ESPAÑOL COMPLETADA !!!
echo.
echo 📋 Información de la eliminación:
echo 📅 Fecha: %date%
echo ⏰ Hora: %time%
echo 📁 Ubicación: %CD%
echo 🖥️ Sistema: %OS%
echo 👤 Usuario: %USERNAME%
echo.
echo Presiona cualquier tecla para continuar...
pause >nul



