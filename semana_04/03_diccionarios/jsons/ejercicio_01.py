import json
data_json = '{"nombre":"Ana","edad":21}'
data_python = json.loads(data_json)

print(data_python)

print(data_python["nombre"])
print(type(data_python))




