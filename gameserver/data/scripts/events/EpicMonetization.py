# ===========================================
# MONETIZACIÓN ÉPICA - L2 HERMANOS
# ===========================================
# Sistema de monetización con créditos y tienda
# Monetization system with credits and shop

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

class EpicMonetization(JQuest):
    def __init__(self, id, name, descr):
        JQuest.__init__(self, id, name, descr)
        self.creditShop = {
            "SCROLLS": {
                "name": "Scrolls Épicos",
                "items": [
                    {"id": 6651, "name": "Scroll de Resurrección Instantánea", "cost": 1000, "description": "Resurrección instantánea sin penalización"},
                    {"id": 6652, "name": "Scroll de Buffs Épicos", "cost": 500, "description": "Buffs épicos por 1 hora"},
                    {"id": 6653, "name": "Scroll de XP x2", "cost": 800, "description": "XP x2 por 2 horas"},
                    {"id": 6654, "name": "Scroll de Drop x2", "cost": 1200, "description": "Drop x2 por 2 horas"},
                    {"id": 6655, "name": "Scroll de PvP Boost", "cost": 1500, "description": "Más créditos por kills por 1 hora"}
                ]
            },
            "TITLES": {
                "name": "Títulos PvP Épicos",
                "items": [
                    {"id": 1001, "name": "Rey del PvP", "cost": 50000, "description": "Título épico para el mejor PvP"},
                    {"id": 1002, "name": "Príncipe del PvP", "cost": 40000, "description": "Título épico para el segundo mejor"},
                    {"id": 1003, "name": "Duque del PvP", "cost": 30000, "description": "Título épico para el tercer mejor"},
                    {"id": 1004, "name": "Caballero del PvP", "cost": 20000, "description": "Título épico para top 5"},
                    {"id": 1005, "name": "Guerrero del PvP", "cost": 10000, "description": "Título épico para top 10"}
                ]
            },
            "SKINS": {
                "name": "Skins de Armas Épicas",
                "items": [
                    {"id": 2001, "name": "Skin Espada de Fuego", "cost": 25000, "description": "Espada con efectos de fuego épicos"},
                    {"id": 2002, "name": "Skin Arco de Hielo", "cost": 25000, "description": "Arco con efectos de hielo épicos"},
                    {"id": 2003, "name": "Skin Daga de Rayo", "cost": 25000, "description": "Daga con efectos de rayo épicos"},
                    {"id": 2004, "name": "Skin Bastón de Oscuridad", "cost": 25000, "description": "Bastón con efectos de oscuridad épicos"},
                    {"id": 2005, "name": "Skin Martillo de Tierra", "cost": 25000, "description": "Martillo con efectos de tierra épicos"}
                ]
            },
            "BOOSTERS": {
                "name": "Boosters PvP Épicos",
                "items": [
                    {"id": 3001, "name": "Booster de Créditos x2", "cost": 2000, "description": "Créditos x2 por kills por 1 hora"},
                    {"id": 3002, "name": "Booster de XP x3", "cost": 3000, "description": "XP x3 por 2 horas"},
                    {"id": 3003, "name": "Booster de Drop x3", "cost": 4000, "description": "Drop x3 por 2 horas"},
                    {"id": 3004, "name": "Booster de Adena x2", "cost": 1500, "description": "Adena x2 por 1 hora"},
                    {"id": 3005, "name": "Booster de PvP x2", "cost": 2500, "description": "Recompensas PvP x2 por 1 hora"}
                ]
            },
            "VIP": {
                "name": "Paquetes VIP Épicos",
                "items": [
                    {"id": 4001, "name": "VIP 1 Día", "cost": 5000, "description": "Acceso VIP por 1 día"},
                    {"id": 4002, "name": "VIP 7 Días", "cost": 30000, "description": "Acceso VIP por 7 días"},
                    {"id": 4003, "name": "VIP 30 Días", "cost": 100000, "description": "Acceso VIP por 30 días"},
                    {"id": 4004, "name": "VIP Premium", "cost": 200000, "description": "Acceso VIP Premium por 30 días"},
                    {"id": 4005, "name": "VIP Legendario", "cost": 500000, "description": "Acceso VIP Legendario por 30 días"}
                ]
            }
        }
        
        self.playerCredits = {}
        
    def onAdvEvent(self, event, npc, player):
        if event == "mostrar_tienda_creditos":
            return self.mostrarTiendaCreditos(player)
        elif event.startswith("categoria_"):
            categoria = event.replace("categoria_", "")
            return self.mostrarCategoria(player, categoria)
        elif event.startswith("comprar_"):
            itemKey = event.replace("comprar_", "")
            return self.comprarItem(player, itemKey)
        elif event == "ver_mis_creditos":
            return self.verMisCreditos(player)
        elif event == "ver_ranking_creditos":
            return self.verRankingCreditos(player)
        elif event == "ver_donaciones":
            return self.verDonaciones(player)
        return None
    
    def mostrarTiendaCreditos(self, player):
        html = "<html><body>"
        html += "<center><font color=\"LEVEL\">¡¡¡ TIENDA DE CRÉDITOS ÉPICA DE L2 HERMANOS !!!</font></center><br>"
        html += "<center><font color=\"LEVEL\">¡¡¡ EPIC CREDITS SHOP OF L2 HERMANOS !!!</font></center><br><br>"
        
        # Mostrar créditos del jugador
        playerCredits = self.obtenerCreditos(player)
        html += "<font color=\"LEVEL\">💰 TUS CRÉDITOS / YOUR CREDITS: " + str(playerCredits) + "</font><br><br>"
        
        html += "<font color=\"LEVEL\">🛒 CATEGORÍAS DISPONIBLES / AVAILABLE CATEGORIES:</font><br><br>"
        
        for categoriaKey, categoriaInfo in self.creditShop.items():
            html += "<font color=\"LEVEL\">" + categoriaInfo["name"] + "</font><br>"
            html += "<font color=\"WHITE\">" + str(len(categoriaInfo["items"])) + " items disponibles</font><br>"
            html += "<font color=\"WHITE\">" + str(len(categoriaInfo["items"])) + " items available</font><br>"
            html += "<button value=\"Ver " + categoriaInfo["name"] + "\" action=\"bypass -h Quest EpicMonetization categoria_" + categoriaKey + "\" width=200 height=25 back=\"L2UI_ct1.button_df\" fore=\"L2UI_ct1.button_df\"><br><br>"
        
        html += "<font color=\"LEVEL\">🎯 ACCIONES DISPONIBLES / AVAILABLE ACTIONS:</font><br>"
        html += "<button value=\"Ver Mis Créditos\" action=\"bypass -h Quest EpicMonetization ver_mis_creditos\" width=200 height=25 back=\"L2UI_ct1.button_df\" fore=\"L2UI_ct1.button_df\"><br>"
        html += "<button value=\"Ver Ranking Créditos\" action=\"bypass -h Quest EpicMonetization ver_ranking_creditos\" width=200 height=25 back=\"L2UI_ct1.button_df\" fore=\"L2UI_ct1.button_df\"><br>"
        html += "<button value=\"Ver Donaciones\" action=\"bypass -h Quest EpicMonetization ver_donaciones\" width=200 height=25 back=\"L2UI_ct1.button_df\" fore=\"L2UI_ct1.button_df\"><br>"
        
        html += "<br><font color=\"LEVEL\">💳 CÓMO OBTENER CRÉDITOS / HOW TO GET CREDITS:</font><br>"
        html += "• PvP Kills: 100 créditos por kill / 100 credits per kill<br>"
        html += "• Kill Streaks: 1,000-50,000 créditos / 1,000-50,000 credits<br>"
        html += "• Ranking semanal: 10,000-100,000 créditos / 10,000-100,000 credits<br>"
        html += "• Donaciones: 1,000-10,000 créditos por $1 / 1,000-10,000 credits per $1<br>"
        html += "• Eventos especiales: Créditos épicos / Epic credits<br>"
        
        html += "<br><font color=\"LEVEL\">🎁 ITEMS DISPONIBLES / AVAILABLE ITEMS:</font><br>"
        html += "• Scrolls épicos / Epic scrolls<br>"
        html += "• Títulos PvP exclusivos / Exclusive PvP titles<br>"
        html += "• Skins de armas épicas / Epic weapon skins<br>"
        html += "• Boosters PvP / PvP boosters<br>"
        html += "• Paquetes VIP / VIP packages<br>"
        
        html += "<br><font color=\"LEVEL\">¡¡¡ COMPRA CON CRÉDITOS ÉPICOS !!!</font><br>"
        html += "<font color=\"LEVEL\">¡¡¡ BUY WITH EPIC CREDITS !!!</font><br>"
        
        html += "</body></html>"
        
        reply = NpcHtmlMessage(1)
        reply.setHtml(html)
        player.sendPacket(reply)
        return None
    
    def mostrarCategoria(self, player, categoriaKey):
        if categoriaKey not in self.creditShop:
            return "Categoría no encontrada."
        
        categoriaInfo = self.creditShop[categoriaKey]
        playerCredits = self.obtenerCreditos(player)
        
        html = "<html><body>"
        html += "<center><font color=\"LEVEL\">" + categoriaInfo["name"] + "</font></center><br>"
        html += "<center><font color=\"YELLOW\">Tus Créditos: " + str(playerCredits) + " / Your Credits: " + str(playerCredits) + "</font></center><br><br>"
        
        html += "<font color=\"LEVEL\">🛒 ITEMS DISPONIBLES / AVAILABLE ITEMS:</font><br><br>"
        
        for i, item in enumerate(categoriaInfo["items"]):
            canAfford = playerCredits >= item["cost"]
            color = "GREEN" if canAfford else "RED"
            
            html += "<font color=\"LEVEL\">" + item["name"] + "</font><br>"
            html += "<font color=\"WHITE\">" + item["description"] + "</font><br>"
            html += "<font color=\"" + color + "\">Costo: " + str(item["cost"]) + " Créditos / Cost: " + str(item["cost"]) + " Credits</font><br>"
            
            if canAfford:
                html += "<button value=\"Comprar " + item["name"] + "\" action=\"bypass -h Quest EpicMonetization comprar_" + categoriaKey + "_" + str(i) + "\" width=200 height=25 back=\"L2UI_ct1.button_df\" fore=\"L2UI_ct1.button_df\"><br><br>"
            else:
                html += "<font color=\"RED\">❌ Créditos insuficientes / Insufficient credits</font><br><br>"
        
        html += "<button value=\"Volver a la Tienda\" action=\"bypass -h Quest EpicMonetization mostrar_tienda_creditos\" width=200 height=25 back=\"L2UI_ct1.button_df\" fore=\"L2UI_ct1.button_df\"><br>"
        
        html += "</body></html>"
        
        reply = NpcHtmlMessage(1)
        reply.setHtml(html)
        player.sendPacket(reply)
        return None
    
    def comprarItem(self, player, itemKey):
        try:
            parts = itemKey.split("_")
            if len(parts) != 2:
                return "Error en el item."
            
            categoriaKey = parts[0]
            itemIndex = int(parts[1])
            
            if categoriaKey not in self.creditShop:
                return "Categoría no encontrada."
            
            categoriaInfo = self.creditShop[categoriaKey]
            if itemIndex >= len(categoriaInfo["items"]):
                return "Item no encontrado."
            
            item = categoriaInfo["items"][itemIndex]
            playerCredits = self.obtenerCreditos(player)
            
            # Verificar si tiene suficientes créditos
            if playerCredits < item["cost"]:
                return "No tienes suficientes créditos. Necesitas: " + str(item["cost"])
            
            # Comprar item
            self.gastarCreditos(player, item["cost"])
            
            # Dar item al jugador
            if item["id"] < 1000:  # Scrolls
                player.addItem("TiendaCreditos", item["id"], 1, player, True)
            elif item["id"] < 2000:  # Títulos
                self.darTitulo(player, item["id"])
            elif item["id"] < 3000:  # Skins
                self.darSkin(player, item["id"])
            elif item["id"] < 4000:  # Boosters
                self.activarBooster(player, item["id"])
            else:  # VIP
                self.activarVIP(player, item["id"])
            
            # Mensaje épico
            player.sendMessage("¡¡¡ COMPRA ÉPICA EXITOSA !!!")
            player.sendMessage("¡¡¡ EPIC PURCHASE SUCCESSFUL !!!")
            player.sendMessage("¡Has comprado: " + item["name"] + "!")
            player.sendMessage("You have purchased: " + item["name"] + "!")
            player.sendMessage("¡Créditos restantes: " + str(self.obtenerCreditos(player)) + "!")
            player.sendMessage("Remaining credits: " + str(self.obtenerCreditos(player)) + "!")
            
            # Anuncio épico
            self.announceToAll(player.getName() + " ha comprado " + item["name"] + " en la tienda de créditos!")
            self.announceToAll(player.getName() + " has purchased " + item["name"] + " in the credits shop!")
            
            return "¡Compra exitosa: " + item["name"] + "!"
            
        except Exception as e:
            return "Error en la compra: " + str(e)
    
    def verMisCreditos(self, player):
        playerCredits = self.obtenerCreditos(player)
        
        html = "<html><body>"
        html += "<center><font color=\"LEVEL\">¡¡¡ MIS CRÉDITOS ÉPICOS !!!</font></center><br>"
        html += "<center><font color=\"LEVEL\">¡¡¡ MY EPIC CREDITS !!!</font></center><br><br>"
        
        html += "<font color=\"LEVEL\">💰 INFORMACIÓN DE CRÉDITOS / CREDITS INFORMATION:</font><br><br>"
        html += "• Créditos actuales: " + str(playerCredits) + " / Current credits: " + str(playerCredits) + "<br>"
        html += "• Créditos gastados: En desarrollo / Credits spent: In development<br>"
        html += "• Créditos ganados: En desarrollo / Credits earned: In development<br>"
        html += "• Última compra: En desarrollo / Last purchase: In development<br>"
        
        html += "<br><font color=\"LEVEL\">📊 ESTADÍSTICAS DE CRÉDITOS / CREDITS STATISTICS:</font><br>"
        html += "• Créditos por PvP: En desarrollo / Credits from PvP: In development<br>"
        html += "• Créditos por Kill Streaks: En desarrollo / Credits from Kill Streaks: In development<br>"
        html += "• Créditos por Ranking: En desarrollo / Credits from Ranking: In development<br>"
        html += "• Créditos por Donaciones: En desarrollo / Credits from Donations: In development<br>"
        
        html += "<br><font color=\"LEVEL\">🎯 CÓMO GANAR MÁS CRÉDITOS / HOW TO EARN MORE CREDITS:</font><br>"
        html += "• Participa en PvP / Participate in PvP<br>"
        html += "• Alcanza Kill Streaks / Achieve Kill Streaks<br>"
        html += "• Sube en el ranking / Climb the ranking<br>"
        html += "• Haz donaciones / Make donations<br>"
        html += "• Participa en eventos / Participate in events<br>"
        
        html += "<br><font color=\"LEVEL\">💳 DONACIONES / DONATIONS:</font><br>"
        html += "• $1 USD = 1,000 Créditos / $1 USD = 1,000 Credits<br>"
        html += "• $5 USD = 5,500 Créditos / $5 USD = 5,500 Credits<br>"
        html += "• $10 USD = 12,000 Créditos / $10 USD = 12,000 Credits<br>"
        html += "• $20 USD = 25,000 Créditos / $20 USD = 25,000 Credits<br>"
        html += "• $50 USD = 65,000 Créditos / $50 USD = 65,000 Credits<br>"
        
        html += "<br><font color=\"LEVEL\">¡¡¡ USA TUS CRÉDITOS ÉPICOS !!!</font><br>"
        html += "<font color=\"LEVEL\">¡¡¡ USE YOUR EPIC CREDITS !!!</font><br>"
        
        html += "</body></html>"
        
        reply = NpcHtmlMessage(1)
        reply.setHtml(html)
        player.sendPacket(reply)
        return None
    
    def verRankingCreditos(self, player):
        html = "<html><body>"
        html += "<center><font color=\"LEVEL\">¡¡¡ RANKING DE CRÉDITOS ÉPICOS !!!</font></center><br>"
        html += "<center><font color=\"LEVEL\">¡¡¡ EPIC CREDITS RANKING !!!</font></center><br><br>"
        
        html += "<font color=\"LEVEL\">🏆 TOP 20 JUGADORES CON MÁS CRÉDITOS / TOP 20 PLAYERS WITH MOST CREDITS:</font><br><br>"
        
        # Simular ranking de créditos (en un servidor real, esto vendría de la base de datos)
        topPlayers = self.generarRankingCreditosSimulado()
        
        for i, playerInfo in enumerate(topPlayers, 1):
            medal = "🥇" if i == 1 else "🥈" if i == 2 else "🥉" if i == 3 else "🏅"
            html += "<font color=\"LEVEL\">" + medal + " #" + str(i) + " " + playerInfo["name"] + "</font><br>"
            html += "<font color=\"WHITE\">Créditos: " + str(playerInfo["credits"]) + " | Compras: " + str(playerInfo["purchases"]) + "</font><br>"
            html += "<font color=\"WHITE\">Credits: " + str(playerInfo["credits"]) + " | Purchases: " + str(playerInfo["purchases"]) + "</font><br><br>"
        
        html += "<font color=\"LEVEL\">📊 ESTADÍSTICAS DEL SERVIDOR / SERVER STATISTICS:</font><br>"
        html += "• Total de créditos en circulación: En desarrollo / Total credits in circulation: In development<br>"
        html += "• Promedio de créditos por jugador: En desarrollo / Average credits per player: In development<br>"
        html += "• Total de compras realizadas: En desarrollo / Total purchases made: In development<br>"
        
        html += "<br><font color=\"LEVEL\">¡¡¡ COMPITE POR EL PRIMER LUGAR EN CRÉDITOS !!!</font><br>"
        html += "<font color=\"LEVEL\">¡¡¡ COMPETE FOR THE FIRST PLACE IN CREDITS !!!</font><br>"
        
        html += "</body></html>"
        
        reply = NpcHtmlMessage(1)
        reply.setHtml(html)
        player.sendPacket(reply)
        return None
    
    def verDonaciones(self, player):
        html = "<html><body>"
        html += "<center><font color=\"LEVEL\">¡¡¡ DONACIONES ÉPICAS DE L2 HERMANOS !!!</font></center><br>"
        html += "<center><font color=\"LEVEL\">¡¡¡ EPIC DONATIONS OF L2 HERMANOS !!!</font></center><br><br>"
        
        html += "<font color=\"LEVEL\">💳 PAQUETES DE DONACIÓN / DONATION PACKAGES:</font><br><br>"
        
        packages = [
            {"name": "Paquete Bronce", "cost": 5, "credits": 5500, "bonus": 10},
            {"name": "Paquete Plata", "cost": 10, "credits": 12000, "bonus": 20},
            {"name": "Paquete Oro", "cost": 20, "credits": 25000, "bonus": 25},
            {"name": "Paquete Diamante", "cost": 50, "credits": 65000, "bonus": 30},
            {"name": "Paquete Legendario", "cost": 100, "credits": 140000, "bonus": 40}
        ]
        
        for package in packages:
            html += "<font color=\"LEVEL\">" + package["name"] + "</font><br>"
            html += "<font color=\"WHITE\">Costo: $" + str(package["cost"]) + " USD / Cost: $" + str(package["cost"]) + " USD</font><br>"
            html += "<font color=\"GREEN\">Créditos: " + str(package["credits"]) + " (+" + str(package["bonus"]) + "% bonus)</font><br>"
            html += "<font color=\"GREEN\">Credits: " + str(package["credits"]) + " (+" + str(package["bonus"]) + "% bonus)</font><br><br>"
        
        html += "<font color=\"LEVEL\">🎁 BENEFICIOS DE DONAR / DONATION BENEFITS:</font><br>"
        html += "• Créditos instantáneos / Instant credits<br>"
        html += "• Bonus por paquete / Package bonus<br>"
        html += "• Acceso VIP / VIP access<br>"
        html += "• Soporte prioritario / Priority support<br>"
        html += "• Items exclusivos / Exclusive items<br>"
        
        html += "<br><font color=\"LEVEL\">💳 MÉTODOS DE PAGO / PAYMENT METHODS:</font><br>"
        html += "• PayPal / PayPal<br>"
        html += "• Tarjeta de Crédito / Credit Card<br>"
        html += "• MercadoPago / MercadoPago<br>"
        html += "• Transferencia Bancaria / Bank Transfer<br>"
        html += "• Criptomonedas / Cryptocurrencies<br>"
        
        html += "<br><font color=\"LEVEL\">📞 CONTACTO / CONTACT:</font><br>"
        html += "• Discord: L2 Hermanos Official<br>"
        html += "• WhatsApp: +1-XXX-XXX-XXXX<br>"
        html += "• Email: l2hermanos@gmail.com<br>"
        
        html += "<br><font color=\"LEVEL\">¡¡¡ APOYA A L2 HERMANOS Y OBTÉN CRÉDITOS ÉPICOS !!!</font><br>"
        html += "<font color=\"LEVEL\">¡¡¡ SUPPORT L2 HERMANOS AND GET EPIC CREDITS !!!</font><br>"
        
        html += "</body></html>"
        
        reply = NpcHtmlMessage(1)
        reply.setHtml(html)
        player.sendPacket(reply)
        return None
    
    def obtenerCreditos(self, player):
        playerName = player.getName()
        if playerName not in self.playerCredits:
            self.playerCredits[playerName] = 0
        return self.playerCredits[playerName]
    
    def gastarCreditos(self, player, amount):
        playerName = player.getName()
        if playerName not in self.playerCredits:
            self.playerCredits[playerName] = 0
        self.playerCredits[playerName] -= amount
    
    def darCreditos(self, player, amount):
        playerName = player.getName()
        if playerName not in self.playerCredits:
            self.playerCredits[playerName] = 0
        self.playerCredits[playerName] += amount
    
    def darTitulo(self, player, tituloId):
        # Implementar sistema de títulos
        player.sendMessage("¡Has recibido un título épico!")
        player.sendMessage("You have received an epic title!")
    
    def darSkin(self, player, skinId):
        # Implementar sistema de skins
        player.sendMessage("¡Has recibido una skin épica!")
        player.sendMessage("You have received an epic skin!")
    
    def activarBooster(self, player, boosterId):
        # Implementar sistema de boosters
        player.sendMessage("¡Booster épico activado!")
        player.sendMessage("Epic booster activated!")
    
    def activarVIP(self, player, vipId):
        # Implementar sistema VIP
        player.sendMessage("¡Acceso VIP épico activado!")
        player.sendMessage("Epic VIP access activated!")
    
    def generarRankingCreditosSimulado(self):
        # Simular ranking de créditos (en un servidor real, esto vendría de la base de datos)
        players = []
        for i in range(20):
            players.append({
                "name": "EpicPlayer" + str(i+1),
                "credits": 100000 - i * 5000,
                "purchases": 50 - i * 2
            })
        return players
    
    def announceToAll(self, message):
        from l2jfrozen.gameserver.network.serverpackets import CreatureSay
        from l2jfrozen.gameserver.model.actor.instance import L2PcInstance
        from l2jfrozen.gameserver.GameServer import GameServer
        
        for player in GameServer.getInstance().getAllPlayers():
            if player and player.isOnline():
                player.sendPacket(CreatureSay(0, 1, "MONETIZACIÓN ÉPICA", message))

# Crear instancia del sistema de monetización épica
MONETIZACION_EPICA = EpicMonetization(-1, "MonetizacionEpica", "Sistema de Monetización Épica")

# Registrar el sistema
MONETIZACION_EPICA.addStartNpc(30006)  # Tienda GM
MONETIZACION_EPICA.addTalkId(30006)



