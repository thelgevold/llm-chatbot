from A2A.samples.python.common.client.card_resolver import A2ACardResolver
from A2A.samples.python.common.types import AgentCard
from A2A.samples.python.common.client.client import A2AClient

urls = [
    "http://localhost:10001",
    "http://localhost:10000"
]
    
class AgentContext:
    _instance = None
    _initialized = False

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance
    
    def __init__(self):
        if not self._initialized:
            self.clients = {}
            self.agent_summary = []

            for url in urls:
                resolver = A2ACardResolver(url)
                card = resolver.get_agent_card()
                self.clients[card.name] = A2AClient(card)

                self.agent_summary.append({"name": card.name, "description": card.description, "url": card.url})

            AgentContext._initialized = True    
