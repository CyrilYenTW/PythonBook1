
for x in range(1, 100):
	for y in range(1, 100):
		x_word = '%02d' % x
		y_word = '%02d' % y
		r_word = '%02d' % (x * y)
		print(x_word + ' * ' + y_word + ' = ' + r_word)