import json

person1 = {
    'name': '김하나',
    'height': 170,
    'weight': 60
}

print(json.dumps(person1))

# 데이터 저장
with open('test.json', 'w') as f:
    json.dump(person1, f)
