@echo off
echo ===========================================
echo L2 HERMANOS - COMANDOS PARA GITHUB
echo ===========================================
echo.
echo 🚀 Subiendo L2 Hermanos a GitHub con comandos...
echo.

echo ===========================================
echo PASO 1: CONFIGURAR GIT
echo ===========================================
echo.
echo 🔧 Configurando Git...

git config --global user.name "Luxiot"
git config --global user.email "luxioage@gmail.com"

echo ✅ Git configurado

echo.
echo ===========================================
echo PASO 2: INICIALIZAR REPOSITORIO
echo ===========================================
echo.
echo 🔧 Inicializando repositorio...

git init

echo ✅ Repositorio inicializado

echo.
echo ===========================================
echo PASO 3: CONFIGURAR REPOSITORIO REMOTO
echo ===========================================
echo.
echo 🔗 Configurando repositorio remoto...

git remote add origin https://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@github.com/Luxiot/l2hermano.git

echo ✅ Repositorio remoto configurado

echo.
echo ===========================================
echo PASO 4: AGREGAR ARCHIVOS
echo ===========================================
echo.
echo 📁 Agregando archivos...

git add .

echo ✅ Archivos agregados

echo.
echo ===========================================
echo PASO 5: HACER COMMIT
echo ===========================================
echo.
echo 💾 Haciendo commit...

git commit -m "L2 Hermanos - Servidor épico completo con tutorial en español"

echo ✅ Commit realizado

echo.
echo ===========================================
echo PASO 6: SUBIR A GITHUB
echo ===========================================
echo.
echo 🚀 Subiendo a GitHub...

git branch -M main
git push -u origin main

echo ✅ Archivos subidos a GitHub

echo.
echo ===========================================
echo PASO 7: VERIFICAR SUBIDA
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
echo 📋 PRÓXIMOS PASOS EN RENDER:
echo 1. Ve a Render.com
echo 2. Crea nuevo Web Service
echo 3. Conecta con GitHub
echo 4. Selecciona: Luxiot/l2hermano
echo 5. Configura con Docker
echo 6. ¡Disfruta tu servidor en la web!
echo.
pause
