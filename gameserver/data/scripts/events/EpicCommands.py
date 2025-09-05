# ===========================================
# COMANDOS ÉPICOS - L2 HERMANOS
# ===========================================
# Sistema de comandos épicos personalizados
# Epic custom commands system

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

class EpicCommands(JQuest):
    def __init__(self, id, name, descr):
        JQuest.__init__(self, id, name, descr)
        self.epicCommands = {
            ".farm1": {
                "name": "Farm Épico 1",
                "description": "Teletransporte a la zona de farm épica 1",
                "location": (186000, -10000, -3000),
                "cost": 0
            },
            ".farm2": {
                "name": "Farm Épico 2", 
                "description": "Teletransporte a la zona de farm épica 2",
                "location": (190000, -15000, -3500),
                "cost": 0
            },
            ".pvp1": {
                "name": "PvP Épico 1",
                "description": "Teletransporte a la zona de PvP épica 1",
                "location": (210000, -35000, -5500),
                "cost": 1000
            },
            ".pvp2": {
                "name": "PvP Épico 2",
                "description": "Teletransporte a la zona de PvP épica 2",
                "location": (215000, -40000, -6000),
                "cost": 1000
            },
            ".boss": {
                "name": "Boss Épico",
                "description": "Teletransporte a la zona de bosses épicos",
                "location": (235000, -60000, -8000),
                "cost": 5000
            },
            ".event": {
                "name": "Evento Épico",
                "description": "Teletransporte a la zona de eventos épicos",
                "location": (260000, -85000, -10500),
                "cost": 0
            },
            ".vip": {
                "name": "Zona VIP",
                "description": "Teletransporte a la zona VIP épica",
                "location": (280000, -105000, -12500),
                "cost": 10000
            },
            ".home": {
                "name": "Casa Épica",
                "description": "Teletransporte a tu casa épica",
                "location": (149999, 46728, -3414),
                "cost": 0
            },
            ".shop": {
                "name": "Tienda Épica",
                "description": "Teletransporte a la tienda épica",
                "location": (81304, 14589, -3469),
                "cost": 0
            },
            ".bank": {
                "name": "Banco Épico",
                "description": "Teletransporte al banco épico",
                "location": (111409, 219364, -3545),
                "cost": 0
            }
        }
        
    def onAdvEvent(self, event, npc, player):
        if event == "mostrar_comandos":
            return self.mostrarComandos(player)
        elif event.startswith("ejecutar_comando_"):
            commandKey = event.replace("ejecutar_comando_", "")
            return self.ejecutarComando(player, commandKey)
        elif event == "ver_ayuda_comandos":
            return self.verAyudaComandos(player)
        return None
    
    def mostrarComandos(self, player):
        html = "<html><body>"
        html += "<center><font color=\"LEVEL\">¡¡¡ COMANDOS ÉPICOS DE L2 HERMANOS !!!</font></center><br>"
        html += "<center><font color=\"LEVEL\">¡¡¡ EPIC COMMANDS OF L2 HERMANOS !!!</font></center><br><br>"
        
        html += "<font color=\"LEVEL\">🎯 COMANDOS DISPONIBLES / AVAILABLE COMMANDS:</font><br><br>"
        
        for commandKey, commandInfo in self.epicCommands.items():
            costText = "GRATIS" if commandInfo["cost"] == 0 else str(commandInfo["cost"]) + " Adena"
            costTextEn = "FREE" if commandInfo["cost"] == 0 else str(commandInfo["cost"]) + " Adena"
            
            html += "<font color=\"LEVEL\">" + commandKey + "</font><br>"
            html += "<font color=\"WHITE\">" + commandInfo["name"] + "</font><br>"
            html += "<font color=\"WHITE\">" + commandInfo["description"] + "</font><br>"
            html += "<font color=\"YELLOW\">Costo: " + costText + " / Cost: " + costTextEn + "</font><br>"
            html += "<button value=\"Ejecutar " + commandKey + "\" action=\"bypass -h Quest EpicCommands ejecutar_comando_" + commandKey.replace(".", "") + "\" width=200 height=25 back=\"L2UI_ct1.button_df\" fore=\"L2UI_ct1.button_df\"><br><br>"
        
        html += "<font color=\"LEVEL\">🎯 ACCIONES DISPONIBLES / AVAILABLE ACTIONS:</font><br>"
        html += "<button value=\"Ver Ayuda\" action=\"bypass -h Quest EpicCommands ver_ayuda_comandos\" width=200 height=25 back=\"L2UI_ct1.button_df\" fore=\"L2UI_ct1.button_df\"><br>"
        
        html += "<br><font color=\"LEVEL\">💰 COSTOS DE COMANDOS / COMMAND COSTS:</font><br>"
        html += "• Comandos básicos: GRATIS / Basic commands: FREE<br>"
        html += "• Comandos PvP: 1,000 Adena / PvP commands: 1,000 Adena<br>"
        html += "• Comandos de Boss: 5,000 Adena / Boss commands: 5,000 Adena<br>"
        html += "• Comandos VIP: 10,000 Adena / VIP commands: 10,000 Adena<br>"
        
        html += "<br><font color=\"LEVEL\">🎮 USO DE COMANDOS / COMMAND USAGE:</font><br>"
        html += "• Escribe el comando en el chat / Type the command in chat<br>"
        html += "• Ejemplo: .farm1 / Example: .farm1<br>"
        html += "• Los comandos son instantáneos / Commands are instant<br>"
        html += "• No hay cooldown / No cooldown<br>"
        
        html += "<br><font color=\"LEVEL\">¡¡¡ USA LOS COMANDOS ÉPICOS PARA DOMINAR EL SERVIDOR !!!</font><br>"
        html += "<font color=\"LEVEL\">¡¡¡ USE THE EPIC COMMANDS TO DOMINATE THE SERVER !!!</font><br>"
        
        html += "</body></html>"
        
        reply = NpcHtmlMessage(1)
        reply.setHtml(html)
        player.sendPacket(reply)
        return None
    
    def ejecutarComando(self, player, commandKey):
        # Restaurar el punto del comando
        commandKey = "." + commandKey
        
        if commandKey not in self.epicCommands:
            return "Comando no encontrado."
        
        commandInfo = self.epicCommands[commandKey]
        
        # Verificar costo
        if commandInfo["cost"] > 0:
            if player.getAdena() < commandInfo["cost"]:
                return "No tienes suficiente Adena. Necesitas: " + str(commandInfo["cost"])
            
            # Cobrar costo
            player.reduceAdena("Comando", commandInfo["cost"])
        
        # Ejecutar comando
        x, y, z = commandInfo["location"]
        player.teleToLocation(x, y, z)
        
        # Mensaje épico
        player.sendMessage("¡¡¡ COMANDO ÉPICO EJECUTADO: " + commandKey + " !!!")
        player.sendMessage("¡¡¡ EPIC COMMAND EXECUTED: " + commandKey + " !!!")
        player.sendMessage("¡Has sido teleportado a " + commandInfo["name"] + "!")
        player.sendMessage("You have been teleported to " + commandInfo["name"] + "!")
        
        # Anuncio épico
        self.announceToAll(player.getName() + " ha usado el comando épico: " + commandKey + "!")
        self.announceToAll(player.getName() + " has used the epic command: " + commandKey + "!")
        
        return "¡Comando épico ejecutado: " + commandKey + "!"
    
    def verAyudaComandos(self, player):
        html = "<html><body>"
        html += "<center><font color=\"LEVEL\">¡¡¡ AYUDA DE COMANDOS ÉPICOS !!!</font></center><br>"
        html += "<center><font color=\"LEVEL\">¡¡¡ EPIC COMMANDS HELP !!!</font></center><br><br>"
        
        html += "<font color=\"LEVEL\">📖 CÓMO USAR LOS COMANDOS / HOW TO USE COMMANDS:</font><br><br>"
        
        html += "<font color=\"LEVEL\">1. COMANDOS BÁSICOS / BASIC COMMANDS:</font><br>"
        html += "• .farm1 - Teletransporte a zona de farm épica 1<br>"
        html += "• .farm2 - Teletransporte a zona de farm épica 2<br>"
        html += "• .home - Teletransporte a tu casa épica<br>"
        html += "• .shop - Teletransporte a la tienda épica<br>"
        html += "• .bank - Teletransporte al banco épico<br>"
        
        html += "<br><font color=\"LEVEL\">2. COMANDOS PVP / PVP COMMANDS:</font><br>"
        html += "• .pvp1 - Teletransporte a zona de PvP épica 1 (1,000 Adena)<br>"
        html += "• .pvp2 - Teletransporte a zona de PvP épica 2 (1,000 Adena)<br>"
        
        html += "<br><font color=\"LEVEL\">3. COMANDOS ESPECIALES / SPECIAL COMMANDS:</font><br>"
        html += "• .boss - Teletransporte a zona de bosses épicos (5,000 Adena)<br>"
        html += "• .event - Teletransporte a zona de eventos épicos<br>"
        html += "• .vip - Teletransporte a zona VIP épica (10,000 Adena)<br>"
        
        html += "<br><font color=\"LEVEL\">💡 CONSEJOS ÚTILES / USEFUL TIPS:</font><br>"
        html += "• Los comandos son instantáneos / Commands are instant<br>"
        html += "• No hay cooldown / No cooldown<br>"
        html += "• Algunos comandos tienen costo / Some commands have cost<br>"
        html += "• Usa los comandos para moverte rápidamente / Use commands to move quickly<br>"
        
        html += "<br><font color=\"LEVEL\">🎯 COMANDOS RECOMENDADOS / RECOMMENDED COMMANDS:</font><br>"
        html += "• Para farm: .farm1, .farm2 / For farming: .farm1, .farm2<br>"
        html += "• Para PvP: .pvp1, .pvp2 / For PvP: .pvp1, .pvp2<br>"
        html += "• Para bosses: .boss / For bosses: .boss<br>"
        html += "• Para eventos: .event / For events: .event<br>"
        
        html += "<br><font color=\"LEVEL\">¡¡¡ DOMINA EL SERVIDOR CON LOS COMANDOS ÉPICOS !!!</font><br>"
        html += "<font color=\"LEVEL\">¡¡¡ DOMINATE THE SERVER WITH THE EPIC COMMANDS !!!</font><br>"
        
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
                player.sendPacket(CreatureSay(0, 1, "COMANDOS ÉPICOS", message))

# Crear instancia del sistema de comandos épicos
COMANDOS_EPICOS = EpicCommands(-1, "ComandosEpicos", "Sistema de Comandos Épicos")

# Registrar el sistema
COMANDOS_EPICOS.addStartNpc(30006)  # Tienda GM
COMANDOS_EPICOS.addTalkId(30006)



