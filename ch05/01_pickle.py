from  pprint import pprint
import pickle

person1 = {
    'name': '김하나',
    'height': 170,
    'weight': 60
}
person2 = {
    'name': '이대호',
    'height': 200,
    'weight': 80
}

# 데이터를 리스트로 만들었다.
people = [person1, person2]

# 데이터를 저장한다.
with open('people.pickle', 'wb') as f:   #<---- 1
    pickle.dump(people, f)               #<---- 2

# 저장된 데이터를 읽는다.
with open('people.pickle', 'rb') as f:   #<---- 3
    loaded_people = pickle.load(f)       #<---- 4

pprint(loaded_people)
