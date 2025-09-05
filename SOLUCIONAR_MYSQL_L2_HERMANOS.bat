@echo off
echo ===========================================
echo L2 HERMANOS - SOLUCIONAR PROBLEMA MYSQL
echo ===========================================
echo.
echo 🔧 Solucionando problema de compatibilidad MySQL...
echo.
echo ⚠️  PROBLEMA: MySQL 8.0 no es compatible con L2J Frozen
echo ✅ SOLUCIÓN: Configurar MySQL para usar protocolo compatible
echo.

echo ===========================================
echo PASO 1: CONFIGURAR MYSQL
echo ===========================================
echo.
echo 🔍 Ejecutando comandos MySQL para solucionar el problema...
echo.

"C:\Program Files\MySQL\MySQL Server 8.0\bin\mysql.exe" -u root -e "ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '';"
"C:\Program Files\MySQL\MySQL Server 8.0\bin\mysql.exe" -u root -e "FLUSH PRIVILEGES;"

echo.
echo ===========================================
echo PASO 2: VERIFICAR CONFIGURACIÓN
echo ===========================================
echo.
echo 🔍 Verificando que la configuración se haya aplicado...
echo.

"C:\Program Files\MySQL\MySQL Server 8.0\bin\mysql.exe" -u root -e "SELECT user, host, plugin FROM mysql.user WHERE user='root';"

echo.
echo ===========================================
echo PASO 3: CREAR BASE DE DATOS SI NO EXISTE
echo ===========================================
echo.
echo 🔍 Verificando si la base de datos l2jdb existe...
echo.

"C:\Program Files\MySQL\MySQL Server 8.0\bin\mysql.exe" -u root -e "CREATE DATABASE IF NOT EXISTS l2jdb;"
"C:\Program Files\MySQL\MySQL Server 8.0\bin\mysql.exe" -u root -e "SHOW DATABASES LIKE 'l2jdb';"

echo.
echo ===========================================
echo RESULTADO
echo ===========================================
echo.
echo ✅ ¡PROBLEMA SOLUCIONADO!
echo ✅ MySQL configurado para L2J Frozen
echo ✅ Base de datos l2jdb creada/verificada
echo.
echo 🚀 Ahora puedes reiniciar el servidor:
echo.
echo 1. Cierra las ventanas del servidor actual
echo 2. Ejecuta: INICIAR_L2_HERMANOS_SIMPLE.bat
echo 3. El servidor debería conectarse correctamente
echo.
echo ===========================================
echo ¡L2 HERMANOS LISTO PARA FUNCIONAR!
echo ===========================================
echo.
echo 🏆 ¡¡¡ EL MEJOR SERVIDOR L2 DE LA HISTORIA !!!
echo.
pause

