# ===========================================
# L2 HERMANOS - INICIO AUTOMÁTICO DEL TUTORIAL
# ===========================================
# Script que inicia automáticamente el tutorial en español

from net.sf.l2j.gameserver.model.actor.instance import L2PcInstance
from net.sf.l2j.gameserver.network.serverpackets import SystemMessage
from net.sf.l2j.gameserver.network.serverpackets import NpcHtmlMessage
from net.sf.l2j.gameserver.model.quest import Quest
from net.sf.l2j.gameserver.model.quest.jython import QuestJython

class EpicTutorialAutoStart(QuestJython):
    def __init__(self, questId, name, descr):
        super(EpicTutorialAutoStart, self).__init__(questId, name, descr)
        
        # Registrar eventos
        self.addPlayerEnterWorldId(0)  # Todos los mundos
        self.addPlayerEnterWorldId(1)
        self.addPlayerEnterWorldId(2)
        self.addPlayerEnterWorldId(3)
        self.addPlayerEnterWorldId(4)
        self.addPlayerEnterWorldId(5)
        self.addPlayerEnterWorldId(6)
        self.addPlayerEnterWorldId(7)
        self.addPlayerEnterWorldId(8)
        self.addPlayerEnterWorldId(9)
        self.addPlayerEnterWorldId(10)
        self.addPlayerEnterWorldId(11)
        self.addPlayerEnterWorldId(12)
        self.addPlayerEnterWorldId(13)
        self.addPlayerEnterWorldId(14)
        self.addPlayerEnterWorldId(15)
        self.addPlayerEnterWorldId(16)
        self.addPlayerEnterWorldId(17)
        self.addPlayerEnterWorldId(18)
        self.addPlayerEnterWorldId(19)
        self.addPlayerEnterWorldId(20)
        self.addPlayerEnterWorldId(21)
        self.addPlayerEnterWorldId(22)
        self.addPlayerEnterWorldId(23)
        self.addPlayerEnterWorldId(24)
        self.addPlayerEnterWorldId(25)
        self.addPlayerEnterWorldId(26)
        self.addPlayerEnterWorldId(27)
        self.addPlayerEnterWorldId(28)
        self.addPlayerEnterWorldId(29)
        self.addPlayerEnterWorldId(30)
        self.addPlayerEnterWorldId(31)
        self.addPlayerEnterWorldId(32)
        self.addPlayerEnterWorldId(33)
        self.addPlayerEnterWorldId(34)
        self.addPlayerEnterWorldId(35)
        self.addPlayerEnterWorldId(36)
        self.addPlayerEnterWorldId(37)
        self.addPlayerEnterWorldId(38)
        self.addPlayerEnterWorldId(39)
        self.addPlayerEnterWorldId(40)
        self.addPlayerEnterWorldId(41)
        self.addPlayerEnterWorldId(42)
        self.addPlayerEnterWorldId(43)
        self.addPlayerEnterWorldId(44)
        self.addPlayerEnterWorldId(45)
        self.addPlayerEnterWorldId(46)
        self.addPlayerEnterWorldId(47)
        self.addPlayerEnterWorldId(48)
        self.addPlayerEnterWorldId(49)
        self.addPlayerEnterWorldId(50)
    
    def onPlayerEnterWorld(self, player):
        """Cuando un jugador entra al mundo"""
        if not isinstance(player, L2PcInstance):
            return
        
        # Verificar si es un jugador nuevo (nivel 1-5)
        if player.getLevel() <= 5:
            # Verificar si no ha completado el tutorial
            if not player.getVar("tutorial_completed"):
                # Iniciar tutorial en español
                self.iniciarTutorialEspañol(player)
    
    def iniciarTutorialEspañol(self, player):
        """Inicia el tutorial en español"""
        if not isinstance(player, L2PcInstance):
            return
        
        # Enviar mensaje de bienvenida
        player.sendPacket(SystemMessage("¡Bienvenido a L2 Hermanos - El mejor servidor L2 de la historia!"))
        
        # Mostrar tutorial completo
        self.mostrarTutorialCompleto(player)
        
        # Marcar como completado
        player.setVar("tutorial_completed", "true")
        
        # Enviar mensaje de confirmación
        player.sendPacket(SystemMessage("¡Tutorial épico en español completado! ¡Disfruta de L2 Hermanos!"))
    
    def mostrarTutorialCompleto(self, player):
        """Muestra el tutorial completo en español"""
        html = NpcHtmlMessage(1)
        html.setFile("data/html/tutorial_spanish.htm")
        
        # Reemplazar variables en el HTML
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

# Crear instancia del quest
QUEST = EpicTutorialAutoStart(-1, "EpicTutorialAutoStart", "L2 Hermanos - Tutorial Automático en Español")



