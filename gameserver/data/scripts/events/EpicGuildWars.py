# ===========================================
# GUILD WARS ÉPICAS - L2 HERMANOS
# ===========================================
# Sistema de guerras de guild épicas
# Epic guild wars system

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

class EpicGuildWars(JQuest):
    def __init__(self, id, name, descr):
        JQuest.__init__(self, id, name, descr)
        self.activeWars = {}
        self.warZones = [
            (149999, 46728, -3414),  # Giran
            (81304, 14589, -3469),   # Aden
            (111409, 219364, -3545), # Rune
            (147928, -55273, -2728), # Heine
            (116819, 76994, -2714),  # Dion
        ]
        
    def onAdvEvent(self, event, npc, player):
        if event == "mostrar_guild_wars":
            return self.mostrarGuildWars(player)
        elif event == "declarar_guerra":
            return self.declararGuerra(player)
        elif event == "aceptar_guerra":
            return self.aceptarGuerra(player)
        elif event == "rechazar_guerra":
            return self.rechazarGuerra(player)
        elif event == "terminar_guerra":
            return self.terminarGuerra(player)
        elif event == "ver_estadisticas":
            return self.verEstadisticas(player)
        return None
    
    def mostrarGuildWars(self, player):
        html = "<html><body>"
        html += "<center><font color=\"LEVEL\">¡¡¡ GUILD WARS ÉPICAS DE L2 HERMANOS !!!</font></center><br>"
        html += "<center><font color=\"LEVEL\">¡¡¡ EPIC GUILD WARS OF L2 HERMANOS !!!</font></center><br><br>"
        
        html += "<font color=\"LEVEL\">⚔️ GUERRAS ACTIVAS / ACTIVE WARS:</font><br>"
        if self.activeWars:
            for warId, warInfo in self.activeWars.items():
                html += "<font color=\"LEVEL\">Guerra #" + str(warId) + "</font><br>"
                html += "<font color=\"WHITE\">" + warInfo["guild1"] + " vs " + warInfo["guild2"] + "</font><br>"
                html += "<font color=\"WHITE\">Duración: " + str(warInfo["duration"]) + " minutos</font><br><br>"
        else:
            html += "<font color=\"WHITE\">No hay guerras activas</font><br><br>"
        
        html += "<font color=\"LEVEL\">🎯 ACCIONES DISPONIBLES / AVAILABLE ACTIONS:</font><br>"
        html += "<button value=\"Declarar Guerra\" action=\"bypass -h Quest EpicGuildWars declarar_guerra\" width=200 height=25 back=\"L2UI_ct1.button_df\" fore=\"L2UI_ct1.button_df\"><br>"
        html += "<button value=\"Ver Estadísticas\" action=\"bypass -h Quest EpicGuildWars ver_estadisticas\" width=200 height=25 back=\"L2UI_ct1.button_df\" fore=\"L2UI_ct1.button_df\"><br>"
        
        html += "<br><font color=\"LEVEL\">🏆 REGLAS DE GUERRA / WAR RULES:</font><br>"
        html += "• Duración: 30 minutos / Duration: 30 minutes<br>"
        html += "• Zona: Campo de batalla épico / Zone: Epic battlefield<br>"
        html += "• Recompensas: Items épicos / Rewards: Epic items<br>"
        html += "• PvP: Sin penalidades / PvP: No penalties<br>"
        html += "• Respawn: Instantáneo / Respawn: Instant<br>"
        
        html += "<br><font color=\"LEVEL\">💰 RECOMPENSAS ÉPICAS / EPIC REWARDS:</font><br>"
        html += "• Ganador: 10M Adena + Items épicos / Winner: 10M Adena + Epic items<br>"
        html += "• Participantes: 1M Adena + Items raros / Participants: 1M Adena + Rare items<br>"
        html += "• MVP: 5M Adena + Items únicos / MVP: 5M Adena + Unique items<br>"
        
        html += "<br><font color=\"LEVEL\">¡¡¡ DOMINA EL CAMPO DE BATALLA ÉPICO !!!</font><br>"
        html += "<font color=\"LEVEL\">¡¡¡ DOMINATE THE EPIC BATTLEFIELD !!!</font><br>"
        
        html += "</body></html>"
        
        reply = NpcHtmlMessage(1)
        reply.setHtml(html)
        player.sendPacket(reply)
        return None
    
    def declararGuerra(self, player):
        if not player.isInGuild():
            return "Debes estar en una guild para declarar guerra."
        
        guild = player.getGuild()
        if not guild:
            return "Error al obtener información de la guild."
        
        # Crear guerra épica
        warId = len(self.activeWars) + 1
        self.activeWars[warId] = {
            "guild1": guild.getName(),
            "guild2": "Esperando oponente",
            "duration": 30,
            "startTime": 0,
            "active": False
        }
        
        # Mensaje épico
        player.sendMessage("¡¡¡ GUERRA ÉPICA DECLARADA !!!")
        player.sendMessage("¡¡¡ EPIC WAR DECLARED !!!")
        player.sendMessage("¡Tu guild está buscando oponente!")
        player.sendMessage("Your guild is looking for an opponent!")
        
        # Anuncio épico
        self.announceToAll("¡¡¡ " + guild.getName() + " HA DECLARADO GUERRA ÉPICA !!!")
        self.announceToAll("¡¡¡ " + guild.getName() + " HAS DECLARED EPIC WAR !!!")
        self.announceToAll("¡¡¡ GUILD WARS ÉPICAS DISPONIBLES !!!")
        self.announceToAll("¡¡¡ EPIC GUILD WARS AVAILABLE !!!")
        
        return "¡Guerra épica declarada! Buscando oponente..."
    
    def aceptarGuerra(self, player):
        if not player.isInGuild():
            return "Debes estar en una guild para aceptar guerra."
        
        guild = player.getGuild()
        if not guild:
            return "Error al obtener información de la guild."
        
        # Buscar guerra disponible
        for warId, warInfo in self.activeWars.items():
            if warInfo["guild2"] == "Esperando oponente" and warInfo["guild1"] != guild.getName():
                warInfo["guild2"] = guild.getName()
                warInfo["active"] = True
                warInfo["startTime"] = System.currentTimeMillis()
                
                # Mensaje épico
                player.sendMessage("¡¡¡ GUERRA ÉPICA ACEPTADA !!!")
                player.sendMessage("¡¡¡ EPIC WAR ACCEPTED !!!")
                player.sendMessage("¡La batalla épica ha comenzado!")
                player.sendMessage("The epic battle has begun!")
                
                # Anuncio épico
                self.announceToAll("¡¡¡ GUERRA ÉPICA INICIADA: " + warInfo["guild1"] + " vs " + warInfo["guild2"] + " !!!")
                self.announceToAll("¡¡¡ EPIC WAR STARTED: " + warInfo["guild1"] + " vs " + warInfo["guild2"] + " !!!")
                
                # Programar fin de la guerra
                self.startQuestTimer("terminar_guerra_" + str(warId), 1800000, None, None)  # 30 minutos
                
                return "¡Guerra épica aceptada! ¡La batalla ha comenzado!"
        
        return "No hay guerras disponibles para aceptar."
    
    def terminarGuerra(self, player):
        # Terminar todas las guerras activas
        for warId, warInfo in self.activeWars.items():
            if warInfo["active"]:
                warInfo["active"] = False
                
                # Anuncio épico
                self.announceToAll("¡¡¡ GUERRA ÉPICA TERMINADA: " + warInfo["guild1"] + " vs " + warInfo["guild2"] + " !!!")
                self.announceToAll("¡¡¡ EPIC WAR FINISHED: " + warInfo["guild1"] + " vs " + warInfo["guild2"] + " !!!")
        
        self.activeWars = {}
        
        # Mensaje épico
        player.sendMessage("¡¡¡ TODAS LAS GUERRAS ÉPICAS TERMINADAS !!!")
        player.sendMessage("¡¡¡ ALL EPIC WARS FINISHED !!!")
        
        return "¡Todas las guerras épicas han sido terminadas!"
    
    def verEstadisticas(self, player):
        html = "<html><body>"
        html += "<center><font color=\"LEVEL\">¡¡¡ ESTADÍSTICAS DE GUILD WARS ÉPICAS !!!</font></center><br>"
        html += "<center><font color=\"LEVEL\">¡¡¡ EPIC GUILD WARS STATISTICS !!!</font></center><br><br>"
        
        html += "<font color=\"LEVEL\">📊 ESTADÍSTICAS GENERALES / GENERAL STATISTICS:</font><br>"
        html += "• Guerras totales: " + str(len(self.activeWars)) + " / Total wars: " + str(len(self.activeWars)) + "<br>"
        html += "• Guerras activas: " + str(len([w for w in self.activeWars.values() if w["active"]])) + " / Active wars: " + str(len([w for w in self.activeWars.values() if w["active"]])) + "<br>"
        html += "• Guerras completadas: " + str(len([w for w in self.activeWars.values() if not w["active"]])) + " / Completed wars: " + str(len([w for w in self.activeWars.values() if not w["active"]])) + "<br>"
        
        html += "<br><font color=\"LEVEL\">🏆 TOP GUILDS / MEJORES GUILDS:</font><br>"
        html += "• Guild más activa: En desarrollo / Most active guild: In development<br>"
        html += "• Guild más victoriosa: En desarrollo / Most victorious guild: In development<br>"
        html += "• Guild más temida: En desarrollo / Most feared guild: In development<br>"
        
        html += "<br><font color=\"LEVEL\">⚔️ ESTADÍSTICAS DE BATALLA / BATTLE STATISTICS:</font><br>"
        html += "• Kills totales: En desarrollo / Total kills: In development<br>"
        html += "• Daño total: En desarrollo / Total damage: In development<br>"
        html += "• Tiempo de batalla: En desarrollo / Battle time: In development<br>"
        
        html += "<br><font color=\"LEVEL\">¡¡¡ CONVIÉRTETE EN LA GUILD MÁS ÉPICA !!!</font><br>"
        html += "<font color=\"LEVEL\">¡¡¡ BECOME THE MOST EPIC GUILD !!!</font><br>"
        
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
                player.sendPacket(CreatureSay(0, 1, "GUILD WARS ÉPICAS", message))

# Crear instancia del sistema de guild wars épicas
GUILD_WARS_EPICAS = EpicGuildWars(-1, "GuildWarsEpicas", "Sistema de Guild Wars Épicas")

# Registrar el sistema
GUILD_WARS_EPICAS.addStartNpc(30006)  # Tienda GM
GUILD_WARS_EPICAS.addTalkId(30006)



