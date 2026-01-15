from a2a.server.tasks import TaskUpdater
from a2a.types import Message, TaskState, Part, TextPart
from a2a.utils import get_message_text, new_agent_text_message

from services.llm import LLM

from messenger import Messenger


class Agent:
    def __init__(self):
        self.messenger = Messenger()
        self.llm = LLM()

    async def run(self, message: Message, updater: TaskUpdater) -> None:
        """Implement your agent logic here.

        Args:
            message: The incoming message
            updater: Report progress (update_status) and results (add_artifact)

        Use self.messenger.talk_to_agent(message, url) to call other agents.
        """
        
        await updater.update_status(
            TaskState.working, new_agent_text_message("Thinking...")
        )
        
        response = self.llm.execute_prompt(
            prompt=get_message_text(message)
        )
        
        await updater.add_artifact(
            parts=[Part(root=TextPart(text=response))],
            name="AgentOutput",
        )
