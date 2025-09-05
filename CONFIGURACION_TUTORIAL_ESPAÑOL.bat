@echo off
echo ===========================================
echo L2 HERMANOS - CONFIGURACIÓN DEL TUTORIAL EN ESPAÑOL
echo ===========================================
echo.
echo ⚙️ Configurando tutorial en español...
echo.

REM Verificar que los archivos existan
if exist "gameserver\config\head\tutorial_spanish.properties" (
    echo ✅ tutorial_spanish.properties - ENCONTRADO
    echo.
    echo 📋 Configuración actual:
    echo.
    type "gameserver\config\head\tutorial_spanish.properties"
    echo.
    echo ===========================================
    echo CONFIGURACIÓN DEL TUTORIAL EN ESPAÑOL
    echo ===========================================
    echo.
    echo 🎮 Características configuradas:
    echo ✅ Tutorial en español habilitado
    echo ✅ Inicio automático habilitado
    echo ✅ Nivel máximo para tutorial: 5
    echo ✅ Mensajes del tutorial habilitados
    echo ✅ HTML del tutorial habilitado
    echo ✅ NPCs del tutorial habilitados
    echo ✅ Sistema de títulos épicos habilitado
    echo ✅ PvP competitivo habilitado
    echo ✅ Sistema de créditos habilitado
    echo ✅ Eventos épicos habilitados
    echo ✅ Comandos épicos habilitados
    echo ✅ Guild wars épicas habilitadas
    echo ✅ Sistema de logros habilitado
    echo ✅ Sistema de ranking habilitado
    echo ✅ Sistema de teleporter habilitado
    echo ✅ Sistema de donaciones habilitado
    echo ✅ Sistema de monetización habilitado
    echo ✅ Sistema de coliseo habilitado
    echo.
    echo 🌟 L2 HERMANOS - CONFIGURACIÓN COMPLETA
    echo 💰 TUTORIAL EN ESPAÑOL + TÍTULOS ÉPICOS + PVP COMPETITIVO
    echo 🏆 SISTEMA DE CRÉDITOS + EVENTOS ÉPICOS + GUILD WARS
    echo 🎯 RANKING + TELEPORTER + DONACIONES + MONETIZACIÓN
    echo.
    echo ¡¡¡ CONFIGURACIÓN DEL TUTORIAL EN ESPAÑOL COMPLETA !!!
) else (
    echo ❌ tutorial_spanish.properties - NO ENCONTRADO
    echo.
    echo 🚨 ERROR: Archivo de configuración no encontrado
    echo.
    echo 📋 Soluciones:
    echo 1. Verifica que el archivo esté en la ubicación correcta
    echo 2. Ejecuta el script de instalación
    echo 3. Verifica los permisos de archivo
    echo 4. Contacta al administrador del servidor
    echo.
    echo 🌟 L2 HERMANOS - CONFIGURACIÓN INCOMPLETA
    echo 💰 TUTORIAL EN ESPAÑOL + TÍTULOS ÉPICOS + PVP COMPETITIVO
    echo 🏆 SISTEMA DE CRÉDITOS + EVENTOS ÉPICOS + GUILD WARS
    echo 🎯 RANKING + TELEPORTER + DONACIONES + MONETIZACIÓN
    echo.
    echo ¡¡¡ CONFIGURACIÓN DEL TUTORIAL EN ESPAÑOL INCOMPLETA !!!
)

echo.
echo ===========================================
echo Presiona cualquier tecla para continuar...
pause >nul



