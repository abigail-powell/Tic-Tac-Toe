'''
Abby Powell
apowell9@binghamton.edu
A52, Elizabeth Voroshylo

Simrohn Iftekhar
siftekh1@binghamton.edu
A53, Jonathan Cen

Final Project

Collaborated equally in designing and building the Piece class
'''

class Piece:

  # --- Constants ---

  START_LOC = -200
  START_SIZE = 12

  # --- Constructor ---

  def __init__(self, char):
    self.__letter = char
    self.__location = Piece.START_LOC

  # --- Accessors ---

  #Gives the location of the piece
  #return int - between 1-9 if piece is on the board, -200 if not on board
  def get_location(self):
    return self.__location

  # --- Mutators ---

  #Sets the location of a piece
  #param - loc (int) - new location of piece
  def set_location(self, loc):
    self.__location = loc

  # --- Other Methods ---

  #Resets the location of a piece to show it is off the board
  def reset(self):
    self.__location = Piece.START_LOC

