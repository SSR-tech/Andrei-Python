user ={
    "name": "SSR",
    "age": 21,
    "CAN_SWIM": True
}

for item in user:
    print(item)

# .items(), .values(), .keys() are keywords
# .items() -> the most frequently used method

for item in user.items(): 
    print(item)

for item in user.values():
    print(item)

for item in user.keys():
    print(item)

for (key,value) in user.items():
    print(f'{key}: {value}')
