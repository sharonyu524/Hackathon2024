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


schema = {
    "properties": {
        "career": {
            "type": "string",
            # "enum": ["Software Engineer", "Web Development", "Cyber Security", "Hardware Design","Product Manager","Machine Learning","Cloud Computing","Network Architect","Mobile App Developer","Academia", "Research","Data Science", "Artificial Intelligence"],
            "description": "The career the student will be ready for after taking the course. Every course must have at least one career."
            
            },   
    },
    "required": ["career"],

}
llm = ChatOpenAI(openai_api_key = constants.API_KEY)
chain = create_tagging_chain(schema,llm)


json_file_path = 'courseDescriptions.json'
with open(json_file_path, 'r') as json_file:
    data = json.load(json_file)
# print(type(data))
tags = {}
for course, description in data.items():
    print(course)
    response = chain.run(description)
    print(response)
    if response:
        tags[course] = response['career']
    else:
        tags[course] = []
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
