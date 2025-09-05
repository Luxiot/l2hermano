# ===========================================
# L2 HERMANOS - TUTORIAL EN ESPAÑOL
# ===========================================
# Script para cambiar el tutorial a español desde el servidor

from net.sf.l2j.gameserver.model.actor.instance import L2PcInstance
from net.sf.l2j.gameserver.network.serverpackets import SystemMessage
from net.sf.l2j.gameserver.network.serverpackets import NpcHtmlMessage

class EpicTutorialSpanish:
    def __init__(self):
        self.tutorial_messages = {
            "welcome": "¡Bienvenido a L2 Hermanos - El mejor servidor L2 de la historia!",
            "sedrick_hall": "Este es el Salón de Entrenamiento Épico de Sedrick. Este lugar es famoso por producir muchos Guerreros épicos notables en L2 Hermanos.",
            "first_step": "Ahora, estás dando tu primer paso para convertirte en un Guerrero Épico Humano. Primero, te explicaré la operación básica del juego épico.",
            "click_here": "Si haces clic aquí, pasarás al siguiente tema de este tutorial épico.",
            "movement": "Movimiento Épico: Usa las teclas WASD o las flechas para moverte por el mundo épico de L2 Hermanos.",
            "attack": "Ataque Épico: Haz clic derecho en un monstruo para atacarlo y ganar experiencia épica.",
            "skills": "Habilidades Épicas: Presiona K para abrir el menú de habilidades épicas y aprender nuevas técnicas.",
            "inventory": "Inventario Épico: Presiona I para abrir tu inventario épico y gestionar tus items.",
            "chat": "Chat Épico: Presiona Enter para abrir el chat épico y comunicarte con otros jugadores.",
            "server_features": "Características Épicas de L2 Hermanos: Rates x20, Eventos épicos, PvP competitivo, Sistema de créditos",
            "commands": "Comandos Épicos: .farm1, .farm2, .pvp1, .pvp2, .boss, .event",
            "titles": "Sistema de Títulos Épicos: Gana títulos épicos participando en eventos, PvP y logros especiales.",
            "pvp_competitive": "PvP Competitivo Épico: Participa en el PvP competitivo épico para ganar créditos y títulos únicos.",
            "monetization": "Sistema de Créditos Épicos: Gana créditos participando en PvP y eventos para comprar items épicos.",
            "events": "Eventos Épicos: Bosses, PvP, Drops, Coliseo - Todos con recompensas increíbles.",
            "tips": "Consejos Épicos: Usa los comandos épicos, participa en eventos, combate en PvP, usa tus créditos, únete a una guild.",
            "complete": "¡Tutorial Épico Completado! ¡Felicidades! Has completado el tutorial épico de L2 Hermanos.",
            "ready": "¡Estás listo para la aventura épica! ¡Ahora puedes explorar el mundo épico de L2 Hermanos y convertirte en una leyenda!"
        }
    
    def enviarMensajeTutorial(self, player, message_key):
        """Envía un mensaje del tutorial en español"""
        if message_key in self.tutorial_messages:
            message = self.tutorial_messages[message_key]
            player.sendPacket(SystemMessage(message))
            return True
        return False
    
    def mostrarTutorialCompleto(self, player):
        """Muestra el tutorial completo en español"""
        html = NpcHtmlMessage(1)
        html.setFile("data/html/tutorial_spanish.htm")
        
        # Reemplazar variables en el HTML
        html.replace("%welcome%", self.tutorial_messages["welcome"])
        html.replace("%sedrick_hall%", self.tutorial_messages["sedrick_hall"])
        html.replace("%first_step%", self.tutorial_messages["first_step"])
        html.replace("%movement%", self.tutorial_messages["movement"])
        html.replace("%attack%", self.tutorial_messages["attack"])
        html.replace("%skills%", self.tutorial_messages["skills"])
        html.replace("%inventory%", self.tutorial_messages["inventory"])
        html.replace("%chat%", self.tutorial_messages["chat"])
        html.replace("%server_features%", self.tutorial_messages["server_features"])
        html.replace("%commands%", self.tutorial_messages["commands"])
        html.replace("%titles%", self.tutorial_messages["titles"])
        html.replace("%pvp_competitive%", self.tutorial_messages["pvp_competitive"])
        html.replace("%monetization%", self.tutorial_messages["monetization"])
        html.replace("%events%", self.tutorial_messages["events"])
        html.replace("%tips%", self.tutorial_messages["tips"])
        html.replace("%complete%", self.tutorial_messages["complete"])
        html.replace("%ready%", self.tutorial_messages["ready"])
        
        player.sendPacket(html)
        return True
    
    def iniciarTutorialEspañol(self, player):
        """Inicia el tutorial en español para un jugador"""
        if not player:
            return False
        
        # Enviar mensaje de bienvenida
        self.enviarMensajeTutorial(player, "welcome")
        
        # Mostrar tutorial completo
        self.mostrarTutorialCompleto(player)
        
        # Enviar mensaje de confirmación
        player.sendPacket(SystemMessage("¡Tutorial épico en español iniciado! ¡Disfruta de L2 Hermanos!"))
        
        return True
    
    def verificarTutorialEspañol(self, player):
        """Verifica si el jugador necesita el tutorial en español"""
        if not player:
            return False
        
        # Verificar si es un jugador nuevo (nivel 1-5)
        if player.getLevel() <= 5:
            return True
        
        # Verificar si no ha completado el tutorial
        if not player.getVar("tutorial_completed"):
            return True
        
        return False

# Instancia global del sistema
epic_tutorial_spanish = EpicTutorialSpanish()

# Función para usar desde otros scripts
def iniciarTutorialEspañol(player):
    """Función global para iniciar el tutorial en español"""
    return epic_tutorial_spanish.iniciarTutorialEspañol(player)

def verificarTutorialEspañol(player):
    """Función global para verificar si necesita tutorial en español"""
    return epic_tutorial_spanish.verificarTutorialEspañol(player)

def enviarMensajeTutorial(player, message_key):
    """Función global para enviar mensaje del tutorial"""
    return epic_tutorial_spanish.enviarMensajeTutorial(player, message_key)



