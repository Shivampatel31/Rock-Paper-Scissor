import tkinter as tk
from tkinter import messagebox


class RockPaperScissors:
    def __init__(self):
        # Create the main window for the game
        self.window = tk.Tk()
        self.window.title("Rock Paper Scissors Game")  # Set the title of the game window
        self.window.geometry("500x650")  # Set the dimensions of the game window
        self.window.configure(bg="#2b2d42")  # Set the background color of the window
        self.window.resizable(False, False)  # Prevent the window from being resized

        # Initialize game variables
        self.player1_name = None  # Store the name of Player 1
        self.player2_name = None  # Store the name of Player 2
        self.player1_choice = None  # Store Player 1's choice (Rock/Paper/Scissors)
        self.player2_choice = None  # Store Player 2's choice (Rock/Paper/Scissors)
        self.current_player = 1  # Set the first player as Player 1
        self.player1_wins = 0  # Initialize the win count for Player 1
        self.player2_wins = 0  # Initialize the win count for Player 2
        self.round_count = 0  # Track the number of rounds played
        self.max_rounds = 5  # Set the maximum number of rounds to 5

        # Show the login screen when the game starts
        self.show_login_screen()

    def show_login_screen(self):
        # Create a new top-level window for player login
        login_window = tk.Toplevel(self.window)
        login_window.title("Login")  # Set the title of the login window
        login_window.geometry("400x300")  # Set the size of the login window
        login_window.configure(bg="#2b2d42")  # Set the background color of the login window

        # Create a label for the login screen's title
        login_title = tk.Label(
            login_window, text="Enter Player Names",
            font=("Helvetica", 18, "bold"), bg="#2b2d42", fg="#F2A900"
        )
        login_title.pack(pady=20)  # Pack the title label with some padding

        # Create a label and text entry for Player 1's name
        self.player1_name_label = tk.Label(
            login_window, text="Player 1 Name:", font=("Helvetica", 14),
            bg="#2b2d42", fg="white"
        )
        self.player1_name_label.pack(pady=5)  # Label for Player 1's name
        self.player1_name_entry = tk.Entry(login_window, font=("Helvetica", 14))
        self.player1_name_entry.pack(pady=5)  # Text entry for Player 1's name

        # Create a label and text entry for Player 2's name
        self.player2_name_label = tk.Label(
            login_window, text="Player 2 Name:", font=("Helvetica", 14),
            bg="#2b2d42", fg="white"
        )
        self.player2_name_label.pack(pady=5)  # Label for Player 2's name
        self.player2_name_entry = tk.Entry(login_window, font=("Helvetica", 14))
        self.player2_name_entry.pack(pady=5)  # Text entry for Player 2's name

        # Create a button to start the game after both names are entered
        start_button = tk.Button(
            login_window, text="Start Game", font=("Helvetica", 14),
            bg="#F2A900", fg="black", command=lambda: self.start_game(login_window)
        )
        start_button.pack(pady=20)  # Pack the button with some padding

        # Block the main window and wait for the login window to close
        login_window.grab_set()  # Make the login window the active window
        self.window.wait_window(login_window)  # Wait until the login window is closed

    def start_game(self, login_window):
        # Retrieve the player names from the login entries
        self.player1_name = self.player1_name_entry.get()
        self.player2_name = self.player2_name_entry.get()

        # Check if both players have entered their names
        if not self.player1_name or not self.player2_name:
            messagebox.showerror("Error", "Both players must enter names!")  # Show error if names are missing
            return

        # Destroy the login window after the game starts
        login_window.destroy()

        # Proceed to create the game dashboard
        self.create_dashboard()

    def create_dashboard(self):
        # Create and display the title of the game
        self.title_label = tk.Label(
            self.window, text="Rock Paper Scissors",
            font=("Helvetica", 26, "bold"),
            bg="#2b2d42", fg="#F2A900"
        )
        self.title_label.pack(pady=20)  # Pack the title label with padding

        # Create a label indicating which player needs to choose
        self.player_label = tk.Label(
            self.window, text=f"{self.player1_name}, choose your option:",
            font=("Helvetica", 16), bg="#2b2d42", fg="white"
        )
        self.player_label.pack(pady=10)  # Pack the player choice label with padding

        # Create buttons for Rock, Paper, and Scissors choices for Player 1
        self.rock_button = tk.Button(
            self.window, text="Rock", font=("Helvetica", 18), width=15, height=2,
            bg="#FF5733", fg="black", command=lambda: self.make_choice("Rock")
        )
        self.rock_button.pack(pady=15)  # Pack the Rock button with padding

        self.paper_button = tk.Button(
            self.window, text="Paper", font=("Helvetica", 18), width=15, height=2,
            bg="#33C3FF", fg="black", command=lambda: self.make_choice("Paper")
        )
        self.paper_button.pack(pady=15)  # Pack the Paper button with padding

        self.scissors_button = tk.Button(
            self.window, text="Scissors", font=("Helvetica", 18), width=15, height=2,
            bg="#98FB98", fg="black", command=lambda: self.make_choice("Scissors")
        )
        self.scissors_button.pack(pady=15)  # Pack the Scissors button with padding

        # Create a result label to display the round outcome
        self.result_label = tk.Label(
            self.window, text="Result: ",
            font=("Helvetica", 16), bg="#2b2d42", fg="white"
        )
        self.result_label.pack(pady=15)  # Pack the result label with padding

        # Create a button to allow players to play again after each round
        self.reset_button = tk.Button(
            self.window, text="Play Again", font=("Helvetica", 14),
            bg="#F2A900", fg="black", command=self.reset_game
        )
        self.reset_button.pack(pady=10)  # Pack the Play Again button with padding

        # Create a scoreboard label to show win counts for both players
        self.score_label = tk.Label(
            self.window,
            text=f"{self.player1_name} Wins: {self.player1_wins} | {self.player2_name} Wins: {self.player2_wins}",
            font=("Helvetica", 14), bg="#2b2d42", fg="white"
        )
        self.score_label.pack(pady=15)  # Pack the scoreboard label with padding

    def make_choice(self, player_choice):
        # Handle player choices
        if self.current_player == 1:
            self.player1_choice = player_choice  # Player 1's choice
            self.player_label.config(text=f"{self.player2_name}, choose your option:")  # Update label for Player 2
            self.current_player = 2  # Switch to Player 2's turn
        else:
            self.player2_choice = player_choice  # Player 2's choice
            self.display_choices()  # Show both players' choices in the result label
            self.determine_winner()  # Compare choices and determine the winner

            # Increase the round count after both players make their choices
            self.round_count += 1

            # Switch back to Player 1 for the next round
            self.current_player = 1
            self.player_label.config(text=f"{self.player1_name}, choose your option:")

            # End the game after the specified number of rounds
            if self.round_count == self.max_rounds:
                self.end_game()

    def display_choices(self):
        # Display both players' choices in the result label
        self.result_label.config(
            text=f"{self.player1_name} chose: {self.player1_choice}\n{self.player2_name} chose: {self.player2_choice}"
        )

    def determine_winner(self):
        # Determine the winner based on the choices
        if self.player1_choice == self.player2_choice:
            messagebox.showinfo("Round Over", "It's a Tie!")  # Show tie message
        elif (self.player1_choice == "Rock" and self.player2_choice == "Scissors") or \
                (self.player1_choice == "Paper" and self.player2_choice == "Rock") or \
                (self.player1_choice == "Scissors" and self.player2_choice == "Paper"):
            messagebox.showinfo("Round Over", f"{self.player1_name} Wins the Round!")  # Player 1 wins the round
            self.player1_wins += 1  # Increase Player 1's win count
        else:
            messagebox.showinfo("Round Over", f"{self.player2_name} Wins the Round!")  # Player 2 wins the round
            self.player2_wins += 1  # Increase Player 2's win count

        # Update the scoreboard with the latest win counts
        self.update_scoreboard()

    def update_scoreboard(self):
        # Update the score label to display the current win counts for both players
        self.score_label.config(
            text=f"{self.player1_name} Wins: {self.player1_wins} | {self.player2_name} Wins: {self.player2_wins}"
        )

    def end_game(self):
        # After 5 rounds, show the final winner based on the win count
        if self.player1_wins > self.player2_wins:
            messagebox.showinfo("Game Over", f"{self.player1_name} Wins the Game!")  # Player 1 wins the game
        elif self.player2_wins > self.player1_wins:
            messagebox.showinfo("Game Over", f"{self.player2_name} Wins the Game!")  # Player 2 wins the game
        else:
            messagebox.showinfo("Game Over", "The game is a tie!")  # In case of a tie

        self.window.quit()  # Close the game window when the game is over

    def reset_game(self):
        # Reset the game for a new round
        self.player1_choice = None  # Clear Player 1's choice
        self.player2_choice = None  # Clear Player 2's choice
        self.result_label.config(text="Result: ")  # Reset the result label
        self.round_count = 0  # Reset the round count
        self.player1_wins = 0  # Reset Player 1's win count
        self.player2_wins = 0  # Reset Player 2's win count
        self.update_scoreboard()  # Update the scoreboard with reset values

    def run(self):
        # Start the game window and begin the main loop
        self.window.mainloop()


# Run the game by creating an instance of RockPaperScissors and calling the run method
game = RockPaperScissors()
game.run()
