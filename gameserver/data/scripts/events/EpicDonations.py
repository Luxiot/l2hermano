# ===========================================
# DONACIONES ÉPICAS - L2 HERMANOS
# ===========================================
# Sistema de donaciones épicas
# Epic donations system

import sys
from java.util import Calendar
from l2jfrozen.gameserver.model.quest import State
from l2jfrozen.gameserver.model.quest import QuestState
from l2jfrozen.gameserver.model.quest import Quest as JQuest
from l2jfrozen.gameserver.model.actor.instance import L2PcInstance
from l2jfrozen.gameserver.network.serverpackets import NpcHtmlMessage
from l2jfrozen.gameserver.network.serverpackets import SystemMessage
from l2jfrozen.gameserver.network.serverpackets import CreatureSay
from l2jfrozen.gameserver.GameServer import GameServer

class EpicDonations(JQuest):
    def __init__(self, id, name, descr):
        JQuest.__init__(self, id, name, descr)
        self.donationPackages = {
            "BRONCE": {
                "name": "Paquete Bronce Épico",
                "description": "Paquete básico para comenzar tu aventura épica",
                "cost": 5,  # USD
                "rewards": {
                    "adena": 5000000,
                    "ancient_adena": 500000,
                    "items": [
                        (6651, 20),  # Life Stone
                        (6652, 10),  # Mid Life Stone
                        (6653, 5),   # High Life Stone
                        (6654, 2),   # Top Life Stone
                        (6655, 1),   # Soul Stone
                    ]
                }
            },
            "PLATA": {
                "name": "Paquete Plata Épico",
                "description": "Paquete intermedio con recompensas épicas",
                "cost": 10,  # USD
                "rewards": {
                    "adena": 15000000,
                    "ancient_adena": 1500000,
                    "items": [
                        (6651, 50),  # Life Stone
                        (6652, 25),  # Mid Life Stone
                        (6653, 15),  # High Life Stone
                        (6654, 8),   # Top Life Stone
                        (6655, 5),   # Soul Stone
                        (6656, 3),   # Mid Soul Stone
                        (6657, 2),   # High Soul Stone
                    ]
                }
            },
            "ORO": {
                "name": "Paquete Oro Épico",
                "description": "Paquete avanzado con recompensas legendarias",
                "cost": 20,  # USD
                "rewards": {
                    "adena": 35000000,
                    "ancient_adena": 3500000,
                    "items": [
                        (6651, 100), # Life Stone
                        (6652, 50),  # Mid Life Stone
                        (6653, 30),  # High Life Stone
                        (6654, 20),  # Top Life Stone
                        (6655, 15),  # Soul Stone
                        (6656, 10),  # Mid Soul Stone
                        (6657, 8),   # High Soul Stone
                        (6658, 5),   # Top Soul Stone
                    ]
                }
            },
            "DIAMANTE": {
                "name": "Paquete Diamante Épico",
                "description": "Paquete premium con recompensas épicas únicas",
                "cost": 50,  # USD
                "rewards": {
                    "adena": 100000000,
                    "ancient_adena": 10000000,
                    "items": [
                        (6651, 200), # Life Stone
                        (6652, 100), # Mid Life Stone
                        (6653, 75),  # High Life Stone
                        (6654, 50),  # Top Life Stone
                        (6655, 40),  # Soul Stone
                        (6656, 30),  # Mid Soul Stone
                        (6657, 25),  # High Soul Stone
                        (6658, 20),  # Top Soul Stone
                        (6659, 15),  # Soul Stone
                        (6660, 10),  # Soul Stone
                    ]
                }
            },
            "LEGENDARIO": {
                "name": "Paquete Legendario Épico",
                "description": "Paquete definitivo con recompensas legendarias",
                "cost": 100,  # USD
                "rewards": {
                    "adena": 250000000,
                    "ancient_adena": 25000000,
                    "items": [
                        (6651, 500), # Life Stone
                        (6652, 250), # Mid Life Stone
                        (6653, 200), # High Life Stone
                        (6654, 150), # Top Life Stone
                        (6655, 100), # Soul Stone
                        (6656, 75),  # Mid Soul Stone
                        (6657, 60),  # High Soul Stone
                        (6658, 50),  # Top Soul Stone
                        (6659, 40),  # Soul Stone
                        (6660, 30),  # Soul Stone
                        (6661, 25),  # Soul Stone
                        (6662, 20),  # Soul Stone
                    ]
                }
            }
        }
        
    def onAdvEvent(self, event, npc, player):
        if event == "mostrar_donaciones":
            return self.mostrarDonaciones(player)
        elif event.startswith("comprar_"):
            packageKey = event.replace("comprar_", "")
            return self.comprarPaquete(player, packageKey)
        elif event == "ver_beneficios":
            return self.verBeneficios(player)
        elif event == "ver_ranking_donadores":
            return self.verRankingDonadores(player)
        return None
    
    def mostrarDonaciones(self, player):
        html = "<html><body>"
        html += "<center><font color=\"LEVEL\">¡¡¡ DONACIONES ÉPICAS DE L2 HERMANOS !!!</font></center><br>"
        html += "<center><font color=\"LEVEL\">¡¡¡ EPIC DONATIONS OF L2 HERMANOS !!!</font></center><br><br>"
        
        html += "<font color=\"LEVEL\">💰 PAQUETES DE DONACIÓN / DONATION PACKAGES:</font><br><br>"
        
        for packageKey, packageInfo in self.donationPackages.items():
            html += "<font color=\"LEVEL\">" + packageInfo["name"] + "</font><br>"
            html += "<font color=\"WHITE\">" + packageInfo["description"] + "</font><br>"
            html += "<font color=\"YELLOW\">Costo: $" + str(packageInfo["cost"]) + " USD / Cost: $" + str(packageInfo["cost"]) + " USD</font><br>"
            html += "<font color=\"GREEN\">Adena: " + str(packageInfo["rewards"]["adena"]) + " / Ancient Adena: " + str(packageInfo["rewards"]["ancient_adena"]) + "</font><br>"
            html += "<font color=\"GREEN\">Items: " + str(len(packageInfo["rewards"]["items"])) + " items épicos</font><br>"
            html += "<button value=\"Comprar " + packageInfo["name"] + "\" action=\"bypass -h Quest EpicDonations comprar_" + packageKey + "\" width=200 height=25 back=\"L2UI_ct1.button_df\" fore=\"L2UI_ct1.button_df\"><br><br>"
        
        html += "<font color=\"LEVEL\">🎯 ACCIONES DISPONIBLES / AVAILABLE ACTIONS:</font><br>"
        html += "<button value=\"Ver Beneficios\" action=\"bypass -h Quest EpicDonations ver_beneficios\" width=200 height=25 back=\"L2UI_ct1.button_df\" fore=\"L2UI_ct1.button_df\"><br>"
        html += "<button value=\"Ver Ranking Donadores\" action=\"bypass -h Quest EpicDonations ver_ranking_donadores\" width=200 height=25 back=\"L2UI_ct1.button_df\" fore=\"L2UI_ct1.button_df\"><br>"
        
        html += "<br><font color=\"LEVEL\">🏆 BENEFICIOS DE DONAR / DONATION BENEFITS:</font><br>"
        html += "• Recompensas épicas instantáneas / Instant epic rewards<br>"
        html += "• Acceso a zonas exclusivas / Access to exclusive zones<br>"
        html += "• Comandos especiales / Special commands<br>"
        html += "• Títulos únicos / Unique titles<br>"
        html += "• Soporte prioritario / Priority support<br>"
        
        html += "<br><font color=\"LEVEL\">💳 MÉTODOS DE PAGO / PAYMENT METHODS:</font><br>"
        html += "• PayPal / PayPal<br>"
        html += "• Tarjeta de Crédito / Credit Card<br>"
        html += "• Transferencia Bancaria / Bank Transfer<br>"
        html += "• Criptomonedas / Cryptocurrencies<br>"
        
        html += "<br><font color=\"LEVEL\">¡¡¡ APOYA A L2 HERMANOS Y OBTÉN RECOMPENSAS ÉPICAS !!!</font><br>"
        html += "<font color=\"LEVEL\">¡¡¡ SUPPORT L2 HERMANOS AND GET EPIC REWARDS !!!</font><br>"
        
        html += "</body></html>"
        
        reply = NpcHtmlMessage(1)
        reply.setHtml(html)
        player.sendPacket(reply)
        return None
    
    def comprarPaquete(self, player, packageKey):
        if packageKey not in self.donationPackages:
            return "Paquete no encontrado."
        
        packageInfo = self.donationPackages[packageKey]
        
        # Simular compra (en un servidor real, esto se conectaría con un sistema de pagos)
        html = "<html><body>"
        html += "<center><font color=\"LEVEL\">¡¡¡ COMPRA DE " + packageInfo["name"].upper() + " !!!</font></center><br>"
        html += "<center><font color=\"LEVEL\">¡¡¡ PURCHASE OF " + packageInfo["name"].upper() + " !!!</font></center><br><br>"
        
        html += "<font color=\"LEVEL\">💰 INFORMACIÓN DE COMPRA / PURCHASE INFORMATION:</font><br>"
        html += "• Paquete: " + packageInfo["name"] + " / Package: " + packageInfo["name"] + "<br>"
        html += "• Costo: $" + str(packageInfo["cost"]) + " USD / Cost: $" + str(packageInfo["cost"]) + " USD<br>"
        html += "• Jugador: " + player.getName() + " / Player: " + player.getName() + "<br>"
        
        html += "<br><font color=\"LEVEL\">🎁 RECOMPENSAS INCLUIDAS / INCLUDED REWARDS:</font><br>"
        html += "• Adena: " + str(packageInfo["rewards"]["adena"]) + "<br>"
        html += "• Ancient Adena: " + str(packageInfo["rewards"]["ancient_adena"]) + "<br>"
        html += "• Items: " + str(len(packageInfo["rewards"]["items"])) + " items épicos<br>"
        
        html += "<br><font color=\"LEVEL\">💳 INSTRUCCIONES DE PAGO / PAYMENT INSTRUCTIONS:</font><br>"
        html += "1. Contacta a un GM en el juego / Contact a GM in-game<br>"
        html += "2. Proporciona tu nombre de usuario / Provide your username<br>"
        html += "3. Realiza el pago / Make the payment<br>"
        html += "4. Recibe tus recompensas épicas / Receive your epic rewards<br>"
        
        html += "<br><font color=\"LEVEL\">📞 CONTACTO / CONTACT:</font><br>"
        html += "• Discord: L2 Hermanos Official<br>"
        html += "• WhatsApp: +1-XXX-XXX-XXXX<br>"
        html += "• Email: l2hermanos@gmail.com<br>"
        
        html += "<br><font color=\"LEVEL\">¡¡¡ GRACIAS POR APOYAR A L2 HERMANOS !!!</font><br>"
        html += "<font color=\"LEVEL\">¡¡¡ THANK YOU FOR SUPPORTING L2 HERMANOS !!!</font><br>"
        
        html += "</body></html>"
        
        reply = NpcHtmlMessage(1)
        reply.setHtml(html)
        player.sendPacket(reply)
        
        # Mensaje épico
        player.sendMessage("¡¡¡ INFORMACIÓN DE COMPRA ENVIADA !!!")
        player.sendMessage("¡¡¡ PURCHASE INFORMATION SENT !!!")
        player.sendMessage("¡Contacta a un GM para completar tu compra!")
        player.sendMessage("Contact a GM to complete your purchase!")
        
        # Anuncio épico
        self.announceToAll(player.getName() + " está interesado en el " + packageInfo["name"] + "!")
        self.announceToAll(player.getName() + " is interested in the " + packageInfo["name"] + "!")
        
        return None
    
    def verBeneficios(self, player):
        html = "<html><body>"
        html += "<center><font color=\"LEVEL\">¡¡¡ BENEFICIOS DE DONAR A L2 HERMANOS !!!</font></center><br>"
        html += "<center><font color=\"LEVEL\">¡¡¡ BENEFITS OF DONATING TO L2 HERMANOS !!!</font></center><br><br>"
        
        html += "<font color=\"LEVEL\">🏆 BENEFICIOS INMEDIATOS / IMMEDIATE BENEFITS:</font><br>"
        html += "• Recompensas épicas instantáneas / Instant epic rewards<br>"
        html += "• Adena y Ancient Adena / Adena and Ancient Adena<br>"
        html += "• Items épicos únicos / Unique epic items<br>"
        html += "• Life Stones y Soul Stones / Life Stones and Soul Stones<br>"
        
        html += "<br><font color=\"LEVEL\">🌟 BENEFICIOS PERMANENTES / PERMANENT BENEFITS:</font><br>"
        html += "• Acceso a zonas exclusivas / Access to exclusive zones<br>"
        html += "• Comandos especiales / Special commands<br>"
        html += "• Títulos únicos / Unique titles<br>"
        html += "• Soporte prioritario / Priority support<br>"
        html += "• Descuentos en futuras compras / Discounts on future purchases<br>"
        
        html += "<br><font color=\"LEVEL\">🎯 BENEFICIOS POR NIVEL / BENEFITS BY LEVEL:</font><br>"
        html += "• Bronce: Acceso básico / Bronze: Basic access<br>"
        html += "• Plata: Acceso intermedio / Silver: Intermediate access<br>"
        html += "• Oro: Acceso avanzado / Gold: Advanced access<br>"
        html += "• Diamante: Acceso premium / Diamond: Premium access<br>"
        html += "• Legendario: Acceso VIP / Legendary: VIP access<br>"
        
        html += "<br><font color=\"LEVEL\">💎 BENEFICIOS VIP / VIP BENEFITS:</font><br>"
        html += "• Zona VIP exclusiva / Exclusive VIP zone<br>"
        html += "• NPCs especiales / Special NPCs<br>"
        html += "• Eventos exclusivos / Exclusive events<br>"
        html += "• Recompensas diarias / Daily rewards<br>"
        html += "• Soporte 24/7 / 24/7 support<br>"
        
        html += "<br><font color=\"LEVEL\">¡¡¡ APOYA A L2 HERMANOS Y DISFRUTA DE BENEFICIOS ÉPICOS !!!</font><br>"
        html += "<font color=\"LEVEL\">¡¡¡ SUPPORT L2 HERMANOS AND ENJOY EPIC BENEFITS !!!</font><br>"
        
        html += "</body></html>"
        
        reply = NpcHtmlMessage(1)
        reply.setHtml(html)
        player.sendPacket(reply)
        return None
    
    def verRankingDonadores(self, player):
        html = "<html><body>"
        html += "<center><font color=\"LEVEL\">¡¡¡ RANKING DE DONADORES ÉPICOS !!!</font></center><br>"
        html += "<center><font color=\"LEVEL\">¡¡¡ EPIC DONATORS RANKING !!!</font></center><br><br>"
        
        html += "<font color=\"LEVEL\">🏆 TOP 10 DONADORES / TOP 10 DONATORS:</font><br><br>"
        
        # Simular ranking (en un servidor real, esto vendría de la base de datos)
        topDonators = [
            {"name": "EpicDonator1", "amount": 500, "level": "Legendario"},
            {"name": "EpicDonator2", "amount": 300, "level": "Diamante"},
            {"name": "EpicDonator3", "amount": 200, "level": "Oro"},
            {"name": "EpicDonator4", "amount": 150, "level": "Oro"},
            {"name": "EpicDonator5", "amount": 100, "level": "Plata"},
            {"name": "EpicDonator6", "amount": 80, "level": "Plata"},
            {"name": "EpicDonator7", "amount": 60, "level": "Bronce"},
            {"name": "EpicDonator8", "amount": 40, "level": "Bronce"},
            {"name": "EpicDonator9", "amount": 20, "level": "Bronce"},
            {"name": "EpicDonator10", "amount": 10, "level": "Bronce"}
        ]
        
        for i, donatorInfo in enumerate(topDonators, 1):
            medal = "🥇" if i == 1 else "🥈" if i == 2 else "🥉" if i == 3 else "🏅"
            html += "<font color=\"LEVEL\">" + medal + " #" + str(i) + " " + donatorInfo["name"] + "</font><br>"
            html += "<font color=\"WHITE\">Monto: $" + str(donatorInfo["amount"]) + " USD | Nivel: " + donatorInfo["level"] + "</font><br>"
            html += "<font color=\"WHITE\">Amount: $" + str(donatorInfo["amount"]) + " USD | Level: " + donatorInfo["level"] + "</font><br><br>"
        
        html += "<font color=\"LEVEL\">📊 ESTADÍSTICAS DEL SERVIDOR / SERVER STATISTICS:</font><br>"
        html += "• Total recaudado: $2,500 USD / Total raised: $2,500 USD<br>"
        html += "• Donadores activos: 150 / Active donators: 150<br>"
        html += "• Promedio por donación: $25 USD / Average per donation: $25 USD<br>"
        
        html += "<br><font color=\"LEVEL\">¡¡¡ ÚNETE A LOS DONADORES ÉPICOS !!!</font><br>"
        html += "<font color=\"LEVEL\">¡¡¡ JOIN THE EPIC DONATORS !!!</font><br>"
        
        html += "</body></html>"
        
        reply = NpcHtmlMessage(1)
        reply.setHtml(html)
        player.sendPacket(reply)
        return None
    
    def announceToAll(self, message):
        from l2jfrozen.gameserver.network.serverpackets import CreatureSay
        from l2jfrozen.gameserver.model.actor.instance import L2PcInstance
        from l2jfrozen.gameserver.GameServer import GameServer
        
        for player in GameServer.getInstance().getAllPlayers():
            if player and player.isOnline():
                player.sendPacket(CreatureSay(0, 1, "DONACIONES ÉPICAS", message))

# Crear instancia del sistema de donaciones épicas
DONACIONES_EPICAS = EpicDonations(-1, "DonacionesEpicas", "Sistema de Donaciones Épicas")

# Registrar el sistema
DONACIONES_EPICAS.addStartNpc(30006)  # Tienda GM
DONACIONES_EPICAS.addTalkId(30006)



