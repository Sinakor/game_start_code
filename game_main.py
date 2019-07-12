import room, item, character

def print_room(in_room, input_player):
	out_string = '\n'*100
	for i in range(in_room.height):
		for j in range(in_room.width):
			if (i, j) == input_player.location:
				out_string += repr(input_player) + ' '
			else:	
				out_string += repr(in_room.coord_dict[(i, j)].has) + ' '
		out_string += '\n'
	out_string += 'Push \'w\' or \'q\'\n'
	out_string += main_room.coord_dict[hero_player.location].announce() # print what is at the player's location
	print(out_string)

hero_player = character.Player()
main_room = room.Room([hero_player], 10, 10)

game_over = False
while game_over == False:
	print_room(main_room, hero_player)
	inkey = input("Next command: ")
	if inkey[0] in ['w', 'W']:
		new_loc = (hero_player.location[0] - 1, hero_player.location[1])
		hero_player.location = new_loc
	elif inkey[0] in ['q', 'Q']:
		game_over = True	






 
