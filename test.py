print("hello world")
print("hello develop")
import json

x = 'lossslhgjhgjhgjhsasdaafdsfdssdsd'

x = {'commits': [{'id': '08c926a8cf657c995463c523268ccb1422654edd', 'tree_id': '0a5db9a27874e9c946f6e007e69287780c633081', 
     'distinct': True, 'message': "'first'", 'timestamp': '2020-04-22T11:24:41+06:00', 'url': 'https://github.com/Toha-K-M/test/commit/08c926a8cf657c995463c523268ccb1422654edd', 
     'author': {'name': 'toha', 'email': 'senor.toha@gmail.com', 'username': 'Toha-K-M'}, 'committer': {'name': 'toha', 'email': 'senor.toha@gmail.com', 'username': 'Toha-K-M'},
      'added': ['test.py'], 'removed': [], 'modified': []}]}

print(type(x), x['commits'])



for item in x['commits']:
	for obj in item:
		print(obj, " : ", item[obj])
		if obj 