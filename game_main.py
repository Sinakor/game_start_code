import room, item, character

hero_player = character.Player()
main_room = room.Room([hero_player], 50, 50)

keep_playing = True
while keep_playing:
	print(repr(main_room))
	# print(main_room.coord_dict)
	inkey = input("Next command: ")
	if inkey[0] in ['w', 'W']:
		new_loc = (hero_player.location[0] - 1, hero_player.location[1])
		hero_player.location = new_loc
	elif inkey[0] in ['q', 'Q']:
		keep_playing = False
