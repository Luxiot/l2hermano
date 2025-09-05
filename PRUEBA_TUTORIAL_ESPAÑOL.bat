@echo off
echo ===========================================
echo L2 HERMANOS - PRUEBA DEL TUTORIAL EN ESPAÑOL
echo ===========================================
echo.
echo 🎮 Probando tutorial en español...
echo.

echo ✅ Verificando servidor...
netstat -an | findstr ":7777" >nul
if %errorlevel% == 0 (
    echo ✅ Game Server funcionando en puerto 7777
) else (
    echo ❌ Game Server no está funcionando
    goto :error
)

netstat -an | findstr ":2106" >nul
if %errorlevel% == 0 (
    echo ✅ Login Server funcionando en puerto 2106
) else (
    echo ❌ Login Server no está funcionando
    goto :error
)

echo.
echo ✅ Verificando scripts del tutorial...
if exist "gameserver\data\scripts\events\EpicTutorialSpanish.py" (
    echo ✅ EpicTutorialSpanish.py encontrado
) else (
    echo ❌ EpicTutorialSpanish.py no encontrado
    goto :error
)

if exist "gameserver\data\scripts\ai\npc\EpicTutorialNPC.py" (
    echo ✅ EpicTutorialNPC.py encontrado
) else (
    echo ❌ EpicTutorialNPC.py no encontrado
    goto :error
)

if exist "gameserver\data\html\tutorial_spanish.htm" (
    echo ✅ tutorial_spanish.htm encontrado
) else (
    echo ❌ tutorial_spanish.htm no encontrado
    goto :error
)

echo.
echo ===========================================
echo L2 HERMANOS - TUTORIAL EN ESPAÑOL LISTO
echo ===========================================
echo.
echo 🎮 Para probar el tutorial en español:
echo.
echo 1. Conéctate al servidor (127.0.0.1:2106)
echo 2. Crea un personaje o usa uno existente
echo 3. Escribe en el chat: .tutorial
echo 4. O busca el NPC "Maestro del Tutorial" en las ciudades
echo 5. O usa: .titulos para ver los títulos épicos
echo.
echo 🌟 Comandos disponibles:
echo - .tutorial - Iniciar tutorial en español
echo - .titulos - Ver títulos épicos
echo - .pvp - PvP competitivo
echo - .creditos - Sistema de créditos
echo - .farm1 / .farm2 - Zonas de farm
echo - .pvp1 / .pvp2 - Zonas de PvP
echo.
echo 🏆 ¡¡¡ L2 HERMANOS - EL MEJOR SERVIDOR L2 DE LA HISTORIA !!!
echo.
echo Presiona cualquier tecla para continuar...
pause >nul
goto :end

:error
echo.
echo ❌ ERROR: El tutorial en español no está funcionando correctamente
echo.
echo 🔧 Soluciones:
echo 1. Reinicia el servidor
echo 2. Verifica que los scripts estén en la carpeta correcta
echo 3. Revisa los logs del servidor
echo.
echo Presiona cualquier tecla para continuar...
pause >nul

:end



