class Game:
    def __init__(self, turn='X', tie=False, winner=None):
        self.turn = turn
        self.tie = tie
        self.winner = winner
        self.board = {
            'a1': None, 'b1': None, 'c1': None,
            'a2': None, 'b2': None, 'c2': None,
            'a3': None, 'b3': None, 'c3': None,
        }

    def print_board(self):
        b = self.board
        print(f"""
                A   B   C
            1)  {b['a1'] or ' '} | {b['b1'] or ' '} | {b['c1'] or ' '}
                ----------
            2)  {b['a2'] or ' '} | {b['b2'] or ' '} | {b['c2'] or ' '}
                ----------
            3)  {b['a3'] or ' '} | {b['b3'] or ' '} | {b['c3'] or ' '}
        """)

    def print_message(self):
        if self.tie:
            print("It's a tie!")
        elif self.winner:
            print(f"{self.winner} wins the game!")
        else:
            print(f"It's player {self.turn}'s turn!")

    def render(self):
        self.print_board()
        self.print_message()

    def player_move(self):
        while True:
            valid_moves = ('a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3')
            move = input(f"Player {self.turn}, enter a valid move (example: A1): ").lower()
            if move in valid_moves and self.board[move] is None:
                self.board[move] = self.turn
                break
            else:
                print("Invalid move or position already taken. Please try again.")

    def check_winner(self):
        winning_combinations = [
            ['a1', 'a2', 'a3'], ['b1', 'b2', 'b3'], ['c1', 'c2', 'c3'],
            ['a1', 'b1', 'c1'], ['a2', 'b2', 'c2'], ['a3', 'b3', 'c3'],
            ['a1', 'b2', 'c3'], ['a3', 'b2', 'c1']
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] and self.board[combo[0]] is not None:
                return True
        return False

    def check_for_tie(self):
        if all(value is not None for value in self.board.values()) and not self.winner:
            self.tie = True

    def switch_turn(self):
        self.turn = {'X': 'O', 'O': 'X'}[self.turn]

    def play_game(self):
        print("Shall we play a game?")

        while not self.winner and not self.tie:
            self.render()
            self.player_move()
            if self.check_winner():
                self.winner = self.turn
                break
            elif self.check_for_tie():
                self.tie = True
                break
            else:
                self.switch_turn()

        self.render()
        print("Game Over!")

game_instance = Game()
game_instance.play_game()

