@echo off
echo ===========================================
echo L2 HERMANOS - SUBIR COMPLETO A GITHUB
echo ===========================================
echo.
echo 🌐 Subiendo L2 Hermanos completo a GitHub...
echo.

echo ===========================================
echo PASO 1: VERIFICAR CONFIGURACIÓN
echo ===========================================
echo.
echo 🔧 Verificando configuración de Git...

git config --global user.name "Luxiot"
git config --global user.email "luxioage@gmail.com"

echo ✅ Configuración verificada

echo.
echo ===========================================
echo PASO 2: CONFIGURAR REPOSITORIO REMOTO
echo ===========================================
echo.
echo 🔗 Configurando repositorio remoto...

git remote remove origin
git remote add origin https://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@github.com/Luxiot/l2hermano.git

echo ✅ Repositorio remoto configurado

echo.
echo ===========================================
echo PASO 3: AGREGAR TODOS LOS ARCHIVOS
echo ===========================================
echo.
echo 📁 Agregando todos los archivos...

git add .
git add -A

echo ✅ Archivos agregados

echo.
echo ===========================================
echo PASO 4: HACER COMMIT
echo ===========================================
echo.
echo 💾 Haciendo commit...

git commit -m "L2 Hermanos - Servidor épico completo con tutorial en español"

echo ✅ Commit realizado

echo.
echo ===========================================
echo PASO 5: SUBIR A GITHUB
echo ===========================================
echo.
echo 🚀 Subiendo a GitHub...

git branch -M main
git push -u origin main

echo ✅ Archivos subidos a GitHub

echo.
echo ===========================================
echo PASO 6: VERIFICAR SUBIDA
echo ===========================================
echo.
echo 🔍 Verificando subida...

git status
git log --oneline -3

echo ✅ Verificación completada

echo.
echo ===========================================
echo ¡L2 HERMANOS SUBIDO EXITOSAMENTE!
echo ===========================================
echo.
echo 🏆 ¡¡¡ EL MEJOR SERVIDOR L2 DE LA HISTORIA !!!
echo.
echo 📋 REPOSITORIO: https://github.com/Luxiot/l2hermano.git
echo.
echo 📋 ARCHIVOS SUBIDOS:
echo ✅ loginserver/ - Servidor de login
echo ✅ gameserver/ - Servidor de juego
echo ✅ sql/ - Base de datos
echo ✅ cliente_espanol/ - Cliente en español
echo ✅ render.yaml - Configuración para Render
echo ✅ Dockerfile - Contenedor Docker
echo ✅ Todas las guías y documentación
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
