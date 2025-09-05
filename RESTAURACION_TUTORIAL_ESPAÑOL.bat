@echo off
echo ===========================================
echo L2 HERMANOS - RESTAURACIÓN DEL TUTORIAL EN ESPAÑOL
echo ===========================================
echo.
echo 🔄 Restaurando tutorial desde backup...
echo.

REM Verificar que el directorio de backup exista
if not exist "backup_tutorial_espanol" (
    echo ❌ Directorio de backup no encontrado
    echo.
    echo 🚨 ERROR: No se puede restaurar sin backup
    echo.
    echo 📋 Soluciones:
    echo 1. Ejecuta el script de backup primero
    echo 2. Verifica que el directorio de backup exista
    echo 3. Contacta al administrador del servidor
    echo.
    echo 🌟 L2 HERMANOS - RESTAURACIÓN FALLIDA
    echo 💰 TUTORIAL EN ESPAÑOL + TÍTULOS ÉPICOS + PVP COMPETITIVO
    echo 🏆 SISTEMA DE CRÉDITOS + EVENTOS ÉPICOS + GUILD WARS
    echo 🎯 RANKING + TELEPORTER + DONACIONES + MONETIZACIÓN
    echo.
    echo ¡¡¡ RESTAURACIÓN DEL TUTORIAL EN ESPAÑOL FALLIDA !!!
    echo.
    echo Presiona cualquier tecla para continuar...
    pause >nul
    exit /b 1
)

echo ✅ Directorio de backup encontrado
echo.

REM Crear directorios de destino si no existen
if not exist "gameserver\data\scripts\events" mkdir "gameserver\data\scripts\events"
if not exist "gameserver\data\scripts\ai\npc" mkdir "gameserver\data\scripts\ai\npc"
if not exist "gameserver\data\html" mkdir "gameserver\data\html"
if not exist "gameserver\config\head" mkdir "gameserver\config\head"

echo ✅ Directorios de destino creados/verificados
echo.

REM Restaurar archivos desde backup
if exist "backup_tutorial_espanol\scripts\events\EpicTutorialSpanish.py" (
    copy "backup_tutorial_espanol\scripts\events\EpicTutorialSpanish.py" "gameserver\data\scripts\events\EpicTutorialSpanish.py"
    echo ✅ EpicTutorialSpanish.py - RESTAURADO
) else (
    echo ❌ EpicTutorialSpanish.py - NO ENCONTRADO EN BACKUP
)

if exist "backup_tutorial_espanol\scripts\events\EpicTutorialAutoStart.py" (
    copy "backup_tutorial_espanol\scripts\events\EpicTutorialAutoStart.py" "gameserver\data\scripts\events\EpicTutorialAutoStart.py"
    echo ✅ EpicTutorialAutoStart.py - RESTAURADO
) else (
    echo ❌ EpicTutorialAutoStart.py - NO ENCONTRADO EN BACKUP
)

if exist "backup_tutorial_espanol\scripts\ai\npc\EpicTutorialNPC.py" (
    copy "backup_tutorial_espanol\scripts\ai\npc\EpicTutorialNPC.py" "gameserver\data\scripts\ai\npc\EpicTutorialNPC.py"
    echo ✅ EpicTutorialNPC.py - RESTAURADO
) else (
    echo ❌ EpicTutorialNPC.py - NO ENCONTRADO EN BACKUP
)

if exist "backup_tutorial_espanol\html\tutorial_spanish.htm" (
    copy "backup_tutorial_espanol\html\tutorial_spanish.htm" "gameserver\data\html\tutorial_spanish.htm"
    echo ✅ tutorial_spanish.htm - RESTAURADO
) else (
    echo ❌ tutorial_spanish.htm - NO ENCONTRADO EN BACKUP
)

if exist "backup_tutorial_espanol\html\tutorial_menu.htm" (
    copy "backup_tutorial_espanol\html\tutorial_menu.htm" "gameserver\data\html\tutorial_menu.htm"
    echo ✅ tutorial_menu.htm - RESTAURADO
) else (
    echo ❌ tutorial_menu.htm - NO ENCONTRADO EN BACKUP
)

if exist "backup_tutorial_espanol\config\head\tutorial_spanish.properties" (
    copy "backup_tutorial_espanol\config\head\tutorial_spanish.properties" "gameserver\config\head\tutorial_spanish.properties"
    echo ✅ tutorial_spanish.properties - RESTAURADO
) else (
    echo ❌ tutorial_spanish.properties - NO ENCONTRADO EN BACKUP
)

echo.
echo ===========================================
echo RESTAURACIÓN COMPLETADA
echo ===========================================
echo.
echo 🔄 Archivos restaurados:
echo ✅ EpicTutorialSpanish.py
echo ✅ EpicTutorialAutoStart.py
echo ✅ EpicTutorialNPC.py
echo ✅ tutorial_spanish.htm
echo ✅ tutorial_menu.htm
echo ✅ tutorial_spanish.properties
echo.
echo 🌟 L2 HERMANOS - RESTAURACIÓN COMPLETADA
echo 💰 TUTORIAL EN ESPAÑOL + TÍTULOS ÉPICOS + PVP COMPETITIVO
echo 🏆 SISTEMA DE CRÉDITOS + EVENTOS ÉPICOS + GUILD WARS
echo 🎯 RANKING + TELEPORTER + DONACIONES + MONETIZACIÓN
echo.
echo ¡¡¡ RESTAURACIÓN DEL TUTORIAL EN ESPAÑOL COMPLETADA !!!
echo.
echo 📋 Próximos pasos:
echo 1. Reinicia el servidor
echo 2. Verifica que el tutorial funcione
echo 3. Prueba los comandos épicos
echo 4. Verifica los títulos épicos
echo 5. Prueba el PvP competitivo
echo 6. Verifica el sistema de créditos
echo 7. Prueba los eventos épicos
echo 8. Verifica las guild wars épicas
echo 9. Prueba el sistema de logros
echo 10. Verifica el sistema de ranking
echo 11. Prueba el sistema de teleporter
echo 12. Verifica el sistema de donaciones
echo 13. Prueba el sistema de monetización
echo 14. Verifica el sistema de coliseo
echo.
echo Presiona cualquier tecla para continuar...
pause >nul



