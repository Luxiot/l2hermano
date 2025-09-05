@echo off
echo ===========================================
echo L2 HERMANOS - RENOMBRADO FINAL DEL TUTORIAL EN ESPAÑOL
echo ===========================================
echo.
echo 📝 Renombrado final del tutorial en español...
echo.

REM Renombrar archivos del tutorial
if exist "gameserver\data\scripts\events\EpicTutorialSpanish.py" (
    ren "gameserver\data\scripts\events\EpicTutorialSpanish.py" "EpicTutorialSpanish_FINAL.py"
    echo ✅ EpicTutorialSpanish.py - RENOMBRADO A EpicTutorialSpanish_FINAL.py
) else (
    echo ❌ EpicTutorialSpanish.py - NO ENCONTRADO
)

if exist "gameserver\data\scripts\events\EpicTutorialAutoStart.py" (
    ren "gameserver\data\scripts\events\EpicTutorialAutoStart.py" "EpicTutorialAutoStart_FINAL.py"
    echo ✅ EpicTutorialAutoStart.py - RENOMBRADO A EpicTutorialAutoStart_FINAL.py
) else (
    echo ❌ EpicTutorialAutoStart.py - NO ENCONTRADO
)

if exist "gameserver\data\scripts\ai\npc\EpicTutorialNPC.py" (
    ren "gameserver\data\scripts\ai\npc\EpicTutorialNPC.py" "EpicTutorialNPC_FINAL.py"
    echo ✅ EpicTutorialNPC.py - RENOMBRADO A EpicTutorialNPC_FINAL.py
) else (
    echo ❌ EpicTutorialNPC.py - NO ENCONTRADO
)

if exist "gameserver\data\html\tutorial_spanish.htm" (
    ren "gameserver\data\html\tutorial_spanish.htm" "tutorial_spanish_FINAL.htm"
    echo ✅ tutorial_spanish.htm - RENOMBRADO A tutorial_spanish_FINAL.htm
) else (
    echo ❌ tutorial_spanish.htm - NO ENCONTRADO
)

if exist "gameserver\data\html\tutorial_menu.htm" (
    ren "gameserver\data\html\tutorial_menu.htm" "tutorial_menu_FINAL.htm"
    echo ✅ tutorial_menu.htm - RENOMBRADO A tutorial_menu_FINAL.htm
) else (
    echo ❌ tutorial_menu.htm - NO ENCONTRADO
)

if exist "gameserver\config\head\tutorial_spanish.properties" (
    ren "gameserver\config\head\tutorial_spanish.properties" "tutorial_spanish_FINAL.properties"
    echo ✅ tutorial_spanish.properties - RENOMBRADO A tutorial_spanish_FINAL.properties
) else (
    echo ❌ tutorial_spanish.properties - NO ENCONTRADO
)

echo.
echo ===========================================
echo RENOMBRADO FINAL COMPLETADO
echo ===========================================
echo.
echo 📝 Archivos renombrados:
echo ✅ EpicTutorialSpanish.py - RENOMBRADO A EpicTutorialSpanish_FINAL.py
echo ✅ EpicTutorialAutoStart.py - RENOMBRADO A EpicTutorialAutoStart_FINAL.py
echo ✅ EpicTutorialNPC.py - RENOMBRADO A EpicTutorialNPC_FINAL.py
echo ✅ tutorial_spanish.htm - RENOMBRADO A tutorial_spanish_FINAL.htm
echo ✅ tutorial_menu.htm - RENOMBRADO A tutorial_menu_FINAL.htm
echo ✅ tutorial_spanish.properties - RENOMBRADO A tutorial_spanish_FINAL.properties
echo.
echo 🌟 L2 HERMANOS - RENOMBRADO FINAL COMPLETADO
echo 💰 TUTORIAL EN ESPAÑOL + TÍTULOS ÉPICOS + PVP COMPETITIVO
echo 🏆 SISTEMA DE CRÉDITOS + EVENTOS ÉPICOS + GUILD WARS
echo 🎯 RANKING + TELEPORTER + DONACIONES + MONETIZACIÓN
echo.
echo ¡¡¡ RENOMBRADO FINAL DEL TUTORIAL EN ESPAÑOL COMPLETADO !!!
echo.
echo 📋 Información del renombrado final:
echo 📅 Fecha: %date%
echo ⏰ Hora: %time%
echo 📁 Ubicación: %CD%
echo 🖥️ Sistema: %OS%
echo 👤 Usuario: %USERNAME%
echo.
echo Presiona cualquier tecla para continuar...
pause >nul