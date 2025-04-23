
from A2A.samples.python.common.client.card_resolver import A2ACardResolver

urls = [
    "http://localhost:10001",
    "http://localhost:10000"
]
    
class AgentService:
    def get_available_agents(self):
        cards = []

        for url in urls:
            resolver = A2ACardResolver(url)
            card = resolver.get_agent_card()
            cards.append({"name": card.name, "description": card.description})

        return cards    