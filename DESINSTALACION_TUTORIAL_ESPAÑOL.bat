@echo off
echo ===========================================
echo L2 HERMANOS - DESINSTALACIÓN DEL TUTORIAL EN ESPAÑOL
echo ===========================================
echo.
echo 🗑️ Desinstalando tutorial en español...
echo.

REM Verificar que los archivos existan antes de eliminarlos
if exist "gameserver\data\scripts\events\EpicTutorialSpanish.py" (
    echo ✅ EpicTutorialSpanish.py - ENCONTRADO
    del "gameserver\data\scripts\events\EpicTutorialSpanish.py"
    echo ✅ EpicTutorialSpanish.py - ELIMINADO
) else (
    echo ❌ EpicTutorialSpanish.py - NO ENCONTRADO
)

if exist "gameserver\data\scripts\events\EpicTutorialAutoStart.py" (
    echo ✅ EpicTutorialAutoStart.py - ENCONTRADO
    del "gameserver\data\scripts\events\EpicTutorialAutoStart.py"
    echo ✅ EpicTutorialAutoStart.py - ELIMINADO
) else (
    echo ❌ EpicTutorialAutoStart.py - NO ENCONTRADO
)

if exist "gameserver\data\scripts\ai\npc\EpicTutorialNPC.py" (
    echo ✅ EpicTutorialNPC.py - ENCONTRADO
    del "gameserver\data\scripts\ai\npc\EpicTutorialNPC.py"
    echo ✅ EpicTutorialNPC.py - ELIMINADO
) else (
    echo ❌ EpicTutorialNPC.py - NO ENCONTRADO
)

if exist "gameserver\data\html\tutorial_spanish.htm" (
    echo ✅ tutorial_spanish.htm - ENCONTRADO
    del "gameserver\data\html\tutorial_spanish.htm"
    echo ✅ tutorial_spanish.htm - ELIMINADO
) else (
    echo ❌ tutorial_spanish.htm - NO ENCONTRADO
)

if exist "gameserver\data\html\tutorial_menu.htm" (
    echo ✅ tutorial_menu.htm - ENCONTRADO
    del "gameserver\data\html\tutorial_menu.htm"
    echo ✅ tutorial_menu.htm - ELIMINADO
) else (
    echo ❌ tutorial_menu.htm - NO ENCONTRADO
)

if exist "gameserver\config\head\tutorial_spanish.properties" (
    echo ✅ tutorial_spanish.properties - ENCONTRADO
    del "gameserver\config\head\tutorial_spanish.properties"
    echo ✅ tutorial_spanish.properties - ELIMINADO
) else (
    echo ❌ tutorial_spanish.properties - NO ENCONTRADO
)

echo.
echo ===========================================
echo L2 HERMANOS - TUTORIAL EN ESPAÑOL DESINSTALADO
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
echo 🌟 L2 HERMANOS - TUTORIAL EN ESPAÑOL DESINSTALADO
echo 💰 SISTEMA DE TÍTULOS ÉPICOS + PVP COMPETITIVO
echo 🏆 SISTEMA DE CRÉDITOS + EVENTOS ÉPICOS + GUILD WARS
echo 🎯 RANKING + TELEPORTER + DONACIONES + MONETIZACIÓN
echo.
echo ¡¡¡ TUTORIAL EN ESPAÑOL DESINSTALADO CORRECTAMENTE !!!
echo.
echo 📋 Próximos pasos:
echo 1. Reinicia el servidor
echo 2. Verifica que el tutorial original funcione
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



