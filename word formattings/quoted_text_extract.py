import re
text = """The "film Titanic" was released in 1998"""
result = re.findall(r'"([^"]*)"', text)

print(result)