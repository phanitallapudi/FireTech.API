from langchain.chains import LLMChain, ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain_community.document_loaders import DirectoryLoader, UnstructuredFileLoader
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from app.classes.base_llm_class import BaseLLMClass
from utils.template_utils import incident_report_analysis_prompt

class IncidentReportAnalysis(BaseLLMClass):
    def __init__(self) -> None:
        super().__init__()
        self.memory = ConversationBufferMemory(memory_key="history", k=5)

    def get_prompt(self):
        return PromptTemplate(
            template=incident_report_analysis_prompt,
            input_variables=["query"]
        )

    def analyze_file_report(self, directory):
        loader = DirectoryLoader(directory, loader_cls=UnstructuredFileLoader)
        load = loader.load()

        prompt = self.get_prompt()
        llm_chain = LLMChain(
            prompt=prompt,
            llm=self.get_llm()
        )

        llm_object = llm_chain({"query" : load})
        return llm_object["text"]


    def analyze_text_report(self, data):
        prompt = self.get_prompt()

        llm_chain = LLMChain(
            prompt=prompt,
            llm=self.get_llm()
        )

        llm_object = llm_chain({"query" : data})
        return llm_object