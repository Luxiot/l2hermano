# ===========================================
# CLASES ÉPICAS PERSONALIZADAS - L2 HERMANOS
# ===========================================
# Sistema de clases épicas únicas para L2 Hermanos
# Epic unique classes system for L2 Hermanos

import sys
from java.util import Calendar
from l2jfrozen.gameserver.model.quest import State
from l2jfrozen.gameserver.model.quest import QuestState
from l2jfrozen.gameserver.model.quest import Quest as JQuest
from l2jfrozen.gameserver.datatables import SkillTable
from l2jfrozen.gameserver.model.actor.instance import L2PcInstance
from l2jfrozen.gameserver.network.serverpackets import NpcHtmlMessage
from l2jfrozen.gameserver.network.serverpackets import SystemMessage
from l2jfrozen.gameserver.network.serverpackets import CreatureSay
from l2jfrozen.gameserver.GameServer import GameServer

class EpicCustomClasses(JQuest):
    def __init__(self, id, name, descr):
        JQuest.__init__(self, id, name, descr)
        self.epicClasses = {
            "GUERRERO_EPICO": {
                "name": "Guerrero Épico",
                "description": "Guerrero con poderes épicos únicos",
                "skills": [1001, 1002, 1003, 1004, 1005],
                "transform": 1001,
                "buffs": [1085, 1086, 1087, 1044, 1045]
            },
            "MAGO_EPICO": {
                "name": "Mago Épico",
                "description": "Mago con magia épica destructiva",
                "skills": [2001, 2002, 2003, 2004, 2005],
                "transform": 2001,
                "buffs": [1085, 1086, 1087, 1044, 1045]
            },
            "ARQUERO_EPICO": {
                "name": "Arquero Épico",
                "description": "Arquero con precisión épica",
                "skills": [3001, 3002, 3003, 3004, 3005],
                "transform": 3001,
                "buffs": [1085, 1086, 1087, 1044, 1045]
            },
            "PICARO_EPICO": {
                "name": "Pícaro Épico",
                "description": "Pícaro con sigilo épico",
                "skills": [4001, 4002, 4003, 4004, 4005],
                "transform": 4001,
                "buffs": [1085, 1086, 1087, 1044, 1045]
            }
        }
        
    def onAdvEvent(self, event, npc, player):
        if event == "mostrar_clases_epicas":
            return self.mostrarClasesEpicas(player)
        elif event == "convertir_guerrero_epico":
            return self.convertirAClaseEpica(player, "GUERRERO_EPICO")
        elif event == "convertir_mago_epico":
            return self.convertirAClaseEpica(player, "MAGO_EPICO")
        elif event == "convertir_arquero_epico":
            return self.convertirAClaseEpica(player, "ARQUERO_EPICO")
        elif event == "convertir_picaro_epico":
            return self.convertirAClaseEpica(player, "PICARO_EPICO")
        elif event == "activar_transformacion_epica":
            return self.activarTransformacionEpica(player)
        elif event == "desactivar_transformacion_epica":
            return self.desactivarTransformacionEpica(player)
        return None
    
    def mostrarClasesEpicas(self, player):
        html = "<html><body>"
        html += "<center><font color=\"LEVEL\">¡¡¡ CLASES ÉPICAS DE L2 HERMANOS !!!</font></center><br>"
        html += "<center><font color=\"LEVEL\">¡¡¡ EPIC CLASSES OF L2 HERMANOS !!!</font></center><br><br>"
        
        html += "<font color=\"LEVEL\">🌟 CLASES ÉPICAS DISPONIBLES / EPIC CLASSES AVAILABLE:</font><br><br>"
        
        for classKey, classInfo in self.epicClasses.items():
            html += "<font color=\"LEVEL\">" + classInfo["name"] + "</font><br>"
            html += "<font color=\"WHITE\">" + classInfo["description"] + "</font><br>"
            html += "<button value=\"Convertir a " + classInfo["name"] + "\" action=\"bypass -h Quest EpicCustomClasses convertir_" + classKey.lower() + "\" width=200 height=25 back=\"L2UI_ct1.button_df\" fore=\"L2UI_ct1.button_df\"><br><br>"
        
        html += "<br><font color=\"LEVEL\">🎯 TRANSFORMACIONES ÉPICAS / EPIC TRANSFORMATIONS:</font><br>"
        html += "<button value=\"Activar Transformación Épica\" action=\"bypass -h Quest EpicCustomClasses activar_transformacion_epica\" width=200 height=25 back=\"L2UI_ct1.button_df\" fore=\"L2UI_ct1.button_df\"><br>"
        html += "<button value=\"Desactivar Transformación Épica\" action=\"bypass -h Quest EpicCustomClasses desactivar_transformacion_epica\" width=200 height=25 back=\"L2UI_ct1.button_df\" fore=\"L2UI_ct1.button_df\"><br>"
        
        html += "<br><font color=\"LEVEL\">🏆 BENEFICIOS ÉPICOS / EPIC BENEFITS:</font><br>"
        html += "• +50% de daño / +50% damage<br>"
        html += "• +50% de velocidad de ataque / +50% attack speed<br>"
        html += "• +50% de velocidad de movimiento / +50% movement speed<br>"
        html += "• +50% de regeneración / +50% regeneration<br>"
        html += "• Habilidades épicas únicas / Unique epic skills<br>"
        html += "• Transformación épica / Epic transformation<br>"
        
        html += "<br><font color=\"LEVEL\">¡¡¡ CONVIÉRTETE EN UNA LEYENDA ÉPICA !!!</font><br>"
        html += "<font color=\"LEVEL\">¡¡¡ BECOME AN EPIC LEGEND !!!</font><br>"
        
        html += "</body></html>"
        
        reply = NpcHtmlMessage(1)
        reply.setHtml(html)
        player.sendPacket(reply)
        return None
    
    def convertirAClaseEpica(self, player, classKey):
        if classKey not in self.epicClasses:
            return "Clase épica no encontrada."
        
        classInfo = self.epicClasses[classKey]
        
        # Dar habilidades épicas
        for skillId in classInfo["skills"]:
            player.addSkill(skillId, 1)
        
        # Dar buffs épicos
        for buffId in classInfo["buffs"]:
            player.addSkill(buffId, 3)
        
        # Dar transformación épica
        player.setTransformation(classInfo["transform"])
        
        # Mensaje épico
        player.sendMessage("¡¡¡ TE HAS CONVERTIDO EN " + classInfo["name"].upper() + " !!!")
        player.sendMessage("¡¡¡ YOU HAVE BECOME " + classInfo["name"].upper() + " !!!")
        player.sendMessage("¡Has recibido habilidades épicas únicas!")
        player.sendMessage("You have received unique epic skills!")
        
        # Anuncio épico
        self.announceToAll(player.getName() + " se ha convertido en " + classInfo["name"] + "!")
        self.announceToAll(player.getName() + " has become " + classInfo["name"] + "!")
        
        return "¡Te has convertido en " + classInfo["name"] + "!"
    
    def activarTransformacionEpica(self, player):
        # Activar transformación épica
        player.setTransformation(1001)  # Transformación épica base
        
        # Buffs épicos adicionales
        epicBuffs = [1085, 1086, 1087, 1044, 1045, 1047, 1048, 1049, 1059, 1062]
        for buffId in epicBuffs:
            player.addSkill(buffId, 3)
        
        # Mensaje épico
        player.sendMessage("¡¡¡ TRANSFORMACIÓN ÉPICA ACTIVADA !!!")
        player.sendMessage("¡¡¡ EPIC TRANSFORMATION ACTIVATED !!!")
        player.sendMessage("¡Has recibido poderes épicos increíbles!")
        player.sendMessage("You have received incredible epic powers!")
        
        # Anuncio épico
        self.announceToAll(player.getName() + " ha activado su transformación épica!")
        self.announceToAll(player.getName() + " has activated their epic transformation!")
        
        return "¡Transformación épica activada!"
    
    def desactivarTransformacionEpica(self, player):
        # Desactivar transformación épica
        player.setTransformation(0)
        
        # Mensaje épico
        player.sendMessage("¡¡¡ TRANSFORMACIÓN ÉPICA DESACTIVADA !!!")
        player.sendMessage("¡¡¡ EPIC TRANSFORMATION DEACTIVATED !!!")
        player.sendMessage("¡Has vuelto a tu forma normal!")
        player.sendMessage("You have returned to your normal form!")
        
        return "¡Transformación épica desactivada!"
    
    def announceToAll(self, message):
        from l2jfrozen.gameserver.network.serverpackets import CreatureSay
        from l2jfrozen.gameserver.model.actor.instance import L2PcInstance
        from l2jfrozen.gameserver.GameServer import GameServer
        
        for player in GameServer.getInstance().getAllPlayers():
            if player and player.isOnline():
                player.sendPacket(CreatureSay(0, 1, "CLASES ÉPICAS", message))

# Crear instancia del sistema de clases épicas
CLASES_EPICAS_PERSONALIZADAS = EpicCustomClasses(-1, "ClasesEpicasPersonalizadas", "Sistema de Clases Épicas Personalizadas")

# Registrar el sistema
CLASES_EPICAS_PERSONALIZADAS.addStartNpc(30006)  # Tienda GM
CLASES_EPICAS_PERSONALIZADAS.addTalkId(30006)



