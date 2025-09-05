# ===========================================
# ITEMS PERSONALIZADOS ÉPICOS - MEJOR SERVIDOR L2
# ===========================================
# Sistema de items personalizados épicos

import sys
from java.util import Calendar
from l2jfrozen.gameserver.model.quest import State
from l2jfrozen.gameserver.model.quest import QuestState
from l2jfrozen.gameserver.model.quest.jython import QuestJython as JQuest
from l2jfrozen.gameserver.model.actor.instance import L2PcInstance
from l2jfrozen.gameserver.model.actor.instance import L2NpcInstance
from l2jfrozen.gameserver.network.serverpackets import NpcHtmlMessage
from l2jfrozen.gameserver.network.serverpackets import SystemMessage

class EpicCustomItems(JQuest):
    def __init__(self, id, name, descr):
        JQuest.__init__(self, id, name, descr)
        
    def onAdvEvent(self, event, npc, player):
        if event == "obtener_armas_epicas":
            self.darArmasEpicas(player)
            return "¡Has recibido armas épicas personalizadas!"
        elif event == "obtener_armaduras_epicas":
            self.darArmadurasEpicas(player)
            return "¡Has recibido armaduras épicas personalizadas!"
        elif event == "obtener_joyas_epicas":
            self.darJoyasEpicas(player)
            return "¡Has recibido joyas épicas personalizadas!"
        elif event == "obtener_consumibles_epicos":
            self.darConsumiblesEpicos(player)
            return "¡Has recibido consumibles épicos personalizados!"
        elif event == "obtener_todos_epicos":
            self.darTodosLosEpicos(player)
            return "¡Has recibido todos los items épicos personalizados!"
        return None
    
    def darArmasEpicas(self, player):
        # Armas épicas personalizadas
        armas_epicas = [
            (6611, 1),   # Draconic Bow
            (6612, 1),   # Draconic Bow
            (6613, 1),   # Draconic Bow
            (6614, 1),   # Draconic Bow
            (6615, 1),   # Draconic Bow
            (6616, 1),   # Draconic Bow
            (6617, 1),   # Draconic Bow
            (6618, 1),   # Draconic Bow
            (6619, 1),   # Draconic Bow
            (6620, 1),   # Draconic Bow
            (6621, 1),   # Draconic Bow
            (6622, 1),   # Draconic Bow
            (6623, 1),   # Draconic Bow
            (6624, 1),   # Draconic Bow
            (6625, 1),   # Draconic Bow
            (6626, 1),   # Draconic Bow
            (6627, 1),   # Draconic Bow
            (6628, 1),   # Draconic Bow
            (6629, 1),   # Draconic Bow
            (6630, 1),   # Draconic Bow
        ]
        
        for itemId, count in armas_epicas:
            player.addItem("ArmasEpicas", itemId, count, player, True)
        
        player.sendMessage("¡Has recibido armas épicas personalizadas!")
    
    def darArmadurasEpicas(self, player):
        # Armaduras épicas personalizadas
        armaduras_epicas = [
            (6651, 50),  # Life Stone
            (6652, 30),  # Mid Life Stone
            (6653, 20),  # High Life Stone
            (6654, 10),  # Top Life Stone
            (6655, 5),   # Soul Stone
            (6656, 3),   # Mid Soul Stone
            (6657, 2),   # High Soul Stone
            (6658, 1),   # Top Soul Stone
            (6659, 1),   # Soul Stone
            (6660, 1),   # Soul Stone
            (6661, 1),   # Soul Stone
            (6662, 1),   # Soul Stone
            (6663, 1),   # Soul Stone
            (6664, 1),   # Soul Stone
            (6665, 1),   # Soul Stone
            (6666, 1),   # Soul Stone
            (6667, 1),   # Soul Stone
            (6668, 1),   # Soul Stone
            (6669, 1),   # Soul Stone
            (6670, 1),   # Soul Stone
        ]
        
        for itemId, count in armaduras_epicas:
            player.addItem("ArmadurasEpicas", itemId, count, player, True)
        
        player.sendMessage("¡Has recibido armaduras épicas personalizadas!")
    
    def darJoyasEpicas(self, player):
        # Joyas épicas personalizadas
        joyas_epicas = [
            (6671, 1),   # Soul Stone
            (6672, 1),   # Soul Stone
            (6673, 1),   # Soul Stone
            (6674, 1),   # Soul Stone
            (6675, 1),   # Soul Stone
            (6676, 1),   # Soul Stone
            (6677, 1),   # Soul Stone
            (6678, 1),   # Soul Stone
            (6679, 1),   # Soul Stone
            (6680, 1),   # Soul Stone
            (6681, 1),   # Soul Stone
            (6682, 1),   # Soul Stone
            (6683, 1),   # Soul Stone
            (6684, 1),   # Soul Stone
            (6685, 1),   # Soul Stone
            (6686, 1),   # Soul Stone
            (6687, 1),   # Soul Stone
            (6688, 1),   # Soul Stone
            (6689, 1),   # Soul Stone
            (6690, 1),   # Soul Stone
        ]
        
        for itemId, count in joyas_epicas:
            player.addItem("JoyasEpicas", itemId, count, player, True)
        
        player.sendMessage("¡Has recibido joyas épicas personalizadas!")
    
    def darConsumiblesEpicos(self, player):
        # Consumibles épicos personalizados
        consumibles_epicos = [
            (6691, 100), # Soul Stone
            (6692, 100), # Soul Stone
            (6693, 100), # Soul Stone
            (6694, 100), # Soul Stone
            (6695, 100), # Soul Stone
            (6696, 100), # Soul Stone
            (6697, 100), # Soul Stone
            (6698, 100), # Soul Stone
            (6699, 100), # Soul Stone
            (6700, 100), # Soul Stone
            (6701, 100), # Soul Stone
            (6702, 100), # Soul Stone
            (6703, 100), # Soul Stone
            (6704, 100), # Soul Stone
            (6705, 100), # Soul Stone
            (6706, 100), # Soul Stone
            (6707, 100), # Soul Stone
            (6708, 100), # Soul Stone
            (6709, 100), # Soul Stone
            (6710, 100), # Soul Stone
        ]
        
        for itemId, count in consumibles_epicos:
            player.addItem("ConsumiblesEpicos", itemId, count, player, True)
        
        player.sendMessage("¡Has recibido consumibles épicos personalizados!")
    
    def darTodosLosEpicos(self, player):
        # Dar todos los items épicos
        self.darArmasEpicas(player)
        self.darArmadurasEpicas(player)
        self.darJoyasEpicas(player)
        self.darConsumiblesEpicos(player)
        
        # Adena épica adicional
        player.addAdena("TodosEpicos", 10000000)
        
        player.sendMessage("¡¡¡ HAS RECIBIDO TODOS LOS ITEMS ÉPICOS PERSONALIZADOS !!!")

# Crear instancia del sistema de items personalizados
ITEMS_PERSONALIZADOS_EPICOS = EpicCustomItems(-1, "ItemsPersonalizadosEpicos", "Sistema de Items Personalizados Épicos")

# Registrar el sistema
ITEMS_PERSONALIZADOS_EPICOS.addStartNpc(30006)  # Tienda GM
ITEMS_PERSONALIZADOS_EPICOS.addTalkId(30006)
