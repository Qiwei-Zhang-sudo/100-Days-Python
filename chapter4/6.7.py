alice = {"name": 'alice','fruit': 'apple','age': 12}
john = {'name': 'john','fruit': 'banana','age':13}
admin = {'name': 'zhangqiwei','fruit': 'orange','age':20}
people = [alice,john,admin]
for item in people:
    print(f'name: {item['name']},fruit: {item['fruit']},age: {item['age']}')