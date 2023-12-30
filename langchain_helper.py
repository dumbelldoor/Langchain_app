from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.llms import OpenAI

import os

""" API key Generated """

os.environ['OPENAI_API_KEY'] = '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'


def Gen_petnames(animal_type, pet_color, number_of_names, name_type):
    llm = OpenAI(temperature=0.7)

    prompt_template_names = PromptTemplate(
        input_variables=['animal_type', 'pet_color', 'number_of_names', 'name_type'],  # input variable {animal_type}
        template=f"I want {number_of_names} {animal_type} names, which color is {pet_color} It must be {name_type}and catchy."
        # prompt template
    )

    name_chain = LLMChain(llm=llm, prompt=prompt_template_names,
                          output_key="Pet_names")  # LLMChain is used to connect LLM's and prompts here
    # name = llm("I want 5 Dog names, It must be cool and catchy.") #Passed simple string into the LLM
    response = name_chain(
        {'animal_type': animal_type, 'pet_color': pet_color, }
    )  # response is being stored in a dictionary

    return response

#
# if __name__ == "__main__":
#     print(Gen_petnames("cow", "brown", 4, 'cute'))
