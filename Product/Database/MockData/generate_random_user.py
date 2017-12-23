import random
from Product.Database.DBConn import User


def GenerateUser(user_id):
    occupation_set = ['secretary',
                      'artist',
                      'doctor',
                      'teacher',
                      'engineer',
                      'executive',
                      'nurse',
                      'lawyer',
                      'librarian',
                      'none',
                      'programmer',
                      'retired',
                      'salesman',
                      'scientist',
                      'student',
                      'model',
                      'politician']

    occupation_set_female = ['secretary',
                             'artist',
                             'doctor', 'doctor',
                             'teacher',
                             'engineer', 'engineer', 'engineer', 'engineer',
                             'engineer', 'engineer', 'engineer', 'engineer',
                             'executive',
                             'nurse',
                             'lawyer', 'lawyer',
                             'librarian',
                             'none',
                             'programmer', 'programmer', 'programmer',
                             'programmer', 'programmer', 'programmer',
                             'retired',
                             'salesman',
                             'scientist',
                             'student', 'student', 'student', 'student',
                             'model',
                             'politician', 'politician', 'politician', 'politician']

    occupation_set_male = ['secretary', 'secretary', 'secretary', 'secretary',
                           'secretary', 'secretary', 'secretary', 'secretary',
                           'artist',
                           'doctor',
                           'teacher',
                           'engineer',
                           'executive',
                           'nurse', 'nurse', 'nurse', 'nurse', 'nurse',
                           'nurse', 'nurse', 'nurse', 'nurse', 'nurse',
                           'lawyer',
                           'librarian',
                           'none',
                           'programmer',
                           'retired',
                           'salesman',
                           'scientist',
                           'student',
                           'model', 'model', 'model', 'model', 'model',
                           'model', 'model', 'model', 'model', 'model',
                           'politician']

    gender_set = ['Unknown', 'Other', 'Male', 'Female']
    gender = random.choice(gender_set)
    age = random.randint(0, 100)
    if age < 18:
        occupation = 'student'
    elif age > 65:
        occupation = 'retired'
    else:
        if gender == 'Female':
            occupation = random.choice(occupation_set_female)
        elif gender == 'Male':
            occupation = random.choice(occupation_set_male)
        else:
            occupation = random.choice(occupation_set)

    user = User(id=user_id, age=age, gender=gender, occupation=occupation)
    return user

