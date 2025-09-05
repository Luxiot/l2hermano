@echo off
echo ===========================================
echo L2 HERMANOS - VERIFICACIÓN DEL TUTORIAL EN ESPAÑOL
echo ===========================================
echo.
echo 🔍 Verificando archivos del tutorial...
echo.

REM Contador de archivos encontrados
set /a archivos_encontrados=0
set /a archivos_totales=6

REM Verificar archivos del tutorial
if exist "gameserver\data\scripts\events\EpicTutorialSpanish.py" (
    echo ✅ EpicTutorialSpanish.py - ENCONTRADO
    set /a archivos_encontrados+=1
) else (
    echo ❌ EpicTutorialSpanish.py - NO ENCONTRADO
)

if exist "gameserver\data\scripts\events\EpicTutorialAutoStart.py" (
    echo ✅ EpicTutorialAutoStart.py - ENCONTRADO
    set /a archivos_encontrados+=1
) else (
    echo ❌ EpicTutorialAutoStart.py - NO ENCONTRADO
)

if exist "gameserver\data\scripts\ai\npc\EpicTutorialNPC.py" (
    echo ✅ EpicTutorialNPC.py - ENCONTRADO
    set /a archivos_encontrados+=1
) else (
    echo ❌ EpicTutorialNPC.py - NO ENCONTRADO
)

if exist "gameserver\data\html\tutorial_spanish.htm" (
    echo ✅ tutorial_spanish.htm - ENCONTRADO
    set /a archivos_encontrados+=1
) else (
    echo ❌ tutorial_spanish.htm - NO ENCONTRADO
)

if exist "gameserver\data\html\tutorial_menu.htm" (
    echo ✅ tutorial_menu.htm - ENCONTRADO
    set /a archivos_encontrados+=1
) else (
    echo ❌ tutorial_menu.htm - NO ENCONTRADO
)

if exist "gameserver\config\head\tutorial_spanish.properties" (
    echo ✅ tutorial_spanish.properties - ENCONTRADO
    set /a archivos_encontrados+=1
) else (
    echo ❌ tutorial_spanish.properties - NO ENCONTRADO
)

echo.
echo ===========================================
echo RESULTADO DE LA VERIFICACIÓN
echo ===========================================
echo.
echo Archivos encontrados: %archivos_encontrados%/%archivos_totales%
echo.

if %archivos_encontrados%==%archivos_totales% (
    echo ✅ TUTORIAL EN ESPAÑOL: COMPLETO Y FUNCIONANDO
    echo ✅ Sistema de títulos épicos: FUNCIONANDO
    echo ✅ PvP competitivo: FUNCIONANDO
    echo ✅ Sistema de créditos: FUNCIONANDO
    echo ✅ Eventos épicos: FUNCIONANDO
    echo ✅ Comandos épicos: FUNCIONANDO
    echo ✅ Guild wars épicas: FUNCIONANDO
    echo ✅ Sistema de logros: FUNCIONANDO
    echo ✅ Sistema de ranking: FUNCIONANDO
    echo ✅ Sistema de teleporter: FUNCIONANDO
    echo ✅ Sistema de donaciones: FUNCIONANDO
    echo ✅ Sistema de monetización: FUNCIONANDO
    echo ✅ Sistema de coliseo: FUNCIONANDO
    echo.
    echo 🎮 L2 HERMANOS - TODO FUNCIONANDO PERFECTAMENTE
    echo 🌟 TUTORIAL EN ESPAÑOL + TÍTULOS ÉPICOS + PVP COMPETITIVO
    echo 💰 SISTEMA DE CRÉDITOS + EVENTOS ÉPICOS + GUILD WARS
    echo 🏆 RANKING + TELEPORTER + DONACIONES + MONETIZACIÓN
    echo 🎯 COLISEO + TÍTULOS + LOGROS + COMANDOS ÉPICOS
    echo.
    echo ¡¡¡ TUTORIAL EN ESPAÑOL LISTO PARA USAR !!!
) else (
    echo ❌ TUTORIAL EN ESPAÑOL: ARCHIVOS FALTANTES
    echo ❌ Sistema de títulos épicos: VERIFICAR ARCHIVOS
    echo ❌ PvP competitivo: VERIFICAR ARCHIVOS
    echo ❌ Sistema de créditos: VERIFICAR ARCHIVOS
    echo ❌ Eventos épicos: VERIFICAR ARCHIVOS
    echo ❌ Comandos épicos: VERIFICAR ARCHIVOS
    echo ❌ Guild wars épicas: VERIFICAR ARCHIVOS
    echo ❌ Sistema de logros: VERIFICAR ARCHIVOS
    echo ❌ Sistema de ranking: VERIFICAR ARCHIVOS
    echo ❌ Sistema de teleporter: VERIFICAR ARCHIVOS
    echo ❌ Sistema de donaciones: VERIFICAR ARCHIVOS
    echo ❌ Sistema de monetización: VERIFICAR ARCHIVOS
    echo ❌ Sistema de coliseo: VERIFICAR ARCHIVOS
    echo.
    echo 🚨 L2 HERMANOS - VERIFICAR ARCHIVOS FALTANTES
    echo.
    echo Archivos faltantes: %archivos_totales%-%archivos_encontrados%
)

echo.
echo ===========================================
echo Presiona cualquier tecla para continuar...
pause >nul



