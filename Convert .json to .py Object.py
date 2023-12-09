import json
import ast
#Create .json Data
json_string="Sudhanex Edit"	#Strings can't able to decode to .py data
json_int='541'
json_float='45.41'
json_dict='{"Name":"Sudhanex","Age":19}'
json_list='["Sudhanex","NotSudhanex"]'
#Loads or Converts .json to .py objects
py_int=json.loads(json_int)
py_float=json.loads(json_float)
py_dict=json.loads(json_dict)
py_list=json.loads(json_list)
#py_string=json.loads(json_string)
#If You would not believe me that I Commented,Try it Yourself BUDDY
#Print .py Data
print("Python Integer: ",py_int)
print("\nPython Float: ",py_float)
print("\nPython Dictionary: ",py_dict)
print("\nPython List: ",py_list)
#print("\nPython String: ",py_string)
    #EXTRA TIP:
#Converts .py object to .py code from converted Python Dictionary object
#py_code=ast.literal_eval(repr(py_dict))
#print("\nPython Code: ",py_code)
