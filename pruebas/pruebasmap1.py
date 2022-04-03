import gc


variable=[
    {
        'id':1,
        'sensor':"sensor1",
        'valor':
        {
            "humedad":1,
            "temperatura":1
        }
    },
    {
        'id':2,
        'sensor':"sensor1",
        'valor':
        {
            "humedad":12,
            "temperatura":11
        }
    }
]
def iterar(v):
    for val in list(v):
        if isinstance(val,list):
            for subval in list(val):
                print(subval)
        else:
            print(val)
    pass
gc.enable()