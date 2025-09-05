@echo off
echo ===========================================
echo L2 HERMANOS - SUBIR A GITHUB
echo ===========================================
echo.
echo 🌐 Subiendo L2 Hermanos a GitHub...
echo.

echo ===========================================
echo PASO 1: CONFIGURAR GIT
echo ===========================================
echo.
echo 🔧 Configurando Git para tu repositorio...

REM Configurar el repositorio remoto
git remote add origin https://github.com/Luxiot/l2hermano.git

echo ✅ Repositorio remoto configurado

echo.
echo ===========================================
echo PASO 2: AGREGAR ARCHIVOS
echo ===========================================
echo.
echo 📁 Agregando archivos al repositorio...

git add .

echo ✅ Archivos agregados

echo.
echo ===========================================
echo PASO 3: HACER COMMIT
echo ===========================================
echo.
echo 💾 Haciendo commit de los archivos...

git commit -m "L2 Hermanos - Servidor épico listo para Render"

echo ✅ Commit realizado

echo.
echo ===========================================
echo PASO 4: SUBIR A GITHUB
echo ===========================================
echo.
echo 🚀 Subiendo archivos a GitHub...

git branch -M main
git push -u origin main

echo ✅ Archivos subidos a GitHub

echo.
echo ===========================================
echo ¡L2 HERMANOS SUBIDO A GITHUB!
echo ===========================================
echo.
echo 🏆 ¡¡¡ EL MEJOR SERVIDOR L2 DE LA HISTORIA !!!
echo.
echo 📋 REPOSITORIO CREADO:
echo https://github.com/Luxiot/l2hermano.git
echo.
echo 📋 PRÓXIMOS PASOS EN RENDER:
echo 1. Ve a Render.com
echo 2. Crea nuevo Web Service
echo 3. Conecta con GitHub
echo 4. Selecciona: Luxiot/l2hermano
echo 5. Configura con Docker
echo 6. ¡Disfruta tu servidor en la web!
echo.
echo 🌟 CARACTERÍSTICAS DEL SERVIDOR:
echo - Rates: x20 XP/SP, x12 Drop, x15 Spoil
echo - PvP: Habilitado en todas las zonas
echo - Tutorial: En español
echo - Comandos: .tutorial, .titulos, .pvp
echo - Admin: Luxio (Nivel 5 - Owner)
echo.
pause
