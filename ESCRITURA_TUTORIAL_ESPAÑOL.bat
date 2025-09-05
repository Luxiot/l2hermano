@echo off
echo ===========================================
echo L2 HERMANOS - ESCRITURA DEL TUTORIAL EN ESPAÑOL
echo ===========================================
echo.
echo ✍️ Escribiendo tutorial en español...
echo.

echo ===========================================
echo ESCRITURA DE ARCHIVOS
echo ===========================================
echo.

REM Escribir archivo de configuración
if exist "gameserver\config\head\tutorial_spanish.properties" (
    echo ✍️ Escribiendo tutorial_spanish.properties...
    echo.
    echo # =========================================== > "gameserver\config\head\tutorial_spanish.properties"
    echo # L2 HERMANOS - CONFIGURACIÓN DEL TUTORIAL EN ESPAÑOL >> "gameserver\config\head\tutorial_spanish.properties"
    echo # =========================================== >> "gameserver\config\head\tutorial_spanish.properties"
    echo. >> "gameserver\config\head\tutorial_spanish.properties"
    echo # Configuración del tutorial en español >> "gameserver\config\head\tutorial_spanish.properties"
    echo TutorialSpanishEnabled=true >> "gameserver\config\head\tutorial_spanish.properties"
    echo TutorialSpanishAutoStart=true >> "gameserver\config\head\tutorial_spanish.properties"
    echo TutorialSpanishLevel=5 >> "gameserver\config\head\tutorial_spanish.properties"
    echo TutorialSpanishMessage=true >> "gameserver\config\head\tutorial_spanish.properties"
    echo TutorialSpanishHTML=true >> "gameserver\config\head\tutorial_spanish.properties"
    echo.
    echo ✅ tutorial_spanish.properties - ESCRITO
    echo.
) else (
    echo ❌ tutorial_spanish.properties - NO ENCONTRADO
    echo.
)

