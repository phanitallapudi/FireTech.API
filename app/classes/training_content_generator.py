from langchain_community.document_loaders import WebBaseLoader
from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate
from app.classes.base_llm_class import BaseLLMClass
from utils.template_utils import training_content_generator_template

class TrainingContentGenerator(BaseLLMClass):
    def __init__(self) -> None:
        super().__init__()

    def generate_training_content(self):
        urls = ["https://www.psglearning.com/blog/psg/2023/06/16/firefighter-training-ideas-and-topics-for-instructors", "https://www.axon.com/resources/firefighter-training-equipment"]
        loader = WebBaseLoader(urls)
        data = loader.load()

        prompt = PromptTemplate(
            template=training_content_generator_template,
            input_variables=["reference"]
        )

        llm_chain = LLMChain(
            prompt=prompt,
            llm=self.get_llm()
        )
        
        llm_object = llm_chain({"reference" : data})

        json_response = {}
        json_response["data"] = llm_object["text"]

        return json_response

