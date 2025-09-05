@echo off
:menu
cls
echo ===========================================
echo L2 HERMANOS - MENÚ PRINCIPAL DEL TUTORIAL EN ESPAÑOL
echo ===========================================
echo.
echo 🎮 Selecciona una opción:
echo.
echo 1. Inicio rápido del tutorial
echo 2. Verificación del tutorial
echo 3. Instalación del tutorial
echo 4. Desinstalación del tutorial
echo 5. Configuración del tutorial
echo 6. Ayuda del tutorial
echo 7. Estado del tutorial
echo 8. Mantenimiento del tutorial
echo 9. Backup del tutorial
echo 10. Restauración del tutorial
echo 11. Limpieza del tutorial
echo 12. Optimización del tutorial
echo 13. Estadísticas del tutorial
echo 14. Información del tutorial
echo 15. Ayuda rápida del tutorial
echo 16. Salir
echo.
echo ===========================================
set /p opcion="Ingresa tu opción (1-16): "

if "%opcion%"=="1" (
    echo.
    echo 🚀 Iniciando tutorial en español...
    call INICIO_RAPIDO_TUTORIAL_ESPAÑOL.bat
    goto menu
)

if "%opcion%"=="2" (
    echo.
    echo 🔍 Verificando tutorial en español...
    call VERIFICACION_TUTORIAL_ESPAÑOL.bat
    goto menu
)

if "%opcion%"=="3" (
    echo.
    echo 📦 Instalando tutorial en español...
    call INSTALACION_TUTORIAL_ESPAÑOL.bat
    goto menu
)

if "%opcion%"=="4" (
    echo.
    echo 🗑️ Desinstalando tutorial en español...
    call DESINSTALACION_TUTORIAL_ESPAÑOL.bat
    goto menu
)

if "%opcion%"=="5" (
    echo.
    echo ⚙️ Configurando tutorial en español...
    call CONFIGURACION_TUTORIAL_ESPAÑOL.bat
    goto menu
)

if "%opcion%"=="6" (
    echo.
    echo 📚 Ayuda del tutorial en español...
    call AYUDA_TUTORIAL_ESPAÑOL.bat
    goto menu
)

if "%opcion%"=="7" (
    echo.
    echo 📊 Estado del tutorial en español...
    call ESTADO_TUTORIAL_ESPAÑOL.bat
    goto menu
)

if "%opcion%"=="8" (
    echo.
    echo 🔧 Mantenimiento del tutorial en español...
    call MANTENIMIENTO_TUTORIAL_ESPAÑOL.bat
    goto menu
)

if "%opcion%"=="9" (
    echo.
    echo 💾 Backup del tutorial en español...
    call BACKUP_TUTORIAL_ESPAÑOL.bat
    goto menu
)

if "%opcion%"=="10" (
    echo.
    echo 🔄 Restauración del tutorial en español...
    call RESTAURACION_TUTORIAL_ESPAÑOL.bat
    goto menu
)

if "%opcion%"=="11" (
    echo.
    echo 🧹 Limpieza del tutorial en español...
    call LIMPIEZA_TUTORIAL_ESPAÑOL.bat
    goto menu
)

if "%opcion%"=="12" (
    echo.
    echo ⚡ Optimización del tutorial en español...
    call OPTIMIZACION_TUTORIAL_ESPAÑOL.bat
    goto menu
)

if "%opcion%"=="13" (
    echo.
    echo 📊 Estadísticas del tutorial en español...
    call ESTADISTICAS_TUTORIAL_ESPAÑOL.bat
    goto menu
)

if "%opcion%"=="14" (
    echo.
    echo 📚 Información del tutorial en español...
    call INFORMACION_TUTORIAL_ESPAÑOL.bat
    goto menu
)

if "%opcion%"=="15" (
    echo.
    echo 🚀 Ayuda rápida del tutorial en español...
    call AYUDA_RAPIDA_TUTORIAL_ESPAÑOL.bat
    goto menu
)

if "%opcion%"=="16" (
    echo.
    echo 👋 ¡Hasta luego!
    echo.
    echo 🌟 L2 HERMANOS - EL MEJOR SERVIDOR L2 DE LA HISTORIA
    echo 💰 TUTORIAL EN ESPAÑOL + TÍTULOS ÉPICOS + PVP COMPETITIVO
    echo 🏆 SISTEMA DE CRÉDITOS + EVENTOS ÉPICOS + GUILD WARS
    echo 🎯 RANKING + TELEPORTER + DONACIONES + MONETIZACIÓN
    echo.
    echo ¡¡¡ DISFRUTA DE LA EXPERIENCIA MÁS ÉPICA DE LINEAGE 2 !!!
    echo.
    pause
    exit /b 0
)

echo.
echo ❌ Opción inválida. Por favor, selecciona una opción del 1 al 16.
echo.
pause
goto menu



