# ===========================================
# TELEPORTER ÉPICO - L2 HERMANOS
# ===========================================
# Sistema de teletransporte épico
# Epic teleporter system

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

class EpicTeleporter(JQuest):
    def __init__(self, id, name, descr):
        JQuest.__init__(self, id, name, descr)
        self.teleportLocations = {
            "CIUDADES": {
                "name": "Ciudades Épicas",
                "locations": [
                    {"name": "Giran", "x": 149999, "y": 46728, "z": -3414, "cost": 0},
                    {"name": "Aden", "x": 81304, "y": 14589, "z": -3469, "cost": 0},
                    {"name": "Rune", "x": 111409, "y": 219364, "z": -3545, "cost": 0},
                    {"name": "Heine", "x": 147928, "y": -55273, "z": -2728, "cost": 0},
                    {"name": "Dion", "x": 116819, "y": 76994, "z": -2714, "cost": 0},
                    {"name": "Gludio", "x": -84318, "y": 244579, "z": -3730, "cost": 0},
                    {"name": "Gludin", "x": -80826, "y": 149775, "z": -3043, "cost": 0},
                    {"name": "Oren", "x": 55412, "y": -112742, "z": -1128, "cost": 0}
                ]
            },
            "ZONAS_FARM": {
                "name": "Zonas de Farm Épicas",
                "locations": [
                    {"name": "Farm Épico 1", "x": 186000, "y": -10000, "z": -3000, "cost": 1000},
                    {"name": "Farm Épico 2", "x": 190000, "y": -15000, "z": -3500, "cost": 1000},
                    {"name": "Farm Épico 3", "x": 195000, "y": -20000, "z": -4000, "cost": 1000},
                    {"name": "Farm Épico 4", "x": 200000, "y": -25000, "z": -4500, "cost": 1000},
                    {"name": "Farm Épico 5", "x": 205000, "y": -30000, "z": -5000, "cost": 1000}
                ]
            },
            "ZONAS_PVP": {
                "name": "Zonas de PvP Épicas",
                "locations": [
                    {"name": "PvP Épico 1", "x": 210000, "y": -35000, "z": -5500, "cost": 2000},
                    {"name": "PvP Épico 2", "x": 215000, "y": -40000, "z": -6000, "cost": 2000},
                    {"name": "PvP Épico 3", "x": 220000, "y": -45000, "z": -6500, "cost": 2000},
                    {"name": "PvP Épico 4", "x": 225000, "y": -50000, "z": -7000, "cost": 2000},
                    {"name": "PvP Épico 5", "x": 230000, "y": -55000, "z": -7500, "cost": 2000}
                ]
            },
            "DUNGEONS": {
                "name": "Mazmorras Épicas",
                "locations": [
                    {"name": "Mazmorra Épica 1", "x": 235000, "y": -60000, "z": -8000, "cost": 5000},
                    {"name": "Mazmorra Épica 2", "x": 240000, "y": -65000, "z": -8500, "cost": 5000},
                    {"name": "Mazmorra Épica 3", "x": 245000, "y": -70000, "z": -9000, "cost": 5000},
                    {"name": "Mazmorra Épica 4", "x": 250000, "y": -75000, "z": -9500, "cost": 5000},
                    {"name": "Mazmorra Épica 5", "x": 255000, "y": -80000, "z": -10000, "cost": 5000}
                ]
            },
            "BOSSES": {
                "name": "Bosses Épicos",
                "locations": [
                    {"name": "Antharas", "x": 179311, "y": 114932, "z": -7709, "cost": 10000},
                    {"name": "Baium", "x": 112898, "y": 10818, "z": -4240, "cost": 10000},
                    {"name": "Zaken", "x": 55568, "y": 216904, "z": -3770, "cost": 10000},
                    {"name": "Orfen", "x": 55024, "y": 17368, "z": -5412, "cost": 10000},
                    {"name": "Frintezza", "x": 174240, "y": -88096, "z": -5119, "cost": 10000}
                ]
            },
            "EVENTOS": {
                "name": "Zonas de Eventos Épicos",
                "locations": [
                    {"name": "Evento Épico 1", "x": 260000, "y": -85000, "z": -10500, "cost": 0},
                    {"name": "Evento Épico 2", "x": 265000, "y": -90000, "z": -11000, "cost": 0},
                    {"name": "Evento Épico 3", "x": 270000, "y": -95000, "z": -11500, "cost": 0},
                    {"name": "Evento Épico 4", "x": 275000, "y": -100000, "z": -12000, "cost": 0},
                    {"name": "Evento Épico 5", "x": 280000, "y": -105000, "z": -12500, "cost": 0}
                ]
            }
        }
        
    def onAdvEvent(self, event, npc, player):
        if event == "mostrar_teleporter":
            return self.mostrarTeleporter(player)
        elif event.startswith("teleport_"):
            locationKey = event.replace("teleport_", "")
            return self.teleportarJugador(player, locationKey)
        elif event.startswith("categoria_"):
            categoria = event.replace("categoria_", "")
            return self.mostrarCategoria(player, categoria)
        return None
    
    def mostrarTeleporter(self, player):
        html = "<html><body>"
        html += "<center><font color=\"LEVEL\">¡¡¡ TELEPORTER ÉPICO DE L2 HERMANOS !!!</font></center><br>"
        html += "<center><font color=\"LEVEL\">¡¡¡ EPIC TELEPORTER OF L2 HERMANOS !!!</font></center><br><br>"
        
        html += "<font color=\"LEVEL\">🌍 CATEGORÍAS DE TELEPORTE / TELEPORT CATEGORIES:</font><br><br>"
        
        for categoriaKey, categoriaInfo in self.teleportLocations.items():
            html += "<font color=\"LEVEL\">" + categoriaInfo["name"] + "</font><br>"
            html += "<font color=\"WHITE\">" + str(len(categoriaInfo["locations"])) + " ubicaciones disponibles</font><br>"
            html += "<font color=\"WHITE\">" + str(len(categoriaInfo["locations"])) + " locations available</font><br>"
            html += "<button value=\"Ver " + categoriaInfo["name"] + "\" action=\"bypass -h Quest EpicTeleporter categoria_" + categoriaKey + "\" width=200 height=25 back=\"L2UI_ct1.button_df\" fore=\"L2UI_ct1.button_df\"><br><br>"
        
        html += "<font color=\"LEVEL\">💰 COSTOS DE TELEPORTE / TELEPORT COSTS:</font><br>"
        html += "• Ciudades: GRATIS / Cities: FREE<br>"
        html += "• Zonas de Farm: 1,000 Adena / Farm Zones: 1,000 Adena<br>"
        html += "• Zonas de PvP: 2,000 Adena / PvP Zones: 2,000 Adena<br>"
        html += "• Mazmorras: 5,000 Adena / Dungeons: 5,000 Adena<br>"
        html += "• Bosses: 10,000 Adena / Bosses: 10,000 Adena<br>"
        html += "• Eventos: GRATIS / Events: FREE<br>"
        
        html += "<br><font color=\"LEVEL\">🎯 COMANDOS RÁPIDOS / QUICK COMMANDS:</font><br>"
        html += "• .farm1 - Farm Épico 1 / Epic Farm 1<br>"
        html += "• .farm2 - Farm Épico 2 / Epic Farm 2<br>"
        html += "• .pvp1 - PvP Épico 1 / Epic PvP 1<br>"
        html += "• .pvp2 - PvP Épico 2 / Epic PvP 2<br>"
        
        html += "<br><font color=\"LEVEL\">¡¡¡ VIAJA POR TODO EL MUNDO ÉPICO !!!</font><br>"
        html += "<font color=\"LEVEL\">¡¡¡ TRAVEL AROUND THE EPIC WORLD !!!</font><br>"
        
        html += "</body></html>"
        
        reply = NpcHtmlMessage(1)
        reply.setHtml(html)
        player.sendPacket(reply)
        return None
    
    def mostrarCategoria(self, player, categoriaKey):
        if categoriaKey not in self.teleportLocations:
            return "Categoría no encontrada."
        
        categoriaInfo = self.teleportLocations[categoriaKey]
        
        html = "<html><body>"
        html += "<center><font color=\"LEVEL\">" + categoriaInfo["name"] + "</font></center><br><br>"
        
        html += "<font color=\"LEVEL\">📍 UBICACIONES DISPONIBLES / AVAILABLE LOCATIONS:</font><br><br>"
        
        for i, location in enumerate(categoriaInfo["locations"]):
            costText = "GRATIS" if location["cost"] == 0 else str(location["cost"]) + " Adena"
            costTextEn = "FREE" if location["cost"] == 0 else str(location["cost"]) + " Adena"
            
            html += "<font color=\"LEVEL\">" + location["name"] + "</font><br>"
            html += "<font color=\"WHITE\">Costo: " + costText + " / Cost: " + costTextEn + "</font><br>"
            html += "<button value=\"Teleportar a " + location["name"] + "\" action=\"bypass -h Quest EpicTeleporter teleport_" + categoriaKey + "_" + str(i) + "\" width=200 height=25 back=\"L2UI_ct1.button_df\" fore=\"L2UI_ct1.button_df\"><br><br>"
        
        html += "<button value=\"Volver al Menú Principal\" action=\"bypass -h Quest EpicTeleporter mostrar_teleporter\" width=200 height=25 back=\"L2UI_ct1.button_df\" fore=\"L2UI_ct1.button_df\"><br>"
        
        html += "</body></html>"
        
        reply = NpcHtmlMessage(1)
        reply.setHtml(html)
        player.sendPacket(reply)
        return None
    
    def teleportarJugador(self, player, locationKey):
        try:
            parts = locationKey.split("_")
            if len(parts) != 2:
                return "Error en la ubicación."
            
            categoriaKey = parts[0]
            locationIndex = int(parts[1])
            
            if categoriaKey not in self.teleportLocations:
                return "Categoría no encontrada."
            
            categoriaInfo = self.teleportLocations[categoriaKey]
            if locationIndex >= len(categoriaInfo["locations"]):
                return "Ubicación no encontrada."
            
            location = categoriaInfo["locations"][locationIndex]
            
            # Verificar costo
            if location["cost"] > 0:
                if player.getAdena() < location["cost"]:
                    return "No tienes suficiente Adena. Necesitas: " + str(location["cost"])
                
                # Cobrar costo
                player.reduceAdena("Teleport", location["cost"])
            
            # Teleportar
            player.teleToLocation(location["x"], location["y"], location["z"])
            
            # Mensaje épico
            player.sendMessage("¡¡¡ TELEPORTE ÉPICO EXITOSO !!!")
            player.sendMessage("¡¡¡ EPIC TELEPORT SUCCESSFUL !!!")
            player.sendMessage("¡Has sido teleportado a " + location["name"] + "!")
            player.sendMessage("You have been teleported to " + location["name"] + "!")
            
            # Anuncio épico
            self.announceToAll(player.getName() + " se ha teleportado a " + location["name"] + "!")
            self.announceToAll(player.getName() + " has teleported to " + location["name"] + "!")
            
            return "¡Teletransporte exitoso a " + location["name"] + "!"
            
        except Exception as e:
            return "Error en el teletransporte: " + str(e)
    
    def announceToAll(self, message):
        from l2jfrozen.gameserver.network.serverpackets import CreatureSay
        from l2jfrozen.gameserver.model.actor.instance import L2PcInstance
        from l2jfrozen.gameserver.GameServer import GameServer
        
        for player in GameServer.getInstance().getAllPlayers():
            if player and player.isOnline():
                player.sendPacket(CreatureSay(0, 1, "TELEPORTER ÉPICO", message))

# Crear instancia del sistema de teleporter épico
TELEPORTER_EPICO = EpicTeleporter(-1, "TeleporterEpico", "Sistema de Teleporter Épico")

# Registrar el sistema
TELEPORTER_EPICO.addStartNpc(30006)  # Tienda GM
TELEPORTER_EPICO.addTalkId(30006)



