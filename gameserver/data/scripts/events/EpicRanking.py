# ===========================================
# RANKING ÉPICO - L2 HERMANOS
# ===========================================
# Sistema de ranking épico
# Epic ranking system

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

class EpicRanking(JQuest):
    def __init__(self, id, name, descr):
        JQuest.__init__(self, id, name, descr)
        self.rankings = {
            "NIVEL": {
                "name": "Ranking de Nivel",
                "description": "Los jugadores de mayor nivel",
                "type": "level"
            },
            "PVP": {
                "name": "Ranking de PvP",
                "description": "Los mejores en combate PvP",
                "type": "pvp"
            },
            "PVE": {
                "name": "Ranking de PvE",
                "description": "Los mejores cazadores de monstruos",
                "type": "pve"
            },
            "ADENA": {
                "name": "Ranking de Adena",
                "description": "Los más ricos del servidor",
                "type": "adena"
            },
            "ONLINE": {
                "name": "Ranking de Tiempo Online",
                "description": "Los que más tiempo pasan en el juego",
                "type": "online"
            },
            "EVENTOS": {
                "name": "Ranking de Eventos",
                "description": "Los que más participan en eventos",
                "type": "events"
            },
            "BOSSES": {
                "name": "Ranking de Bosses",
                "description": "Los que más bosses han matado",
                "type": "bosses"
            },
            "GUILD": {
                "name": "Ranking de Guilds",
                "description": "Las guilds más poderosas",
                "type": "guild"
            }
        }
        
    def onAdvEvent(self, event, npc, player):
        if event == "mostrar_ranking":
            return self.mostrarRanking(player)
        elif event.startswith("ver_ranking_"):
            rankingType = event.replace("ver_ranking_", "")
            return self.verRankingEspecifico(player, rankingType)
        elif event == "ver_mi_posicion":
            return self.verMiPosicion(player)
        elif event == "ver_recompensas_ranking":
            return self.verRecompensasRanking(player)
        return None
    
    def mostrarRanking(self, player):
        html = "<html><body>"
        html += "<center><font color=\"LEVEL\">¡¡¡ RANKING ÉPICO DE L2 HERMANOS !!!</font></center><br>"
        html += "<center><font color=\"LEVEL\">¡¡¡ EPIC RANKING OF L2 HERMANOS !!!</font></center><br><br>"
        
        html += "<font color=\"LEVEL\">🏆 CATEGORÍAS DE RANKING / RANKING CATEGORIES:</font><br><br>"
        
        for rankingKey, rankingInfo in self.rankings.items():
            html += "<font color=\"LEVEL\">" + rankingInfo["name"] + "</font><br>"
            html += "<font color=\"WHITE\">" + rankingInfo["description"] + "</font><br>"
            html += "<button value=\"Ver " + rankingInfo["name"] + "\" action=\"bypass -h Quest EpicRanking ver_ranking_" + rankingKey + "\" width=200 height=25 back=\"L2UI_ct1.button_df\" fore=\"L2UI_ct1.button_df\"><br><br>"
        
        html += "<font color=\"LEVEL\">🎯 ACCIONES DISPONIBLES / AVAILABLE ACTIONS:</font><br>"
        html += "<button value=\"Ver Mi Posición\" action=\"bypass -h Quest EpicRanking ver_mi_posicion\" width=200 height=25 back=\"L2UI_ct1.button_df\" fore=\"L2UI_ct1.button_df\"><br>"
        html += "<button value=\"Ver Recompensas\" action=\"bypass -h Quest EpicRanking ver_recompensas_ranking\" width=200 height=25 back=\"L2UI_ct1.button_df\" fore=\"L2UI_ct1.button_df\"><br>"
        
        html += "<br><font color=\"LEVEL\">💰 RECOMPENSAS DE RANKING / RANKING REWARDS:</font><br>"
        html += "• Top 1: 10M Adena + Items épicos / Top 1: 10M Adena + Epic items<br>"
        html += "• Top 3: 5M Adena + Items raros / Top 3: 5M Adena + Rare items<br>"
        html += "• Top 10: 2M Adena + Items especiales / Top 10: 2M Adena + Special items<br>"
        html += "• Top 50: 1M Adena + Items únicos / Top 50: 1M Adena + Unique items<br>"
        
        html += "<br><font color=\"LEVEL\">🔄 ACTUALIZACIÓN DE RANKING / RANKING UPDATE:</font><br>"
        html += "• Cada hora / Every hour<br>"
        html += "• Recompensas diarias / Daily rewards<br>"
        html += "• Recompensas semanales / Weekly rewards<br>"
        html += "• Recompensas mensuales / Monthly rewards<br>"
        
        html += "<br><font color=\"LEVEL\">¡¡¡ COMPITE POR EL PRIMER LUGAR ÉPICO !!!</font><br>"
        html += "<font color=\"LEVEL\">¡¡¡ COMPETE FOR THE EPIC FIRST PLACE !!!</font><br>"
        
        html += "</body></html>"
        
        reply = NpcHtmlMessage(1)
        reply.setHtml(html)
        player.sendPacket(reply)
        return None
    
    def verRankingEspecifico(self, player, rankingType):
        if rankingType not in self.rankings:
            return "Tipo de ranking no encontrado."
        
        rankingInfo = self.rankings[rankingType]
        
        html = "<html><body>"
        html += "<center><font color=\"LEVEL\">" + rankingInfo["name"] + "</font></center><br>"
        html += "<center><font color=\"WHITE\">" + rankingInfo["description"] + "</font></center><br><br>"
        
        html += "<font color=\"LEVEL\">🏆 TOP 20 JUGADORES / TOP 20 PLAYERS:</font><br><br>"
        
        # Simular ranking (en un servidor real, esto vendría de la base de datos)
        topPlayers = self.generarRankingSimulado(rankingType)
        
        for i, playerInfo in enumerate(topPlayers, 1):
            medal = "🥇" if i == 1 else "🥈" if i == 2 else "🥉" if i == 3 else "🏅"
            html += "<font color=\"LEVEL\">" + medal + " #" + str(i) + " " + playerInfo["name"] + "</font><br>"
            html += "<font color=\"WHITE\">" + playerInfo["value"] + " | Nivel: " + str(playerInfo["level"]) + "</font><br>"
            html += "<font color=\"WHITE\">" + playerInfo["value"] + " | Level: " + str(playerInfo["level"]) + "</font><br><br>"
        
        html += "<button value=\"Volver al Menú Principal\" action=\"bypass -h Quest EpicRanking mostrar_ranking\" width=200 height=25 back=\"L2UI_ct1.button_df\" fore=\"L2UI_ct1.button_df\"><br>"
        
        html += "</body></html>"
        
        reply = NpcHtmlMessage(1)
        reply.setHtml(html)
        player.sendPacket(reply)
        return None
    
    def verMiPosicion(self, player):
        html = "<html><body>"
        html += "<center><font color=\"LEVEL\">¡¡¡ MI POSICIÓN EN LOS RANKINGS !!!</font></center><br>"
        html += "<center><font color=\"LEVEL\">¡¡¡ MY POSITION IN THE RANKINGS !!!</font></center><br><br>"
        
        html += "<font color=\"LEVEL\">📊 TU POSICIÓN ACTUAL / YOUR CURRENT POSITION:</font><br><br>"
        
        for rankingKey, rankingInfo in self.rankings.items():
            position = self.calcularPosicion(player, rankingKey)
            html += "<font color=\"LEVEL\">" + rankingInfo["name"] + "</font><br>"
            html += "<font color=\"WHITE\">Posición: #" + str(position) + " / Position: #" + str(position) + "</font><br>"
            html += "<font color=\"WHITE\">Valor: " + self.obtenerValor(player, rankingKey) + "</font><br><br>"
        
        html += "<font color=\"LEVEL\">🎯 ESTADÍSTICAS PERSONALES / PERSONAL STATISTICS:</font><br>"
        html += "• Nivel: " + str(player.getLevel()) + " / Level: " + str(player.getLevel()) + "<br>"
        html += "• Adena: " + str(player.getAdena()) + " / Adena: " + str(player.getAdena()) + "<br>"
        html += "• Tiempo online: En desarrollo / Online time: In development<br>"
        html += "• Kills PvP: En desarrollo / PvP Kills: In development<br>"
        html += "• Kills PvE: En desarrollo / PvE Kills: In development<br>"
        html += "• Bosses matados: En desarrollo / Bosses killed: In development<br>"
        html += "• Eventos participados: En desarrollo / Events participated: In development<br>"
        
        html += "<br><font color=\"LEVEL\">¡¡¡ SIGUE PROGRESANDO HACIA EL TOP !!!</font><br>"
        html += "<font color=\"LEVEL\">¡¡¡ KEEP PROGRESSING TOWARDS THE TOP !!!</font><br>"
        
        html += "</body></html>"
        
        reply = NpcHtmlMessage(1)
        reply.setHtml(html)
        player.sendPacket(reply)
        return None
    
    def verRecompensasRanking(self, player):
        html = "<html><body>"
        html += "<center><font color=\"LEVEL\">¡¡¡ RECOMPENSAS DE RANKING ÉPICAS !!!</font></center><br>"
        html += "<center><font color=\"LEVEL\">¡¡¡ EPIC RANKING REWARDS !!!</font></center><br><br>"
        
        html += "<font color=\"LEVEL\">🏆 RECOMPENSAS DIARIAS / DAILY REWARDS:</font><br>"
        html += "• Top 1: 10,000,000 Adena + 50 Life Stones<br>"
        html += "• Top 2: 8,000,000 Adena + 40 Life Stones<br>"
        html += "• Top 3: 6,000,000 Adena + 30 Life Stones<br>"
        html += "• Top 5: 4,000,000 Adena + 20 Life Stones<br>"
        html += "• Top 10: 2,000,000 Adena + 10 Life Stones<br>"
        html += "• Top 20: 1,000,000 Adena + 5 Life Stones<br>"
        html += "• Top 50: 500,000 Adena + 2 Life Stones<br>"
        
        html += "<br><font color=\"LEVEL\">💰 RECOMPENSAS SEMANALES / WEEKLY REWARDS:</font><br>"
        html += "• Top 1: 50,000,000 Adena + 100 Life Stones + 10 Soul Stones<br>"
        html += "• Top 2: 40,000,000 Adena + 80 Life Stones + 8 Soul Stones<br>"
        html += "• Top 3: 30,000,000 Adena + 60 Life Stones + 6 Soul Stones<br>"
        html += "• Top 5: 20,000,000 Adena + 40 Life Stones + 4 Soul Stones<br>"
        html += "• Top 10: 10,000,000 Adena + 20 Life Stones + 2 Soul Stones<br>"
        
        html += "<br><font color=\"LEVEL\">🎁 RECOMPENSAS MENSUALES / MONTHLY REWARDS:</font><br>"
        html += "• Top 1: 200,000,000 Adena + 500 Life Stones + 50 Soul Stones + Título Épico<br>"
        html += "• Top 2: 150,000,000 Adena + 400 Life Stones + 40 Soul Stones + Título Épico<br>"
        html += "• Top 3: 100,000,000 Adena + 300 Life Stones + 30 Soul Stones + Título Épico<br>"
        html += "• Top 5: 75,000,000 Adena + 200 Life Stones + 20 Soul Stones<br>"
        html += "• Top 10: 50,000,000 Adena + 100 Life Stones + 10 Soul Stones<br>"
        
        html += "<br><font color=\"LEVEL\">🌟 RECOMPENSAS ESPECIALES / SPECIAL REWARDS:</font><br>"
        html += "• MVP del mes: Items únicos + Transformación épica<br>"
        html += "• Mejor PvP: Armas épicas + Armaduras épicas<br>"
        html += "• Mejor PvE: Items de farm + Buffs épicos<br>"
        html += "• Más activo: Acceso VIP + Comandos especiales<br>"
        
        html += "<br><font color=\"LEVEL\">🔄 SISTEMA DE RECOMPENSAS / REWARD SYSTEM:</font><br>"
        html += "• Recompensas automáticas / Automatic rewards<br>"
        html += "• Entrega diaria a las 00:00 / Daily delivery at 00:00<br>"
        html += "• Entrega semanal los domingos / Weekly delivery on Sundays<br>"
        html += "• Entrega mensual el día 1 / Monthly delivery on the 1st<br>"
        
        html += "<br><font color=\"LEVEL\">¡¡¡ COMPITE POR LAS MEJORES RECOMPENSAS ÉPICAS !!!</font><br>"
        html += "<font color=\"LEVEL\">¡¡¡ COMPETE FOR THE BEST EPIC REWARDS !!!</font><br>"
        
        html += "</body></html>"
        
        reply = NpcHtmlMessage(1)
        reply.setHtml(html)
        player.sendPacket(reply)
        return None
    
    def generarRankingSimulado(self, rankingType):
        # Simular datos de ranking (en un servidor real, esto vendría de la base de datos)
        players = []
        for i in range(20):
            if rankingType == "NIVEL":
                players.append({
                    "name": "EpicPlayer" + str(i+1),
                    "value": "Nivel " + str(80-i),
                    "level": 80-i
                })
            elif rankingType == "PVP":
                players.append({
                    "name": "EpicPvP" + str(i+1),
                    "value": str(1000-i*50) + " kills",
                    "level": 75-i
                })
            elif rankingType == "PVE":
                players.append({
                    "name": "EpicPvE" + str(i+1),
                    "value": str(10000-i*500) + " kills",
                    "level": 78-i
                })
            elif rankingType == "ADENA":
                players.append({
                    "name": "EpicRich" + str(i+1),
                    "value": str(100000000-i*5000000) + " Adena",
                    "level": 80-i
                })
            else:
                players.append({
                    "name": "EpicPlayer" + str(i+1),
                    "value": "Valor " + str(1000-i*50),
                    "level": 75-i
                })
        return players
    
    def calcularPosicion(self, player, rankingType):
        # Simular posición (en un servidor real, esto se calcularía de la base de datos)
        if rankingType == "NIVEL":
            return max(1, 100 - player.getLevel())
        elif rankingType == "ADENA":
            return max(1, 100 - (player.getAdena() // 1000000))
        else:
            return 50  # Posición promedio
    
    def obtenerValor(self, player, rankingType):
        if rankingType == "NIVEL":
            return "Nivel " + str(player.getLevel())
        elif rankingType == "ADENA":
            return str(player.getAdena()) + " Adena"
        else:
            return "En desarrollo"
    
    def announceToAll(self, message):
        from l2jfrozen.gameserver.network.serverpackets import CreatureSay
        from l2jfrozen.gameserver.model.actor.instance import L2PcInstance
        from l2jfrozen.gameserver.GameServer import GameServer
        
        for player in GameServer.getInstance().getAllPlayers():
            if player and player.isOnline():
                player.sendPacket(CreatureSay(0, 1, "RANKING ÉPICO", message))

# Crear instancia del sistema de ranking épico
RANKING_EPICO = EpicRanking(-1, "RankingEpico", "Sistema de Ranking Épico")

# Registrar el sistema
RANKING_EPICO.addStartNpc(30006)  # Tienda GM
RANKING_EPICO.addTalkId(30006)



