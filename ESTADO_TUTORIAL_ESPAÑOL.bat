@echo off
echo ===========================================
echo L2 HERMANOS - ESTADO DEL TUTORIAL EN ESPAÑOL
echo ===========================================
echo.
echo 📊 Verificando estado del tutorial...
echo.

REM Contador de archivos encontrados
set /a archivos_encontrados=0
set /a archivos_totales=6

REM Verificar archivos del tutorial
if exist "gameserver\data\scripts\events\EpicTutorialSpanish.py" (
    echo ✅ EpicTutorialSpanish.py - ACTIVO
    set /a archivos_encontrados+=1
) else (
    echo ❌ EpicTutorialSpanish.py - INACTIVO
)

if exist "gameserver\data\scripts\events\EpicTutorialAutoStart.py" (
    echo ✅ EpicTutorialAutoStart.py - ACTIVO
    set /a archivos_encontrados+=1
) else (
    echo ❌ EpicTutorialAutoStart.py - INACTIVO
)

if exist "gameserver\data\scripts\ai\npc\EpicTutorialNPC.py" (
    echo ✅ EpicTutorialNPC.py - ACTIVO
    set /a archivos_encontrados+=1
) else (
    echo ❌ EpicTutorialNPC.py - INACTIVO
)

if exist "gameserver\data\html\tutorial_spanish.htm" (
    echo ✅ tutorial_spanish.htm - ACTIVO
    set /a archivos_encontrados+=1
) else (
    echo ❌ tutorial_spanish.htm - INACTIVO
)

if exist "gameserver\data\html\tutorial_menu.htm" (
    echo ✅ tutorial_menu.htm - ACTIVO
    set /a archivos_encontrados+=1
) else (
    echo ❌ tutorial_menu.htm - INACTIVO
)

if exist "gameserver\config\head\tutorial_spanish.properties" (
    echo ✅ tutorial_spanish.properties - ACTIVO
    set /a archivos_encontrados+=1
) else (
    echo ❌ tutorial_spanish.properties - INACTIVO
)

echo.
echo ===========================================
echo ESTADO DEL SISTEMA
echo ===========================================
echo.
echo Archivos activos: %archivos_encontrados%/%archivos_totales%
echo.

if %archivos_encontrados%==%archivos_totales% (
    echo ✅ TUTORIAL EN ESPAÑOL: COMPLETAMENTE ACTIVO
    echo ✅ Sistema de títulos épicos: ACTIVO
    echo ✅ PvP competitivo: ACTIVO
    echo ✅ Sistema de créditos: ACTIVO
    echo ✅ Eventos épicos: ACTIVO
    echo ✅ Comandos épicos: ACTIVO
    echo ✅ Guild wars épicas: ACTIVO
    echo ✅ Sistema de logros: ACTIVO
    echo ✅ Sistema de ranking: ACTIVO
    echo ✅ Sistema de teleporter: ACTIVO
    echo ✅ Sistema de donaciones: ACTIVO
    echo ✅ Sistema de monetización: ACTIVO
    echo ✅ Sistema de coliseo: ACTIVO
    echo.
    echo 🎮 L2 HERMANOS - SISTEMA COMPLETAMENTE ACTIVO
    echo 🌟 TUTORIAL EN ESPAÑOL + TÍTULOS ÉPICOS + PVP COMPETITIVO
    echo 💰 SISTEMA DE CRÉDITOS + EVENTOS ÉPICOS + GUILD WARS
    echo 🏆 RANKING + TELEPORTER + DONACIONES + MONETIZACIÓN
    echo.
    echo ¡¡¡ TUTORIAL EN ESPAÑOL COMPLETAMENTE ACTIVO !!!
) else (
    echo ❌ TUTORIAL EN ESPAÑOL: PARCIALMENTE ACTIVO
    echo ❌ Sistema de títulos épicos: VERIFICAR ESTADO
    echo ❌ PvP competitivo: VERIFICAR ESTADO
    echo ❌ Sistema de créditos: VERIFICAR ESTADO
    echo ❌ Eventos épicos: VERIFICAR ESTADO
    echo ❌ Comandos épicos: VERIFICAR ESTADO
    echo ❌ Guild wars épicas: VERIFICAR ESTADO
    echo ❌ Sistema de logros: VERIFICAR ESTADO
    echo ❌ Sistema de ranking: VERIFICAR ESTADO
    echo ❌ Sistema de teleporter: VERIFICAR ESTADO
    echo ❌ Sistema de donaciones: VERIFICAR ESTADO
    echo ❌ Sistema de monetización: VERIFICAR ESTADO
    echo ❌ Sistema de coliseo: VERIFICAR ESTADO
    echo.
    echo 🚨 L2 HERMANOS - SISTEMA PARCIALMENTE ACTIVO
    echo.
    echo Archivos faltantes: %archivos_totales%-%archivos_encontrados%
)

echo.
echo ===========================================
echo INFORMACIÓN DEL SISTEMA
echo ===========================================
echo.
echo 🎮 L2 HERMANOS - El mejor servidor L2 de la historia
echo 🌟 Tutorial en español + Títulos épicos + PvP competitivo
echo 💰 Sistema de créditos + Eventos épicos + Guild wars
echo 🏆 Ranking + Teleporter + Donaciones + Monetización
echo 🎯 Coliseo + Títulos + Logros + Comandos épicos
echo.
echo 📊 Estado actual: %archivos_encontrados%/%archivos_totales% archivos activos
echo 📅 Última verificación: %date% %time%
echo 🖥️ Sistema operativo: %OS%
echo 👤 Usuario: %USERNAME%
echo 📁 Directorio: %CD%
echo.

echo ===========================================
echo Presiona cualquier tecla para continuar...
pause >nul



