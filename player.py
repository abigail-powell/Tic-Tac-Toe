'''
Abby Powell
apowell9@binghamton.edu
A52, Elizabeth Voroshylo

Simrohn Iftekhar
siftekh1@binghamton.edu
A53, Jonathan Cen

Final Project

Collaborated equally in designing and building the Player class
'''

import piece
import random

class Player:

  # --- Constants ---
  START = 0
  MAGIC_NUM = 15
  START_LOC = -200
  FIRST = 1
  LAST = 9
  MIN_PIECES = 3

  # --- Constructor ---

  def __init__(self, char):
    self.__num_wins = Player.START
    self.__spots_open = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    self.__spots_used = []
    self.__piece1 = piece.Piece(char)
    self.__piece2 = piece.Piece(char)
    self.__piece3 = piece.Piece(char)
    self.__piece4 = piece.Piece(char)
    self.__piece5 = piece.Piece(char)
    self.__pieces_left = [self.__piece1, self.__piece2, self.__piece3, \
                          self.__piece4, self.__piece5]
    self.__pieces_used = []
    self.__status = True

  # --- Accessors ---

  #Removes one piece from the list of unused pieces and returns it
  #invokes list.pop(index) to remove the piece from the list of unused pieces
  #  and to return it to the player
  #return Piece - the next piece that is still available to be used
  def __get_next_piece(self):
    return self.__pieces_left.pop(Player.START)

  #Shows which spots are open
  #return str - string version of the list of available spots
  def get_spots_open(self):
    return str(self.__spots_open)

  #Shows which spots are being used
  #return str - string version of the list of used spots
  def get_spots_used(self):
    return str(self.__spots_used)

  #Says whether or not it is the player's turn to move
  #return bool - the player's status
  def get_status(self):
    return self.__status

  # --- Mutators ---

  #Sets the status to a specified boolean value
  #param bool_val - the boolean value that the status should be changed to
  def __set_status(self, bool_val):
    self.__status = bool_val
    #self.change_status()

  #Updates the list of spots that are taken
  #invokes list.index(val), list.pop(index), and list.append(val)
  def set_spots_used(self, loc):
    i_num = self.__spots_open.index(loc)
    self.__spots_open.pop(i_num)
    self.__spots_used.append(loc)

  # --- Other Methods ---

  #Checks if the player won the game
  #Piece locations are based on a 3x3 magic square, which means that if the
  #  sum of 3 piece locations = 15, the player won
  #invokes Piece.get_location(), Player.__update_winner()
  #return bool - whether or not the player won
  def check_if_win(self):
    total = 0
    win = False
    #Checks that at least 3 pieces were already used
    if len(self.__pieces_used) >= Player.MIN_PIECES:
      #i1 is the index in self.__pieces_used of the first piece checked
      for i1 in range(len(self.__pieces_used) - 2):
        #i2 is the index in self.__pieces_used of the second piece checked
        for i2 in range(i1 + 1, len(self.__pieces_used) - 1):
          #i3 is the index in self.__pieces_used of the third piece checked
          for i3 in range(i2 + 1, len(self.__pieces_used)):

            #Accesses the pieces
            piece_1 = self.__pieces_used[i1]
            piece_2 = self.__pieces_used[i2]
            piece_3 = self.__pieces_used[i3]

            #Finds the board location of each piece checked
            loc_1 = piece_1.get_location()
            loc_2 = piece_2.get_location()
            loc_3 = piece_3.get_location()

            #Calculates the sum of the locations of 3 pieces
            total = loc_1 + loc_2 + loc_3

            #Checks if player won by seeing if total == 15
            #Says what to do if player won
            if total == Player.MAGIC_NUM:
              self.__update_winner()
              #self.reset_pieces()
              win = True

    #returns boolean showing whether or not player has won yet
    return win

  #Increments player's win count
  def __update_winner(self):
    self.__num_wins += 1

  #Resets the locations of the used pieces
  #invokes Piece.set_location(num), list.append(val)
  def reset_pieces(self):    
    #Resets the location of each used piece to show they are no longer on
    #  the board
    for piece in self.__pieces_used:
      piece.set_location(Player.START_LOC)
      self.__pieces_left.append(piece)
    #Resets the list of used pieces
    self.__pieces_used = []

    #Adds all used locations back to the list of available locations
    for loc in self.__spots_used:
      self.__spots_open.append(loc)
    #Resets the list of used pieces
    self.__spots_used = []

  #Resets the player's data
  #invokes Player.__set_status(bool_val), Player.reset_pieces()
  def reset_player(self):
    self.__num_wins = Player.START
    self.__set_status(False)
    self.reset_pieces()

  #Uses a piece and updates its information
  #invokes Player.__get_next_piece(), Player.change_status,
  #  Piece.set_location(num), list.index(val), list.pop(index),
  #  list.append(val)
  #param - new_loc (int) - the used piece's location on the board
  def use_piece(self, new_loc):
    #Accesses next available piece
    next_piece = self.__get_next_piece()
    
    #Changes the pieces location to show it is on the board
    next_piece.set_location(new_loc)

    #Shows that piece is used and another location is occupied
    self.__pieces_used.append(next_piece)
    i_num = self.__spots_open.index(new_loc)
    self.__spots_open.pop(i_num)
    self.__spots_used.append(new_loc)

    #Changes the player's status to show that their turn finished
    self.change_status()

  #Changes player's status to the opposite of its current value
  def change_status(self):
    self.__status = not self.__status

  #Says the number of remaining available spots
  #return int - number of available spots
  def show_num_spots_open(self):
    return len(self.__spots_open)

#Uses inheritance to allow the computer to be a player
class ComputerPlayer(Player):

  def __init__(self, char):
    Player.__init__(self, char)
    self.__spots_open = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    self.__spots_used = []
    self.__status = False

  #The computer uses a turn
  #invokes Player.get_spots_used(), Player.use_piece(num)
  #return int - location of the piece that was just used
  def make_move(self):
    
    #Randomly chooses an open space on the board
    rand_num = random.randint(Player.FIRST, Player.LAST)
    while str(rand_num) in self.get_spots_used():
      rand_num = random.randint(Player.FIRST, Player.LAST)
      
    #Places piece into the space
    self.use_piece(rand_num)
    
    return rand_num