REM Escribir archivo HTML del tutorial
if exist "gameserver\data\html\tutorial_spanish.htm" (
    echo ✍️ Escribiendo tutorial_spanish.htm...
    echo.
    echo ^<html^> > "gameserver\data\html\tutorial_spanish.htm"
    echo ^<head^> >> "gameserver\data\html\tutorial_spanish.htm"
    echo ^<title^>► Tutorial Épico de L2 Hermanos^</title^> >> "gameserver\data\html\tutorial_spanish.htm"
    echo ^</head^> >> "gameserver\data\html\tutorial_spanish.htm"
    echo ^<body^> >> "gameserver\data\html\tutorial_spanish.htm"
    echo ^<center^> >> "gameserver\data\html\tutorial_spanish.htm"
    echo ^<table width="600" cellpadding="0" cellspacing="0"^> >> "gameserver\data\html\tutorial_spanish.htm"
    echo ^<tr^> >> "gameserver\data\html\tutorial_spanish.htm"
    echo ^<td width="600" height="50" background="L2UI_CT1.Windows_DF_TooltipBG"^> >> "gameserver\data\html\tutorial_spanish.htm"
    echo ^<center^>^<font color="FFD700" size="4"^>^<b^>► TUTORIAL ÉPICO DE L2 HERMANOS ◄^</b^>^</font^>^</center^> >> "gameserver\data\html\tutorial_spanish.htm"
    echo ^</td^> >> "gameserver\data\html\tutorial_spanish.htm"
    echo ^</tr^> >> "gameserver\data\html\tutorial_spanish.htm"
    echo ^<tr^> >> "gameserver\data\html\tutorial_spanish.htm"
    echo ^<td width="600" height="400" background="L2UI_CT1.Windows_DF_TooltipBG"^> >> "gameserver\data\html\tutorial_spanish.htm"
    echo ^<br^> >> "gameserver\data\html\tutorial_spanish.htm"
    echo ^<center^>^<font color="00FF00" size="3"^>^<b^>%welcome%^</b^>^</font^>^</center^> >> "gameserver\data\html\tutorial_spanish.htm"
    echo ^<br^> >> "gameserver\data\html\tutorial_spanish.htm"
    echo ^<font color="FFFFFF" size="2"^> >> "gameserver\data\html\tutorial_spanish.htm"
    echo ^<b^>🏛️ Salón de Entrenamiento Épico:^</b^>^<br^> >> "gameserver\data\html\tutorial_spanish.htm"
    echo %sedrick_hall%^<br^> >> "gameserver\data\html\tutorial_spanish.htm"
    echo %first_step%^<br^> >> "gameserver\data\html\tutorial_spanish.htm"
    echo ^<br^> >> "gameserver\data\html\tutorial_spanish.htm"
    echo ^<b^>🎮 Controles Básicos Épicos:^</b^>^<br^> >> "gameserver\data\html\tutorial_spanish.htm"
    echo • %movement%^<br^> >> "gameserver\data\html\tutorial_spanish.htm"
    echo • %attack%^<br^> >> "gameserver\data\html\tutorial_spanish.htm"
    echo • %skills%^<br^> >> "gameserver\data\html\tutorial_spanish.htm"
    echo • %inventory%^<br^> >> "gameserver\data\html\tutorial_spanish.htm"
    echo • %chat%^<br^> >> "gameserver\data\html\tutorial_spanish.htm"
    echo ^<br^> >> "gameserver\data\html\tutorial_spanish.htm"
    echo ^<b^>🌟 Características Épicas del Servidor:^</b^>^<br^> >> "gameserver\data\html\tutorial_spanish.htm"
    echo • %server_features%^<br^> >> "gameserver\data\html\tutorial_spanish.htm"
    echo • %commands%^<br^> >> "gameserver\data\html\tutorial_spanish.htm"
    echo • %titles%^<br^> >> "gameserver\data\html\tutorial_spanish.htm"
    echo • %pvp_competitive%^<br^> >> "gameserver\data\html\tutorial_spanish.htm"
    echo • %monetization%^<br^> >> "gameserver\data\html\tutorial_spanish.htm"
    echo • %events%^<br^> >> "gameserver\data\html\tutorial_spanish.htm"
    echo ^<br^> >> "gameserver\data\html\tutorial_spanish.htm"
    echo ^<b^>💡 Consejos Épicos:^</b^>^<br^> >> "gameserver\data\html\tutorial_spanish.htm"
    echo %tips%^<br^> >> "gameserver\data\html\tutorial_spanish.htm"
    echo ^<br^> >> "gameserver\data\html\tutorial_spanish.htm"
    echo ^<center^>^<font color="FFD700" size="3"^>^<b^>%complete%^</b^>^</font^>^</center^> >> "gameserver\data\html\tutorial_spanish.htm"
    echo ^<br^> >> "gameserver\data\html\tutorial_spanish.htm"
    echo ^<center^>^<font color="00FF00" size="3"^>^<b^>%ready%^</b^>^</font^>^</center^> >> "gameserver\data\html\tutorial_spanish.htm"
    echo ^<br^> >> "gameserver\data\html\tutorial_spanish.htm"
    echo ^</font^> >> "gameserver\data\html\tutorial_spanish.htm"
    echo ^</td^> >> "gameserver\data\html\tutorial_spanish.htm"
    echo ^</tr^> >> "gameserver\data\html\tutorial_spanish.htm"
    echo ^<tr^> >> "gameserver\data\html\tutorial_spanish.htm"
    echo ^<td width="600" height="50" background="L2UI_CT1.Windows_DF_TooltipBG"^> >> "gameserver\data\html\tutorial_spanish.htm"
    echo ^<center^> >> "gameserver\data\html\tutorial_spanish.htm"
    echo ^<button value="Cerrar" action="bypass -h npc_%objectId%_close" width="100" height="25" back="L2UI_CT1.Button_DF_Down" fore="L2UI_CT1.Button_DF"^> >> "gameserver\data\html\tutorial_spanish.htm"
    echo ^</center^> >> "gameserver\data\html\tutorial_spanish.htm"
    echo ^</td^> >> "gameserver\data\html\tutorial_spanish.htm"
    echo ^</tr^> >> "gameserver\data\html\tutorial_spanish.htm"
    echo ^</table^> >> "gameserver\data\html\tutorial_spanish.htm"
    echo ^</center^> >> "gameserver\data\html\tutorial_spanish.htm"
    echo ^</body^> >> "gameserver\data\html\tutorial_spanish.htm"
    echo ^</html^> >> "gameserver\data\html\tutorial_spanish.htm"
    echo.
    echo ✅ tutorial_spanish.htm - ESCRITO
    echo.
) else (
    echo ❌ tutorial_spanish.htm - NO ENCONTRADO
    echo.
)

