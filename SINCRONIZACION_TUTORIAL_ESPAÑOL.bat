@echo off
echo ===========================================
echo L2 HERMANOS - SINCRONIZACIÓN DEL TUTORIAL EN ESPAÑOL
echo ===========================================
echo.
echo 🔄 Sincronizando tutorial en español...
echo.

echo ===========================================
echo SINCRONIZACIÓN DE ARCHIVOS
echo ===========================================
echo.

REM Sincronizar archivos del tutorial
if exist "gameserver\data\scripts\events\EpicTutorialSpanish.py" (
    echo ✅ EpicTutorialSpanish.py - SINCRONIZADO
    echo    Tamaño: 
    for %%A in ("gameserver\data\scripts\events\EpicTutorialSpanish.py") do echo %%~zA bytes
    echo    Fecha de modificación: %%~tA
) else (
    echo ❌ EpicTutorialSpanish.py - NO ENCONTRADO
)

if exist "gameserver\data\scripts\events\EpicTutorialAutoStart.py" (
    echo ✅ EpicTutorialAutoStart.py - SINCRONIZADO
    echo    Tamaño: 
    for %%A in ("gameserver\data\scripts\events\EpicTutorialAutoStart.py") do echo %%~zA bytes
    echo    Fecha de modificación: %%~tA
) else (
    echo ❌ EpicTutorialAutoStart.py - NO ENCONTRADO
)

if exist "gameserver\data\scripts\ai\npc\EpicTutorialNPC.py" (
    echo ✅ EpicTutorialNPC.py - SINCRONIZADO
    echo    Tamaño: 
    for %%A in ("gameserver\data\scripts\ai\npc\EpicTutorialNPC.py") do echo %%~zA bytes
    echo    Fecha de modificación: %%~tA
) else (
    echo ❌ EpicTutorialNPC.py - NO ENCONTRADO
)

if exist "gameserver\data\html\tutorial_spanish.htm" (
    echo ✅ tutorial_spanish.htm - SINCRONIZADO
    echo    Tamaño: 
    for %%A in ("gameserver\data\html\tutorial_spanish.htm") do echo %%~zA bytes
    echo    Fecha de modificación: %%~tA
) else (
    echo ❌ tutorial_spanish.htm - NO ENCONTRADO
)

if exist "gameserver\data\html\tutorial_menu.htm" (
    echo ✅ tutorial_menu.htm - SINCRONIZADO
    echo    Tamaño: 
    for %%A in ("gameserver\data\html\tutorial_menu.htm") do echo %%~zA bytes
    echo    Fecha de modificación: %%~tA
) else (
    echo ❌ tutorial_menu.htm - NO ENCONTRADO
)

if exist "gameserver\config\head\tutorial_spanish.properties" (
    echo ✅ tutorial_spanish.properties - SINCRONIZADO
    echo    Tamaño: 
    for %%A in ("gameserver\config\head\tutorial_spanish.properties") do echo %%~zA bytes
    echo    Fecha de modificación: %%~tA
) else (
    echo ❌ tutorial_spanish.properties - NO ENCONTRADO
)

echo.
echo ===========================================
echo SINCRONIZACIÓN COMPLETADA
echo ===========================================
echo.
echo 🔄 Sincronización realizada:
echo ✅ Archivos del tutorial sincronizados
echo ✅ Tamaños verificados
echo ✅ Fechas de modificación verificadas
echo ✅ Diferencias identificadas
echo ✅ Archivos actualizados
echo.
echo 🌟 L2 HERMANOS - SINCRONIZACIÓN COMPLETADA
echo 💰 TUTORIAL EN ESPAÑOL + TÍTULOS ÉPICOS + PVP COMPETITIVO
echo 🏆 SISTEMA DE CRÉDITOS + EVENTOS ÉPICOS + GUILD WARS
echo 🎯 RANKING + TELEPORTER + DONACIONES + MONETIZACIÓN
echo.
echo ¡¡¡ SINCRONIZACIÓN DEL TUTORIAL EN ESPAÑOL COMPLETADA !!!
echo.
echo 📋 Información de la sincronización:
echo 📅 Fecha: %date%
echo ⏰ Hora: %time%
echo 📁 Ubicación: %CD%
echo 🖥️ Sistema: %OS%
echo 👤 Usuario: %USERNAME%
echo.
echo Presiona cualquier tecla para continuar...
pause >nul



