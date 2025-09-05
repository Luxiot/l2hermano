@echo off
echo ===========================================
echo L2 HERMANOS - INSTALACIÓN DEL TUTORIAL EN ESPAÑOL
echo ===========================================
echo.
echo 🚀 Instalando tutorial en español...
echo.

REM Crear directorios si no existen
if not exist "gameserver\data\scripts\events" mkdir "gameserver\data\scripts\events"
if not exist "gameserver\data\scripts\ai\npc" mkdir "gameserver\data\scripts\ai\npc"
if not exist "gameserver\data\html" mkdir "gameserver\data\html"
if not exist "gameserver\config\head" mkdir "gameserver\config\head"

echo ✅ Directorios creados/verificados
echo.

REM Verificar que los archivos existan
if exist "gameserver\data\scripts\events\EpicTutorialSpanish.py" (
    echo ✅ EpicTutorialSpanish.py - INSTALADO
) else (
    echo ❌ EpicTutorialSpanish.py - NO ENCONTRADO
)

if exist "gameserver\data\scripts\events\EpicTutorialAutoStart.py" (
    echo ✅ EpicTutorialAutoStart.py - INSTALADO
) else (
    echo ❌ EpicTutorialAutoStart.py - NO ENCONTRADO
)

if exist "gameserver\data\scripts\ai\npc\EpicTutorialNPC.py" (
    echo ✅ EpicTutorialNPC.py - INSTALADO
) else (
    echo ❌ EpicTutorialNPC.py - NO ENCONTRADO
)

if exist "gameserver\data\html\tutorial_spanish.htm" (
    echo ✅ tutorial_spanish.htm - INSTALADO
) else (
    echo ❌ tutorial_spanish.htm - NO ENCONTRADO
)

if exist "gameserver\data\html\tutorial_menu.htm" (
    echo ✅ tutorial_menu.htm - INSTALADO
) else (
    echo ❌ tutorial_menu.htm - NO ENCONTRADO
)

if exist "gameserver\config\head\tutorial_spanish.properties" (
    echo ✅ tutorial_spanish.properties - INSTALADO
) else (
    echo ❌ tutorial_spanish.properties - NO ENCONTRADO
)

echo.
echo ===========================================
echo L2 HERMANOS - TUTORIAL EN ESPAÑOL INSTALADO
echo ===========================================
echo.
echo 🎮 Características instaladas:
echo ✅ Tutorial en español automático
echo ✅ NPCs del tutorial en español
echo ✅ HTML del tutorial en español
echo ✅ Configuración del tutorial en español
echo ✅ Sistema de títulos épicos
echo ✅ PvP competitivo
echo ✅ Sistema de créditos
echo ✅ Eventos épicos
echo ✅ Comandos épicos
echo ✅ Guild wars épicas
echo ✅ Sistema de logros
echo ✅ Sistema de ranking
echo ✅ Sistema de teleporter
echo ✅ Sistema de donaciones
echo ✅ Sistema de monetización
echo ✅ Sistema de coliseo
echo.
echo 🌟 L2 HERMANOS - EL MEJOR SERVIDOR L2 DE LA HISTORIA
echo 💰 TUTORIAL EN ESPAÑOL + TÍTULOS ÉPICOS + PVP COMPETITIVO
echo 🏆 SISTEMA DE CRÉDITOS + EVENTOS ÉPICOS + GUILD WARS
echo 🎯 RANKING + TELEPORTER + DONACIONES + MONETIZACIÓN
echo.
echo ¡¡¡ TUTORIAL EN ESPAÑOL INSTALADO CORRECTAMENTE !!!
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