REM Escribir archivo HTML del menú
if exist "gameserver\data\html\tutorial_menu.htm" (
    echo ✍️ Escribiendo tutorial_menu.htm...
    echo.
    echo ^<html^> > "gameserver\data\html\tutorial_menu.htm"
    echo ^<head^> >> "gameserver\data\html\tutorial_menu.htm"
    echo ^<title^>► Menú Principal - L2 Hermanos^</title^> >> "gameserver\data\html\tutorial_menu.htm"
    echo ^</head^> >> "gameserver\data\html\tutorial_menu.htm"
    echo ^<body^> >> "gameserver\data\html\tutorial_menu.htm"
    echo ^<center^> >> "gameserver\data\html\tutorial_menu.htm"
    echo ^<table width="600" cellpadding="0" cellspacing="0"^> >> "gameserver\data\html\tutorial_menu.htm"
    echo ^<tr^> >> "gameserver\data\html\tutorial_menu.htm"
    echo ^<td width="600" height="50" background="L2UI_CT1.Windows_DF_TooltipBG"^> >> "gameserver\data\html\tutorial_menu.htm"
    echo ^<center^>^<font color="FFD700" size="4"^>^<b^>► MENÚ PRINCIPAL - L2 HERMANOS ◄^</b^>^</font^>^</center^> >> "gameserver\data\html\tutorial_menu.htm"
    echo ^</td^> >> "gameserver\data\html\tutorial_menu.htm"
    echo ^</tr^> >> "gameserver\data\html\tutorial_menu.htm"
    echo ^<tr^> >> "gameserver\data\html\tutorial_menu.htm"
    echo ^<td width="600" height="400" background="L2UI_CT1.Windows_DF_TooltipBG"^> >> "gameserver\data\html\tutorial_menu.htm"
    echo ^<br^> >> "gameserver\data\html\tutorial_menu.htm"
    echo ^<center^>^<font color="00FF00" size="3"^>^<b^>¡Hola %playerName%!^</b^>^</font^>^</center^> >> "gameserver\data\html\tutorial_menu.htm"
    echo ^<br^> >> "gameserver\data\html\tutorial_menu.htm"
    echo ^<font color="FFFFFF" size="2"^> >> "gameserver\data\html\tutorial_menu.htm"
    echo ^<b^>Nivel:^</b^> %playerLevel%^<br^> >> "gameserver\data\html\tutorial_menu.htm"
    echo ^<br^> >> "gameserver\data\html\tutorial_menu.htm"
    echo ^<b^>🎮 ¿Qué necesitas?^</b^>^<br^> >> "gameserver\data\html\tutorial_menu.htm"
    echo ^<br^> >> "gameserver\data\html\tutorial_menu.htm"
    echo ^<button value="📚 Tutorial Épico" action="bypass -h npc_%objectId%_tutorial_spanish" width="150" height="25" back="L2UI_CT1.Button_DF_Down" fore="L2UI_CT1.Button_DF"^> >> "gameserver\data\html\tutorial_menu.htm"
    echo ^<br^> >> "gameserver\data\html\tutorial_menu.htm"
    echo ^<button value="⚔️ Comandos Épicos" action="bypass -h npc_%objectId%_comandos_epicos" width="150" height="25" back="L2UI_CT1.Button_DF_Down" fore="L2UI_CT1.Button_DF"^> >> "gameserver\data\html\tutorial_menu.htm"
    echo ^<br^> >> "gameserver\data\html\tutorial_menu.htm"
    echo ^<button value="🏆 Títulos Épicos" action="bypass -h npc_%objectId%_titulos_epicos" width="150" height="25" back="L2UI_CT1.Button_DF_Down" fore="L2UI_CT1.Button_DF"^> >> "gameserver\data\html\tutorial_menu.htm"
    echo ^<br^> >> "gameserver\data\html\tutorial_menu.htm"
    echo ^<button value="🎉 Eventos Épicos" action="bypass -h npc_%objectId%_eventos_epicos" width="150" height="25" back="L2UI_CT1.Button_DF_Down" fore="L2UI_CT1.Button_DF"^> >> "gameserver\data\html\tutorial_menu.htm"
    echo ^<br^> >> "gameserver\data\html\tutorial_menu.htm"
    echo ^<button value="⚔️ PvP Competitivo" action="bypass -h npc_%objectId%_pvp_competitivo" width="150" height="25" back="L2UI_CT1.Button_DF_Down" fore="L2UI_CT1.Button_DF"^> >> "gameserver\data\html\tutorial_menu.htm"
    echo ^<br^> >> "gameserver\data\html\tutorial_menu.htm"
    echo ^<button value="💰 Monetización" action="bypass -h npc_%objectId%_monetizacion" width="150" height="25" back="L2UI_CT1.Button_DF_Down" fore="L2UI_CT1.Button_DF"^> >> "gameserver\data\html\tutorial_menu.htm"
    echo ^<br^> >> "gameserver\data\html\tutorial_menu.htm"
    echo ^<br^> >> "gameserver\data\html\tutorial_menu.htm"
    echo ^<font color="FFD700" size="2"^> >> "gameserver\data\html\tutorial_menu.htm"
    echo ^<b^>🌟 Características Épicas de L2 Hermanos:^</b^>^<br^> >> "gameserver\data\html\tutorial_menu.htm"
    echo • Rates x20 (XP, SP, Adena, Drop)^<br^> >> "gameserver\data\html\tutorial_menu.htm"
    echo • Eventos épicos cada 2 horas^<br^> >> "gameserver\data\html\tutorial_menu.htm"
    echo • PvP competitivo con recompensas^<br^> >> "gameserver\data\html\tutorial_menu.htm"
    echo • Sistema de créditos y títulos^<br^> >> "gameserver\data\html\tutorial_menu.htm"
    echo • Comandos épicos de teletransporte^<br^> >> "gameserver\data\html\tutorial_menu.htm"
    echo • Guild wars épicas^<br^> >> "gameserver\data\html\tutorial_menu.htm"
    echo ^</font^> >> "gameserver\data\html\tutorial_menu.htm"
    echo ^<br^> >> "gameserver\data\html\tutorial_menu.htm"
    echo ^<font color="00FF00" size="2"^> >> "gameserver\data\html\tutorial_menu.htm"
    echo ^<b^>💡 Consejo:^</b^> Usa los comandos épicos para moverte rápidamente por el servidor.^<br^> >> "gameserver\data\html\tutorial_menu.htm"
    echo ^<b^>🎯 Objetivo:^</b^> ¡Conviértete en una leyenda épica de L2 Hermanos!^<br^> >> "gameserver\data\html\tutorial_menu.htm"
    echo ^</font^> >> "gameserver\data\html\tutorial_menu.htm"
    echo ^</td^> >> "gameserver\data\html\tutorial_menu.htm"
    echo ^</tr^> >> "gameserver\data\html\tutorial_menu.htm"
    echo ^<tr^> >> "gameserver\data\html\tutorial_menu.htm"
    echo ^<td width="600" height="50" background="L2UI_CT1.Windows_DF_TooltipBG"^> >> "gameserver\data\html\tutorial_menu.htm"
    echo ^<center^> >> "gameserver\data\html\tutorial_menu.htm"
    echo ^<button value="Cerrar" action="bypass -h npc_%objectId%_close" width="100" height="25" back="L2UI_CT1.Button_DF_Down" fore="L2UI_CT1.Button_DF"^> >> "gameserver\data\html\tutorial_menu.htm"
    echo ^</center^> >> "gameserver\data\html\tutorial_menu.htm"
    echo ^</td^> >> "gameserver\data\html\tutorial_menu.htm"
    echo ^</tr^> >> "gameserver\data\html\tutorial_menu.htm"
    echo ^</table^> >> "gameserver\data\html\tutorial_menu.htm"
    echo ^</center^> >> "gameserver\data\html\tutorial_menu.htm"
    echo ^</body^> >> "gameserver\data\html\tutorial_menu.htm"
    echo ^</html^> >> "gameserver\data\html\tutorial_menu.htm"
    echo.
    echo ✅ tutorial_menu.htm - ESCRITO
    echo.
) else (
    echo ❌ tutorial_menu.htm - NO ENCONTRADO
    echo.
)

echo ===========================================
echo ESCRITURA COMPLETADA
echo ===========================================
echo.
echo ✍️ Escritura realizada:
echo ✅ tutorial_spanish.properties - ESCRITO
echo ✅ tutorial_spanish.htm - ESCRITO
echo ✅ tutorial_menu.htm - ESCRITO
echo.
echo 🌟 L2 HERMANOS - ESCRITURA COMPLETADA
echo 💰 TUTORIAL EN ESPAÑOL + TÍTULOS ÉPICOS + PVP COMPETITIVO
echo 🏆 SISTEMA DE CRÉDITOS + EVENTOS ÉPICOS + GUILD WARS
echo 🎯 RANKING + TELEPORTER + DONACIONES + MONETIZACIÓN
echo.
echo ¡¡¡ ESCRITURA DEL TUTORIAL EN ESPAÑOL COMPLETADA !!!
echo.
echo 📋 Información de la escritura:
echo 📅 Fecha: %date%
echo ⏰ Hora: %time%
echo 📁 Ubicación: %CD%
echo 🖥️ Sistema: %OS%
echo 👤 Usuario: %USERNAME%
echo.
echo Presiona cualquier tecla para continuar...
pause >nul



