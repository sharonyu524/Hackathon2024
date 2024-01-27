import os 
import sys

import json
# import openai
import constants
from langchain_openai import OpenAIEmbeddings
# from langchain_community.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator
# # from langchain_community.llms import OpenAI
# #  from langchain.taggers import OpenAITagger
from langchain_community.chat_models import ChatOpenAI
# from langchain_openai import ChatOpenAI
# from langchain_community.vectorstores import Chroma

# from langchain_community.chat_models import ChatOpenAI
from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import JSONLoader
from langchain.chains import create_tagging_chain, create_extraction_chain
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain.chains import create_tagging_chain_pydantic

# class Tags(BaseModel):
#     FirstCareer: str = Field (
#         ..., enum  = ["Software Engineer", "Web Development", "Cyber Security", "Hardware Design","Product Manager","Machine Learning","Cloud Computing","Network Architect","Mobile App Developer","Academia", "Research","Data Science", "Artificial Intelligence"],
#         )
#     secondCareer: str = Field (
#         ..., enum  = ["Software Engineer", "Web Development", "Cyber Security", "Hardware Design","Product Manager","Machine Learning","Cloud Computing","Network Architect","Mobile App Developer","Academia", "Research","Data Science", "Artificial Intelligence"],
#         )
schema = {
    "properties": {
        "First career": {
            "type": "string",
            "enum": ["Software Engineer", "Web Development", "Cyber Security", "Hardware Design","Product Manager","Machine Learning","Cloud Computing","Network Architect","Mobile App Developer","Academia", "Research","Data Science", "Artificial Intelligence"],
            "description": "The career the student will be ready for after taking the course. Every course must have at least one career."
            
            }, 
        # "Second career": {
        #     "type": "string",
        #     "enum": ["Software Engineer", "Web Development", "Cyber Security", "Hardware Design","Product Manager","Machine Learning","Cloud Computing","Network Architect","Mobile App Developer","Academia", "Research","Data Science", "Artificial Intelligence"],
        #     "description": "The career the student will be ready for after taking the course. Every course must have at least one career."

        # },  
    },
    "required": ["First career"],

}


os.environ["OPENAI_API_KEY"] = constants.API_KEY
llm = ChatOpenAI(temperature=0, model = "gpt-3.5-turbo-0613")
chain = create_tagging_chain(schema,llm)


json_file_path = 'courseDescriptions.json'
with open(json_file_path, 'r') as json_file:
    data = json.load(json_file)
# print(type(data))
tags = {}
for course, description in data.items():
    # print(course)
    response = chain.invoke(description["Description"])
    # print(response)
    if response["text"] != {}:
        if response['text']['First career']:
            tags[course] = [response['text'].get('First career', 'N/A')]

        # if response['text']['Second career']:
        #     tags[course].append(response['text'].get('Seond career', 'N/A'))
    else:
        tags[course] = ["Software Engineer"]


    # if response.secondCareer in response['text']:
    #     tags[course].append(response['text']['Second career'])
    # else:
    #     tags[course] = []
# print(tags)
with open('careerTags.json', 'w') as fp:
    json.dump(tags, fp)
    # print(len(filtered_courses))

# if len(sys.argv) != 2:
#     print("Usage: python script.py <query>")
#     sys.exit(1)


# query = sys.argv[1] 


# loader =  TextLoader('data.txt')
# index = VectorstoreIndexCreator().from_loaders([loader])

# print(index.query(query, llm=ChatOpenAI))

# chatModel = ChatOpenAI(openai_api_key = constants.API_KEY)
# loader = JSONLoader('courseDescriptions.json',jq_schema=".",json_lines=True, text_content=False)
# docs = loader.load()

# query = sys.argv[1]
# index = VectorstoreIndexCreator().from_loaders([loader])
# print(index.query(query, llm=chatModel))



#  careerList = [Software Engineer, Web Development, Cyber Security, Hardware Deisgn]
#  template = "You are a helpful assistant that helps tag {course} with {career choice} from a list of {potential options} based on {course description}."
#  chat_prompt = template.format(course = data.keys(), career choice = "career choice", potential options = careerList, course description = data.values())
    
# tags = {}
# def tag():
    # for element in json:
    # result = chatModel.invoke(chat_prompt)

# result = chatModel.invoke("hi")
# print(result)

#  helper function 
