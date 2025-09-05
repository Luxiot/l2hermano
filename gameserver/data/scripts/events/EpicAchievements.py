# ===========================================
# ACHIEVEMENTS ÉPICOS - L2 HERMANOS
# ===========================================
# Sistema de logros épicos únicos
# Epic achievements system

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

class EpicAchievements(JQuest):
    def __init__(self, id, name, descr):
        JQuest.__init__(self, id, name, descr)
        self.achievements = {
            "PRIMER_NIVEL": {
                "name": "Primer Nivel Épico",
                "description": "Alcanza el nivel 10",
                "requirement": 10,
                "type": "level",
                "reward": {"adena": 100000, "items": [(6651, 5)]},
                "unlocked": False
            },
            "CAZADOR_EPICO": {
                "name": "Cazador Épico",
                "description": "Mata 1000 monstruos",
                "requirement": 1000,
                "type": "kills",
                "reward": {"adena": 500000, "items": [(6652, 3)]},
                "unlocked": False
            },
            "ASESINO_EPICO": {
                "name": "Asesino Épico",
                "description": "Mata 100 jugadores en PvP",
                "requirement": 100,
                "type": "pvp_kills",
                "reward": {"adena": 1000000, "items": [(6653, 2)]},
                "unlocked": False
            },
            "EXPLORADOR_EPICO": {
                "name": "Explorador Épico",
                "description": "Visita 50 zonas diferentes",
                "requirement": 50,
                "type": "zones",
                "reward": {"adena": 750000, "items": [(6654, 1)]},
                "unlocked": False
            },
            "RICO_EPICO": {
                "name": "Rico Épico",
                "description": "Acumula 10,000,000 de Adena",
                "requirement": 10000000,
                "type": "adena",
                "reward": {"adena": 2000000, "items": [(6655, 1)]},
                "unlocked": False
            },
            "BOSS_SLAYER": {
                "name": "Asesino de Bosses Épico",
                "description": "Mata 50 bosses épicos",
                "requirement": 50,
                "type": "boss_kills",
                "reward": {"adena": 5000000, "items": [(6656, 1)]},
                "unlocked": False
            },
            "EVENT_MASTER": {
                "name": "Maestro de Eventos Épicos",
                "description": "Participa en 25 eventos épicos",
                "requirement": 25,
                "type": "events",
                "reward": {"adena": 3000000, "items": [(6657, 1)]},
                "unlocked": False
            },
            "LEGENDARY_HERO": {
                "name": "Héroe Legendario Épico",
                "description": "Alcanza el nivel 80",
                "requirement": 80,
                "type": "level",
                "reward": {"adena": 10000000, "items": [(6658, 1)]},
                "unlocked": False
            }
        }
        
    def onAdvEvent(self, event, npc, player):
        if event == "mostrar_achievements":
            return self.mostrarAchievements(player)
        elif event == "reclamar_recompensa":
            return self.reclamarRecompensa(player)
        elif event == "ver_progreso":
            return self.verProgreso(player)
        elif event == "ver_ranking":
            return self.verRanking(player)
        return None
    
    def mostrarAchievements(self, player):
        html = "<html><body>"
        html += "<center><font color=\"LEVEL\">¡¡¡ ACHIEVEMENTS ÉPICOS DE L2 HERMANOS !!!</font></center><br>"
        html += "<center><font color=\"LEVEL\">¡¡¡ EPIC ACHIEVEMENTS OF L2 HERMANOS !!!</font></center><br><br>"
        
        html += "<font color=\"LEVEL\">🏆 ACHIEVEMENTS DISPONIBLES / AVAILABLE ACHIEVEMENTS:</font><br><br>"
        
        for achievementKey, achievementInfo in self.achievements.items():
            status = "✅ DESBLOQUEADO" if achievementInfo["unlocked"] else "❌ BLOQUEADO"
            status_en = "✅ UNLOCKED" if achievementInfo["unlocked"] else "❌ LOCKED"
            
            html += "<font color=\"LEVEL\">" + achievementInfo["name"] + "</font><br>"
            html += "<font color=\"WHITE\">" + achievementInfo["description"] + "</font><br>"
            html += "<font color=\"YELLOW\">" + status + " / " + status_en + "</font><br>"
            html += "<font color=\"GREEN\">Recompensa: " + str(achievementInfo["reward"]["adena"]) + " Adena + Items épicos</font><br>"
            html += "<font color=\"GREEN\">Reward: " + str(achievementInfo["reward"]["adena"]) + " Adena + Epic items</font><br><br>"
        
        html += "<font color=\"LEVEL\">🎯 ACCIONES DISPONIBLES / AVAILABLE ACTIONS:</font><br>"
        html += "<button value=\"Ver Progreso\" action=\"bypass -h Quest EpicAchievements ver_progreso\" width=200 height=25 back=\"L2UI_ct1.button_df\" fore=\"L2UI_ct1.button_df\"><br>"
        html += "<button value=\"Ver Ranking\" action=\"bypass -h Quest EpicAchievements ver_ranking\" width=200 height=25 back=\"L2UI_ct1.button_df\" fore=\"L2UI_ct1.button_df\"><br>"
        html += "<button value=\"Reclamar Recompensas\" action=\"bypass -h Quest EpicAchievements reclamar_recompensa\" width=200 height=25 back=\"L2UI_ct1.button_df\" fore=\"L2UI_ct1.button_df\"><br>"
        
        html += "<br><font color=\"LEVEL\">💰 RECOMPENSAS ÉPICAS / EPIC REWARDS:</font><br>"
        html += "• Adena épica / Epic Adena<br>"
        html += "• Items épicos únicos / Unique epic items<br>"
        html += "• Títulos épicos / Epic titles<br>"
        html += "• Habilidades épicas / Epic skills<br>"
        html += "• Transformaciones épicas / Epic transformations<br>"
        
        html += "<br><font color=\"LEVEL\">¡¡¡ CONVIÉRTETE EN UNA LEYENDA ÉPICA !!!</font><br>"
        html += "<font color=\"LEVEL\">¡¡¡ BECOME AN EPIC LEGEND !!!</font><br>"
        
        html += "</body></html>"
        
        reply = NpcHtmlMessage(1)
        reply.setHtml(html)
        player.sendPacket(reply)
        return None
    
    def verProgreso(self, player):
        html = "<html><body>"
        html += "<center><font color=\"LEVEL\">¡¡¡ PROGRESO DE ACHIEVEMENTS ÉPICOS !!!</font></center><br>"
        html += "<center><font color=\"LEVEL\">¡¡¡ EPIC ACHIEVEMENTS PROGRESS !!!</font></center><br><br>"
        
        html += "<font color=\"LEVEL\">📊 TU PROGRESO / YOUR PROGRESS:</font><br><br>"
        
        for achievementKey, achievementInfo in self.achievements.items():
            current = self.getCurrentProgress(player, achievementInfo["type"])
            required = achievementInfo["requirement"]
            progress = min(100, (current * 100) // required)
            
            html += "<font color=\"LEVEL\">" + achievementInfo["name"] + "</font><br>"
            html += "<font color=\"WHITE\">Progreso: " + str(current) + " / " + str(required) + " (" + str(progress) + "%)</font><br>"
            html += "<font color=\"WHITE\">Progress: " + str(current) + " / " + str(required) + " (" + str(progress) + "%)</font><br>"
            
            # Barra de progreso visual
            html += "<font color=\"GREEN\">"
            for i in range(0, 100, 5):
                if i < progress:
                    html += "█"
                else:
                    html += "░"
            html += "</font><br><br>"
        
        html += "<font color=\"LEVEL\">🎯 ESTADÍSTICAS PERSONALES / PERSONAL STATISTICS:</font><br>"
        html += "• Nivel actual: " + str(player.getLevel()) + " / Current level: " + str(player.getLevel()) + "<br>"
        html += "• Adena actual: " + str(player.getAdena()) + " / Current Adena: " + str(player.getAdena()) + "<br>"
        html += "• Kills PvP: En desarrollo / PvP Kills: In development<br>"
        html += "• Bosses matados: En desarrollo / Bosses killed: In development<br>"
        
        html += "<br><font color=\"LEVEL\">¡¡¡ SIGUE PROGRESANDO HACIA LA GLORIA ÉPICA !!!</font><br>"
        html += "<font color=\"LEVEL\">¡¡¡ KEEP PROGRESSING TOWARDS EPIC GLORY !!!</font><br>"
        
        html += "</body></html>"
        
        reply = NpcHtmlMessage(1)
        reply.setHtml(html)
        player.sendPacket(reply)
        return None
    
    def verRanking(self, player):
        html = "<html><body>"
        html += "<center><font color=\"LEVEL\">¡¡¡ RANKING DE ACHIEVEMENTS ÉPICOS !!!</font></center><br>"
        html += "<center><font color=\"LEVEL\">¡¡¡ EPIC ACHIEVEMENTS RANKING !!!</font></center><br><br>"
        
        html += "<font color=\"LEVEL\">🏆 TOP 10 JUGADORES / TOP 10 PLAYERS:</font><br><br>"
        
        # Simular ranking (en un servidor real, esto vendría de la base de datos)
        topPlayers = [
            {"name": "EpicHero1", "achievements": 8, "level": 80},
            {"name": "EpicHero2", "achievements": 7, "level": 78},
            {"name": "EpicHero3", "achievements": 6, "level": 75},
            {"name": "EpicHero4", "achievements": 5, "level": 72},
            {"name": "EpicHero5", "achievements": 4, "level": 70},
            {"name": "EpicHero6", "achievements": 3, "level": 68},
            {"name": "EpicHero7", "achievements": 2, "level": 65},
            {"name": "EpicHero8", "achievements": 1, "level": 60},
            {"name": "EpicHero9", "achievements": 0, "level": 55},
            {"name": "EpicHero10", "achievements": 0, "level": 50}
        ]
        
        for i, playerInfo in enumerate(topPlayers, 1):
            medal = "🥇" if i == 1 else "🥈" if i == 2 else "🥉" if i == 3 else "🏅"
            html += "<font color=\"LEVEL\">" + medal + " #" + str(i) + " " + playerInfo["name"] + "</font><br>"
            html += "<font color=\"WHITE\">Achievements: " + str(playerInfo["achievements"]) + " | Nivel: " + str(playerInfo["level"]) + "</font><br>"
            html += "<font color=\"WHITE\">Achievements: " + str(playerInfo["achievements"]) + " | Level: " + str(playerInfo["level"]) + "</font><br><br>"
        
        html += "<font color=\"LEVEL\">📊 ESTADÍSTICAS DEL SERVIDOR / SERVER STATISTICS:</font><br>"
        html += "• Total de jugadores: En desarrollo / Total players: In development<br>"
        html += "• Achievements desbloqueados: En desarrollo / Achievements unlocked: In development<br>"
        html += "• Promedio de nivel: En desarrollo / Average level: In development<br>"
        
        html += "<br><font color=\"LEVEL\">¡¡¡ COMPITE POR EL PRIMER LUGAR ÉPICO !!!</font><br>"
        html += "<font color=\"LEVEL\">¡¡¡ COMPETE FOR THE EPIC FIRST PLACE !!!</font><br>"
        
        html += "</body></html>"
        
        reply = NpcHtmlMessage(1)
        reply.setHtml(html)
        player.sendPacket(reply)
        return None
    
    def reclamarRecompensa(self, player):
        recompensasReclamadas = 0
        
        for achievementKey, achievementInfo in self.achievements.items():
            if achievementInfo["unlocked"] and not achievementInfo.get("claimed", False):
                # Dar recompensa
                player.addAdena("Achievement", achievementInfo["reward"]["adena"])
                
                for itemId, count in achievementInfo["reward"]["items"]:
                    player.addItem("Achievement", itemId, count, player, True)
                
                achievementInfo["claimed"] = True
                recompensasReclamadas += 1
                
                # Mensaje épico
                player.sendMessage("¡¡¡ ACHIEVEMENT DESBLOQUEADO: " + achievementInfo["name"] + " !!!")
                player.sendMessage("¡¡¡ ACHIEVEMENT UNLOCKED: " + achievementInfo["name"] + " !!!")
                player.sendMessage("¡Has recibido recompensas épicas!")
                player.sendMessage("You have received epic rewards!")
        
        if recompensasReclamadas > 0:
            # Anuncio épico
            self.announceToAll(player.getName() + " ha reclamado " + str(recompensasReclamadas) + " achievements épicos!")
            self.announceToAll(player.getName() + " has claimed " + str(recompensasReclamadas) + " epic achievements!")
            
            return "¡Has reclamado " + str(recompensasReclamadas) + " recompensas épicas!"
        else:
            return "No tienes recompensas disponibles para reclamar."
    
    def getCurrentProgress(self, player, progressType):
        if progressType == "level":
            return player.getLevel()
        elif progressType == "adena":
            return player.getAdena()
        elif progressType == "kills":
            return 0  # En desarrollo
        elif progressType == "pvp_kills":
            return 0  # En desarrollo
        elif progressType == "zones":
            return 0  # En desarrollo
        elif progressType == "boss_kills":
            return 0  # En desarrollo
        elif progressType == "events":
            return 0  # En desarrollo
        return 0
    
    def checkAchievements(self, player):
        for achievementKey, achievementInfo in self.achievements.items():
            if not achievementInfo["unlocked"]:
                current = self.getCurrentProgress(player, achievementInfo["type"])
                if current >= achievementInfo["requirement"]:
                    achievementInfo["unlocked"] = True
                    
                    # Mensaje épico
                    player.sendMessage("¡¡¡ ACHIEVEMENT DESBLOQUEADO: " + achievementInfo["name"] + " !!!")
                    player.sendMessage("¡¡¡ ACHIEVEMENT UNLOCKED: " + achievementInfo["name"] + " !!!")
                    
                    # Anuncio épico
                    self.announceToAll(player.getName() + " ha desbloqueado el achievement: " + achievementInfo["name"] + "!")
                    self.announceToAll(player.getName() + " has unlocked the achievement: " + achievementInfo["name"] + "!")
    
    def announceToAll(self, message):
        from l2jfrozen.gameserver.network.serverpackets import CreatureSay
        from l2jfrozen.gameserver.model.actor.instance import L2PcInstance
        from l2jfrozen.gameserver.GameServer import GameServer
        
        for player in GameServer.getInstance().getAllPlayers():
            if player and player.isOnline():
                player.sendPacket(CreatureSay(0, 1, "ACHIEVEMENTS ÉPICOS", message))

# Crear instancia del sistema de achievements épicos
ACHIEVEMENTS_EPICOS = EpicAchievements(-1, "AchievementsEpicos", "Sistema de Achievements Épicos")

# Registrar el sistema
ACHIEVEMENTS_EPICOS.addStartNpc(30006)  # Tienda GM
ACHIEVEMENTS_EPICOS.addTalkId(30006)



