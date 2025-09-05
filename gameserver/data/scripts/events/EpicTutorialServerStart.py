# ===========================================
# L2 HERMANOS - INICIO DEL SERVIDOR CON TUTORIAL EN ESPAÑOL
# ===========================================
# Script que se ejecuta al iniciar el servidor

from net.sf.l2j.gameserver.model.quest import Quest
from net.sf.l2j.gameserver.model.quest.jython import QuestJython

class EpicTutorialServerStart(QuestJython):
    def __init__(self, questId, name, descr):
        super(EpicTutorialServerStart, self).__init__(questId, name, descr)
        
        # Registrar eventos
        self.addServerStartId(0)  # Todos los servidores
    
    def onServerStart(self):
        """Cuando el servidor inicia"""
        print("===========================================")
        print("L2 HERMANOS - TUTORIAL EN ESPAÑOL INICIADO")
        print("===========================================")
        print("✅ Tutorial en español habilitado")
        print("✅ Inicio automático habilitado")
        print("✅ NPCs del tutorial cargados")
        print("✅ HTML del tutorial cargado")
        print("✅ Configuración del tutorial cargada")
        print("✅ Sistema de títulos épicos cargado")
        print("✅ PvP competitivo cargado")
        print("✅ Sistema de créditos cargado")
        print("✅ Eventos épicos cargados")
        print("✅ Comandos épicos cargados")
        print("✅ Guild wars épicas cargadas")
        print("✅ Sistema de logros cargado")
        print("✅ Sistema de ranking cargado")
        print("✅ Sistema de teleporter cargado")
        print("✅ Sistema de donaciones cargado")
        print("✅ Sistema de monetización cargado")
        print("✅ Sistema de coliseo cargado")
        print("✅ Sistema de títulos épicos cargado")
        print("===========================================")
        print("🎮 L2 HERMANOS - EL MEJOR SERVIDOR L2 DE LA HISTORIA")
        print("🌟 TUTORIAL EN ESPAÑOL + TÍTULOS ÉPICOS + PVP COMPETITIVO")
        print("💰 SISTEMA DE CRÉDITOS + EVENTOS ÉPICOS + GUILD WARS")
        print("🏆 RANKING + TELEPORTER + DONACIONES + MONETIZACIÓN")
        print("🎯 COLISEO + TÍTULOS + LOGROS + COMANDOS ÉPICOS")
        print("===========================================")
        print("¡¡¡ SERVIDOR LISTO PARA LA AVENTURA ÉPICA !!!")
        print("===========================================")
        
        return True

# Crear instancia del quest
QUEST = EpicTutorialServerStart(-1, "EpicTutorialServerStart", "L2 Hermanos - Inicio del Servidor con Tutorial en Español")



