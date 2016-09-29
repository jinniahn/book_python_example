people = [
    {"name": "noah", "age": 19}
    , {"name": "liam", "age": 23}
    , {"name": "jacob", "age": 9}
    , {"name": "mason", "age": 21} ]

people.sort(key=lambda x: x["age"])
print(people)
