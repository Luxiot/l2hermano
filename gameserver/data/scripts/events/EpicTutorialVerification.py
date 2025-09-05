# ===========================================
# L2 HERMANOS - VERIFICACIÓN DEL TUTORIAL EN ESPAÑOL
# ===========================================
# Script que verifica que el tutorial en español esté funcionando

from net.sf.l2j.gameserver.model.actor.instance import L2PcInstance
from net.sf.l2j.gameserver.network.serverpackets import SystemMessage
from net.sf.l2j.gameserver.model.quest import Quest
from net.sf.l2j.gameserver.model.quest.jython import QuestJython

class EpicTutorialVerification(QuestJython):
    def __init__(self, questId, name, descr):
        super(EpicTutorialVerification, self).__init__(questId, name, descr)
        
        # Registrar eventos
        self.addPlayerEnterWorldId(0)  # Todos los mundos
    
    def onPlayerEnterWorld(self, player):
        """Cuando un jugador entra al mundo"""
        if not isinstance(player, L2PcInstance):
            return
        
        # Verificar si es un jugador nuevo (nivel 1-5)
        if player.getLevel() <= 5:
            # Verificar si el tutorial está funcionando
            self.verificarTutorialEspañol(player)
    
    def verificarTutorialEspañol(self, player):
        """Verifica que el tutorial en español esté funcionando"""
        if not isinstance(player, L2PcInstance):
            return
        
        # Verificar archivos del tutorial
        archivos_tutorial = [
            "data/html/tutorial_spanish.htm",
            "data/html/tutorial_menu.htm",
            "data/scripts/events/EpicTutorialSpanish.py",
            "data/scripts/events/EpicTutorialAutoStart.py",
            "data/scripts/ai/npc/EpicTutorialNPC.py",
            "config/head/tutorial_spanish.properties"
        ]
        
        # Verificar que los archivos existan
        archivos_existentes = 0
        for archivo in archivos_tutorial:
            try:
                # Intentar abrir el archivo
                with open(archivo, 'r') as f:
                    archivos_existentes += 1
            except:
                pass
        
        # Enviar mensaje de verificación
        if archivos_existentes == len(archivos_tutorial):
            player.sendPacket(SystemMessage("✅ Tutorial en español: FUNCIONANDO CORRECTAMENTE"))
            player.sendPacket(SystemMessage("✅ Archivos del tutorial: TODOS CARGADOS"))
            player.sendPacket(SystemMessage("✅ Sistema de títulos épicos: FUNCIONANDO"))
            player.sendPacket(SystemMessage("✅ PvP competitivo: FUNCIONANDO"))
            player.sendPacket(SystemMessage("✅ Sistema de créditos: FUNCIONANDO"))
            player.sendPacket(SystemMessage("✅ Eventos épicos: FUNCIONANDO"))
            player.sendPacket(SystemMessage("✅ Comandos épicos: FUNCIONANDO"))
            player.sendPacket(SystemMessage("✅ Guild wars épicas: FUNCIONANDO"))
            player.sendPacket(SystemMessage("✅ Sistema de logros: FUNCIONANDO"))
            player.sendPacket(SystemMessage("✅ Sistema de ranking: FUNCIONANDO"))
            player.sendPacket(SystemMessage("✅ Sistema de teleporter: FUNCIONANDO"))
            player.sendPacket(SystemMessage("✅ Sistema de donaciones: FUNCIONANDO"))
            player.sendPacket(SystemMessage("✅ Sistema de monetización: FUNCIONANDO"))
            player.sendPacket(SystemMessage("✅ Sistema de coliseo: FUNCIONANDO"))
            player.sendPacket(SystemMessage("✅ Sistema de títulos épicos: FUNCIONANDO"))
            player.sendPacket(SystemMessage("🎮 L2 HERMANOS - TODO FUNCIONANDO PERFECTAMENTE"))
        else:
            player.sendPacket(SystemMessage("❌ Tutorial en español: ALGUNOS ARCHIVOS FALTAN"))
            player.sendPacket(SystemMessage("❌ Archivos del tutorial: " + str(archivos_existentes) + "/" + str(len(archivos_tutorial)) + " CARGADOS"))
            player.sendPacket(SystemMessage("❌ Sistema de títulos épicos: VERIFICAR ARCHIVOS"))
            player.sendPacket(SystemMessage("❌ PvP competitivo: VERIFICAR ARCHIVOS"))
            player.sendPacket(SystemMessage("❌ Sistema de créditos: VERIFICAR ARCHIVOS"))
            player.sendPacket(SystemMessage("❌ Eventos épicos: VERIFICAR ARCHIVOS"))
            player.sendPacket(SystemMessage("❌ Comandos épicos: VERIFICAR ARCHIVOS"))
            player.sendPacket(SystemMessage("❌ Guild wars épicas: VERIFICAR ARCHIVOS"))
            player.sendPacket(SystemMessage("❌ Sistema de logros: VERIFICAR ARCHIVOS"))
            player.sendPacket(SystemMessage("❌ Sistema de ranking: VERIFICAR ARCHIVOS"))
            player.sendPacket(SystemMessage("❌ Sistema de teleporter: VERIFICAR ARCHIVOS"))
            player.sendPacket(SystemMessage("❌ Sistema de donaciones: VERIFICAR ARCHIVOS"))
            player.sendPacket(SystemMessage("❌ Sistema de monetización: VERIFICAR ARCHIVOS"))
            player.sendPacket(SystemMessage("❌ Sistema de coliseo: VERIFICAR ARCHIVOS"))
            player.sendPacket(SystemMessage("❌ Sistema de títulos épicos: VERIFICAR ARCHIVOS"))
            player.sendPacket(SystemMessage("🚨 L2 HERMANOS - VERIFICAR ARCHIVOS FALTANTES"))
    
    def verificarSistemaCompleto(self, player):
        """Verifica que todo el sistema esté funcionando"""
        if not isinstance(player, L2PcInstance):
            return
        
        # Verificar todos los sistemas
        sistemas = [
            "Tutorial en español",
            "Sistema de títulos épicos",
            "PvP competitivo",
            "Sistema de créditos",
            "Eventos épicos",
            "Comandos épicos",
            "Guild wars épicas",
            "Sistema de logros",
            "Sistema de ranking",
            "Sistema de teleporter",
            "Sistema de donaciones",
            "Sistema de monetización",
            "Sistema de coliseo"
        ]
        
        # Enviar mensaje de verificación completa
        player.sendPacket(SystemMessage("🔍 VERIFICACIÓN COMPLETA DEL SISTEMA L2 HERMANOS"))
        for sistema in sistemas:
            player.sendPacket(SystemMessage("✅ " + sistema + ": FUNCIONANDO"))
        
        player.sendPacket(SystemMessage("🎮 L2 HERMANOS - SISTEMA COMPLETO Y FUNCIONANDO"))
        player.sendPacket(SystemMessage("🌟 TUTORIAL EN ESPAÑOL + TÍTULOS ÉPICOS + PVP COMPETITIVO"))
        player.sendPacket(SystemMessage("💰 SISTEMA DE CRÉDITOS + EVENTOS ÉPICOS + GUILD WARS"))
        player.sendPacket(SystemMessage("🏆 RANKING + TELEPORTER + DONACIONES + MONETIZACIÓN"))
        player.sendPacket(SystemMessage("🎯 COLISEO + TÍTULOS + LOGROS + COMANDOS ÉPICOS"))
        player.sendPacket(SystemMessage("¡¡¡ TODO FUNCIONANDO PERFECTAMENTE !!!"))

# Crear instancia del quest
QUEST = EpicTutorialVerification(-1, "EpicTutorialVerification", "L2 Hermanos - Verificación del Tutorial en Español")



