# ===========================================
# EVENTO ÉPICO DE PVP - MEJOR SERVIDOR L2
# ===========================================
# Evento de PvP épico con recompensas increíbles

import sys
from java.util import Calendar
from l2jfrozen.gameserver.model.quest import State
from l2jfrozen.gameserver.model.quest import QuestState
from l2jfrozen.gameserver.model.quest.jython import QuestJython as JQuest
from l2jfrozen.gameserver.model.actor.instance import L2PcInstance
from l2jfrozen.gameserver.model.actor.instance import L2NpcInstance
from l2jfrozen.gameserver.network.serverpackets import NpcHtmlMessage
from l2jfrozen.gameserver.network.serverpackets import SystemMessage
from l2jfrozen.gameserver.model.zone.type import L2PvpZone

class EpicPvPEvent(JQuest):
    def __init__(self, id, name, descr):
        JQuest.__init__(self, id, name, descr)
        self.eventActive = False
        self.participants = []
        self.kills = {}
        self.startTime = 0
        
    def onAdvEvent(self, event, npc, player):
        if event == "unirse_pvp_epico":
            if not self.eventActive:
                return "El evento no está activo. Espera a que comience."
            
            if player in self.participants:
                return "¡Ya estás participando en el evento!"
            
            self.participants.append(player)
            self.kills[player] = 0
            
            # Teleportar al jugador a la zona PvP
            player.teleToLocation(149999, 46728, -3414)
            player.sendMessage("¡Bienvenido al EVENTO ÉPICO DE PVP!")
            player.sendMessage("¡Mata a otros jugadores para ganar puntos!")
            
            return "¡Te has unido al EVENTO ÉPICO DE PVP!"
            
        elif event == "iniciar_pvp_epico":
            if not self.eventActive:
                self.iniciarPvPEpico()
                return "¡El EVENTO ÉPICO DE PVP ha comenzado!"
            else:
                return "¡El evento ya está activo!"
                
        elif event == "detener_pvp_epico":
            if self.eventActive:
                self.detenerPvPEpico()
                return "¡El EVENTO ÉPICO DE PVP ha terminado!"
            else:
                return "¡El evento no está activo!"
                
        return None
    
    def iniciarPvPEpico(self):
        self.eventActive = True
        self.startTime = System.currentTimeMillis()
        self.participants = []
        self.kills = {}
        
        # Anuncio épico
        self.announceToAll("¡¡¡ EVENTO ÉPICO DE PVP INICIADO !!!")
        self.announceToAll("¡¡¡ EPIC PVP EVENT STARTED !!!")
        self.announceToAll("¡Únete al evento hablando con la Tienda GM!")
        self.announceToAll("Join the event by talking to the GM Shop!")
        self.announceToAll("¡Recompensas épicas por cada kill!")
        self.announceToAll("Epic rewards for each kill!")
        
        # Programar fin del evento en 1 hora
        self.startQuestTimer("finalizar_pvp_epico", 3600000, None, None)  # 1 hora
    
    def detenerPvPEpico(self):
        self.eventActive = False
        
        # Calcular ganadores
        if self.kills:
            winner = max(self.kills, key=self.kills.get)
            winner_kills = self.kills[winner]
            
            # Recompensas épicas para el ganador
            self.darRecompensasPvPEpicas(winner, winner_kills, True)
            
            # Anuncio del ganador
            self.announceToAll("¡¡¡ " + winner.getName() + " GANÓ EL EVENTO ÉPICO DE PVP !!!")
            self.announceToAll("¡¡¡ " + winner.getName() + " WON THE EPIC PVP EVENT !!!")
            self.announceToAll("¡Con " + str(winner_kills) + " kills épicos!")
            self.announceToAll("With " + str(winner_kills) + " epic kills!")
        
        # Recompensas para todos los participantes
        for player in self.participants:
            if player and player.isOnline():
                kills = self.kills.get(player, 0)
                if kills > 0:
                    self.darRecompensasPvPEpicas(player, kills, False)
        
        self.participants = []
        self.kills = {}
        
        # Anuncio de fin
        self.announceToAll("¡¡¡ EVENTO ÉPICO DE PVP TERMINADO !!!")
        self.announceToAll("¡¡¡ EPIC PVP EVENT FINISHED !!!")
    
    def onKill(self, npc, player, isPet):
        if self.eventActive and player in self.participants:
            # Verificar si el objetivo también está en el evento
            if npc in self.participants:
                # Incrementar kills
                self.kills[player] = self.kills.get(player, 0) + 1
                
                # Recompensa inmediata por kill
                player.addAdena("EpicPvP", 1000000)
                player.addExpAndSp(1000000, 500000)
                
                # Anuncio del kill
                self.announceToAll(player.getName() + " eliminó a " + npc.getName() + " en el EVENTO ÉPICO DE PVP!")
                self.announceToAll(player.getName() + " eliminated " + npc.getName() + " in the EPIC PVP EVENT!")
                self.announceToAll("¡Kills totales: " + str(self.kills[player]) + "!")
                self.announceToAll("Total kills: " + str(self.kills[player]) + "!")
        
        return None
    
    def darRecompensasPvPEpicas(self, player, kills, esGanador):
        if esGanador:
            # Recompensas épicas para el ganador
            player.addAdena("EpicPvP_Winner", 50000000)
            player.addExpAndSp(50000000, 25000000)
            
            # Items épicos únicos
            items_ganador_epicos = [
                (6651, 50),  # Life Stone
                (6652, 30),  # Mid Life Stone
                (6653, 20),  # High Life Stone
                (6654, 10),  # Top Life Stone
                (6655, 5),   # Soul Stone
                (6656, 3),   # Mid Soul Stone
                (6657, 2),   # High Soul Stone
                (6658, 1),   # Top Soul Stone
            ]
            
            for itemId, count in items_ganador_epicos:
                player.addItem("GanadorPvPEpico", itemId, count, player, True)
            
            player.sendMessage("¡¡¡ ERES EL GANADOR DEL EVENTO ÉPICO DE PVP !!!")
            player.sendMessage("¡Has recibido recompensas épicas increíbles!")
            
        else:
            # Recompensas por participación
            player.addAdena("ParticipantePvPEpico", kills * 2000000)
            player.addExpAndSp(kills * 2000000, kills * 1000000)
            
            # Items por participación
            if kills >= 5:
                player.addItem("ParticipantePvPEpico", 6651, 10, player, True)
            if kills >= 10:
                player.addItem("ParticipantePvPEpico", 6652, 5, player, True)
            if kills >= 20:
                player.addItem("ParticipantePvPEpico", 6653, 3, player, True)
            
            player.sendMessage("¡Gracias por participar en el EVENTO ÉPICO DE PVP!")
            player.sendMessage("¡Kills: " + str(kills) + " - Recompensas recibidas!")
    
    def announceToAll(self, message):
        from l2jfrozen.gameserver.network.serverpackets import CreatureSay
        from l2jfrozen.gameserver.model.actor.instance import L2PcInstance
        from l2jfrozen.gameserver.GameServer import GameServer
        
        for player in GameServer.getInstance().getAllPlayers():
            if player and player.isOnline():
                player.sendPacket(CreatureSay(0, 1, "EVENTO ÉPICO DE PVP", message))
    
    def onTimer(self, event, npc, player):
        if event == "finalizar_pvp_epico":
            self.detenerPvPEpico()
        return None

# Crear instancia del evento
EVENTO_EPICO_PVP = EpicPvPEvent(-1, "EventoEpicoPvP", "Evento Épico de PvP")

# Registrar el evento
EVENTO_EPICO_PVP.addStartNpc(30006)  # Tienda GM
EVENTO_EPICO_PVP.addTalkId(30006)
