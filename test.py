places = []

while True:
	temp = input('If you could visit one placein the world, where would you go ? ')
	places.append(temp)

	if input('Do you want to exit ? (y/n) ') == 'y':
		break;

print(places)