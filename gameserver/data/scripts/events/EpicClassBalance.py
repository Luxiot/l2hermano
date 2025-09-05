# ===========================================
# BALANCEO ÉPICO DE CLASES - MEJOR SERVIDOR L2
# ===========================================
# Sistema de balanceo épico para todas las clases

import sys
from java.util import Calendar
from l2jfrozen.gameserver.model.quest import State
from l2jfrozen.gameserver.model.quest import QuestState
from l2jfrozen.gameserver.model.quest.jython import QuestJython as JQuest
from l2jfrozen.gameserver.model.actor.instance import L2PcInstance
from l2jfrozen.gameserver.model.actor.instance import L2NpcInstance
from l2jfrozen.gameserver.network.serverpackets import NpcHtmlMessage
from l2jfrozen.gameserver.network.serverpackets import SystemMessage

class EpicClassBalance(JQuest):
    def __init__(self, id, name, descr):
        JQuest.__init__(self, id, name, descr)
        
    def onAdvEvent(self, event, npc, player):
        if event == "balancear_guerrero":
            self.balancearGuerrero(player)
            return "¡Clase Guerrero balanceada épicamente!"
        elif event == "balancear_mago":
            self.balancearMago(player)
            return "¡Clase Mago balanceada épicamente!"
        elif event == "balancear_arquero":
            self.balancearArquero(player)
            return "¡Clase Arquero balanceada épicamente!"
        elif event == "balancear_picaro":
            self.balancearPicaro(player)
            return "¡Clase Pícaro balanceada épicamente!"
        elif event == "balancear_todas":
            self.balancearTodasLasClases(player)
            return "¡Todas las clases balanceadas épicamente!"
        return None
    
    def balancearGuerrero(self, player):
        # Buffs épicos para guerreros
        buffs_guerrero = [
            (1085, 3),   # Acumen
            (1086, 2),   # Haste
            (1087, 3),   # Agility
            (1044, 3),   # Regeneration
            (1045, 6),   # Mental Shield
            (1048, 6),   # Spell Shield
            (1059, 3),   # Empower
            (1062, 2),   # Berserker Spirit
            (1068, 3),   # Might
            (1077, 3),   # Focus
            (1078, 6),   # Concentration
            (1086, 2),   # Haste
            (1204, 2),   # Wind Walk
            (1242, 3),   # Death Whisper
            (1243, 6),   # Bless Shield
            (1257, 3),   # Decrease Weight
            (1259, 4),   # Resist Shock
            (1268, 4),   # Vampiric Rage
            (1282, 2),   # Pa'agrio's Haste
            (1284, 3),   # Pa'agrio's Gift
            (1303, 2),   # Wild Magic
            (1304, 3),   # Advanced Block
            (1306, 6),   # Rune of Protection
            (1308, 3),   # Advanced Fortitude
            (1309, 3),   # Advanced Resist
            (1310, 4),   # Master's Blessing
            (1311, 6),   # Body of Avatar
            (1352, 1),   # Golem Armor
            (1353, 3),   # Pa'agrio's Eye
            (1354, 1),   # Pa'agrio's Soul
            (1355, 1),   # Pa'agrio's Blessing
            (1356, 1),   # Pa'agrio's Wisdom
            (1357, 33),  # Pa'agrio's Protection
            (1362, 1),   # Pa'agrio's Haste
            (1363, 1),   # Pa'agrio's Gift
            (1388, 3),   # Greater Might
            (1389, 3),   # Greater Shield
            (1390, 3),   # Greater Magic Barrier
            (1391, 3),   # Greater Magic Haste
            (1397, 3),   # Clarity
            (1413, 1),   # Pa'agrio's Protection
        ]
        
        for skillId, level in buffs_guerrero:
            player.addSkill(skillId, level)
        
        player.sendMessage("¡Has recibido buffs épicos de Guerrero!")
        player.sendSkillList()
    
    def balancearMago(self, player):
        # Buffs épicos para magos
        buffs_mago = [
            (1085, 3),   # Acumen
            (1086, 2),   # Haste
            (1087, 3),   # Agility
            (1044, 3),   # Regeneration
            (1045, 6),   # Mental Shield
            (1048, 6),   # Spell Shield
            (1059, 3),   # Empower
            (1062, 2),   # Berserker Spirit
            (1068, 3),   # Might
            (1077, 3),   # Focus
            (1078, 6),   # Concentration
            (1086, 2),   # Haste
            (1204, 2),   # Wind Walk
            (1242, 3),   # Death Whisper
            (1243, 6),   # Bless Shield
            (1257, 3),   # Decrease Weight
            (1259, 4),   # Resist Shock
            (1268, 4),   # Vampiric Rage
            (1282, 2),   # Pa'agrio's Haste
            (1284, 3),   # Pa'agrio's Gift
            (1303, 2),   # Wild Magic
            (1304, 3),   # Advanced Block
            (1306, 6),   # Rune of Protection
            (1308, 3),   # Advanced Fortitude
            (1309, 3),   # Advanced Resist
            (1310, 4),   # Master's Blessing
            (1311, 6),   # Body of Avatar
            (1352, 1),   # Golem Armor
            (1353, 3),   # Pa'agrio's Eye
            (1354, 1),   # Pa'agrio's Soul
            (1355, 1),   # Pa'agrio's Blessing
            (1356, 1),   # Pa'agrio's Wisdom
            (1357, 33),  # Pa'agrio's Protection
            (1362, 1),   # Pa'agrio's Haste
            (1363, 1),   # Pa'agrio's Gift
            (1388, 3),   # Greater Might
            (1389, 3),   # Greater Shield
            (1390, 3),   # Greater Magic Barrier
            (1391, 3),   # Greater Magic Haste
            (1397, 3),   # Clarity
            (1413, 1),   # Pa'agrio's Protection
        ]
        
        for skillId, level in buffs_mago:
            player.addSkill(skillId, level)
        
        player.sendMessage("¡Has recibido buffs épicos de Mago!")
        player.sendSkillList()
    
    def balancearArquero(self, player):
        # Buffs épicos para arqueros
        buffs_arquero = [
            (1085, 3),   # Acumen
            (1086, 2),   # Haste
            (1087, 3),   # Agility
            (1044, 3),   # Regeneration
            (1045, 6),   # Mental Shield
            (1048, 6),   # Spell Shield
            (1059, 3),   # Empower
            (1062, 2),   # Berserker Spirit
            (1068, 3),   # Might
            (1077, 3),   # Focus
            (1078, 6),   # Concentration
            (1086, 2),   # Haste
            (1204, 2),   # Wind Walk
            (1242, 3),   # Death Whisper
            (1243, 6),   # Bless Shield
            (1257, 3),   # Decrease Weight
            (1259, 4),   # Resist Shock
            (1268, 4),   # Vampiric Rage
            (1282, 2),   # Pa'agrio's Haste
            (1284, 3),   # Pa'agrio's Gift
            (1303, 2),   # Wild Magic
            (1304, 3),   # Advanced Block
            (1306, 6),   # Rune of Protection
            (1308, 3),   # Advanced Fortitude
            (1309, 3),   # Advanced Resist
            (1310, 4),   # Master's Blessing
            (1311, 6),   # Body of Avatar
            (1352, 1),   # Golem Armor
            (1353, 3),   # Pa'agrio's Eye
            (1354, 1),   # Pa'agrio's Soul
            (1355, 1),   # Pa'agrio's Blessing
            (1356, 1),   # Pa'agrio's Wisdom
            (1357, 33),  # Pa'agrio's Protection
            (1362, 1),   # Pa'agrio's Haste
            (1363, 1),   # Pa'agrio's Gift
            (1388, 3),   # Greater Might
            (1389, 3),   # Greater Shield
            (1390, 3),   # Greater Magic Barrier
            (1391, 3),   # Greater Magic Haste
            (1397, 3),   # Clarity
            (1413, 1),   # Pa'agrio's Protection
        ]
        
        for skillId, level in buffs_arquero:
            player.addSkill(skillId, level)
        
        player.sendMessage("¡Has recibido buffs épicos de Arquero!")
        player.sendSkillList()
    
    def balancearPicaro(self, player):
        # Buffs épicos para pícaros
        buffs_picaro = [
            (1085, 3),   # Acumen
            (1086, 2),   # Haste
            (1087, 3),   # Agility
            (1044, 3),   # Regeneration
            (1045, 6),   # Mental Shield
            (1048, 6),   # Spell Shield
            (1059, 3),   # Empower
            (1062, 2),   # Berserker Spirit
            (1068, 3),   # Might
            (1077, 3),   # Focus
            (1078, 6),   # Concentration
            (1086, 2),   # Haste
            (1204, 2),   # Wind Walk
            (1242, 3),   # Death Whisper
            (1243, 6),   # Bless Shield
            (1257, 3),   # Decrease Weight
            (1259, 4),   # Resist Shock
            (1268, 4),   # Vampiric Rage
            (1282, 2),   # Pa'agrio's Haste
            (1284, 3),   # Pa'agrio's Gift
            (1303, 2),   # Wild Magic
            (1304, 3),   # Advanced Block
            (1306, 6),   # Rune of Protection
            (1308, 3),   # Advanced Fortitude
            (1309, 3),   # Advanced Resist
            (1310, 4),   # Master's Blessing
            (1311, 6),   # Body of Avatar
            (1352, 1),   # Golem Armor
            (1353, 3),   # Pa'agrio's Eye
            (1354, 1),   # Pa'agrio's Soul
            (1355, 1),   # Pa'agrio's Blessing
            (1356, 1),   # Pa'agrio's Wisdom
            (1357, 33),  # Pa'agrio's Protection
            (1362, 1),   # Pa'agrio's Haste
            (1363, 1),   # Pa'agrio's Gift
            (1388, 3),   # Greater Might
            (1389, 3),   # Greater Shield
            (1390, 3),   # Greater Magic Barrier
            (1391, 3),   # Greater Magic Haste
            (1397, 3),   # Clarity
            (1413, 1),   # Pa'agrio's Protection
        ]
        
        for skillId, level in buffs_picaro:
            player.addSkill(skillId, level)
        
        player.sendMessage("¡Has recibido buffs épicos de Pícaro!")
        player.sendSkillList()
    
    def balancearTodasLasClases(self, player):
        # Balancear todas las clases
        self.balancearGuerrero(player)
        self.balancearMago(player)
        self.balancearArquero(player)
        self.balancearPicaro(player)
        
        player.sendMessage("¡¡¡ TODAS LAS CLASES BALANCEADAS ÉPICAMENTE !!!")

# Crear instancia del sistema de balanceo
BALANCEO_EPICO_CLASES = EpicClassBalance(-1, "BalanceoEpicoClases", "Sistema de Balanceo Épico de Clases")

# Registrar el sistema
BALANCEO_EPICO_CLASES.addStartNpc(30006)  # Tienda GM
BALANCEO_EPICO_CLASES.addTalkId(30006)
