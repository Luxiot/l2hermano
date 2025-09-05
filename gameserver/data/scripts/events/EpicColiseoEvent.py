# ===========================================
# EVENTO RELÁMPAGO "EL REY DEL COLISEO" - L2 HERMANOS
# ===========================================
# Evento relámpago de PvP con premios reales
# Lightning PvP event with real prizes

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

class EpicColiseoEvent(JQuest):
    def __init__(self, id, name, descr):
        JQuest.__init__(self, id, name, descr)
        self.eventActive = False
        self.participants = []
        self.kills = {}
        self.startTime = 0
        self.duration = 3600000  # 1 hora en milisegundos
        self.coliseoLocation = (149999, 46728, -3414)  # Coliseo épico
        
    def onAdvEvent(self, event, npc, player):
        if event == "mostrar_evento_coliseo":
            return self.mostrarEventoColiseo(player)
        elif event == "unirse_evento_coliseo":
            return self.unirseEventoColiseo(player)
        elif event == "iniciar_evento_coliseo":
            return self.iniciarEventoColiseo(player)
        elif event == "detener_evento_coliseo":
            return self.detenerEventoColiseo(player)
        elif event == "ver_ranking_coliseo":
            return self.verRankingColiseo(player)
        elif event == "ver_recompensas_coliseo":
            return self.verRecompensasColiseo(player)
        return None
    
    def mostrarEventoColiseo(self, player):
        html = "<html><body>"
        html += "<center><font color=\"LEVEL\">¡¡¡ EL REY DEL COLISEO ÉPICO !!!</font></center><br>"
        html += "<center><font color=\"LEVEL\">¡¡¡ THE EPIC COLISEUM KING !!!</font></center><br><br>"
        
        if self.eventActive:
            timeLeft = self.duration - (System.currentTimeMillis() - self.startTime)
            minutesLeft = max(0, timeLeft // 60000)
            html += "<font color=\"LEVEL\">🔥 EVENTO ACTIVO / ACTIVE EVENT:</font><br>"
            html += "<font color=\"YELLOW\">Tiempo restante: " + str(minutesLeft) + " minutos / Time left: " + str(minutesLeft) + " minutes</font><br>"
            html += "<font color=\"YELLOW\">Participantes: " + str(len(self.participants)) + " / Participants: " + str(len(self.participants)) + "</font><br><br>"
        else:
            html += "<font color=\"RED\">❌ EVENTO INACTIVO / INACTIVE EVENT</font><br><br>"
        
        html += "<font color=\"LEVEL\">⚔️ DESCRIPCIÓN DEL EVENTO / EVENT DESCRIPTION:</font><br>"
        html += "• Duración: 1 hora / Duration: 1 hour<br>"
        html += "• Zona: Coliseo Épico / Zone: Epic Coliseum<br>"
        html += "• Objetivo: Más kills en 1 hora / Objective: Most kills in 1 hour<br>"
        html += "• PvP: Sin penalización / PvP: No penalty<br>"
        html += "• Respawn: Instantáneo / Respawn: Instant<br>"
        
        html += "<br><font color=\"LEVEL\">🏆 RECOMPENSAS ÉPICAS / EPIC REWARDS:</font><br>"
        html += "• 🥇 1er Lugar: 500 Créditos + Título \"Rey del Coliseo\"<br>"
        html += "• 🥈 2do Lugar: 300 Créditos + Título \"Príncipe del Coliseo\"<br>"
        html += "• 🥉 3er Lugar: 200 Créditos + Título \"Duque del Coliseo\"<br>"
        html += "• 🏅 Top 10: 100 Créditos + Título \"Guerrero del Coliseo\"<br>"
        html += "• 🏅 Participantes: 50 Créditos + Título \"Gladiador\"<br>"
        
        html += "<br><font color=\"LEVEL\">🎯 ACCIONES DISPONIBLES / AVAILABLE ACTIONS:</font><br>"
        
        if self.eventActive:
            if player in self.participants:
                html += "<font color=\"GREEN\">✅ Ya estás participando / You are already participating</font><br>"
            else:
                html += "<button value=\"Unirse al Evento\" action=\"bypass -h Quest EpicColiseoEvent unirse_evento_coliseo\" width=200 height=25 back=\"L2UI_ct1.button_df\" fore=\"L2UI_ct1.button_df\"><br>"
        else:
            html += "<button value=\"Iniciar Evento\" action=\"bypass -h Quest EpicColiseoEvent iniciar_evento_coliseo\" width=200 height=25 back=\"L2UI_ct1.button_df\" fore=\"L2UI_ct1.button_df\"><br>"
        
        html += "<button value=\"Ver Ranking\" action=\"bypass -h Quest EpicColiseoEvent ver_ranking_coliseo\" width=200 height=25 back=\"L2UI_ct1.button_df\" fore=\"L2UI_ct1.button_df\"><br>"
        html += "<button value=\"Ver Recompensas\" action=\"bypass -h Quest EpicColiseoEvent ver_recompensas_coliseo\" width=200 height=25 back=\"L2UI_ct1.button_df\" fore=\"L2UI_ct1.button_df\"><br>"
        
        html += "<br><font color=\"LEVEL\">💰 PREMIOS REALES / REAL PRIZES:</font><br>"
        html += "• Créditos canjeables por items épicos / Credits exchangeable for epic items<br>"
        html += "• Títulos exclusivos / Exclusive titles<br>"
        html += "• Reconocimiento en el servidor / Server recognition<br>"
        html += "• Acceso a zonas VIP / VIP zone access<br>"
        
        html += "<br><font color=\"LEVEL\">¡¡¡ CONVIÉRTETE EN EL REY DEL COLISEO !!!</font><br>"
        html += "<font color=\"LEVEL\">¡¡¡ BECOME THE COLISEUM KING !!!</font><br>"
        
        html += "</body></html>"
        
        reply = NpcHtmlMessage(1)
        reply.setHtml(html)
        player.sendPacket(reply)
        return None
    
    def unirseEventoColiseo(self, player):
        if not self.eventActive:
            return "El evento no está activo."
        
        if player in self.participants:
            return "Ya estás participando en el evento."
        
        # Agregar participante
        self.participants.append(player)
        self.kills[player] = 0
        
        # Teleportar al Coliseo
        player.teleToLocation(self.coliseoLocation[0], self.coliseoLocation[1], self.coliseoLocation[2])
        
        # Activar PvP flag
        player.setPvpFlag(1)
        
        # Dar buffs épicos
        self.darBuffsEpicos(player)
        
        # Mensaje épico
        player.sendMessage("¡¡¡ BIENVENIDO AL REY DEL COLISEO ÉPICO !!!")
        player.sendMessage("¡¡¡ WELCOME TO THE EPIC COLISEUM KING !!!")
        player.sendMessage("¡Combate épico iniciado! ¡Mata a otros jugadores!")
        player.sendMessage("Epic combat started! Kill other players!")
        
        # Anuncio épico
        self.announceToAll(player.getName() + " se ha unido al REY DEL COLISEO ÉPICO!")
        self.announceToAll(player.getName() + " has joined the EPIC COLISEUM KING!")
        self.announceToAll("¡Participantes: " + str(len(self.participants)) + "!")
        self.announceToAll("Participants: " + str(len(self.participants)) + "!")
        
        return "¡Te has unido al REY DEL COLISEO ÉPICO!"
    
    def iniciarEventoColiseo(self, player):
        if self.eventActive:
            return "El evento ya está activo."
        
        # Iniciar evento
        self.eventActive = True
        self.startTime = System.currentTimeMillis()
        self.participants = []
        self.kills = {}
        
        # Anuncio épico
        self.announceToAll("¡¡¡ EL REY DEL COLISEO ÉPICO HA COMENZADO !!!")
        self.announceToAll("¡¡¡ THE EPIC COLISEUM KING HAS STARTED !!!")
        self.announceToAll("¡¡¡ DURACIÓN: 1 HORA - PREMIO: 500 CRÉDITOS !!!")
        self.announceToAll("¡¡¡ DURATION: 1 HOUR - PRIZE: 500 CREDITS !!!")
        self.announceToAll("¡¡¡ ÚNETE AL COLISEO PARA PARTICIPAR !!!")
        self.announceToAll("¡¡¡ JOIN THE COLISEUM TO PARTICIPATE !!!")
        
        # Programar fin del evento
        self.startQuestTimer("finalizar_evento_coliseo", self.duration, None, None)
        
        # Mensaje épico
        player.sendMessage("¡¡¡ EVENTO REY DEL COLISEO INICIADO !!!")
        player.sendMessage("¡¡¡ COLISEUM KING EVENT STARTED !!!")
        
        return "¡Evento REY DEL COLISEO iniciado!"
    
    def detenerEventoColiseo(self, player):
        if not self.eventActive:
            return "El evento no está activo."
        
        # Finalizar evento
        self.finalizarEvento()
        
        # Mensaje épico
        player.sendMessage("¡¡¡ EVENTO REY DEL COLISEO DETENIDO !!!")
        player.sendMessage("¡¡¡ COLISEUM KING EVENT STOPPED !!!")
        
        return "¡Evento REY DEL COLISEO detenido!"
    
    def verRankingColiseo(self, player):
        html = "<html><body>"
        html += "<center><font color=\"LEVEL\">¡¡¡ RANKING DEL REY DEL COLISEO !!!</font></center><br>"
        html += "<center><font color=\"LEVEL\">¡¡¡ COLISEUM KING RANKING !!!</font></center><br><br>"
        
        if self.eventActive:
            timeLeft = self.duration - (System.currentTimeMillis() - self.startTime)
            minutesLeft = max(0, timeLeft // 60000)
            html += "<font color=\"LEVEL\">🔥 EVENTO ACTIVO / ACTIVE EVENT:</font><br>"
            html += "<font color=\"YELLOW\">Tiempo restante: " + str(minutesLeft) + " minutos / Time left: " + str(minutesLeft) + " minutes</font><br><br>"
        
        html += "<font color=\"LEVEL\">🏆 RANKING ACTUAL / CURRENT RANKING:</font><br><br>"
        
        if self.kills:
            # Ordenar por kills
            sortedKills = sorted(self.kills.items(), key=lambda x: x[1], reverse=True)
            
            for i, (player, kills) in enumerate(sortedKills[:20], 1):
                medal = "🥇" if i == 1 else "🥈" if i == 2 else "🥉" if i == 3 else "🏅"
                html += "<font color=\"LEVEL\">" + medal + " #" + str(i) + " " + player.getName() + "</font><br>"
                html += "<font color=\"WHITE\">Kills: " + str(kills) + " | Nivel: " + str(player.getLevel()) + "</font><br>"
                html += "<font color=\"WHITE\">Kills: " + str(kills) + " | Level: " + str(player.getLevel()) + "</font><br><br>"
        else:
            html += "<font color=\"WHITE\">No hay participantes aún / No participants yet</font><br><br>"
        
        html += "<font color=\"LEVEL\">📊 ESTADÍSTICAS DEL EVENTO / EVENT STATISTICS:</font><br>"
        html += "• Participantes: " + str(len(self.participants)) + " / Participants: " + str(len(self.participants)) + "<br>"
        html += "• Kills totales: " + str(sum(self.kills.values())) + " / Total kills: " + str(sum(self.kills.values())) + "<br>"
        html += "• Tiempo transcurrido: En desarrollo / Time elapsed: In development<br>"
        
        html += "<br><font color=\"LEVEL\">¡¡¡ COMPITE POR EL PRIMER LUGAR ÉPICO !!!</font><br>"
        html += "<font color=\"LEVEL\">¡¡¡ COMPETE FOR THE EPIC FIRST PLACE !!!</font><br>"
        
        html += "</body></html>"
        
        reply = NpcHtmlMessage(1)
        reply.setHtml(html)
        player.sendPacket(reply)
        return None
    
    def verRecompensasColiseo(self, player):
        html = "<html><body>"
        html += "<center><font color=\"LEVEL\">¡¡¡ RECOMPENSAS DEL REY DEL COLISEO !!!</font></center><br>"
        html += "<center><font color=\"LEVEL\">¡¡¡ COLISEUM KING REWARDS !!!</font></center><br><br>"
        
        html += "<font color=\"LEVEL\">🏆 RECOMPENSAS POR POSICIÓN / POSITION REWARDS:</font><br><br>"
        html += "• 🥇 1er Lugar: 500 Créditos + Título \"Rey del Coliseo\" + Skin épica<br>"
        html += "• 🥈 2do Lugar: 300 Créditos + Título \"Príncipe del Coliseo\" + Skin épica<br>"
        html += "• 🥉 3er Lugar: 200 Créditos + Título \"Duque del Coliseo\" + Skin épica<br>"
        html += "• 🏅 Top 5: 150 Créditos + Título \"Caballero del Coliseo\"<br>"
        html += "• 🏅 Top 10: 100 Créditos + Título \"Guerrero del Coliseo\"<br>"
        html += "• 🏅 Top 20: 75 Créditos + Título \"Soldado del Coliseo\"<br>"
        html += "• 🏅 Participantes: 50 Créditos + Título \"Gladiador\"<br>"
        
        html += "<br><font color=\"LEVEL\">💰 RECOMPENSAS ESPECIALES / SPECIAL REWARDS:</font><br>"
        html += "• MVP del evento: 100 Créditos extra / Event MVP: 100 extra credits<br>"
        html += "• Más kills en 1 hora: 200 Créditos extra / Most kills in 1 hour: 200 extra credits<br>"
        html += "• Mejor ratio K/D: 150 Créditos extra / Best K/D ratio: 150 extra credits<br>"
        html += "• Más participaciones: 100 Créditos extra / Most participations: 100 extra credits<br>"
        
        html += "<br><font color=\"LEVEL\">🎁 ITEMS DISPONIBLES CON CRÉDITOS / ITEMS AVAILABLE WITH CREDITS:</font><br>"
        html += "• Scrolls de resurrección / Resurrection scrolls<br>"
        html += "• Títulos PvP exclusivos / Exclusive PvP titles<br>"
        html += "• Skins de armas épicas / Epic weapon skins<br>"
        html += "• Boosters PvP / PvP boosters<br>"
        html += "• Paquetes VIP / VIP packages<br>"
        
        html += "<br><font color=\"LEVEL\">🔄 SISTEMA DE ENTREGA / DELIVERY SYSTEM:</font><br>"
        html += "• Recompensas automáticas al final / Automatic rewards at the end<br>"
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
    
    def darBuffsEpicos(self, player):
        # Buffs épicos para el Coliseo
        epicBuffs = [1085, 1086, 1087, 1044, 1045, 1047, 1048, 1049, 1059, 1062]
        for buffId in epicBuffs:
            player.addSkill(buffId, 3)
        
        player.sendMessage("¡Has recibido buffs épicos para el Coliseo!")
        player.sendMessage("You have received epic buffs for the Coliseum!")
    
    def onKill(self, npc, player, isPet):
        if self.eventActive and isinstance(npc, L2PcInstance) and isinstance(player, L2PcInstance):
            # Verificar si ambos están en el evento
            if player in self.participants and npc in self.participants:
                # Actualizar kills
                self.kills[player] = self.kills.get(player, 0) + 1
                
                # Recompensa inmediata
                player.addAdena("Coliseo", 10000)
                
                # Anuncio del kill
                self.announceToAll(player.getName() + " eliminó a " + npc.getName() + " en el REY DEL COLISEO!")
                self.announceToAll(player.getName() + " eliminated " + npc.getName() + " in the COLISEUM KING!")
                self.announceToAll("¡Kills totales: " + str(self.kills[player]) + "!")
                self.announceToAll("Total kills: " + str(self.kills[player]) + "!")
                
                # Verificar si es el líder
                if self.kills[player] == max(self.kills.values()):
                    self.announceToAll("¡¡¡ " + player.getName() + " ES EL NUEVO LÍDER DEL COLISEO !!!")
                    self.announceToAll("¡¡¡ " + player.getName() + " IS THE NEW COLISEUM LEADER !!!")
        
        return None
    
    def finalizarEvento(self):
        self.eventActive = False
        
        # Calcular ganadores
        if self.kills:
            sortedKills = sorted(self.kills.items(), key=lambda x: x[1], reverse=True)
            
            # Recompensas para los ganadores
            for i, (player, kills) in enumerate(sortedKills[:20], 1):
                if i == 1:
                    # 1er lugar
                    self.darRecompensa(player, 500, "Rey del Coliseo")
                    self.announceToAll("¡¡¡ " + player.getName() + " ES EL REY DEL COLISEO ÉPICO !!!")
                    self.announceToAll("¡¡¡ " + player.getName() + " IS THE EPIC COLISEUM KING !!!")
                elif i == 2:
                    # 2do lugar
                    self.darRecompensa(player, 300, "Príncipe del Coliseo")
                elif i == 3:
                    # 3er lugar
                    self.darRecompensa(player, 200, "Duque del Coliseo")
                elif i <= 5:
                    # Top 5
                    self.darRecompensa(player, 150, "Caballero del Coliseo")
                elif i <= 10:
                    # Top 10
                    self.darRecompensa(player, 100, "Guerrero del Coliseo")
                elif i <= 20:
                    # Top 20
                    self.darRecompensa(player, 75, "Soldado del Coliseo")
                else:
                    # Participantes
                    self.darRecompensa(player, 50, "Gladiador")
        
        # Recompensas para todos los participantes
        for player in self.participants:
            if player and player.isOnline():
                if player not in self.kills:
                    self.darRecompensa(player, 50, "Gladiador")
        
        # Anuncio de fin
        self.announceToAll("¡¡¡ EL REY DEL COLISEO ÉPICO HA TERMINADO !!!")
        self.announceToAll("¡¡¡ THE EPIC COLISEUM KING HAS ENDED !!!")
        self.announceToAll("¡¡¡ GRACIAS POR PARTICIPAR EN L2 HERMANOS !!!")
        self.announceToAll("¡¡¡ THANK YOU FOR PARTICIPATING IN L2 HERMANOS !!!")
        
        # Limpiar datos
        self.participants = []
        self.kills = {}
    
    def darRecompensa(self, player, credits, titulo):
        # Dar créditos (esto se conectaría con el sistema de monetización)
        player.sendMessage("¡¡¡ RECOMPENSA ÉPICA RECIBIDA !!!")
        player.sendMessage("¡¡¡ EPIC REWARD RECEIVED !!!")
        player.sendMessage("¡Créditos: " + str(credits) + " + Título: " + titulo + "!")
        player.sendMessage("Credits: " + str(credits) + " + Title: " + titulo + "!")
        
        # Dar título
        player.setTitle(titulo)
        
        # Anuncio épico
        self.announceToAll(player.getName() + " ha recibido: " + str(credits) + " Créditos + " + titulo + "!")
        self.announceToAll(player.getName() + " has received: " + str(credits) + " Credits + " + titulo + "!")
    
    def onTimer(self, event, npc, player):
        if event == "finalizar_evento_coliseo":
            self.finalizarEvento()
        return None
    
    def announceToAll(self, message):
        from l2jfrozen.gameserver.network.serverpackets import CreatureSay
        from l2jfrozen.gameserver.model.actor.instance import L2PcInstance
        from l2jfrozen.gameserver.GameServer import GameServer
        
        for player in GameServer.getInstance().getAllPlayers():
            if player and player.isOnline():
                player.sendPacket(CreatureSay(0, 1, "REY DEL COLISEO ÉPICO", message))

# Crear instancia del evento del Coliseo épico
EVENTO_COLISEO_EPICO = EpicColiseoEvent(-1, "EventoColiseoEpico", "Evento Rey del Coliseo Épico")

# Registrar el evento
EVENTO_COLISEO_EPICO.addStartNpc(30006)  # Tienda GM
EVENTO_COLISEO_EPICO.addTalkId(30006)



