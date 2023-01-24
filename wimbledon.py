# 0 15 30 40 W
import random


class Player():
    def __init__(self):
        self.score = 0
        self.count_win_set = 0

    def win_serve(self):
        if self.score == 30:
            self.score += 10
        self.score += 20

    def get_score(self):
        return self.score

    def get_set(self):
        return self.count_win_set

    def win_set(self):
        self.count_win_set += 1

    def is_winner(self):
        return self.count_win_set == 3

    def show_score(self, oppenent_score):
        different = abs(self.score - oppenent_score)
        if(self.score <=40):
            return self.score
        if(different > 20 and self.score > oppenent_score):
            return "Won"
        if(self.score < oppenent_score and self.score >40):
            return 40
        if (self.score == oppenent_score and self.score >= 40):
            return "D"
        if(self.score > 40 and (self.score - oppenent_score)==20):
            return "Ad"


class GameLogic():
    def __init__(self):
        pass

    def is_winner(self,player1_score,player2_score):
        maximum = max(player1_score,player2_score)
        different = self.get_diff(player1_score,player2_score)
        return maximum >=60 and different >20

    def get_diff(self,player1_score,player2_score):
        return abs(player1_score - player2_score)

    def get_winner(self,player1_score,player2_score):
        if(player1_score > player2_score):
            return "player1"
        if(player2_score > player1_score):
            return "player2"
def main():
    player1 = Player()
    player2 = Player()
    game = GameLogic()
    is_serve = True
    count = 0
    while True:
        is_serve = True
        count = int(max(player1.get_set(),player2.get_set()))
        if(count == 3):
            break
        player1.score = 0
        player2.score = 0
        while is_serve:
            player_number = int(random.randint(1,2))

            if(player_number == 1):
                player1.win_serve()
            if(player_number == 2):
                player2.win_serve()
            print("player1: ",player1.show_score(player2.score),"player2: ",player2.show_score(player1.score))
            if(game.is_winner(player1.score,player2.score)):
                winner = game.get_winner(player1.score,player2.score)
                if(winner == "player1"):
                    player1.win_set()
                if(winner == "player2"):
                    player2.win_set()
                print("***" * 30)
                print(player1.get_set(), player2.get_set())
                is_serve = False






main()