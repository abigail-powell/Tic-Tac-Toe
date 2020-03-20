
'''
Abby Powell
apowell9@binghamton.edu
A52, Elizabeth Voroshylo

Simrohn Iftekhar
siftekh1@binghamton.edu
A53, Jonathan Cen

Final Project

Collaborated equally in designing and building the GameGUI
'''

import piece
import player

from tkinter import *

class GameGUI:

  START_LOC = -200
  ONE_MORE = 1
  NONE = 0

  def __init__(self):

    #Creates the person and computer players
    self.__human = player.Player('X')
    self.__computer = player.ComputerPlayer('O')

    #Says if there is a winner yet
    self.__has_winner = False

    #Creates the main window
    self.__game_wn = Tk()

    #Renames title of the main window
    self.__game_wn.title('Tic Tac Toe')

    #Creates labels for Player1 to show who they are and their wins
    self.__player_1_label = Label(self.__game_wn, font=('Times 15 bold'),
                                  text = 'Player')
    self.__player_1_wins_label = Label(self.__game_wn, font=('Times 13'),
                                       text = 'Wins: ')

    #Creates labels for Player2 to show it is the computer
    #  and its wins    
    self.__player_2_label = Label(self.__game_wn, font=('Times 15 bold'),
                                  text = 'Computer')
    self.__player_2_wins_label = Label(self.__game_wn, font=('Times 13'),
                                       text = 'Wins: ')

    #Creates a label to show player1's number of wins
    self.__player_1_num_wins = IntVar()
    self.__player_1_num_wins.set(0)
    self.__player_1_wins_count = Label(self.__game_wn, font = 'Times 13',
      textvariable = self.__player_1_num_wins)

    #Creates a label to show player2's number of wins
    self.__player_2_num_wins = IntVar()
    self.__player_2_num_wins.set(0)
    self.__player_2_wins_count = Label(self.__game_wn, font = 'Times 13',
      textvariable = self.__player_2_num_wins)

    #Sets up the buttons on the tic-tac-toe board
    self.__space_1_2_str = StringVar()
    self.__space_1_2_str.set('\t\n\t')
    self.__space_1_2 = Button(self.__game_wn, font=('Times 15 bold'),
                              fg = 'red', height=3, width=6,
      textvariable = self.__space_1_2_str, command = self.set_space_1_2)

    self.__space_1_7_str = StringVar()
    self.__space_1_7_str.set('\t\n\t')
    self.__space_1_7 = Button(self.__game_wn, font=('Times 15 bold'),
                              fg = 'red', height=3, width=6,
      textvariable = self.__space_1_7_str, command = self.set_space_1_7)

    self.__space_1_6_str = StringVar()
    self.__space_1_6_str.set('\t\n\t')
    self.__space_1_6 = Button(self.__game_wn, font=('Times 15 bold'),
                              fg = 'red', height=3, width=6,
      textvariable = self.__space_1_6_str, command = self.set_space_1_6)

    self.__space_2_9_str = StringVar()
    self.__space_2_9_str.set('\t\n\t')
    self.__space_2_9 = Button(self.__game_wn, font=('Times 15 bold'),
                              fg = 'red', height=3, width=6,
      textvariable = self.__space_2_9_str, command = self.set_space_2_9)

    self.__space_2_5_str = StringVar()
    self.__space_2_5_str.set('\t\n\t')
    self.__space_2_5 = Button(self.__game_wn, font=('Times 15 bold'),
                              fg = 'red', height=3, width=6,
      textvariable = self.__space_2_5_str, command = self.set_space_2_5)

    self.__space_2_1_str = StringVar()
    self.__space_2_1_str.set('\t\n\t')
    self.__space_2_1 = Button(self.__game_wn, font=('Times 15 bold'),
                              fg = 'red', height=3, width=6,
      textvariable = self.__space_2_1_str, command = self.set_space_2_1)

    self.__space_3_4_str = StringVar()
    self.__space_3_4_str.set('\t\n\t')
    self.__space_3_4 = Button(self.__game_wn, font=('Times 15 bold'),
                              fg = 'red', height=3, width=6,
      textvariable = self.__space_3_4_str, command = self.set_space_3_4)

    self.__space_3_3_str = StringVar()
    self.__space_3_3_str.set('\t\n\t')
    self.__space_3_3 = Button(self.__game_wn, font=('Times 15 bold'),
                              fg = 'red', height=3, width=6,
      textvariable = self.__space_3_3_str, command = self.set_space_3_3)

    self.__space_3_8_str = StringVar()
    self.__space_3_8_str.set('\t\n\t')
    self.__space_3_8 = Button(self.__game_wn, font=('Times 15 bold'),
                              fg = 'red', height=3, width=6,
      textvariable = self.__space_3_8_str, command = self.set_space_3_8)

    #Sets up a button that allows the user to change some of the game settings
    self.__gear_img = PhotoImage(file = 'smallGear.png')
    self.__settings_button = Button(image = self.__gear_img,
                                    command = self.open_settings)

    #Creates spacer labels for the game board
    self.__vertical_space_1 = Label(self.__game_wn,
                                    text = '|\n|\n|\n|\n|\n|\n|')
    self.__vertical_space_2 = Label(self.__game_wn,
                                    text = '|\n|\n|\n|\n|\n|\n|')
    self.__vertical_space_3 = Label(self.__game_wn,
                                    text = '|\n|\n|\n|\n|\n|\n|')
    self.__vertical_space_4 = Label(self.__game_wn,
                                    text = '|\n|\n|\n|\n|\n|\n|')
    self.__vertical_space_5 = Label(self.__game_wn,
                                    text = '|\n|\n|\n|\n|\n|\n|')
    self.__vertical_space_6 = Label(self.__game_wn,
                                    text = '|\n|\n|\n|\n|\n|\n|')

    self.__horizontal_space_1 = Label(self.__game_wn,
                                      text = '------------------')
    self.__horizontal_space_2 = Label(self.__game_wn,
                                      text = '------------------')
    self.__horizontal_space_3 = Label(self.__game_wn,
                                      text = '------------------')
    self.__horizontal_space_4 = Label(self.__game_wn,
                                      text = '------------------')
    self.__horizontal_space_5 = Label(self.__game_wn,
                                      text = '------------------')
    self.__horizontal_space_6 = Label(self.__game_wn,
                                      text = '------------------')

    #Creates a button if user wants to start a new game
    self.__new_game_button = Button(self.__game_wn, text = 'New\nGame', \
      font = 'Times 11', command = self.start_new_game)
    #Creates a button if user wants to reset the game information
    self.__reset_button = Button(self.__game_wn, text = 'Reset', \
      font = 'Times 11', command = self.reset_everything)

    #Creates a label to show who won the past game
    self.__winner_var = StringVar()
    self.__winner_var.set('')
    self.__winner_label = Label(self.__game_wn, font = 'Times 15 bold',
                                textvariable = self.__winner_var)

    #Sets up widgets in the window
    self.__player_1_label.grid(row=0, column=0)
    self.__player_1_wins_label.grid(row=1, column=0)
    self.__player_2_label.grid(row=2, column=0)
    self.__player_2_wins_label.grid(row=3, column=0)

    self.__player_1_wins_count.grid(row=1, column=1)
    self.__player_2_wins_count.grid(row=3, column=1)

    self.__space_1_2.grid(row=0, column=2, sticky=S + N + E + W)
    self.__horizontal_space_1.grid(row=1, column=2)
    self.__space_2_9.grid(row=2, column=2, sticky=S + N + E + W)
    self.__horizontal_space_2.grid(row=3, column=2)
    self.__space_3_4.grid(row=4, column=2, sticky=S + N + E + W)

    self.__vertical_space_1.grid(row=0, column=3)
    self.__vertical_space_2.grid(row=2, column=3)
    self.__vertical_space_3.grid(row=4, column=3)

    self.__space_1_7.grid(row=0, column=4, sticky=S + N + E + W)
    self.__horizontal_space_3.grid(row=1, column=4)
    self.__space_2_5.grid(row=2, column=4, sticky=S + N + E + W)
    self.__horizontal_space_4.grid(row=3, column=4)
    self.__space_3_3.grid(row=4, column=4, sticky=S + N + E + W)

    self.__vertical_space_4.grid(row=0, column=5)
    self.__vertical_space_5.grid(row=2, column=5)
    self.__vertical_space_6.grid(row=4, column=5)

    self.__space_1_6.grid(row=0, column=6, sticky=S + N + E + W)
    self.__horizontal_space_5.grid(row=1, column=6)
    self.__space_2_1.grid(row=2, column=6, sticky=S + N + E + W)
    self.__horizontal_space_6.grid(row=3, column=6)
    self.__space_3_8.grid(row=4, column=6, sticky=S + N + E + W)

    self.__new_game_button.grid(row=0, column=7)
    self.__reset_button.grid(row=2, column=7)

    self.__winner_label.grid(row=4, column=0)

    self.__settings_button.grid(row=4, column=7)

    #Runs the mainloop
    mainloop()

  #The following methods say what to do if the user selects a space
  #Called when the Button self.__space_1_2 is pushed
  #invoke __can_make_move(loc), __set_space(loc), __update_round()
  def set_space_1_2(self):
    #Checks if user is allowed to select the location
    if self.__can_make_move(2):
      #Uses piece, updates information, allows computer to move next
      self.__set_space(2)
      #Places character on button to show that user already chose the space
      self.__space_1_2_str.set('X')
      #Checks whether their is a winner, a tie, or if the computer can move
      self.__update_round()

  #Same logic as set_space_1_2
  def set_space_1_7(self):
    if self.__can_make_move(7):
      self.__set_space(7)
      self.__space_1_7_str.set('X')
      self.__update_round()

  #Same logic as set_space_1_2
  def set_space_1_6(self):
    if self.__can_make_move(6):
      self.__set_space(6)
      self.__space_1_6_str.set('X')
      self.__update_round()

  #Same logic as set_space_1_2
  def set_space_2_9(self):
    if self.__can_make_move(9):
      self.__set_space(9)
      self.__space_2_9_str.set('X')
      self.__update_round()

  #Same logic as set_space_1_2
  def set_space_2_5(self):
    if self.__can_make_move(5):
      self.__set_space(5)
      self.__space_2_5_str.set('X')
      self.__update_round()

  #Same logic as set_space_1_2
  def set_space_2_1(self):
    if self.__can_make_move(1):
      self.__set_space(1)
      self.__space_2_1_str.set('X')
      self.__update_round()

  #Same logic as set_space_1_2
  def set_space_3_4(self):
    if self.__can_make_move(4):
      self.__set_space(4)
      self.__space_3_4_str.set('X')
      self.__update_round()

  #Same logic as set_space_1_2
  def set_space_3_3(self):
    if self.__can_make_move(3):
      self.__set_space(3)
      self.__space_3_3_str.set('X')
      self.__update_round()

  #Same logic as set_space_1_2
  def set_space_3_8(self):
    if self.__can_make_move(8):
      self.__set_space(8)
      self.__space_3_8_str.set('X')
      self.__update_round()

  #Says if user is allowed to make a move based on whether it is their
  #  turn, there is no winner yet, and that the spot they chose is open
  #param - num (int) - assigned location of the selected space
  #return bool - whether or not user can choose the selected space
  def __can_make_move(self, num):
    return self.__human.get_status() and (not self.__has_winner) and \
      (str(num) in self.__human.get_spots_open())

  #After player has taken their turn says what to do next
  def __update_round(self):
    #Says what to do if person wins
    if self.__human.check_if_win():
      self.__has_winner = True
      num_wins = self.__player_1_num_wins.get() + GameGUI.ONE_MORE
      self.__player_1_num_wins.set(num_wins)
      self.__winner_var.set('You Win!')
      self.__winner_label['fg'] = 'green'
    #Says what to do if there is a tie
    elif self.__check_if_tie():
      self.__has_winner = True
      self.__winner_var.set('It\'s a tie!')
      self.__winner_label['fg'] = 'orange'
    #Allows the computer to move if the user neither wins nor ties
    else:
      self.__play_computer()

  #Computer takes a turn playing
  #invokes __set_computer_space, ComputerPlayer.make_move(),
  #  Player.check_if_win(), Player.change_status()
  def __play_computer(self):

    #Computer selects open location
    computer_num = self.__computer.make_move()

    #Computer uses a piece in the selected location
    self.__set_computer_space(computer_num)
    
    #Says what to do if the computer won
    if self.__computer.check_if_win():
      self.__has_winner = True
      num_wins = self.__player_2_num_wins.get() + 1
      self.__player_2_num_wins.set(num_wins)
      self.__winner_var.set('You Lose')
      self.__winner_label['fg'] = 'red'
      
    #Allows user to move again if the computer did not win
    else:
      self.__human.change_status()

  #Reserves a selected space that is open
  #param num - selected location
  def __set_space(self, num):
    #Person uses a piece in the selected location
    self.__human.use_piece(num)
    #Updates spots available for computer to choose from
    self.__computer.set_spots_used(num)
    #Shows that it is the computer's turn to move
    self.__computer.change_status()

  #Updates information after computer chooses a location
  #param - num (int) - location that the computer selected
  def __set_computer_space(self, num):
    #For any location that the computer chose, marks the spots as used and
    #  updates user's information to how that they cannot take the same spot
    if num == 1:
      self.__space_2_1_str.set('O')
      self.__human.set_spots_used(1)
    elif num == 2:
      self.__space_1_2_str.set('O')
      self.__human.set_spots_used(2)
    elif num == 3:
      self.__space_3_3_str.set('O')
      self.__human.set_spots_used(3)
    elif num == 4:
      self.__space_3_4_str.set('O')
      self.__human.set_spots_used(4)
    elif num == 5:
      self.__space_2_5_str.set('O')
      self.__human.set_spots_used(5)
    elif num == 6:
      self.__space_1_6_str.set('O')
      self.__human.set_spots_used(6)
    elif num == 7:
      self.__space_1_7_str.set('O')
      self.__human.set_spots_used(7)
    elif num == 8:
      self.__space_3_8_str.set('O')
      self.__human.set_spots_used(8)
    else:
      self.__space_2_9_str.set('O')
      self.__human.set_spots_used(9)

  #Checks if there is a tie by seeing if there are any more spots available
  #invokes Player.show_num_spots_open()
  #return bool - whether or not there is a tie
  def __check_if_tie(self):
    return (self.__human.show_num_spots_open() == GameGUI.NONE) or\
      (self.__computer.show_num_spots_open() == GameGUI.NONE)

  #Starts the game again
  #invokes __reset_spaces, Player.reset_pieces()
  #Called by the __new_game_button
  def start_new_game(self):
    #Resets the locations of both player's pieces to be off the board
    self.__human.reset_pieces()
    self.__computer.reset_pieces()

    #Says that there is no winner yet since the game is restarted
    self.__has_winner = False

    #Removes location markers from GUI
    self.__reset_spaces()

  #Resets all information
  #Called by the reset button
  def reset_everything(self):
    
    #Resets both players' information
    self.__human.reset_player()
    self.__player_1_num_wins.set(0)
    self.__computer.reset_player()
    self.__player_2_num_wins.set(0)
    
    #Shows that there is no winner yet since the game is restarted
    self.__has_winner = False

    #Removes the location markers from the GUI
    self.__reset_spaces()

  #Resets all tic-tac-toe spaces to be blank again
  def __reset_spaces(self):
    self.__space_1_2_str.set('\t\n\t')
    self.__space_1_7_str.set('\t\n\t')
    self.__space_1_6_str.set('\t\n\t')

    self.__space_2_9_str.set('\t\n\t')
    self.__space_2_5_str.set('\t\n\t')
    self.__space_2_1_str.set('\t\n\t')

    self.__space_3_4_str.set('\t\n\t')
    self.__space_3_3_str.set('\t\n\t')
    self.__space_3_8_str.set('\t\n\t')

    self.__winner_var.set('')

    #Says that it is the user's turn, not the computer's turn
    if not self.__human.get_status():
      self.__human.change_status()
    if self.__computer.get_status():
      self.__computer.change_status()

  #Opens another window to allow a user to change the game's color settings
  #Called by the __settings_button
  def open_settings(self):
    
    #Creates a new window
    settings_wn = Tk()

    #Changes the title of the window
    settings_wn.title('settings')
    
    piece_color_label = Label(settings_wn, text = 'Set Pieces Color:')

    #Creates button that allow the user to change the color of the pieces
    black_button = Button(settings_wn, text = 'Black', fg = 'black',
                          font = 'Times 15 bold',
                          command = self.set_black_color)
    red_button = Button(settings_wn, text = 'Red', fg = 'red',
                        font = 'Times 15 bold', command = self.set_red_color)
    blue_button = Button(settings_wn, text = 'Blue', fg = 'blue',
                           font = 'Times 15 bold',
                           command = self.set_blue_color)
    green_button = Button(settings_wn, text = 'Green', fg = 'green',
                          font = 'Times 15 bold',
                          command = self.set_green_color)

    #Sets up the buttons and the label in the settings swindow
    piece_color_label.grid(sticky = S + N + E + W)
    black_button.grid(row = 1, sticky = S + N + E + W)
    red_button.grid(row = 2, sticky = S + N + E + W)
    blue_button.grid(row = 3, sticky = S + N + E + W)
    green_button.grid(row = 4, sticky = S + N + E + W)    

    #Runs the mainloop of the settings window
    mainloop()

  #Sets the color of the pieces to black
  def set_black_color(self):
    self.__set_color('black')

  #Sets the color of the pieces to red
  def set_red_color(self):
    self.__set_color('red')

  #Sets the color of the pieces to blue
  def set_blue_color(self):
    self.__set_color('blue')

  #Sets the color of the pieces to green
  def set_green_color(self):
    self.__set_color('green')

  #Sets the color of the piece markers on the game board buttons to a
  #  specified color
  #param - color_str (str) - color to change the pieces to
  def __set_color(self, color_str):
    self.__space_1_2['fg'] = color_str
    self.__space_1_7['fg'] = color_str
    self.__space_1_6['fg'] = color_str
    
    self.__space_2_9['fg'] = color_str
    self.__space_2_5['fg'] = color_str
    self.__space_2_1['fg'] = color_str
    
    self.__space_3_4['fg'] = color_str
    self.__space_3_3['fg'] = color_str
    self.__space_3_8['fg'] = color_str

GameGUI()
