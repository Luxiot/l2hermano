@echo off
echo ===========================================
echo L2 HERMANOS - RENOMBRADO DEL TUTORIAL EN ESPAÑOL
echo ===========================================
echo.
echo 📝 Renombrando tutorial en español...
echo.

REM Renombrar archivos del tutorial
if exist "gameserver\data\scripts\events\EpicTutorialSpanish.py" (
    ren "gameserver\data\scripts\events\EpicTutorialSpanish.py" "EpicTutorialSpanish_OLD.py"
    echo ✅ EpicTutorialSpanish.py - RENOMBRADO A EpicTutorialSpanish_OLD.py
) else (
    echo ❌ EpicTutorialSpanish.py - NO ENCONTRADO
)

if exist "gameserver\data\scripts\events\EpicTutorialAutoStart.py" (
    ren "gameserver\data\scripts\events\EpicTutorialAutoStart.py" "EpicTutorialAutoStart_OLD.py"
    echo ✅ EpicTutorialAutoStart.py - RENOMBRADO A EpicTutorialAutoStart_OLD.py
) else (
    echo ❌ EpicTutorialAutoStart.py - NO ENCONTRADO
)

if exist "gameserver\data\scripts\ai\npc\EpicTutorialNPC.py" (
    ren "gameserver\data\scripts\ai\npc\EpicTutorialNPC.py" "EpicTutorialNPC_OLD.py"
    echo ✅ EpicTutorialNPC.py - RENOMBRADO A EpicTutorialNPC_OLD.py
) else (
    echo ❌ EpicTutorialNPC.py - NO ENCONTRADO
)

if exist "gameserver\data\html\tutorial_spanish.htm" (
    ren "gameserver\data\html\tutorial_spanish.htm" "tutorial_spanish_OLD.htm"
    echo ✅ tutorial_spanish.htm - RENOMBRADO A tutorial_spanish_OLD.htm
) else (
    echo ❌ tutorial_spanish.htm - NO ENCONTRADO
)

if exist "gameserver\data\html\tutorial_menu.htm" (
    ren "gameserver\data\html\tutorial_menu.htm" "tutorial_menu_OLD.htm"
    echo ✅ tutorial_menu.htm - RENOMBRADO A tutorial_menu_OLD.htm
) else (
    echo ❌ tutorial_menu.htm - NO ENCONTRADO
)

if exist "gameserver\config\head\tutorial_spanish.properties" (
    ren "gameserver\config\head\tutorial_spanish.properties" "tutorial_spanish_OLD.properties"
    echo ✅ tutorial_spanish.properties - RENOMBRADO A tutorial_spanish_OLD.properties
) else (
    echo ❌ tutorial_spanish.properties - NO ENCONTRADO
)

echo.
echo ===========================================
echo RENOMBRADO COMPLETADO
echo ===========================================
echo.
echo 📝 Archivos renombrados:
echo ✅ EpicTutorialSpanish.py - RENOMBRADO A EpicTutorialSpanish_OLD.py
echo ✅ EpicTutorialAutoStart.py - RENOMBRADO A EpicTutorialAutoStart_OLD.py
echo ✅ EpicTutorialNPC.py - RENOMBRADO A EpicTutorialNPC_OLD.py
echo ✅ tutorial_spanish.htm - RENOMBRADO A tutorial_spanish_OLD.htm
echo ✅ tutorial_menu.htm - RENOMBRADO A tutorial_menu_OLD.htm
echo ✅ tutorial_spanish.properties - RENOMBRADO A tutorial_spanish_OLD.properties
echo.
echo 🌟 L2 HERMANOS - RENOMBRADO COMPLETADO
echo 💰 TUTORIAL EN ESPAÑOL + TÍTULOS ÉPICOS + PVP COMPETITIVO
echo 🏆 SISTEMA DE CRÉDITOS + EVENTOS ÉPICOS + GUILD WARS
echo 🎯 RANKING + TELEPORTER + DONACIONES + MONETIZACIÓN
echo.
echo ¡¡¡ RENOMBRADO DEL TUTORIAL EN ESPAÑOL COMPLETADO !!!
echo.
echo 📋 Información del renombrado:
echo 📅 Fecha: %date%
echo ⏰ Hora: %time%
echo 📁 Ubicación: %CD%
echo 🖥️ Sistema: %OS%
echo 👤 Usuario: %USERNAME%
echo.
echo Presiona cualquier tecla para continuar...
pause >nul



