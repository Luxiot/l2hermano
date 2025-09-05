@echo off
echo ===========================================
echo L2 HERMANOS - INSTRUCCIONES PARA ACTIVAR ADMIN
echo ===========================================
echo.
echo 🚀 ACTIVAR MODO ADMIN PARA LUXIO
echo.
echo ===========================================
echo PASO 1: DETENER EL SERVIDOR
echo ===========================================
echo.
echo ⚠️  IMPORTANTE: Debes detener el servidor antes de continuar
echo.
echo 1. Cierra las ventanas del Login Server y Game Server
echo 2. Espera a que se cierren completamente
echo 3. Presiona cualquier tecla cuando esté listo...
pause >nul

echo.
echo ===========================================
echo PASO 2: EJECUTAR SCRIPT SQL
echo ===========================================
echo.
echo 📋 OPCIÓN A - PHPMyAdmin (Recomendado):
echo.
echo 1. Abre tu navegador web
echo 2. Ve a: http://localhost/phpmyadmin
echo 3. Selecciona la base de datos de L2 Hermanos
echo 4. Ve a la pestaña "SQL"
echo 5. Copia y pega el contenido del archivo: ACTIVAR_ADMIN_LUXIO.sql
echo 6. Haz clic en "Ejecutar"
echo.
echo 📋 OPCIÓN B - MySQL Workbench:
echo.
echo 1. Abre MySQL Workbench
echo 2. Conéctate a tu base de datos
echo 3. Abre el archivo: ACTIVAR_ADMIN_LUXIO.sql
echo 4. Ejecuta el script
echo.
echo 📋 OPCIÓN C - Línea de comandos MySQL:
echo.
echo 1. Abre CMD como administrador
echo 2. Ejecuta: mysql -u root -p
echo 3. Selecciona la base de datos: USE l2hermanos;
echo 4. Ejecuta: source ACTIVAR_ADMIN_LUXIO.sql;
echo.
echo Presiona cualquier tecla cuando hayas ejecutado el SQL...
pause >nul

echo.
echo ===========================================
echo PASO 3: REINICIAR EL SERVIDOR
echo ===========================================
echo.
echo ✅ SQL ejecutado correctamente
echo.
echo 🚀 Ahora reinicia el servidor:
echo.
echo 1. Ejecuta: INICIAR_L2_HERMANOS_SIMPLE.bat
echo 2. Espera a que ambos servidores estén funcionando
echo 3. Conéctate con el personaje "Luxio"
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
echo 🎮 COMANDOS DE GESTIÓN:
echo - .ban - Banear jugadores
echo - .kick - Expulsar jugadores
echo - .unban - Desbanear jugadores
echo - .announce - Anuncios globales
echo - .shutdown - Apagar servidor
echo - .restart - Reiniciar servidor
echo.
echo 🎮 COMANDOS ESPECIALES L2 HERMANOS:
echo - .tutorial - Tutorial en español
echo - .titulos - Títulos épicos
echo - .pvp - PvP competitivo
echo - .creditos - Sistema de créditos
echo - .farm1 / .farm2 - Zonas de farm
echo - .pvp1 / .pvp2 - Zonas de PvP
echo.
echo ===========================================
echo ¡LUXIO ES AHORA EL ADMIN DE L2 HERMANOS!
echo ===========================================
echo.
echo 🏆 ¡¡¡ EL MEJOR SERVIDOR L2 DE LA HISTORIA !!!
echo.
pause

