# ===========================================
# ANUNCIOS ÉPICOS - MEJOR SERVIDOR L2
# ===========================================
# Sistema de anuncios automáticos épicos

import sys
from java.util import Calendar
from l2jfrozen.gameserver.model.quest import State
from l2jfrozen.gameserver.model.quest import QuestState
from l2jfrozen.gameserver.model.quest.jython import QuestJython as JQuest
from l2jfrozen.gameserver.model.actor.instance import L2PcInstance
from l2jfrozen.gameserver.model.actor.instance import L2NpcInstance
from l2jfrozen.gameserver.network.serverpackets import NpcHtmlMessage
from l2jfrozen.gameserver.network.serverpackets import SystemMessage

class EpicAnnouncements(JQuest):
    def __init__(self, id, name, descr):
        JQuest.__init__(self, id, name, descr)
        self.announcementIndex = 0
        self.announcements = [
            "¡¡¡ BIENVENIDO A L2 HERMANOS - EL MEJOR SERVIDOR L2 DE LA HISTORIA !!!",
            "¡¡¡ WELCOME TO L2 HERMANOS - THE BEST L2 SERVER IN HISTORY !!!",
            "¡Rates x20, eventos épicos, recompensas increíbles!",
            "Rates x20, epic events, incredible rewards!",
            "¡Únete a la aventura más épica de Lineage 2!",
            "Join the most epic adventure of Lineage 2!",
            "🎮 EVENTOS ÉPICOS: EVENTO DE BOSSES, EVENTO DE PVP, EVENTO DE DROPS!",
            "🎮 EPIC EVENTS: BOSS EVENT, PVP EVENT, DROP EVENT!",
            "💰 RATES ÉPICOS: XP x20, SP x20, Adena x15, Drop x12!",
            "💰 EPIC RATES: XP x20, SP x20, Adena x15, Drop x12!",
            "🏆 RECOMPENSAS: 1M Adena + 100K AA + Items épicos!",
            "🏆 REWARDS: 1M Adena + 100K AA + Epic items!",
            "⚔️ PVP ÉPICO: Combates épicos con recompensas increíbles!",
            "⚔️ EPIC PVP: Epic battles with incredible rewards!",
            "🎯 COMANDOS: .farm1, .farm2, .pvp1, .pvp2 disponibles!",
            "🎯 COMMANDS: .farm1, .farm2, .pvp1, .pvp2 available!",
            "🌟 CARACTERÍSTICAS: AIO, Buffs, Drops múltiples, Regeneración x3!",
            "🌟 FEATURES: AIO, Buffs, Multiple drops, x3 regeneration!",
            "¡¡¡ DISFRUTA DE L2 HERMANOS - EL MEJOR SERVIDOR L2 DE LA HISTORIA !!!",
            "¡¡¡ ENJOY L2 HERMANOS - THE BEST L2 SERVER IN HISTORY !!!",
            "🎮 ¡Únete ahora y vive la aventura más épica!",
            "🎮 Join now and live the most epic adventure!",
            "⚔️ ¡Combates épicos te esperan!",
            "⚔️ Epic battles await you!",
            "💰 ¡Recompensas épicas te esperan!",
            "💰 Epic rewards await you!",
            "🏆 ¡Gloria épica te espera!",
            "🏆 Epic glory awaits you!",
            "¡¡¡ L2 HERMANOS - EL MEJOR SERVIDOR L2 DE LA HISTORIA x20 !!!",
            "¡¡¡ L2 HERMANOS - THE BEST L2 SERVER IN HISTORY x20 !!!"
        ]
        
    def onAdvEvent(self, event, npc, player):
        if event == "iniciar_anuncios":
            self.startQuestTimer("anuncio_epico", 300000, None, None)  # Cada 5 minutos
            return "¡Anuncios épicos activados!"
        elif event == "detener_anuncios":
            self.cancelQuestTimer("anuncio_epico", None, None)
            return "¡Anuncios épicos desactivados!"
        return None
    
    def onTimer(self, event, npc, player):
        if event == "anuncio_epico":
            self.enviarAnuncioEpico()
            # Programar siguiente anuncio
            self.startQuestTimer("anuncio_epico", 300000, None, None)  # Cada 5 minutos
        return None
    
    def enviarAnuncioEpico(self):
        if self.announcementIndex >= len(self.announcements):
            self.announcementIndex = 0
        
        message = self.announcements[self.announcementIndex]
        self.announcementIndex += 1
        
        self.announceToAll(message)
    
    def announceToAll(self, message):
        from l2jfrozen.gameserver.network.serverpackets import CreatureSay
        from l2jfrozen.gameserver.model.actor.instance import L2PcInstance
        from l2jfrozen.gameserver.GameServer import GameServer
        
        for player in GameServer.getInstance().getAllPlayers():
            if player and player.isOnline():
                player.sendPacket(CreatureSay(0, 1, "SERVIDOR ÉPICO", message))

# Crear instancia del sistema de anuncios
ANUNCIOS_EPICOS = EpicAnnouncements(-1, "AnunciosEpicos", "Sistema de Anuncios Épicos")

# Registrar el sistema
ANUNCIOS_EPICOS.addStartNpc(30006)  # Tienda GM
ANUNCIOS_EPICOS.addTalkId(30006)

# Iniciar anuncios automáticamente
ANUNCIOS_EPICOS.startQuestTimer("anuncio_epico", 60000, None, None)  # Primer anuncio en 1 minuto
