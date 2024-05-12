from langchain.chains import LLMChain, ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain_community.document_loaders import DirectoryLoader, UnstructuredFileLoader
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from app.classes.base_llm_class import BaseLLMClass
from utils.template_utils import incident_report_analysis_prompt, get_casualties_count_template
from utils.models import InjuriesChart

import re
import base64
import plotly.graph_objects as go
import plotly.io as pio
import pandas as pd

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

        prompt = PromptTemplate(
            template=incident_report_analysis_prompt,
            input_variables=["query"]
        )

        llm_chain = LLMChain(
            prompt=prompt,
            llm=self.get_llm()
        )

        llm_object = llm_chain({"query" : load})
        json_response = {}
        json_response["analysis_report"] = llm_object["text"]

        return json_response


    def analyze_text_report(self, data):
        prompt = self.get_prompt()

        llm_chain = LLMChain(
            prompt=prompt,
            llm=self.get_llm()
        )

        llm_object = llm_chain({"query" : data})
        return llm_object
    
    def generate_casualties_count_charts(self, data):
        charts_data = []

        get_casualties_count_parser = JsonOutputParser(pydantic_object=InjuriesChart)
        get_casualties_count_prompt = PromptTemplate(
                input_variables=["data"], template=get_casualties_count_template, partial_variables={"format_instructions": get_casualties_count_parser.get_format_instructions()}
            )
        
        llm_chain = LLMChain(
                llm = self.get_llm(temperature=0.9),
                prompt = get_casualties_count_prompt
            )
        data = llm_chain.invoke(data)["text"]
        pattern = r'(\w+): (.+)'
        matches = re.findall(pattern, data)
        details_dict = {key.lower(): int(value) for key, value in matches}

        stacked_bar_fig = go.Figure(data=[
            go.Bar(name='Civilians', x=list(details_dict.keys())[:4], y=list(details_dict.values())[:4]),
            go.Bar(name='Firefighters', x=list(details_dict.keys())[:4], y=list(details_dict.values())[4:])
        ])
        stacked_bar_fig.update_layout(title='Injuries by Category', xaxis_title='Injury Category', yaxis_title='Number of Injuries', barmode='stack')

        html_str = pio.to_html(stacked_bar_fig, full_html=False)
        html_bytes = html_str.encode('utf-8')
        html_base64 = base64.b64encode(html_bytes).decode('utf-8')
        charts_data.append({"injury_by_category" : html_base64})

        return charts_data