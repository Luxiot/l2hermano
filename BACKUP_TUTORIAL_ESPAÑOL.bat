@echo off
echo ===========================================
echo L2 HERMANOS - BACKUP DEL TUTORIAL EN ESPAÑOL
echo ===========================================
echo.
echo 💾 Creando backup del tutorial...
echo.

REM Crear directorio de backup si no existe
if not exist "backup_tutorial_espanol" mkdir "backup_tutorial_espanol"

REM Crear subdirectorios
if not exist "backup_tutorial_espanol\scripts\events" mkdir "backup_tutorial_espanol\scripts\events"
if not exist "backup_tutorial_espanol\scripts\ai\npc" mkdir "backup_tutorial_espanol\scripts\ai\npc"
if not exist "backup_tutorial_espanol\html" mkdir "backup_tutorial_espanol\html"
if not exist "backup_tutorial_espanol\config\head" mkdir "backup_tutorial_espanol\config\head"

echo ✅ Directorios de backup creados
echo.

REM Hacer backup de los archivos
if exist "gameserver\data\scripts\events\EpicTutorialSpanish.py" (
    copy "gameserver\data\scripts\events\EpicTutorialSpanish.py" "backup_tutorial_espanol\scripts\events\EpicTutorialSpanish.py"
    echo ✅ EpicTutorialSpanish.py - BACKUP CREADO
) else (
    echo ❌ EpicTutorialSpanish.py - NO ENCONTRADO
)

if exist "gameserver\data\scripts\events\EpicTutorialAutoStart.py" (
    copy "gameserver\data\scripts\events\EpicTutorialAutoStart.py" "backup_tutorial_espanol\scripts\events\EpicTutorialAutoStart.py"
    echo ✅ EpicTutorialAutoStart.py - BACKUP CREADO
) else (
    echo ❌ EpicTutorialAutoStart.py - NO ENCONTRADO
)

if exist "gameserver\data\scripts\ai\npc\EpicTutorialNPC.py" (
    copy "gameserver\data\scripts\ai\npc\EpicTutorialNPC.py" "backup_tutorial_espanol\scripts\ai\npc\EpicTutorialNPC.py"
    echo ✅ EpicTutorialNPC.py - BACKUP CREADO
) else (
    echo ❌ EpicTutorialNPC.py - NO ENCONTRADO
)

if exist "gameserver\data\html\tutorial_spanish.htm" (
    copy "gameserver\data\html\tutorial_spanish.htm" "backup_tutorial_espanol\html\tutorial_spanish.htm"
    echo ✅ tutorial_spanish.htm - BACKUP CREADO
) else (
    echo ❌ tutorial_spanish.htm - NO ENCONTRADO
)

if exist "gameserver\data\html\tutorial_menu.htm" (
    copy "gameserver\data\html\tutorial_menu.htm" "backup_tutorial_espanol\html\tutorial_menu.htm"
    echo ✅ tutorial_menu.htm - BACKUP CREADO
) else (
    echo ❌ tutorial_menu.htm - NO ENCONTRADO
)

if exist "gameserver\config\head\tutorial_spanish.properties" (
    copy "gameserver\config\head\tutorial_spanish.properties" "backup_tutorial_espanol\config\head\tutorial_spanish.properties"
    echo ✅ tutorial_spanish.properties - BACKUP CREADO
) else (
    echo ❌ tutorial_spanish.properties - NO ENCONTRADO
)

echo.
echo ===========================================
echo BACKUP COMPLETADO
echo ===========================================
echo.
echo 💾 Backup creado en: backup_tutorial_espanol\
echo.
echo 📁 Archivos respaldados:
echo ✅ EpicTutorialSpanish.py
echo ✅ EpicTutorialAutoStart.py
echo ✅ EpicTutorialNPC.py
echo ✅ tutorial_spanish.htm
echo ✅ tutorial_menu.htm
echo ✅ tutorial_spanish.properties
echo.
echo 🌟 L2 HERMANOS - BACKUP COMPLETADO
echo 💰 TUTORIAL EN ESPAÑOL + TÍTULOS ÉPICOS + PVP COMPETITIVO
echo 🏆 SISTEMA DE CRÉDITOS + EVENTOS ÉPICOS + GUILD WARS
echo 🎯 RANKING + TELEPORTER + DONACIONES + MONETIZACIÓN
echo.
echo ¡¡¡ BACKUP DEL TUTORIAL EN ESPAÑOL COMPLETADO !!!
echo.
echo 📋 Información del backup:
echo 📅 Fecha: %date%
echo ⏰ Hora: %time%
echo 📁 Ubicación: %CD%\backup_tutorial_espanol\
echo 🖥️ Sistema: %OS%
echo 👤 Usuario: %USERNAME%
echo.
echo Presiona cualquier tecla para continuar...
pause >nul



