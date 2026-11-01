import json

data_python = {"nombre": "Ana", "edad":21, "activo": True, "nota": None}
data_json = json.dumps(data_python)

print(data_json)
print(type(data_json))

