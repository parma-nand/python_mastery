import json
x={
    1:"First",
    "Second":2
}

print(x)

# Keys → unique, immutable (str, int, tuple)
# Values → anything (list, dict, int, etc.)

y={
    1:"First",
    'Second':2,
    (3,4):"3 and 4"
}

print(y.get(1))
print(y.get("Second"))
print(y.get(0))
print(y.get((3,4)))
y[1]=1 #Updated the value
print(y[1])

# Iteration

for key in y:
    print(key,y[key])
for k,v in y.items():
    print(k," : ",v)
    
# Nested Dictionary

a={
    "skills":{"backend":['java','python'],
              "frontend":['java','python']},
    "skills1":{"frontend":['java','python']}
}
print(a)
print(a["skills"]["backend"])

datas={
    'status':"success",
    "user":{'name':"parma","age":28}
}
json_data=json.dumps(datas)
print(json_data)
print(datas)