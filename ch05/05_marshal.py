from  pprint import pprint
import marshal

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

people = [person1, person2]

# 데이터를 저장한다.
with open('people.marshal', 'wb') as f:   #<---- 1
    marshal.dump(people, f)               #<---- 2

# 저장된 데이터를 읽는다.
with open('people.marshal', 'rb') as f:   #<---- 3
    loaded_people = marshal.load(f)       #<---- 4

pprint(loaded_people)
