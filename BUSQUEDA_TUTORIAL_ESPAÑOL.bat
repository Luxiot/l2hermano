@echo off
echo ===========================================
echo L2 HERMANOS - BÚSQUEDA DEL TUTORIAL EN ESPAÑOL
echo ===========================================
echo.
echo 🔍 Buscando tutorial en español...
echo.

echo ===========================================
echo BÚSQUEDA DE ARCHIVOS
echo ===========================================
echo.

REM Buscar archivos del tutorial
if exist "gameserver\data\scripts\events\EpicTutorialSpanish.py" (
    echo ✅ EpicTutorialSpanish.py - ENCONTRADO
    echo    Ubicación: gameserver\data\scripts\events\EpicTutorialSpanish.py
    echo    Tamaño: 
    for %%A in ("gameserver\data\scripts\events\EpicTutorialSpanish.py") do echo %%~zA bytes
    echo    Fecha de modificación: %%~tA
) else (
    echo ❌ EpicTutorialSpanish.py - NO ENCONTRADO
)

if exist "gameserver\data\scripts\events\EpicTutorialAutoStart.py" (
    echo ✅ EpicTutorialAutoStart.py - ENCONTRADO
    echo    Ubicación: gameserver\data\scripts\events\EpicTutorialAutoStart.py
    echo    Tamaño: 
    for %%A in ("gameserver\data\scripts\events\EpicTutorialAutoStart.py") do echo %%~zA bytes
    echo    Fecha de modificación: %%~tA
) else (
    echo ❌ EpicTutorialAutoStart.py - NO ENCONTRADO
)

if exist "gameserver\data\scripts\ai\npc\EpicTutorialNPC.py" (
    echo ✅ EpicTutorialNPC.py - ENCONTRADO
    echo    Ubicación: gameserver\data\scripts\ai\npc\EpicTutorialNPC.py
    echo    Tamaño: 
    for %%A in ("gameserver\data\scripts\ai\npc\EpicTutorialNPC.py") do echo %%~zA bytes
    echo    Fecha de modificación: %%~tA
) else (
    echo ❌ EpicTutorialNPC.py - NO ENCONTRADO
)

if exist "gameserver\data\html\tutorial_spanish.htm" (
    echo ✅ tutorial_spanish.htm - ENCONTRADO
    echo    Ubicación: gameserver\data\html\tutorial_spanish.htm
    echo    Tamaño: 
    for %%A in ("gameserver\data\html\tutorial_spanish.htm") do echo %%~zA bytes
    echo    Fecha de modificación: %%~tA
) else (
    echo ❌ tutorial_spanish.htm - NO ENCONTRADO
)

if exist "gameserver\data\html\tutorial_menu.htm" (
    echo ✅ tutorial_menu.htm - ENCONTRADO
    echo    Ubicación: gameserver\data\html\tutorial_menu.htm
    echo    Tamaño: 
    for %%A in ("gameserver\data\html\tutorial_menu.htm") do echo %%~zA bytes
    echo    Fecha de modificación: %%~tA
) else (
    echo ❌ tutorial_menu.htm - NO ENCONTRADO
)

if exist "gameserver\config\head\tutorial_spanish.properties" (
    echo ✅ tutorial_spanish.properties - ENCONTRADO
    echo    Ubicación: gameserver\config\head\tutorial_spanish.properties
    echo    Tamaño: 
    for %%A in ("gameserver\config\head\tutorial_spanish.properties") do echo %%~zA bytes
    echo    Fecha de modificación: %%~tA
) else (
    echo ❌ tutorial_spanish.properties - NO ENCONTRADO
)

echo.
echo ===========================================
echo BÚSQUEDA COMPLETADA
echo ===========================================
echo.
echo 🔍 Búsqueda realizada:
echo ✅ Archivos del tutorial buscados
echo ✅ Ubicaciones verificadas
echo ✅ Tamaños verificados
echo ✅ Fechas de modificación verificadas
echo.
echo 🌟 L2 HERMANOS - BÚSQUEDA COMPLETADA
echo 💰 TUTORIAL EN ESPAÑOL + TÍTULOS ÉPICOS + PVP COMPETITIVO
echo 🏆 SISTEMA DE CRÉDITOS + EVENTOS ÉPICOS + GUILD WARS
echo 🎯 RANKING + TELEPORTER + DONACIONES + MONETIZACIÓN
echo.
echo ¡¡¡ BÚSQUEDA DEL TUTORIAL EN ESPAÑOL COMPLETADA !!!
echo.
echo 📋 Información de la búsqueda:
echo 📅 Fecha: %date%
echo ⏰ Hora: %time%
echo 📁 Ubicación: %CD%
echo 🖥️ Sistema: %OS%
echo 👤 Usuario: %USERNAME%
echo.
echo Presiona cualquier tecla para continuar...
pause >nul



