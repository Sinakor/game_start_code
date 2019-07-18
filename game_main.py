import room, item, character

hero_player = character.Player()
main_room = room.Room([hero_player], 10, 10)

keep_playing = True
while keep_playing:
	print(repr(main_room))
	# print(main_room.coord_dict)
	
	main_room.coord_dict[hero_player.location].place(None)

	inkey = input("Next command: ")
	if inkey[0] in ['n', 'north','up','u']:
		new_loc = (hero_player.location[0] - 1, hero_player.location[1])

	elif inkey[0] in ['s', 'south','down','d']:
		new_loc = (hero_player.location[0] + 1, hero_player.location[1])
	
	elif inkey[0] in ['e', 'east', 'r', 'right']:
		new_loc = (hero_player.location[0], hero_player.location[1] + 1)
	
	elif inkey[0] in ['w', 'west', 'l', 'left']:
		new_loc = (hero_player.location[0], hero_player.location[1] - 1)


	i, j = new_loc
	if i in range(0, main_room.height) and j in range(0, main_room.width):
		hero_player.location = new_loc
		print(repr(new_loc))
	else:
		print('Ouch!')

	print(main_room.coord_dict[hero_player.location].has)

	if main_room.coord_dict[hero_player.location].has:
		hero_player.loot.append(main_room.coord_dict[hero_player.location].has)

	### Check to see if in item in loot list: Exampe if hero has sword while fighting enemy
	if 'sword' in hero_player:
		print('My name is inigo montoya')
	
	print(hero_player.loot)
	main_room.update()
#print(repr(main_room))
# #keep_playing = False