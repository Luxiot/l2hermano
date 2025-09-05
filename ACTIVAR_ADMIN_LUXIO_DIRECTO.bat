@echo off
echo ===========================================
echo L2 HERMANOS - ACTIVAR ADMIN LUXIO (DIRECTO)
echo ===========================================
echo.
echo 🚀 Activando modo admin para Luxio...
echo.
echo 📋 Configuración detectada:
echo - Base de datos: l2jdb
echo - Usuario: root
echo - Contraseña: (sin contraseña)
echo.

echo ===========================================
echo OPCIÓN 1: USAR MYSQL DESDE CMD
echo ===========================================
echo.
echo 🔍 Verificando si MySQL está disponible...
mysql --version >nul 2>&1
if %errorlevel% == 0 (
    echo ✅ MySQL encontrado
    echo.
    echo 🚀 Ejecutando comando directo...
    echo.
    mysql -u root -D l2jdb -e "UPDATE characters SET accesslevel = 5 WHERE char_name = 'Luxio';"
    mysql -u root -D l2jdb -e "SELECT char_name, accesslevel, level FROM characters WHERE char_name = 'Luxio';"
    echo.
    echo ✅ ¡MODO ADMIN ACTIVADO PARA LUXIO!
    echo.
    goto :success
) else (
    echo ❌ MySQL no está en el PATH
    echo.
    goto :manual
)

:manual
echo ===========================================
echo OPCIÓN 2: INSTRUCCIONES MANUALES
echo ===========================================
echo.
echo 📋 PASO A PASO:
echo.
echo 1. Abre tu navegador web
echo 2. Ve a: http://localhost/phpmyadmin
echo 3. Selecciona la base de datos: l2jdb
echo 4. Ve a la pestaña "SQL"
echo 5. Copia y pega este código:
echo.
echo ===========================================
echo CÓDIGO SQL PARA COPIAR:
echo ===========================================
echo.
echo UPDATE characters SET accesslevel = 5 WHERE char_name = 'Luxio';
echo.
echo SELECT char_name, accesslevel, level FROM characters WHERE char_name = 'Luxio';
echo.
echo ===========================================
echo.
echo 6. Haz clic en "Ejecutar"
echo 7. Deberías ver que accesslevel cambió a 5
echo.
echo Presiona cualquier tecla cuando hayas ejecutado el SQL...
pause >nul

:success
echo ===========================================
echo VERIFICACIÓN FINAL
echo ===========================================
echo.
echo 🔍 Verificando que el servidor esté funcionando...
netstat -an | findstr ":2106" >nul
if %errorlevel% == 0 (
    echo ✅ Login Server: FUNCIONANDO
) else (
    echo ❌ Login Server: NO FUNCIONA
)

netstat -an | findstr ":7777" >nul
if %errorlevel% == 0 (
    echo ✅ Game Server: FUNCIONANDO
) else (
    echo ❌ Game Server: NO FUNCIONA
)

echo.
echo ===========================================
echo COMANDOS ADMIN DISPONIBLES
echo ===========================================
echo.
echo 🎮 COMANDOS BÁSICOS:
echo - .admin - Panel de administración
echo - .gm - Activar/desactivar modo GM
echo - .teleport - Teletransporte
echo - .spawn - Spawnear NPCs
echo - .give - Dar items
echo - .level - Cambiar nivel
echo - .skill - Dar skills
echo.
echo 🎮 COMANDOS ESPECIALES L2 HERMANOS:
echo - .tutorial - Tutorial en español
echo - .titulos - Títulos épicos
echo - .pvp - PvP competitivo
echo - .creditos - Sistema de créditos
echo.
echo ===========================================
echo ¡LUXIO ES AHORA EL ADMIN DE L2 HERMANOS!
echo ===========================================
echo.
echo 🏆 ¡¡¡ EL MEJOR SERVIDOR L2 DE LA HISTORIA !!!
echo.
echo ⚠️  IMPORTANTE: Si no funciona, reinicia el servidor
echo.
pause

