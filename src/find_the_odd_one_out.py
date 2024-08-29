import tkinter as tk
from tkinter import messagebox
import random
import time
import patterns
import chosen


class GameGui:

    def __init__(self):

        # To save the patterns that appear in the game
        self.logs = open('logs.txt', 'w', encoding='utf-16')

        # To count the number of correct choices
        self.score_hit = 0

        # To count the number of missed choices
        self.score_missed = 0

        # To count the number of incorrect choices
        self.score_wrong = 0

        # To store the number of wrong buttons
        self.wrong_buttons = 0

        # To store the button index
        self.button_index = 0

        # To Show the level number on the interface
        self.level_counter = 1

        # To store all the buttons
        self.button_list = []

        # To store all the tiles
        self.tiles = []

        # To rember if the uncommon button was pressed
        self.uncommon_found = False

        # To remember if the wrong button was pressed
        self.wrong_button_smashed = False

        # To remember if the hack button was pressed
        self.hack_button_pressed = False

        # To provide the time to the player to find the odd button
        self.normal_mode_time_counter = 4000

        # Total number of leves
        self.total_number_of_levels = 30

        # nurmal mode frame = level number
        self.normal_mode_frame_counter = self.total_number_of_levels

        # To keep the game's frames stable
        slow_pc = True
        if slow_pc:
            self.hack_mode_hacked_frame_timer = 100
        else:
            self.hack_mode_hacked_frame_timer = 45

        # To keep track of number of levels in hacked mode
        self.hacked_frames = 0

        # To get the uncommon button's index
        self.uncommon_index = patterns.square(chosen.choose.uncommon, chosen.choose.common)

        # Create the GUI
        self.root = tk.Tk()

        # Provided name to the interface
        self.root.title("Find the odd one out")

        # Provided the dimensions of the interface window
        self.root.geometry("400x560")

        # To not allow the user to resize the window to maintain the stability of the interface
        self.root.resizable(False, False)

        # If user presses the exit button then ask if they really want to quit
        self.root.protocol("WM_DELETE_WINDOW", self.no_quitting)

        # To show the score details
        self.label = None

        # To create the button frame
        self.button_frame = None

        # To create the hack button
        self.hack_button = None

        # Create the Start button
        self.start_button = tk.Button(self.root, text='Start Game', font=('Agency FB', 20), background="#5da842",
                                      command=self.destroy_button1)
        self.start_button.pack(padx=10, pady=230)
        self.root.mainloop()

    def no_quitting(self):
        """Asks if the user really wants to quit"""

        if messagebox.askyesno(title="Do not quit.", message="You Quit, You Lose"):
            self.root.destroy()

    def begin_game(self):
        """Start of the game"""

        # To make a choice of odd and even characters
        chosen.choice()

        # To show the score on the interface
        self.score_generator()

        # To show the even and odd buttons on the interface
        self.level_generator()

        # To generate the hack button
        self.generate_hack_button()

        # After "normal_mode_time_counter" seconds goto next level
        self.root.after(self.normal_mode_time_counter, self.next_timed_level)

    def score_generator(self):
        """Generates the score, to display"""

        # Score of the user
        text_score = "Level: " + str(self.level_counter) + "\n" + "Hit : " + str(self.score_hit) + "   " + "Missed :" +\
                     str(self.score_missed) + "   " + "Deceived: " + str(self.score_wrong)
        self.label = tk.Label(self.root, text=text_score, font=('Agency FB', 20), foreground='#eb0c0f')
        self.label.pack(padx=20, pady=20)

    def level_generator(self):
        """To create the level"""

        self.button_list = []

        # To create the button frame
        self.button_frame = tk.Frame(self.root)

        # To create all the buttons
        for row in range(patterns.rows):
            self.button_frame.columnconfigure(row, weight=1)
        for i in range(patterns.rows):
            for j in range(patterns.columns):

                # If the index of button = index of the odd button, then create add button
                if self.button_index == self.uncommon_index:
                    self.button_list.append(tk.Button(self.button_frame, text=patterns.sequence[self.button_index],
                                                      font=('Agency FB', 18), command=self.right_button_pressed,
                                                      height=1, width=4, background='White', border=True))
                    self.button_list[self.button_index].grid(row=i, column=j, sticky=tk.W + tk.E, padx=4, pady=4)
                    print(patterns.sequence[self.button_index], end=" ", file=self.logs)
                    self.button_index += 1

                else:
                    self.button_list.append(tk.Button(self.button_frame, text=patterns.sequence[self.button_index],
                                                      font=('Agency FB', 18), command=self.wrong_button_pressed,
                                                      height=1, width=4, background='White', border=True))
                    self.button_list[self.button_index].grid(row=i, column=j, sticky=tk.W + tk.E, padx=4, pady=4)
                    print(patterns.sequence[self.button_index], end=" ", file=self.logs)
                    self.button_index += 1

            # Print the buttons/patterns to keep track of all the level that user has played
            print(file=self.logs)
        print(
            "---------------------------------------------------------------------------------------------------------",
            file=self.logs)
        self.button_frame.pack()
        self.button_index = 0

    def right_button_pressed(self):
        """When the player finds the odd one"""

        # Chanege the backgrouund color of the button
        self.button_list[self.uncommon_index].config(background="#15c39a", state='disabled')

        # Increase the "Hit" score of the user
        self.score_hit += 1
        self.label['text'] = "Level: " + str(self.level_counter) + "\n" + "Hit: " + str(self.score_hit) + "   " + \
                             "Missed: " + str(self.score_missed) + "   " + "Deceived: " + str(self.score_wrong)
        self.uncommon_found = True

    def wrong_button_pressed(self):
        """When the wrong button is pressed"""

        # Disable the correct button
        self.button_list[self.uncommon_index].config(background="White", state='disabled')

        # To make only one wrong button is pressed
        if self.wrong_buttons == 0:
            self.score_wrong += 1
            self.label['text'] = "Level: " + str(self.level_counter) + "\n" + "Hit: " + str(self.score_hit) + "   " + \
                                 "Missed: " + str(self.score_missed) + "   " + "Deceived: " + str(self.score_wrong)
        self.wrong_buttons += 1
        self.wrong_button_smashed = True

    def reset_level_counter(self):
        """Resets the number of level"""

        self.level_counter = 0
        self.hacked_level()

    def hacked_level(self):
        """Create the hacked levels"""

        # If the number of hacked levels = 7, then end game
        if self.level_counter == 7:

            # If the number of correct buttons pressed is >= 4, payer wins
            if not (self.score_hit >= 4):
                messagebox.askyesno(title="Hack Failed", message="You Lose")
                exit()
            else:
                messagebox.askyesno(title="Hack Complete", message="You Win")
                exit()

        self.hack_button_pressed = True

        # Destroy the current frame in order to generate the next frame
        self.label.destroy()
        self.button_frame.destroy()
        self.hack_button.destroy()
        chosen.choice()
        self.uncommon_index = patterns.square(chosen.choose.uncommon, chosen.choose.common)
        self.score_generator()
        self.level_generator()
        self.generate_hack_button()
        self.hack_button['state'] = "disabled"
        self.label['text'] = "Level: " + str(random.randint(0, 1000)) + "\n" + "Hit: " + str(random.randint(0, 1000)) + "   " + \
                             "Missed: " + str(random.randint(0, 1000)) + "   " + "Deceived: " + str(random.randint(0, 1000))

        # Keep flashing the unplayable levels untill a playable level appears
        if self.hacked_frames < 20:
            self.hacked_frames += 1
            self.root.after(self.hack_mode_hacked_frame_timer, self.hacked_level)
            if self.hacked_frames == 19:
                print("Hacked", file=self.logs)
        else:
            self.level_counter += 1
            self.hacked_frames = random.randint(-10, 0)
            self.root.after(random.randint(1750, 2250), self.hacked_level)

    def next_timed_level(self):
        """Generate the next level"""

        if not self.hack_button_pressed:
            self.level_counter += 1
            if self.normal_mode_frame_counter == 0:
                # If all the levels have been vistited then End game and show the score, else continue to the next level
                accuracy = int((self.score_hit /  self.total_number_of_levels)* 100)
                messagebox.askyesno(title="Game Over", message="Hit: " + str(self.score_hit) + "   " + "Missed: " +
                                                           str(self.score_missed) + "   " + "Deceived: " + "   " +
                                    str(self.score_wrong) + "\n" + "Accuracy: " + str(accuracy) + "%")
                self.root.destroy()
                self.logs.close()
                exit()
            else:
                self.normal_mode_frame_counter -= 1
            self.label.destroy()
            self.button_frame.destroy()
            self.hack_button.destroy()
            chosen.choice()
            self.uncommon_index = patterns.square(chosen.choose.uncommon, chosen.choose.common)
            self.score_generator()
            self.level_generator()
            self.generate_hack_button()
            self.wrong_buttons = 0

            # If no button pressed, increase the "Missed" score
            if not self.uncommon_found and not self.wrong_button_smashed:
                self.score_missed += 1
            self.label['text'] = "Level: " + str(self.level_counter) + "\n" + "Hit: " + str(self.score_hit) + "   " + \
                                 "Missed: " + str(self.score_missed) + "   " + "Deceived: " + str(self.score_wrong)
            self.uncommon_found = False
            self.wrong_button_smashed = False
            self.normal_mode_time_counter -= 125
            self.root.after(self.normal_mode_time_counter, self.next_timed_level)

    def generate_hack_button(self):
        """Generate the hacked button"""

        self.hack_button = tk.Button(self.root, text='Hack', width=6, height=1, font=20, background='#138dc4',
                                     command=self.reset_level_counter)
        self.hack_button.pack(padx=10, pady=10)

    def destroy_button1(self):
        """Destroy the Start button and begin the game"""

        self.start_button.destroy()
        self.begin_game()


GameGui()
