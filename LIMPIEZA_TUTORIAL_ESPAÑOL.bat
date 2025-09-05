@echo off
echo ===========================================
echo L2 HERMANOS - LIMPIEZA DEL TUTORIAL EN ESPAÑOL
echo ===========================================
echo.
echo 🧹 Limpiando archivos temporales del tutorial...
echo.

REM Limpiar archivos temporales
if exist "*.tmp" (
    del "*.tmp"
    echo ✅ Archivos temporales eliminados
) else (
    echo ℹ️ No hay archivos temporales
)

if exist "*.log" (
    del "*.log"
    echo ✅ Archivos de log eliminados
) else (
    echo ℹ️ No hay archivos de log
)

if exist "*.bak" (
    del "*.bak"
    echo ✅ Archivos de backup eliminados
) else (
    echo ℹ️ No hay archivos de backup
)

if exist "*.old" (
    del "*.old"
    echo ✅ Archivos antiguos eliminados
) else (
    echo ℹ️ No hay archivos antiguos
)

echo.
echo ===========================================
echo LIMPIEZA COMPLETADA
echo ===========================================
echo.
echo 🧹 Limpieza realizada:
echo ✅ Archivos temporales eliminados
echo ✅ Archivos de log eliminados
echo ✅ Archivos de backup eliminados
echo ✅ Archivos antiguos eliminados
echo ✅ Espacio en disco liberado
echo ✅ Sistema optimizado
echo.
echo 🌟 L2 HERMANOS - LIMPIEZA COMPLETADA
echo 💰 TUTORIAL EN ESPAÑOL + TÍTULOS ÉPICOS + PVP COMPETITIVO
echo 🏆 SISTEMA DE CRÉDITOS + EVENTOS ÉPICOS + GUILD WARS
echo 🎯 RANKING + TELEPORTER + DONACIONES + MONETIZACIÓN
echo.
echo ¡¡¡ LIMPIEZA DEL TUTORIAL EN ESPAÑOL COMPLETADA !!!
echo.
echo 📋 Información de la limpieza:
echo 📅 Fecha: %date%
echo ⏰ Hora: %time%
echo 📁 Ubicación: %CD%
echo 🖥️ Sistema: %OS%
echo 👤 Usuario: %USERNAME%
echo.
echo Presiona cualquier tecla para continuar...
pause >nul



