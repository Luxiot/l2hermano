# ===========================================
# EVENTO ÉPICO DE DROPS - MEJOR SERVIDOR L2
# ===========================================
# Evento que aumenta drásticamente los drops

import sys
from java.util import Calendar
from l2jfrozen.gameserver.model.quest import State
from l2jfrozen.gameserver.model.quest import QuestState
from l2jfrozen.gameserver.model.quest.jython import QuestJython as JQuest
from l2jfrozen.gameserver.model.actor.instance import L2PcInstance
from l2jfrozen.gameserver.model.actor.instance import L2NpcInstance
from l2jfrozen.gameserver.model.actor.instance import L2MonsterInstance
from l2jfrozen.gameserver.network.serverpackets import NpcHtmlMessage
from l2jfrozen.gameserver.network.serverpackets import SystemMessage

class EpicDropEvent(JQuest):
    def __init__(self, id, name, descr):
        JQuest.__init__(self, id, name, descr)
        self.eventActive = False
        self.startTime = 0
        
    def onAdvEvent(self, event, npc, player):
        if event == "iniciar_drops_epicos":
            if not self.eventActive:
                self.iniciarDropsEpicos()
                return "¡El EVENTO ÉPICO DE DROPS ha comenzado!"
            else:
                return "¡El evento ya está activo!"
                
        elif event == "detener_drops_epicos":
            if self.eventActive:
                self.detenerDropsEpicos()
                return "¡El EVENTO ÉPICO DE DROPS ha terminado!"
            else:
                return "¡El evento no está activo!"
                
        return None
    
    def iniciarDropsEpicos(self):
        self.eventActive = True
        self.startTime = System.currentTimeMillis()
        
        # Anuncio épico
        self.announceToAll("¡¡¡ EVENTO ÉPICO DE DROPS INICIADO !!!")
        self.announceToAll("¡¡¡ EPIC DROP EVENT STARTED !!!")
        self.announceToAll("¡Drops aumentados x50 por 3 horas!")
        self.announceToAll("Drops increased x50 for 3 hours!")
        self.announceToAll("¡Aprovecha esta oportunidad única!")
        self.announceToAll("Take advantage of this unique opportunity!")
        
        # Programar fin del evento en 3 horas
        self.startQuestTimer("finalizar_drops_epicos", 10800000, None, None)  # 3 horas
    
    def detenerDropsEpicos(self):
        self.eventActive = False
        
        # Anuncio de fin
        self.announceToAll("¡¡¡ EVENTO ÉPICO DE DROPS TERMINADO !!!")
        self.announceToAll("¡¡¡ EPIC DROP EVENT FINISHED !!!")
        self.announceToAll("¡Gracias por participar en L2 Hermanos!")
        self.announceToAll("Thank you for participating in L2 Hermanos!")
    
    def onKill(self, npc, player, isPet):
        if self.eventActive and isinstance(npc, L2MonsterInstance):
            # Dar drops épicos adicionales
            self.darDropsEpicos(player, npc)
        
        return None
    
    def darDropsEpicos(self, player, monster):
        # Adena épica
        adena_epica = monster.getLevel() * 10000
        player.addAdena("DropsEpicos", adena_epica)
        
        # Items épicos aleatorios
        items_epicos = [
            (6651, 5),   # Life Stone
            (6652, 3),   # Mid Life Stone
            (6653, 2),   # High Life Stone
            (6654, 1),   # Top Life Stone
            (6655, 1),   # Soul Stone
            (6656, 1),   # Mid Soul Stone
            (6657, 1),   # High Soul Stone
            (6658, 1),   # Top Soul Stone
        ]
        
        # Dar items aleatorios
        import random
        for itemId, count in items_epicos:
            if random.randint(1, 100) <= 30:  # 30% de chance
                player.addItem("DropsEpicos", itemId, count, player, True)
        
        # XP y SP épicos
        xp_epico = monster.getExpReward() * 10
        sp_epico = monster.getSpReward() * 10
        player.addExpAndSp(xp_epico, sp_epico)
        
        # Mensaje ocasional
        if random.randint(1, 100) <= 10:  # 10% de chance
            player.sendMessage("¡¡¡ DROP ÉPICO !!! Has recibido recompensas increíbles!")
            player.sendMessage("¡¡¡ EPIC DROP !!! You have received incredible rewards!")
    
    def announceToAll(self, message):
        from l2jfrozen.gameserver.network.serverpackets import CreatureSay
        from l2jfrozen.gameserver.model.actor.instance import L2PcInstance
        from l2jfrozen.gameserver.GameServer import GameServer
        
        for player in GameServer.getInstance().getAllPlayers():
            if player and player.isOnline():
                player.sendPacket(CreatureSay(0, 1, "EVENTO ÉPICO DE DROPS", message))
    
    def onTimer(self, event, npc, player):
        if event == "finalizar_drops_epicos":
            self.detenerDropsEpicos()
        return None

# Crear instancia del evento
EVENTO_EPICO_DROPS = EpicDropEvent(-1, "EventoEpicoDrops", "Evento Épico de Drops")

# Registrar el evento
EVENTO_EPICO_DROPS.addStartNpc(30006)  # Tienda GM
EVENTO_EPICO_DROPS.addTalkId(30006)
