# ===========================================
# L2 HERMANOS - NPC DEL TUTORIAL EN ESPAÑOL
# ===========================================
# NPC que maneja el tutorial en español

from net.sf.l2j.gameserver.model.actor.instance import L2PcInstance
from net.sf.l2j.gameserver.model.actor.instance import L2NpcInstance
from net.sf.l2j.gameserver.network.serverpackets import NpcHtmlMessage
from net.sf.l2j.gameserver.network.serverpackets import SystemMessage
from net.sf.l2j.gameserver.ai import CtrlIntention
from net.sf.l2j.gameserver.model.quest import Quest
from net.sf.l2j.gameserver.model.quest import State
from net.sf.l2j.gameserver.model.quest import QuestState
from net.sf.l2j.gameserver.model.quest.jython import QuestJython

class EpicTutorialNPC(QuestJython):
    def __init__(self, questId, name, descr):
        super(EpicTutorialNPC, self).__init__(questId, name, descr)
        
        # IDs de NPCs que manejan el tutorial
        self.tutorial_npcs = [30006, 30007, 30008, 30009, 30010]  # Sedrick y otros NPCs de tutorial
        
        # Registrar eventos
        for npcId in self.tutorial_npcs:
            self.addStartNpc(npcId)
            self.addTalkId(npcId)
            self.addFirstTalkId(npcId)
    
    def onFirstTalk(self, npc, player):
        """Primera conversación con el NPC"""
        if not isinstance(npc, L2NpcInstance) or not isinstance(player, L2PcInstance):
            return None
        
        # Verificar si es un jugador nuevo
        if player.getLevel() <= 5:
            return self.mostrarTutorialEspañol(npc, player)
        else:
            return self.mostrarMenuPrincipal(npc, player)
    
    def onTalk(self, npc, player):
        """Conversación con el NPC"""
        if not isinstance(npc, L2NpcInstance) or not isinstance(player, L2PcInstance):
            return None
        
        return self.mostrarMenuPrincipal(npc, player)
    
    def mostrarTutorialEspañol(self, npc, player):
        """Muestra el tutorial en español"""
        html = NpcHtmlMessage(npc.getObjectId())
        html.setFile("data/html/tutorial_spanish.htm")
        
        # Reemplazar variables
        html.replace("%objectId%", str(npc.getObjectId()))
        html.replace("%welcome%", "¡Bienvenido a L2 Hermanos - El mejor servidor L2 de la historia!")
        html.replace("%sedrick_hall%", "Este es el Salón de Entrenamiento Épico de Sedrick. Este lugar es famoso por producir muchos Guerreros épicos notables en L2 Hermanos.")
        html.replace("%first_step%", "Ahora, estás dando tu primer paso para convertirte en un Guerrero Épico Humano. Primero, te explicaré la operación básica del juego épico.")
        html.replace("%movement%", "Movimiento Épico: Usa las teclas WASD o las flechas para moverte por el mundo épico de L2 Hermanos.")
        html.replace("%attack%", "Ataque Épico: Haz clic derecho en un monstruo para atacarlo y ganar experiencia épica.")
        html.replace("%skills%", "Habilidades Épicas: Presiona K para abrir el menú de habilidades épicas y aprender nuevas técnicas.")
        html.replace("%inventory%", "Inventario Épico: Presiona I para abrir tu inventario épico y gestionar tus items.")
        html.replace("%chat%", "Chat Épico: Presiona Enter para abrir el chat épico y comunicarte con otros jugadores.")
        html.replace("%server_features%", "Características Épicas de L2 Hermanos: Rates x20, Eventos épicos, PvP competitivo, Sistema de créditos")
        html.replace("%commands%", "Comandos Épicos: .farm1, .farm2, .pvp1, .pvp2, .boss, .event")
        html.replace("%titles%", "Sistema de Títulos Épicos: Gana títulos épicos participando en eventos, PvP y logros especiales.")
        html.replace("%pvp_competitive%", "PvP Competitivo Épico: Participa en el PvP competitivo épico para ganar créditos y títulos únicos.")
        html.replace("%monetization%", "Sistema de Créditos Épicos: Gana créditos participando en PvP y eventos para comprar items épicos.")
        html.replace("%events%", "Eventos Épicos: Bosses, PvP, Drops, Coliseo - Todos con recompensas increíbles.")
        html.replace("%tips%", "Consejos Épicos: Usa los comandos épicos, participa en eventos, combate en PvP, usa tus créditos, únete a una guild.")
        html.replace("%complete%", "¡Tutorial Épico Completado! ¡Felicidades! Has completado el tutorial épico de L2 Hermanos.")
        html.replace("%ready%", "¡Estás listo para la aventura épica! ¡Ahora puedes explorar el mundo épico de L2 Hermanos y convertirte en una leyenda!")
        
        player.sendPacket(html)
        return None
    
    def mostrarMenuPrincipal(self, npc, player):
        """Muestra el menú principal del NPC"""
        html = NpcHtmlMessage(npc.getObjectId())
        html.setFile("data/html/tutorial_menu.htm")
        
        # Reemplazar variables
        html.replace("%objectId%", str(npc.getObjectId()))
        html.replace("%playerName%", player.getName())
        html.replace("%playerLevel%", str(player.getLevel()))
        
        player.sendPacket(html)
        return None
    
    def onAdvEvent(self, event, npc, player):
        """Maneja eventos del NPC"""
        if not isinstance(npc, L2NpcInstance) or not isinstance(player, L2PcInstance):
            return None
        
        if event == "tutorial_spanish":
            return self.mostrarTutorialEspañol(npc, player)
        elif event == "menu_principal":
            return self.mostrarMenuPrincipal(npc, player)
        elif event == "comandos_epicos":
            return self.mostrarComandosEpicos(npc, player)
        elif event == "titulos_epicos":
            return self.mostrarTitulosEpicos(npc, player)
        elif event == "eventos_epicos":
            return self.mostrarEventosEpicos(npc, player)
        elif event == "pvp_competitivo":
            return self.mostrarPvPCompetitivo(npc, player)
        elif event == "monetizacion":
            return self.mostrarMonetizacion(npc, player)
        
        return None
    
    def mostrarComandosEpicos(self, npc, player):
        """Muestra los comandos épicos"""
        html = NpcHtmlMessage(npc.getObjectId())
        html.setFile("data/html/comandos_epicos.htm")
        
        html.replace("%objectId%", str(npc.getObjectId()))
        
        player.sendPacket(html)
        return None
    
    def mostrarTitulosEpicos(self, npc, player):
        """Muestra los títulos épicos"""
        html = NpcHtmlMessage(npc.getObjectId())
        html.setFile("data/html/titulos_epicos.htm")
        
        html.replace("%objectId%", str(npc.getObjectId()))
        
        player.sendPacket(html)
        return None
    
    def mostrarEventosEpicos(self, npc, player):
        """Muestra los eventos épicos"""
        html = NpcHtmlMessage(npc.getObjectId())
        html.setFile("data/html/eventos_epicos.htm")
        
        html.replace("%objectId%", str(npc.getObjectId()))
        
        player.sendPacket(html)
        return None
    
    def mostrarPvPCompetitivo(self, npc, player):
        """Muestra el PvP competitivo"""
        html = NpcHtmlMessage(npc.getObjectId())
        html.setFile("data/html/pvp_competitivo.htm")
        
        html.replace("%objectId%", str(npc.getObjectId()))
        
        player.sendPacket(html)
        return None
    
    def mostrarMonetizacion(self, npc, player):
        """Muestra la monetización"""
        html = NpcHtmlMessage(npc.getObjectId())
        html.setFile("data/html/monetizacion.htm")
        
        html.replace("%objectId%", str(npc.getObjectId()))
        
        player.sendPacket(html)
        return None

# Crear instancia del quest
QUEST = EpicTutorialNPC(-1, "EpicTutorialNPC", "L2 Hermanos - Tutorial en Español")



