import item, character


class Coord():
    def __init__(self, in_coord, item=None):
        self.coord = in_coord
        self.has = item

    def __str__(self):
        if self.has == None:
            return ' '
        else:
            return repr(self.has)


    def __repr__(self):
        return str(self.has)

    def place(self, in_item):
        self.has = in_item


class Room():
    def __init__(self, characters, width, height):
        self.characters = characters
        self.coord_dict = {}
        self.width = width
        self.height = height

        # Fill the room with coordinates that have no item
        for i in range(height):
            for j in range(width):
                self.coord_dict[(i, j)] = Coord((i, j))

        # Make a single sample box at 1 down, 5 right

        # single_box = item.Item('box', '☐') 
        key = item.Item('key', '🗝')
        treasure = item.Item('treasure', '💰')
        sword = item.Item('sword', '🗡')
        
        # self.coord_dict[(1, 5)].place(single_box)
        self.coord_dict[(7, 2)].place(key)
        self.coord_dict[(1, 1)].place(sword)
        self.coord_dict[(4, 9)].place(treasure)

        single_box = item.Item('box', '☐') 
        self.coord_dict[(1, 5)].place(single_box)
        self.update()

    def update(self):
        # ply = character.Player() 
        # self.coord_dict
        for player in self.characters:
            self.coord_dict[(player.location)].place(player)


    def __repr__(self):

        border = []
        border.append('* '* (self.width + 2))
    
        for i in range(self.height):
            row = ['*']
            for j in range(self.width):
                if (i, j) in self.coord_dict:
                    row.append(str(self.coord_dict[(i, j)]))
                else:
                    row.append(' ')
            row.append('*')
            border.append(' '.join(row))
        
        border.append('* '* (self.width + 2))
        
        return ('\n'.join(border))

        # star_list = []
        # for y_coord in range(self.height): 
        #     # print('*')
        #     for x_coord in range(self.width):
        #         if [x_coord, y_coord] in star_list:
        #             print('*', end='')
        #         else:
        #             print('', end='')
        # # # print()
        # # return str(border)   
    
        # FIX THIS REPR
        # return (' MAP '*10 + '\n') * 10 + ''.join([str(character.location) + '\n' for character in self.characters])


if __name__ == '__main__':
    pass
