# ===========================================
# PVP COMPETITIVO ÉPICO - L2 HERMANOS
# ===========================================
# Sistema de PvP competitivo con monetización
# Competitive PvP system with monetization

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

class EpicPvPCompetitive(JQuest):
    def __init__(self, id, name, descr):
        JQuest.__init__(self, id, name, descr)
        self.pvpZones = {
            "COLISEO": {
                "name": "Coliseo Épico",
                "description": "Arena de combate épica",
                "location": (149999, 46728, -3414),
                "cost": 0,
                "active": True
            },
            "RUINAS": {
                "name": "Ruinas Épicas",
                "description": "Zona de combate en ruinas",
                "location": (186000, -10000, -3000),
                "cost": 1000,
                "active": True
            },
            "GIRAN_PVP": {
                "name": "Giran PvP Zone",
                "description": "Zona PvP en Giran",
                "location": (81304, 14589, -3469),
                "cost": 500,
                "active": True
            }
        }
        
        self.killStreaks = {
            5: {"name": "Killing Spree", "reward": 1000, "announce": True},
            10: {"name": "Rampage", "reward": 2500, "announce": True},
            15: {"name": "Unstoppable", "reward": 5000, "announce": True},
            20: {"name": "Dominating", "reward": 10000, "announce": True},
            25: {"name": "Legendary", "reward": 25000, "announce": True},
            30: {"name": "Godlike", "reward": 50000, "announce": True}
        }
        
        self.weeklyRanking = {}
        self.playerStats = {}
        
    def onAdvEvent(self, event, npc, player):
        if event == "mostrar_pvp_competitivo":
            return self.mostrarPvPCompetitivo(player)
        elif event.startswith("entrar_zona_"):
            zoneKey = event.replace("entrar_zona_", "")
            return self.entrarZonaPvP(player, zoneKey)
        elif event == "ver_ranking_semanal":
            return self.verRankingSemanal(player)
        elif event == "ver_mis_estadisticas":
            return self.verMisEstadisticas(player)
        elif event == "ver_kill_streaks":
            return self.verKillStreaks(player)
        elif event == "ver_recompensas_semanales":
            return self.verRecompensasSemanales(player)
        return None
    
    def mostrarPvPCompetitivo(self, player):
        html = "<html><body>"
        html += "<center><font color=\"LEVEL\">¡¡¡ PVP COMPETITIVO ÉPICO DE L2 HERMANOS !!!</font></center><br>"
        html += "<center><font color=\"LEVEL\">¡¡¡ EPIC COMPETITIVE PVP OF L2 HERMANOS !!!</font></center><br><br>"
        
        html += "<font color=\"LEVEL\">⚔️ ZONAS PVP DISPONIBLES / AVAILABLE PVP ZONES:</font><br><br>"
        
        for zoneKey, zoneInfo in self.pvpZones.items():
            status = "🟢 ACTIVA" if zoneInfo["active"] else "🔴 INACTIVA"
            statusEn = "🟢 ACTIVE" if zoneInfo["active"] else "🔴 INACTIVE"
            costText = "GRATIS" if zoneInfo["cost"] == 0 else str(zoneInfo["cost"]) + " Adena"
            costTextEn = "FREE" if zoneInfo["cost"] == 0 else str(zoneInfo["cost"]) + " Adena"
            
            html += "<font color=\"LEVEL\">" + zoneInfo["name"] + "</font><br>"
            html += "<font color=\"WHITE\">" + zoneInfo["description"] + "</font><br>"
            html += "<font color=\"YELLOW\">Estado: " + status + " / Status: " + statusEn + "</font><br>"
            html += "<font color=\"GREEN\">Costo: " + costText + " / Cost: " + costTextEn + "</font><br>"
            html += "<button value=\"Entrar a " + zoneInfo["name"] + "\" action=\"bypass -h Quest EpicPvPCompetitive entrar_zona_" + zoneKey + "\" width=200 height=25 back=\"L2UI_ct1.button_df\" fore=\"L2UI_ct1.button_df\"><br><br>"
        
        html += "<font color=\"LEVEL\">🎯 ACCIONES DISPONIBLES / AVAILABLE ACTIONS:</font><br>"
        html += "<button value=\"Ver Ranking Semanal\" action=\"bypass -h Quest EpicPvPCompetitive ver_ranking_semanal\" width=200 height=25 back=\"L2UI_ct1.button_df\" fore=\"L2UI_ct1.button_df\"><br>"
        html += "<button value=\"Ver Mis Estadísticas\" action=\"bypass -h Quest EpicPvPCompetitive ver_mis_estadisticas\" width=200 height=25 back=\"L2UI_ct1.button_df\" fore=\"L2UI_ct1.button_df\"><br>"
        html += "<button value=\"Ver Kill Streaks\" action=\"bypass -h Quest EpicPvPCompetitive ver_kill_streaks\" width=200 height=25 back=\"L2UI_ct1.button_df\" fore=\"L2UI_ct1.button_df\"><br>"
        html += "<button value=\"Ver Recompensas Semanales\" action=\"bypass -h Quest EpicPvPCompetitive ver_recompensas_semanales\" width=200 height=25 back=\"L2UI_ct1.button_df\" fore=\"L2UI_ct1.button_df\"><br>"
        
        html += "<br><font color=\"LEVEL\">🏆 BENEFICIOS DE PVP COMPETITIVO / COMPETITIVE PVP BENEFITS:</font><br>"
        html += "• Buffs automáticos al entrar / Automatic buffs when entering<br>"
        html += "• Sin penalización por muerte / No death penalty<br>"
        html += "• Recompensas por kills / Rewards for kills<br>"
        html += "• Kill streaks épicos / Epic kill streaks<br>"
        html += "• Ranking semanal / Weekly ranking<br>"
        html += "• Recompensas semanales / Weekly rewards<br>"
        
        html += "<br><font color=\"LEVEL\">💰 MONETIZACIÓN / MONETIZATION:</font><br>"
        html += "• Scrolls de resurrección / Resurrection scrolls<br>"
        html += "• Títulos PvP exclusivos / Exclusive PvP titles<br>"
        html += "• Skins de armas épicas / Epic weapon skins<br>"
        html += "• Boosters PvP / PvP boosters<br>"
        html += "• Créditos por kills / Credits for kills<br>"
        
        html += "<br><font color=\"LEVEL\">¡¡¡ DOMINA EL PVP COMPETITIVO ÉPICO !!!</font><br>"
        html += "<font color=\"LEVEL\">¡¡¡ DOMINATE THE EPIC COMPETITIVE PVP !!!</font><br>"
        
        html += "</body></html>"
        
        reply = NpcHtmlMessage(1)
        reply.setHtml(html)
        player.sendPacket(reply)
        return None
    
    def entrarZonaPvP(self, player, zoneKey):
        if zoneKey not in self.pvpZones:
            return "Zona PvP no encontrada."
        
        zoneInfo = self.pvpZones[zoneKey]
        
        if not zoneInfo["active"]:
            return "La zona PvP está inactiva."
        
        # Verificar costo
        if zoneInfo["cost"] > 0:
            if player.getAdena() < zoneInfo["cost"]:
                return "No tienes suficiente Adena. Necesitas: " + str(zoneInfo["cost"])
            
            # Cobrar costo
            player.reduceAdena("PvPZone", zoneInfo["cost"])
        
        # Teleportar a la zona PvP
        x, y, z = zoneInfo["location"]
        player.teleToLocation(x, y, z)
        
        # Activar PvP flag automático
        player.setPvpFlag(1)
        
        # Dar buffs épicos automáticos
        self.darBuffsEpicos(player)
        
        # Inicializar estadísticas si no existen
        if player.getName() not in self.playerStats:
            self.playerStats[player.getName()] = {
                "kills": 0,
                "deaths": 0,
                "killStreak": 0,
                "bestStreak": 0,
                "credits": 0
            }
        
        # Mensaje épico
        player.sendMessage("¡¡¡ BIENVENIDO AL " + zoneInfo["name"].upper() + " !!!")
        player.sendMessage("¡¡¡ WELCOME TO THE " + zoneInfo["name"].upper() + " !!!")
        player.sendMessage("¡PvP flag activado! ¡Combate épico iniciado!")
        player.sendMessage("PvP flag activated! Epic combat started!")
        
        # Anuncio épico
        self.announceToAll(player.getName() + " ha entrado al " + zoneInfo["name"] + "!")
        self.announceToAll(player.getName() + " has entered the " + zoneInfo["name"] + "!")
        
        return "¡Bienvenido al " + zoneInfo["name"] + "!"
    
    def darBuffsEpicos(self, player):
        # Buffs épicos para PvP
        epicBuffs = [1085, 1086, 1087, 1044, 1045, 1047, 1048, 1049, 1059, 1062]
        for buffId in epicBuffs:
            player.addSkill(buffId, 3)
        
        player.sendMessage("¡Has recibido buffs épicos para PvP!")
        player.sendMessage("You have received epic buffs for PvP!")
    
    def verRankingSemanal(self, player):
        html = "<html><body>"
        html += "<center><font color=\"LEVEL\">¡¡¡ RANKING SEMANAL PVP ÉPICO !!!</font></center><br>"
        html += "<center><font color=\"LEVEL\">¡¡¡ EPIC WEEKLY PVP RANKING !!!</font></center><br><br>"
        
        html += "<font color=\"LEVEL\">🏆 TOP 20 PVP KILLERS / TOP 20 PVP KILLERS:</font><br><br>"
        
        # Simular ranking semanal (en un servidor real, esto vendría de la base de datos)
        topPlayers = self.generarRankingPvPSimulado()
        
        for i, playerInfo in enumerate(topPlayers, 1):
            medal = "🥇" if i == 1 else "🥈" if i == 2 else "🥉" if i == 3 else "🏅"
            html += "<font color=\"LEVEL\">" + medal + " #" + str(i) + " " + playerInfo["name"] + "</font><br>"
            html += "<font color=\"WHITE\">Kills: " + str(playerInfo["kills"]) + " | Deaths: " + str(playerInfo["deaths"]) + " | Streak: " + str(playerInfo["streak"]) + "</font><br>"
            html += "<font color=\"WHITE\">Kills: " + str(playerInfo["kills"]) + " | Deaths: " + str(playerInfo["deaths"]) + " | Streak: " + str(playerInfo["streak"]) + "</font><br><br>"
        
        html += "<font color=\"LEVEL\">💰 RECOMPENSAS SEMANALES / WEEKLY REWARDS:</font><br>"
        html += "• Top 1: 100,000 Créditos + Título \"Rey del PvP\"<br>"
        html += "• Top 2: 75,000 Créditos + Título \"Príncipe del PvP\"<br>"
        html += "• Top 3: 50,000 Créditos + Título \"Duque del PvP\"<br>"
        html += "• Top 5: 25,000 Créditos + Título \"Caballero del PvP\"<br>"
        html += "• Top 10: 10,000 Créditos + Título \"Guerrero del PvP\"<br>"
        
        html += "<br><font color=\"LEVEL\">🔄 RESET SEMANAL / WEEKLY RESET:</font><br>"
        html += "• Cada domingo a las 00:00 / Every Sunday at 00:00<br>"
        html += "• Recompensas automáticas / Automatic rewards<br>"
        html += "• Ranking se reinicia / Ranking resets<br>"
        
        html += "<br><font color=\"LEVEL\">¡¡¡ COMPITE POR EL PRIMER LUGAR ÉPICO !!!</font><br>"
        html += "<font color=\"LEVEL\">¡¡¡ COMPETE FOR THE EPIC FIRST PLACE !!!</font><br>"
        
        html += "</body></html>"
        
        reply = NpcHtmlMessage(1)
        reply.setHtml(html)
        player.sendPacket(reply)
        return None
    
    def verMisEstadisticas(self, player):
        playerName = player.getName()
        stats = self.playerStats.get(playerName, {
            "kills": 0,
            "deaths": 0,
            "killStreak": 0,
            "bestStreak": 0,
            "credits": 0
        })
        
        html = "<html><body>"
        html += "<center><font color=\"LEVEL\">¡¡¡ MIS ESTADÍSTICAS PVP ÉPICAS !!!</font></center><br>"
        html += "<center><font color=\"LEVEL\">¡¡¡ MY EPIC PVP STATISTICS !!!</font></center><br><br>"
        
        html += "<font color=\"LEVEL\">📊 ESTADÍSTICAS PERSONALES / PERSONAL STATISTICS:</font><br><br>"
        html += "• Kills totales: " + str(stats["kills"]) + " / Total kills: " + str(stats["kills"]) + "<br>"
        html += "• Muertes totales: " + str(stats["deaths"]) + " / Total deaths: " + str(stats["deaths"]) + "<br>"
        html += "• Kill streak actual: " + str(stats["killStreak"]) + " / Current kill streak: " + str(stats["killStreak"]) + "<br>"
        html += "• Mejor kill streak: " + str(stats["bestStreak"]) + " / Best kill streak: " + str(stats["bestStreak"]) + "<br>"
        html += "• Créditos ganados: " + str(stats["credits"]) + " / Credits earned: " + str(stats["credits"]) + "<br>"
        
        # Calcular ratio
        ratio = stats["kills"] / max(1, stats["deaths"])
        html += "• Ratio K/D: " + str(round(ratio, 2)) + " / K/D Ratio: " + str(round(ratio, 2)) + "<br>"
        
        html += "<br><font color=\"LEVEL\">🎯 LOGROS DESBLOQUEADOS / UNLOCKED ACHIEVEMENTS:</font><br>"
        
        # Verificar logros
        if stats["kills"] >= 100:
            html += "• ✅ Asesino Épico (100+ kills) / Epic Killer (100+ kills)<br>"
        if stats["kills"] >= 500:
            html += "• ✅ Maestro del PvP (500+ kills) / PvP Master (500+ kills)<br>"
        if stats["kills"] >= 1000:
            html += "• ✅ Leyenda del PvP (1000+ kills) / PvP Legend (1000+ kills)<br>"
        if stats["bestStreak"] >= 10:
            html += "• ✅ Kill Streak Master (10+ streak) / Kill Streak Master (10+ streak)<br>"
        if stats["bestStreak"] >= 25:
            html += "• ✅ Kill Streak Legend (25+ streak) / Kill Streak Legend (25+ streak)<br>"
        
        html += "<br><font color=\"LEVEL\">🏆 POSICIÓN EN RANKING / RANKING POSITION:</font><br>"
        position = self.calcularPosicionRanking(playerName)
        html += "• Posición actual: #" + str(position) + " / Current position: #" + str(position) + "<br>"
        
        html += "<br><font color=\"LEVEL\">¡¡¡ SIGUE COMBATIENDO PARA MEJORAR TUS ESTADÍSTICAS !!!</font><br>"
        html += "<font color=\"LEVEL\">¡¡¡ KEEP FIGHTING TO IMPROVE YOUR STATISTICS !!!</font><br>"
        
        html += "</body></html>"
        
        reply = NpcHtmlMessage(1)
        reply.setHtml(html)
        player.sendPacket(reply)
        return None
    
    def verKillStreaks(self, player):
        html = "<html><body>"
        html += "<center><font color=\"LEVEL\">¡¡¡ KILL STREAKS ÉPICOS !!!</font></center><br>"
        html += "<center><font color=\"LEVEL\">¡¡¡ EPIC KILL STREAKS !!!</font></center><br><br>"
        
        html += "<font color=\"LEVEL\">🔥 KILL STREAKS DISPONIBLES / AVAILABLE KILL STREAKS:</font><br><br>"
        
        for streak, info in self.killStreaks.items():
            html += "<font color=\"LEVEL\">" + str(streak) + " Kills - " + info["name"] + "</font><br>"
            html += "<font color=\"WHITE\">Recompensa: " + str(info["reward"]) + " Créditos / Reward: " + str(info["reward"]) + " Credits</font><br>"
            if info["announce"]:
                html += "<font color=\"YELLOW\">✅ Anuncio global / Global announcement</font><br>"
            html += "<br>"
        
        html += "<font color=\"LEVEL\">💰 CÓMO FUNCIONAN / HOW THEY WORK:</font><br>"
        html += "• Mata jugadores consecutivamente / Kill players consecutively<br>"
        html += "• Sin morir entre kills / Without dying between kills<br>"
        html += "• Recompensas automáticas / Automatic rewards<br>"
        html += "• Anuncios épicos / Epic announcements<br>"
        html += "• Créditos instantáneos / Instant credits<br>"
        
        html += "<br><font color=\"LEVEL\">🎯 CONSEJOS PARA KILL STREAKS / KILL STREAK TIPS:</font><br>"
        html += "• Usa buffs épicos / Use epic buffs<br>"
        html += "• Combate en grupo / Fight in groups<br>"
        html += "• Conoce las zonas PvP / Know the PvP zones<br>"
        html += "• Usa items de resurrección / Use resurrection items<br>"
        
        html += "<br><font color=\"LEVEL\">¡¡¡ ALCANZA KILL STREAKS ÉPICOS !!!</font><br>"
        html += "<font color=\"LEVEL\">¡¡¡ ACHIEVE EPIC KILL STREAKS !!!</font><br>"
        
        html += "</body></html>"
        
        reply = NpcHtmlMessage(1)
        reply.setHtml(html)
        player.sendPacket(reply)
        return None
    
    def verRecompensasSemanales(self, player):
        html = "<html><body>"
        html += "<center><font color=\"LEVEL\">¡¡¡ RECOMPENSAS SEMANALES PVP ÉPICAS !!!</font></center><br>"
        html += "<center><font color=\"LEVEL\">¡¡¡ EPIC WEEKLY PVP REWARDS !!!</font></center><br><br>"
        
        html += "<font color=\"LEVEL\">🏆 RECOMPENSAS POR POSICIÓN / POSITION REWARDS:</font><br><br>"
        html += "• 🥇 Top 1: 100,000 Créditos + Título \"Rey del PvP\" + Skin épica<br>"
        html += "• 🥈 Top 2: 75,000 Créditos + Título \"Príncipe del PvP\" + Skin épica<br>"
        html += "• 🥉 Top 3: 50,000 Créditos + Título \"Duque del PvP\" + Skin épica<br>"
        html += "• 🏅 Top 5: 25,000 Créditos + Título \"Caballero del PvP\"<br>"
        html += "• 🏅 Top 10: 10,000 Créditos + Título \"Guerrero del PvP\"<br>"
        html += "• 🏅 Top 20: 5,000 Créditos + Título \"Soldado del PvP\"<br>"
        html += "• 🏅 Top 50: 2,500 Créditos + Título \"Novato del PvP\"<br>"
        
        html += "<br><font color=\"LEVEL\">💰 RECOMPENSAS POR KILL STREAKS / KILL STREAK REWARDS:</font><br>"
        html += "• 5 Kills: 1,000 Créditos + Anuncio global<br>"
        html += "• 10 Kills: 2,500 Créditos + Anuncio global<br>"
        html += "• 15 Kills: 5,000 Créditos + Anuncio global<br>"
        html += "• 20 Kills: 10,000 Créditos + Anuncio global<br>"
        html += "• 25 Kills: 25,000 Créditos + Anuncio global<br>"
        html += "• 30 Kills: 50,000 Créditos + Anuncio global<br>"
        
        html += "<br><font color=\"LEVEL\">🎁 RECOMPENSAS ESPECIALES / SPECIAL REWARDS:</font><br>"
        html += "• MVP del día: 5,000 Créditos + Título \"MVP del Día\"<br>"
        html += "• Más kills en 1 hora: 10,000 Créditos + Título \"Rey de la Hora\"<br>"
        html += "• Mejor ratio K/D: 15,000 Créditos + Título \"Precisión Épica\"<br>"
        html += "• Más participaciones: 8,000 Créditos + Título \"Guerrero Incansable\"<br>"
        
        html += "<br><font color=\"LEVEL\">🔄 SISTEMA DE ENTREGA / DELIVERY SYSTEM:</font><br>"
        html += "• Recompensas automáticas / Automatic rewards<br>"
        html += "• Entrega cada domingo / Delivery every Sunday<br>"
        html += "• Créditos instantáneos / Instant credits<br>"
        html += "• Títulos automáticos / Automatic titles<br>"
        html += "• Skins automáticas / Automatic skins<br>"
        
        html += "<br><font color=\"LEVEL\">¡¡¡ COMPITE POR LAS MEJORES RECOMPENSAS ÉPICAS !!!</font><br>"
        html += "<font color=\"LEVEL\">¡¡¡ COMPETE FOR THE BEST EPIC REWARDS !!!</font><br>"
        
        html += "</body></html>"
        
        reply = NpcHtmlMessage(1)
        reply.setHtml(html)
        player.sendPacket(reply)
        return None
    
    def generarRankingPvPSimulado(self):
        # Simular ranking PvP (en un servidor real, esto vendría de la base de datos)
        players = []
        for i in range(20):
            players.append({
                "name": "EpicPvP" + str(i+1),
                "kills": 1000 - i * 50,
                "deaths": 100 + i * 10,
                "streak": 30 - i
            })
        return players
    
    def calcularPosicionRanking(self, playerName):
        # Simular posición (en un servidor real, esto se calcularía de la base de datos)
        return 25  # Posición promedio
    
    def onKill(self, npc, player, isPet):
        if isinstance(npc, L2PcInstance) and isinstance(player, L2PcInstance):
            # Verificar si ambos están en zona PvP
            if self.estaEnZonaPvP(player) and self.estaEnZonaPvP(npc):
                self.procesarKillPvP(player, npc)
        return None
    
    def estaEnZonaPvP(self, player):
        # Verificar si el jugador está en alguna zona PvP
        for zoneInfo in self.pvpZones.values():
            x, y, z = zoneInfo["location"]
            if abs(player.getX() - x) < 1000 and abs(player.getY() - y) < 1000:
                return True
        return False
    
    def procesarKillPvP(self, killer, victim):
        killerName = killer.getName()
        victimName = victim.getName()
        
        # Inicializar estadísticas si no existen
        if killerName not in self.playerStats:
            self.playerStats[killerName] = {
                "kills": 0,
                "deaths": 0,
                "killStreak": 0,
                "bestStreak": 0,
                "credits": 0
            }
        
        if victimName not in self.playerStats:
            self.playerStats[victimName] = {
                "kills": 0,
                "deaths": 0,
                "killStreak": 0,
                "bestStreak": 0,
                "credits": 0
            }
        
        # Actualizar estadísticas del killer
        self.playerStats[killerName]["kills"] += 1
        self.playerStats[killerName]["killStreak"] += 1
        
        # Actualizar mejor streak
        if self.playerStats[killerName]["killStreak"] > self.playerStats[killerName]["bestStreak"]:
            self.playerStats[killerName]["bestStreak"] = self.playerStats[killerName]["killStreak"]
        
        # Actualizar estadísticas de la víctima
        self.playerStats[victimName]["deaths"] += 1
        self.playerStats[victimName]["killStreak"] = 0
        
        # Verificar kill streaks
        currentStreak = self.playerStats[killerName]["killStreak"]
        if currentStreak in self.killStreaks:
            streakInfo = self.killStreaks[currentStreak]
            
            # Dar recompensa
            self.playerStats[killerName]["credits"] += streakInfo["reward"]
            
            # Anuncio épico
            if streakInfo["announce"]:
                self.announceToAll("¡¡¡ " + killerName + " ALCANZÓ " + streakInfo["name"] + " (" + str(currentStreak) + " KILLS) !!!")
                self.announceToAll("¡¡¡ " + killerName + " ACHIEVED " + streakInfo["name"] + " (" + str(currentStreak") + " KILLS) !!!")
                self.announceToAll("¡¡¡ RECOMPENSA: " + str(streakInfo["reward"]) + " CRÉDITOS !!!")
                self.announceToAll("¡¡¡ REWARD: " + str(streakInfo["reward"]) + " CREDITS !!!")
            
            # Mensaje al killer
            killer.sendMessage("¡¡¡ " + streakInfo["name"] + " ALCANZADO !!!")
            killer.sendMessage("¡¡¡ " + streakInfo["name"] + " ACHIEVED !!!")
            killer.sendMessage("¡Recompensa: " + str(streakInfo["reward"]) + " Créditos!")
            killer.sendMessage("Reward: " + str(streakInfo["reward"]) + " Credits!")
        
        # Recompensa básica por kill
        basicReward = 100
        self.playerStats[killerName]["credits"] += basicReward
        
        # Mensaje al killer
        killer.sendMessage("¡¡¡ KILL ÉPICO !!! +" + str(basicReward) + " Créditos!")
        killer.sendMessage("¡¡¡ EPIC KILL !!! +" + str(basicReward) + " Credits!")
        
        # Anuncio del kill
        self.announceToAll(killerName + " eliminó a " + victimName + " en PvP Épico!")
        self.announceToAll(killerName + " eliminated " + victimName + " in Epic PvP!")
    
    def announceToAll(self, message):
        from l2jfrozen.gameserver.network.serverpackets import CreatureSay
        from l2jfrozen.gameserver.model.actor.instance import L2PcInstance
        from l2jfrozen.gameserver.GameServer import GameServer
        
        for player in GameServer.getInstance().getAllPlayers():
            if player and player.isOnline():
                player.sendPacket(CreatureSay(0, 1, "PVP COMPETITIVO ÉPICO", message))

# Crear instancia del sistema de PvP competitivo épico
PVP_COMPETITIVO_EPICO = EpicPvPCompetitive(-1, "PvPCompetitivoEpico", "Sistema de PvP Competitivo Épico")

# Registrar el sistema
PVP_COMPETITIVO_EPICO.addStartNpc(30006)  # Tienda GM
PVP_COMPETITIVO_EPICO.addTalkId(30006)



