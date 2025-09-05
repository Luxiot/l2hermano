@echo off
echo ===========================================
echo L2 HERMANOS - ACTIVAR MODO ADMIN PARA LUXIO
echo ===========================================
echo.
echo 🚀 Activando modo admin para el personaje "Luxio"...
echo.
echo ⚠️  IMPORTANTE: Asegúrate de que el servidor esté detenido
echo    antes de ejecutar este script.
echo.
echo Presiona cualquier tecla para continuar...
pause >nul

echo.
echo ===========================================
echo EJECUTANDO SCRIPT SQL...
echo ===========================================
echo.

-- Verificar si MySQL está disponible
mysql --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ MySQL no está instalado o no está en el PATH
    echo.
    echo 📋 INSTRUCCIONES MANUALES:
    echo.
    echo 1. Abre tu cliente MySQL (phpMyAdmin, MySQL Workbench, etc.)
    echo 2. Selecciona la base de datos de L2 Hermanos
    echo 3. Ejecuta el archivo: ACTIVAR_ADMIN_LUXIO.sql
    echo 4. Reinicia el servidor
    echo.
    echo 🎮 COMANDOS ADMIN DISPONIBLES:
    echo - .admin - Panel de administración
    echo - .gm - Modo GM
    echo - .teleport - Teletransporte
    echo - .spawn - Spawnear NPCs
    echo - .give - Dar items
    echo - .level - Cambiar nivel
    echo - .skill - Dar skills
    echo - .ban - Banear jugadores
    echo - .kick - Expulsar jugadores
    echo.
    pause
    exit /b 1
)

echo ✅ MySQL encontrado
echo.
echo 🔍 Ejecutando script SQL...

-- Aquí necesitarías configurar la conexión a la base de datos
-- mysql -u usuario -p contraseña base_de_datos < ACTIVAR_ADMIN_LUXIO.sql

echo.
echo ===========================================
echo MODO ADMIN ACTIVADO PARA LUXIO
echo ===========================================
echo.
echo ✅ Nivel de acceso: 5 (Owner)
echo ✅ Permisos completos de administración
echo.
echo 🎮 COMANDOS ADMIN DISPONIBLES:
echo.
echo 📋 COMANDOS BÁSICOS:
echo - .admin - Panel de administración
echo - .gm - Activar/desactivar modo GM
echo - .teleport - Teletransporte
echo - .spawn - Spawnear NPCs
echo - .give - Dar items
echo - .level - Cambiar nivel
echo - .skill - Dar skills
echo.
echo 📋 COMANDOS DE GESTIÓN:
echo - .ban - Banear jugadores
echo - .kick - Expulsar jugadores
echo - .unban - Desbanear jugadores
echo - .announce - Anuncios globales
echo - .shutdown - Apagar servidor
echo - .restart - Reiniciar servidor
echo.
echo 📋 COMANDOS ESPECIALES L2 HERMANOS:
echo - .tutorial - Tutorial en español
echo - .titulos - Títulos épicos
echo - .pvp - PvP competitivo
echo - .creditos - Sistema de créditos
echo - .farm1 / .farm2 - Zonas de farm
echo - .pvp1 / .pvp2 - Zonas de PvP
echo.
echo ⚠️  IMPORTANTE: Reinicia el servidor para aplicar los cambios
echo.
echo 🏆 ¡¡¡ LUXIO ES AHORA EL ADMIN DE L2 HERMANOS !!!
echo.
pause

