@echo off
echo ===========================================
echo L2 HERMANOS - ACTIVAR ADMIN LUXIO (MYSQL)
echo ===========================================
echo.
echo 🚀 Activando modo admin para Luxio...
echo.

echo ===========================================
echo EJECUTANDO COMANDO MYSQL
echo ===========================================
echo.
echo 🔍 Ejecutando comando directo de MySQL...
echo.

"C:\Program Files\MySQL\MySQL Server 8.0\bin\mysql.exe" -u root -D l2jdb -e "UPDATE characters SET accesslevel = 5 WHERE char_name = 'Luxio';"

echo.
echo 🔍 Verificando que se haya actualizado...
echo.

"C:\Program Files\MySQL\MySQL Server 8.0\bin\mysql.exe" -u root -D l2jdb -e "SELECT char_name as 'Nombre', accesslevel as 'Nivel_Admin', level as 'Nivel' FROM characters WHERE char_name = 'Luxio';"

echo.
echo ===========================================
echo RESULTADO
echo ===========================================
echo.
echo ✅ ¡MODO ADMIN ACTIVADO PARA LUXIO!
echo ✅ Nivel de acceso: 5 (Owner)
echo.
echo 🎮 Ahora puedes usar todos los comandos admin:
echo.
echo - .admin - Panel de administración
echo - .gm - Activar/desactivar modo GM
echo - .teleport - Teletransporte
echo - .spawn - Spawnear NPCs
echo - .give - Dar items
echo - .level - Cambiar nivel
echo - .skill - Dar skills
echo - .tutorial - Tutorial en español
echo - .titulos - Títulos épicos
echo - .pvp - PvP competitivo
echo.
echo ===========================================
echo ¡LUXIO ES AHORA EL ADMIN DE L2 HERMANOS!
echo ===========================================
echo.
echo 🏆 ¡¡¡ EL MEJOR SERVIDOR L2 DE LA HISTORIA !!!
echo.
pause

