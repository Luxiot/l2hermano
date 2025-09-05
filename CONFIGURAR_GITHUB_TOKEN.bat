@echo off
echo ===========================================
echo L2 HERMANOS - CONFIGURAR GITHUB TOKEN
echo ===========================================
echo.
echo 🔑 Configurando token de GitHub para subir archivos...
echo.

echo ===========================================
echo PASO 1: CREAR TOKEN EN GITHUB
echo ===========================================
echo.
echo 📋 INSTRUCCIONES PARA CREAR TOKEN:
echo.
echo 1️⃣ Ve a: https://github.com/settings/tokens
echo 2️⃣ Haz clic en "Generate new token"
echo 3️⃣ Selecciona "Generate new token (classic)"
echo 4️⃣ Configuración:
echo    - Note: L2 Hermanos Token
echo    - Expiration: 90 days
echo    - Scopes: Selecciona "repo" (acceso completo)
echo 5️⃣ Haz clic en "Generate token"
echo 6️⃣ COPIA EL TOKEN (no lo pierdas)
echo.
echo ⚠️ IMPORTANTE: El token solo se muestra una vez
echo.

echo ===========================================
echo PASO 2: CONFIGURAR GIT CON TOKEN
echo ===========================================
echo.
echo 🔧 Configurando Git con tu token...

REM Configurar usuario
git config --global user.name "Luxiot"
git config --global user.email "luxio@l2hermanos.com"

echo ✅ Usuario configurado

echo.
echo ===========================================
echo PASO 3: CONFIGURAR URL CON TOKEN
echo ===========================================
echo.
echo 🔑 Ahora necesitas configurar la URL con tu token:
echo.
echo 📋 COMANDO A EJECUTAR:
echo git remote set-url origin https://TU_TOKEN@github.com/Luxiot/l2hermano.git
echo.
echo ⚠️ Reemplaza TU_TOKEN con el token que copiaste
echo.

echo ===========================================
echo PASO 4: SUBIR ARCHIVOS
echo ===========================================
echo.
echo 🚀 Después de configurar el token, ejecuta:
echo.
echo git add .
echo git commit -m "L2 Hermanos - Servidor épico"
echo git push -u origin main
echo.

echo ===========================================
echo ALTERNATIVA: USAR GITHUB DESKTOP
echo ===========================================
echo.
echo 🖥️ Si prefieres interfaz gráfica:
echo.
echo 1️⃣ Descarga GitHub Desktop
echo 2️⃣ Inicia sesión con tu cuenta
echo 3️⃣ Clona el repositorio: Luxiot/l2hermano
echo 4️⃣ Copia los archivos del servidor
echo 5️⃣ Haz commit y push
echo.

echo ===========================================
echo ¡L2 HERMANOS LISTO PARA GITHUB!
echo ===========================================
echo.
echo 🏆 ¡¡¡ EL MEJOR SERVIDOR L2 DE LA HISTORIA !!!
echo.
echo 📋 REPOSITORIO: https://github.com/Luxiot/l2hermano.git
echo.
echo 📋 PRÓXIMOS PASOS:
echo 1. Crear token en GitHub
echo 2. Configurar Git con token
echo 3. Subir archivos
echo 4. Conectar con Render
echo 5. ¡Disfrutar del servidor en la web!
echo.
pause
