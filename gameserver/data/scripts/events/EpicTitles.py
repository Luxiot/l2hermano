# ===========================================
# SISTEMA DE TÍTULOS ÉPICOS - L2 HERMANOS
# ===========================================
# Sistema de títulos épicos personalizados
# Epic titles system

import sys
from java.util import Calendar
from l2jfrozen.gameserver.model.quest import State
from l2jfrozen.gameserver.model.quest import QuestState
from l2jfrozen.gameserver.model.quest import Quest as JQuest
from l2jfrozen.gameserver.model.actor.instance import L2PcInstance
from l2jfrozen.gameserver.network.serverpackets import NpcHtmlMessage
from l2jfrozen.gameserver.network.serverpackets import SystemMessage
from l2jfrozen.gameserver.network.serverpackets import CreatureSay
from l2jfrozen.gameserver.GameServer import GameServer

class EpicTitles(JQuest):
    def __init__(self, id, name, descr):
        JQuest.__init__(self, id, name, descr)
        self.epicTitles = {
            "PVP": {
                "name": "Títulos PvP Épicos",
                "titles": [
                    {"id": "REY_PVP", "name": "Rey del PvP", "description": "El mejor en combate PvP", "color": "FFD700", "cost": 50000},
                    {"id": "PRINCIPE_PVP", "name": "Príncipe del PvP", "description": "El segundo mejor en PvP", "color": "C0C0C0", "cost": 40000},
                    {"id": "DUQUE_PVP", "name": "Duque del PvP", "description": "El tercer mejor en PvP", "color": "CD7F32", "cost": 30000},
                    {"id": "CABALLERO_PVP", "name": "Caballero del PvP", "description": "Top 5 en PvP", "color": "FF69B4", "cost": 20000},
                    {"id": "GUERRERO_PVP", "name": "Guerrero del PvP", "description": "Top 10 en PvP", "color": "FF4500", "cost": 10000},
                    {"id": "SOLDADO_PVP", "name": "Soldado del PvP", "description": "Top 20 en PvP", "color": "32CD32", "cost": 5000},
                    {"id": "NOVATO_PVP", "name": "Novato del PvP", "description": "Top 50 en PvP", "color": "87CEEB", "cost": 1000}
                ]
            },
            "COLISEO": {
                "name": "Títulos del Coliseo",
                "titles": [
                    {"id": "REY_COLISEO", "name": "Rey del Coliseo", "description": "Ganador del evento Rey del Coliseo", "color": "FFD700", "cost": 0},
                    {"id": "PRINCIPE_COLISEO", "name": "Príncipe del Coliseo", "description": "Segundo lugar en el Coliseo", "color": "C0C0C0", "cost": 0},
                    {"id": "DUQUE_COLISEO", "name": "Duque del Coliseo", "description": "Tercer lugar en el Coliseo", "color": "CD7F32", "cost": 0},
                    {"id": "GLADIADOR", "name": "Gladiador", "description": "Participante en el Coliseo", "color": "FF6347", "cost": 0}
                ]
            },
            "EVENTOS": {
                "name": "Títulos de Eventos",
                "titles": [
                    {"id": "MAESTRO_EVENTOS", "name": "Maestro de Eventos", "description": "Participa en 25 eventos épicos", "color": "FF1493", "cost": 0},
                    {"id": "CAMPEON_EVENTOS", "name": "Campeón de Eventos", "description": "Gana 10 eventos épicos", "color": "00CED1", "cost": 0},
                    {"id": "LEGENDARIO_EVENTOS", "name": "Legendario de Eventos", "description": "Gana 50 eventos épicos", "color": "FF8C00", "cost": 0}
                ]
            },
            "BOSSES": {
                "name": "Títulos de Bosses",
                "titles": [
                    {"id": "ASESINO_BOSSES", "name": "Asesino de Bosses", "description": "Mata 50 bosses épicos", "color": "8B0000", "cost": 0},
                    {"id": "CAZADOR_BOSSES", "name": "Cazador de Bosses", "description": "Mata 100 bosses épicos", "color": "2F4F4F", "cost": 0},
                    {"id": "EXTERMINADOR_BOSSES", "name": "Exterminador de Bosses", "description": "Mata 500 bosses épicos", "color": "4B0082", "cost": 0}
                ]
            },
            "NIVEL": {
                "name": "Títulos de Nivel",
                "titles": [
                    {"id": "NOVATO", "name": "Novato", "description": "Nivel 1-20", "color": "87CEEB", "cost": 0},
                    {"id": "APRENDIZ", "name": "Aprendiz", "description": "Nivel 21-40", "color": "32CD32", "cost": 0},
                    {"id": "GUERRERO", "name": "Guerrero", "description": "Nivel 41-60", "color": "FF4500", "cost": 0},
                    {"id": "MAESTRO", "name": "Maestro", "description": "Nivel 61-75", "color": "FF69B4", "cost": 0},
                    {"id": "LEGENDARIO", "name": "Legendario", "description": "Nivel 76-80", "color": "FFD700", "cost": 0}
                ]
            },
            "ESPECIALES": {
                "name": "Títulos Especiales",
                "titles": [
                    {"id": "FUNDADOR", "name": "Fundador de L2 Hermanos", "description": "Jugador fundador del servidor", "color": "FF0000", "cost": 0},
                    {"id": "VIP", "name": "VIP Épico", "description": "Miembro VIP del servidor", "color": "FFD700", "cost": 0},
                    {"id": "DONADOR", "name": "Donador Épico", "description": "Donador del servidor", "color": "00FF00", "cost": 0},
                    {"id": "GM", "name": "Game Master", "description": "Game Master del servidor", "color": "0000FF", "cost": 0}
                ]
            }
        }
        
    def onAdvEvent(self, event, npc, player):
        if event == "mostrar_titulos":
            return self.mostrarTitulos(player)
        elif event.startswith("categoria_"):
            categoria = event.replace("categoria_", "")
            return self.mostrarCategoriaTitulos(player, categoria)
        elif event.startswith("equipar_titulo_"):
            tituloId = event.replace("equipar_titulo_", "")
            return self.equiparTitulo(player, tituloId)
        elif event == "ver_mi_titulo":
            return self.verMiTitulo(player)
        elif event == "ver_titulos_disponibles":
            return self.verTitulosDisponibles(player)
        return None
    
    def mostrarTitulos(self, player):
        html = "<html><body>"
        html += "<center><font color=\"LEVEL\">¡¡¡ SISTEMA DE TÍTULOS ÉPICOS DE L2 HERMANOS !!!</font></center><br>"
        html += "<center><font color=\"LEVEL\">¡¡¡ EPIC TITLES SYSTEM OF L2 HERMANOS !!!</font></center><br><br>"
        
        # Mostrar título actual del jugador
        currentTitle = player.getTitle()
        html += "<font color=\"LEVEL\">🏆 TU TÍTULO ACTUAL / YOUR CURRENT TITLE:</font><br>"
        html += "<font color=\"YELLOW\">" + (currentTitle if currentTitle else "Sin título / No title") + "</font><br><br>"
        
        html += "<font color=\"LEVEL\">📋 CATEGORÍAS DE TÍTULOS / TITLE CATEGORIES:</font><br><br>"
        
        for categoriaKey, categoriaInfo in self.epicTitles.items():
            html += "<font color=\"LEVEL\">" + categoriaInfo["name"] + "</font><br>"
            html += "<font color=\"WHITE\">" + str(len(categoriaInfo["titles"])) + " títulos disponibles</font><br>"
            html += "<font color=\"WHITE\">" + str(len(categoriaInfo["titles"])) + " titles available</font><br>"
            html += "<button value=\"Ver " + categoriaInfo["name"] + "\" action=\"bypass -h Quest EpicTitles categoria_" + categoriaKey + "\" width=200 height=25 back=\"L2UI_ct1.button_df\" fore=\"L2UI_ct1.button_df\"><br><br>"
        
        html += "<font color=\"LEVEL\">🎯 ACCIONES DISPONIBLES / AVAILABLE ACTIONS:</font><br>"
        html += "<button value=\"Ver Mi Título\" action=\"bypass -h Quest EpicTitles ver_mi_titulo\" width=200 height=25 back=\"L2UI_ct1.button_df\" fore=\"L2UI_ct1.button_df\"><br>"
        html += "<button value=\"Ver Títulos Disponibles\" action=\"bypass -h Quest EpicTitles ver_titulos_disponibles\" width=200 height=25 back=\"L2UI_ct1.button_df\" fore=\"L2UI_ct1.button_df\"><br>"
        
        html += "<br><font color=\"LEVEL\">💡 CÓMO OBTENER TÍTULOS / HOW TO GET TITLES:</font><br>"
        html += "• PvP: Participa en combates PvP / Participate in PvP battles<br>"
        html += "• Eventos: Participa en eventos épicos / Participate in epic events<br>"
        html += "• Bosses: Mata bosses épicos / Kill epic bosses<br>"
        html += "• Nivel: Alcanza niveles altos / Reach high levels<br>"
        html += "• Especiales: Logros únicos / Unique achievements<br>"
        
        html += "<br><font color=\"LEVEL\">🎨 CARACTERÍSTICAS DE TÍTULOS / TITLE FEATURES:</font><br>"
        html += "• Colores únicos / Unique colors<br>"
        html += "• Efectos visuales / Visual effects<br>"
        html += "• Reconocimiento / Recognition<br>"
        html += "• Prestigio / Prestige<br>"
        
        html += "<br><font color=\"LEVEL\">¡¡¡ CONVIÉRTETE EN UNA LEYENDA CON TÍTULOS ÉPICOS !!!</font><br>"
        html += "<font color=\"LEVEL\">¡¡¡ BECOME A LEGEND WITH EPIC TITLES !!!</font><br>"
        
        html += "</body></html>"
        
        reply = NpcHtmlMessage(1)
        reply.setHtml(html)
        player.sendPacket(reply)
        return None
    
    def mostrarCategoriaTitulos(self, player, categoriaKey):
        if categoriaKey not in self.epicTitles:
            return "Categoría no encontrada."
        
        categoriaInfo = self.epicTitles[categoriaKey]
        
        html = "<html><body>"
        html += "<center><font color=\"LEVEL\">" + categoriaInfo["name"] + "</font></center><br><br>"
        
        html += "<font color=\"LEVEL\">🏆 TÍTULOS DISPONIBLES / AVAILABLE TITLES:</font><br><br>"
        
        for titulo in categoriaInfo["titles"]:
            costText = "GRATIS" if titulo["cost"] == 0 else str(titulo["cost"]) + " Créditos"
            costTextEn = "FREE" if titulo["cost"] == 0 else str(titulo["cost"]) + " Credits"
            
            html += "<font color=\"#" + titulo["color"] + "\">" + titulo["name"] + "</font><br>"
            html += "<font color=\"WHITE\">" + titulo["description"] + "</font><br>"
            html += "<font color=\"YELLOW\">Costo: " + costText + " / Cost: " + costTextEn + "</font><br>"
            html += "<button value=\"Equipar " + titulo["name"] + "\" action=\"bypass -h Quest EpicTitles equipar_titulo_" + titulo["id"] + "\" width=200 height=25 back=\"L2UI_ct1.button_df\" fore=\"L2UI_ct1.button_df\"><br><br>"
        
        html += "<button value=\"Volver a Títulos\" action=\"bypass -h Quest EpicTitles mostrar_titulos\" width=200 height=25 back=\"L2UI_ct1.button_df\" fore=\"L2UI_ct1.button_df\"><br>"
        
        html += "</body></html>"
        
        reply = NpcHtmlMessage(1)
        reply.setHtml(html)
        player.sendPacket(reply)
        return None
    
    def equiparTitulo(self, player, tituloId):
        # Buscar el título en todas las categorías
        tituloInfo = None
        for categoriaInfo in self.epicTitles.values():
            for titulo in categoriaInfo["titles"]:
                if titulo["id"] == tituloId:
                    tituloInfo = titulo
                    break
            if tituloInfo:
                break
        
        if not tituloInfo:
            return "Título no encontrado."
        
        # Verificar si tiene suficientes créditos (si el título tiene costo)
        if tituloInfo["cost"] > 0:
            # Aquí se verificaría el sistema de créditos
            # Por ahora, asumimos que tiene suficientes créditos
            pass
        
        # Equipar el título
        player.setTitle(tituloInfo["name"])
        
        # Mensaje épico
        player.sendMessage("¡¡¡ TÍTULO ÉPICO EQUIPADO !!!")
        player.sendMessage("¡¡¡ EPIC TITLE EQUIPPED !!!")
        player.sendMessage("¡Has equipado el título: " + tituloInfo["name"] + "!")
        player.sendMessage("You have equipped the title: " + tituloInfo["name"] + "!")
        
        # Anuncio épico
        self.announceToAll(player.getName() + " ha equipado el título épico: " + tituloInfo["name"] + "!")
        self.announceToAll(player.getName() + " has equipped the epic title: " + tituloInfo["name"] + "!")
        
        return "¡Título épico equipado: " + tituloInfo["name"] + "!"
    
    def verMiTitulo(self, player):
        currentTitle = player.getTitle()
        
        html = "<html><body>"
        html += "<center><font color=\"LEVEL\">¡¡¡ MI TÍTULO ÉPICO !!!</font></center><br>"
        html += "<center><font color=\"LEVEL\">¡¡¡ MY EPIC TITLE !!!</font></center><br><br>"
        
        html += "<font color=\"LEVEL\">🏆 INFORMACIÓN DE TÍTULO / TITLE INFORMATION:</font><br><br>"
        html += "• Título actual: " + (currentTitle if currentTitle else "Sin título") + " / Current title: " + (currentTitle if currentTitle else "No title") + "<br>"
        html += "• Color: En desarrollo / Color: In development<br>"
        html += "• Efectos: En desarrollo / Effects: In development<br>"
        html += "• Prestigio: En desarrollo / Prestige: In development<br>"
        
        html += "<br><font color=\"LEVEL\">📊 ESTADÍSTICAS DE TÍTULOS / TITLE STATISTICS:</font><br>"
        html += "• Títulos obtenidos: En desarrollo / Titles obtained: In development<br>"
        html += "• Títulos equipados: En desarrollo / Titles equipped: In development<br>"
        html += "• Títulos favoritos: En desarrollo / Favorite titles: In development<br>"
        
        html += "<br><font color=\"LEVEL\">🎯 CÓMO CAMBIAR TÍTULO / HOW TO CHANGE TITLE:</font><br>"
        html += "• Ve a la categoría de títulos / Go to title category<br>"
        html += "• Selecciona el título deseado / Select desired title<br>"
        html += "• Haz clic en \"Equipar\" / Click \"Equip\"<br>"
        html += "• ¡Disfruta tu nuevo título! / Enjoy your new title!<br>"
        
        html += "<br><font color=\"LEVEL\">💡 CONSEJOS PARA TÍTULOS / TITLE TIPS:</font><br>"
        html += "• Participa en PvP para títulos PvP / Participate in PvP for PvP titles<br>"
        html += "• Únete a eventos para títulos de eventos / Join events for event titles<br>"
        html += "• Mata bosses para títulos de bosses / Kill bosses for boss titles<br>"
        html += "• Sube de nivel para títulos de nivel / Level up for level titles<br>"
        
        html += "<br><font color=\"LEVEL\">¡¡¡ MUESTRA TU TÍTULO ÉPICO CON ORGULLO !!!</font><br>"
        html += "<font color=\"LEVEL\">¡¡¡ SHOW YOUR EPIC TITLE WITH PRIDE !!!</font><br>"
        
        html += "</body></html>"
        
        reply = NpcHtmlMessage(1)
        reply.setHtml(html)
        player.sendPacket(reply)
        return None
    
    def verTitulosDisponibles(self, player):
        html = "<html><body>"
        html += "<center><font color=\"LEVEL\">¡¡¡ TÍTULOS DISPONIBLES ÉPICOS !!!</font></center><br>"
        html += "<center><font color=\"LEVEL\">¡¡¡ AVAILABLE EPIC TITLES !!!</font></center><br><br>"
        
        html += "<font color=\"LEVEL\">📋 TODOS LOS TÍTULOS DISPONIBLES / ALL AVAILABLE TITLES:</font><br><br>"
        
        for categoriaKey, categoriaInfo in self.epicTitles.items():
            html += "<font color=\"LEVEL\">" + categoriaInfo["name"] + "</font><br>"
            
            for titulo in categoriaInfo["titles"]:
                costText = "GRATIS" if titulo["cost"] == 0 else str(titulo["cost"]) + " Créditos"
                costTextEn = "FREE" if titulo["cost"] == 0 else str(titulo["cost"]) + " Credits"
                
                html += "<font color=\"#" + titulo["color"] + "\">• " + titulo["name"] + "</font><br>"
                html += "<font color=\"WHITE\">  " + titulo["description"] + "</font><br>"
                html += "<font color=\"YELLOW\">  Costo: " + costText + " / Cost: " + costTextEn + "</font><br><br>"
        
        html += "<font color=\"LEVEL\">🎯 CÓMO OBTENER TÍTULOS / HOW TO GET TITLES:</font><br>"
        html += "• PvP: Participa en combates PvP / Participate in PvP battles<br>"
        html += "• Eventos: Participa en eventos épicos / Participate in epic events<br>"
        html += "• Bosses: Mata bosses épicos / Kill epic bosses<br>"
        html += "• Nivel: Alcanza niveles altos / Reach high levels<br>"
        html += "• Especiales: Logros únicos / Unique achievements<br>"
        
        html += "<br><font color=\"LEVEL\">¡¡¡ CONVIÉRTETE EN UNA LEYENDA CON TÍTULOS ÉPICOS !!!</font><br>"
        html += "<font color=\"LEVEL\">¡¡¡ BECOME A LEGEND WITH EPIC TITLES !!!</font><br>"
        
        html += "</body></html>"
        
        reply = NpcHtmlMessage(1)
        reply.setHtml(html)
        player.sendPacket(reply)
        return None
    
    def announceToAll(self, message):
        from l2jfrozen.gameserver.network.serverpackets import CreatureSay
        from l2jfrozen.gameserver.model.actor.instance import L2PcInstance
        from l2jfrozen.gameserver.GameServer import GameServer
        
        for player in GameServer.getInstance().getAllPlayers():
            if player and player.isOnline():
                player.sendPacket(CreatureSay(0, 1, "TÍTULOS ÉPICOS", message))

# Crear instancia del sistema de títulos épicos
TITULOS_EPICOS = EpicTitles(-1, "TitulosEpicos", "Sistema de Títulos Épicos")

# Registrar el sistema
TITULOS_EPICOS.addStartNpc(30006)  # Tienda GM
TITULOS_EPICOS.addTalkId(30006)



