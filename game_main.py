import room, item, character, curses

myscreen = curses.initscr()

def print_room(in_room, input_player):
	for (i, j) in in_room.coord_dict:
		myscreen.addstr(i, j*2, repr(in_room.coord_dict[(i, j)].z0))
	myscreen.addstr(input_player.location[0], input_player.location[1] * 2, repr(input_player))

hero_player = character.Player()
main_room = room.Room([hero_player])

myscreen.keypad(True)

game_over = False
while game_over == False:
	myscreen.clear()
	print_room(main_room, hero_player)
	myscreen.addstr(26, 0, main_room.coord_dict[hero_player.location].announce()) # print what is at the player's location
	inkey = myscreen.getkey()
	if inkey == 'KEY_UP':
		new_loc = (hero_player.location[0] - 1, hero_player.location[1])
		hero_player.location = new_loc
	elif inkey == 'q':
		game_over = True	

curses.endwin()





 
