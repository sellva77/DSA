from utils.Timer import timer_dec
data=[]

data.append({
    "input":{
        "arr":[1,2,3,4,5,6,7,8,9],
        "query":2
    },
    "output":1
    })
data.append({
    "input":{
        "arr":[],
        "query":2
    },
    "output":-1
    })
data.append({
    "input":{
        "arr":[1,2,3,4,5,6,7,8,9],
        "query":10
    },
    "output":-1
    })
data.append({
    "input":{
        "arr":[1,2,3,3,3,3,4,5,6,7,8,9],
        "query":3
    },
    "output":2
    })
data.append({
    "input": {
        "arr": list(range(1, 1_000_001)),
        "query": 999_999
    },
    "output": 999_998
})
@timer_dec
def locate_position(data,query):
    print(f"{data=}  {query=}")
    
    for x in range(len(data)):
        if data[x] == query:
            return x
    return -1
    
    
for x in data:
    print(locate_position(x["input"]["arr"],x["input"]["query"]),x["output"])