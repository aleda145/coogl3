import random
import csv

'''
Author: Eric Petersson
Date: 10/15/2017
Last update: 20/11/2017
Purpose: This script is used to create mock metadata for users. It currently gives each
         user age, gender and occupation. The generated users will be saved to user.csv
         from where it will be read for the database to be populated. Having the .csv file
         in the repository ensures that all databases created will be the same.
         The reason for having a script to do this is to make it easy to regenerate
         mock metadata should we change to another dataset.

'''

with open('occupation_list.csv') as csvfile:
    occupations_list = list(csv.reader(csvfile))

with open('occupation_list_female.csv') as csvfile_female:
    occupation_list_female = list(csv.reader(csvfile_female))

with open('occupation_list_male.csv') as csvfile_male:
    occupation_list_male = list(csv.reader(csvfile_male))

with open('gender_list.csv') as csvfile_genders:
    gender_list = list(csv.reader(csvfile_genders))

for x in range(1, 701):
    placeholder_gender = random.choice(gender_list)
    gender = placeholder_gender[0]
    age = random.randint(5, 75)
    if(gender=='Female'):
        placeholder = random.choice(occupation_list_female)
    elif(gender=='Male'):
         placeholder = random.choice(occupation_list_male)
    else:
         placeholder = random.choice(occupations_list)
    occupation = placeholder[0]
    if(age > 65):
        occupation = 'retired'
    elif(10 < age < 20 ):
        occupation = 'student'
    elif(age < 10):
        occupation = 'none'

    print(str(age) + ',' + gender + ',' + occupation, file=open("users_with_mock_metadata.csv", "a"))
