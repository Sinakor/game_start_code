import room, item, character

hero_player = character.Player()
main_room = room.Room([hero_player], 10, 10)

keep_playing = True
while keep_playing:
	print(repr(main_room))
	# print(main_room.coord_dict)
	inkey = input("Next command: ")
	if inkey[0] in ['w', 'west', 'l', 'left']:
		new_loc = (hero_player.location[0] - 1, hero_player.location[1])
		hero_player.location = new_loc
		print(repr(new_loc))
	elif inkey[0] in ['e', 'east', 'r', 'right']:
		new_loc = (hero_player.location[0] + 1, hero_player.location[1])
		hero_player.location = new_loc
		print(new_loc)
	elif inkey[0] in ['n', 'north','up','u']:
		new_loc = (hero_player.location[0], hero_player.location[1] + 1)
		hero_player.location = new_loc
		print(new_loc)

	elif inkey[0] in ['s', 'south','down','d']:
		new_loc = (hero_player.location[0], hero_player.location[1] - 1)
		hero_player.location = new_loc
		print(new_loc)
	#print(repr(main_room))
# #keep_playing = False
#testing branch