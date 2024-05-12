from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain_core.prompts import PromptTemplate
from app.classes.base_llm_class import BaseLLMClass
from utils.template_utils import realtime_decision_system_template

class RealtimeDecisionSupportSystem(BaseLLMClass):
    def __init__(self) -> None:
        super().__init__()
        self.memory = ConversationBufferMemory(memory_key="history", k=10)
    
    def get_response_rtdss(self, data):
        prompt = PromptTemplate(
            template=realtime_decision_system_template,
            input_variables=["data"]
        )

        chain = ConversationChain(
            llm=self.get_llm(temperature=0.9),
            memory=self.memory
        )

        formatted_prompt: str = prompt.format(data=data)

        llm_response = chain(formatted_prompt)
        return llm_response
        