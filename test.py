template = {
	'interger' : 1,
	'string' : 'word',
	'list' : ['a', 'b', 'c', 'd'],
	'tuple' : ('a', 'b', 'c', 'd'),
	'dictionary' : {'key':'A', 'value': 'B'},
}

for key, value in template.items():
	print(key + ' => ' + str(type(value)))