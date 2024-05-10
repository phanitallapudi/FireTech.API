from langchain.chains import LLMChain
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from app.classes.base_llm_class import BaseLLMClass
from utils.models import EmergencyScenario
from utils.template_utils import generate_scenario, generate_realtime_responses


class EmergencyResponseSimulator(BaseLLMClass):
    def __init__(self) -> None:
        pass

    def generate_scenario_parser(self):
        return JsonOutputParser(pydantic_object=EmergencyScenario)
    
    def generate_scenario_prompt(self):
        parser = self.generate_scenario_parser()
        return PromptTemplate(
            template=generate_scenario,
            input_variables=["query"],
            partial_variables={"format_instructions": parser.get_format_instructions()},
        )
    
    def generate_scenario(self):
        chain = self.generate_scenario_prompt() | self.get_llm(temperature=0.6) | self.generate_scenario_parser()
        result = chain.invoke({"query": "generate the scenario for me to use in my simulation, try to generate various scenarios"})
        return result
    
    def generate_response_scenario(self, trainee_response, scenario):
        prompt = PromptTemplate(
            template=generate_realtime_responses,
            input_variables=["previous_data", "trainee_input"]
        )
        llm_chain = LLMChain(
            prompt=prompt,
            llm=self.get_llm()
        )

        llm_response = llm_chain({"previous_data": scenario, "trainee_input": trainee_response})
        return llm_response
        
