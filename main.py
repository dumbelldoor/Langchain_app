import langchain_helper as lch
import streamlit as stl

stl.title("Pet Name Generator")

number_of_pet = stl.sidebar.selectbox("Enter the number of pet names you want:", ("1", "2", " 3", "4", "5", "6"))
name_type = stl.sidebar.selectbox("What Kind of name you want:", ("Cute", "Cool", "Sassy", "Strong"))
animal_type = stl.sidebar.selectbox("What is your Pet type:",
                                    ("Cat", "Dog", "Cow", "Sheep", " Piglet"))

if animal_type == 'Cat':
    pet_color = stl.sidebar.text_area(label="What is the color of your Cat:", max_chars=15,
                                      placeholder="Enter your pet's color")
if animal_type == 'Dog':
    pet_color = stl.sidebar.text_area(label="What is the color of your Dog:", max_chars=15,
                                      placeholder="Enter your pet's color")
if animal_type == 'Cow':
    pet_color = stl.sidebar.text_area(label="What is the color of your Cow:", max_chars=15,
                                      placeholder="Enter your pet's color")
if animal_type == 'Sheep':
    pet_color = stl.sidebar.text_area(label="What is the color of your Sheep:", max_chars=15,
                                      placeholder="Enter your pet's color")
if animal_type == 'Piglet':
    pet_color = stl.sidebar.text_area(label="What is the color of your Piglet:", max_chars=15,
                                      placeholder="Enter your pet's color")

if pet_color:
    response = lch.Gen_petnames(animal_type, pet_color, number_of_pet, name_type)
    stl.text(response['Pet_names'])
