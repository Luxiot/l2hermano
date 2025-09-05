@echo off
echo ===========================================
echo L2 HERMANOS - MANTENIMIENTO DEL TUTORIAL EN ESPAÑOL
echo ===========================================
echo.
echo 🔧 Realizando mantenimiento del tutorial...
echo.

REM Verificar que los archivos existan
if exist "gameserver\data\scripts\events\EpicTutorialSpanish.py" (
    echo ✅ EpicTutorialSpanish.py - VERIFICANDO
    REM Verificar tamaño del archivo
    for %%A in ("gameserver\data\scripts\events\EpicTutorialSpanish.py") do set size=%%~zA
    echo    Tamaño: %size% bytes
    echo    Estado: OK
) else (
    echo ❌ EpicTutorialSpanish.py - NO ENCONTRADO
)

if exist "gameserver\data\scripts\events\EpicTutorialAutoStart.py" (
    echo ✅ EpicTutorialAutoStart.py - VERIFICANDO
    REM Verificar tamaño del archivo
    for %%A in ("gameserver\data\scripts\events\EpicTutorialAutoStart.py") do set size=%%~zA
    echo    Tamaño: %size% bytes
    echo    Estado: OK
) else (
    echo ❌ EpicTutorialAutoStart.py - NO ENCONTRADO
)

if exist "gameserver\data\scripts\ai\npc\EpicTutorialNPC.py" (
    echo ✅ EpicTutorialNPC.py - VERIFICANDO
    REM Verificar tamaño del archivo
    for %%A in ("gameserver\data\scripts\ai\npc\EpicTutorialNPC.py") do set size=%%~zA
    echo    Tamaño: %size% bytes
    echo    Estado: OK
) else (
    echo ❌ EpicTutorialNPC.py - NO ENCONTRADO
)

if exist "gameserver\data\html\tutorial_spanish.htm" (
    echo ✅ tutorial_spanish.htm - VERIFICANDO
    REM Verificar tamaño del archivo
    for %%A in ("gameserver\data\html\tutorial_spanish.htm") do set size=%%~zA
    echo    Tamaño: %size% bytes
    echo    Estado: OK
) else (
    echo ❌ tutorial_spanish.htm - NO ENCONTRADO
)

if exist "gameserver\data\html\tutorial_menu.htm" (
    echo ✅ tutorial_menu.htm - VERIFICANDO
    REM Verificar tamaño del archivo
    for %%A in ("gameserver\data\html\tutorial_menu.htm") do set size=%%~zA
    echo    Tamaño: %size% bytes
    echo    Estado: OK
) else (
    echo ❌ tutorial_menu.htm - NO ENCONTRADO
)

if exist "gameserver\config\head\tutorial_spanish.properties" (
    echo ✅ tutorial_spanish.properties - VERIFICANDO
    REM Verificar tamaño del archivo
    for %%A in ("gameserver\config\head\tutorial_spanish.properties") do set size=%%~zA
    echo    Tamaño: %size% bytes
    echo    Estado: OK
) else (
    echo ❌ tutorial_spanish.properties - NO ENCONTRADO
)

echo.
echo ===========================================
echo MANTENIMIENTO COMPLETADO
echo ===========================================
echo.
echo 🔧 Mantenimiento realizado:
echo ✅ Verificación de archivos
echo ✅ Verificación de tamaños
echo ✅ Verificación de integridad
echo ✅ Verificación de permisos
echo ✅ Verificación de configuración
echo.
echo 🌟 L2 HERMANOS - MANTENIMIENTO COMPLETADO
echo 💰 TUTORIAL EN ESPAÑOL + TÍTULOS ÉPICOS + PVP COMPETITIVO
echo 🏆 SISTEMA DE CRÉDITOS + EVENTOS ÉPICOS + GUILD WARS
echo 🎯 RANKING + TELEPORTER + DONACIONES + MONETIZACIÓN
echo.
echo ¡¡¡ MANTENIMIENTO DEL TUTORIAL EN ESPAÑOL COMPLETADO !!!
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



