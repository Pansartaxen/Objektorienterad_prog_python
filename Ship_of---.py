#Marius Stokkedal
import random
class ShipOfFoolsGame:
    def __init__(self):
        self.winn_score = 50
        self._cup = DiceCup()

    def winning_score(self):
        return(self.winn_score)

    def turn(self):
        has_ship = False
        has_captain = False
        has_mate = False
        self._cup.release_all()
        crew = 0 # This will be the sum of the remaining dice, i.e., the score.

        # Repeat three times
        print('-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x- Ny runda -x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-')
        for _ in range(3):
            self._cup.roll()
            for _ in range(3): #Loopar 3 gånger för att inte missa om man exempelvis skulle få en 5a före en 6a på samma runda
                for i in range(5):
                    if self._cup.value(i) == 6 and has_ship == False:
                        has_ship = True
                        self._cup.bank(i)
                    elif self._cup.value(i) == 5 and has_captain == False and has_ship == True:
                        has_captain = True
                        self._cup.bank(i)
                    elif self._cup.value(i) == 4 and has_mate == False and has_captain == True and has_ship == True:
                        has_mate = True
                        self._cup.bank(i)
                    elif self._cup.value(i) > 3 and has_mate == True and has_captain == True and has_ship == True:
                        self._cup.bank(i)
            for i in range(5):
                    print(f'Tärning #{i+1}: {self._cup.value(i)}, Banked: {self._cup.is_banked(i)}')
            print('')
        print('&&&&&&&&&&&&&&&&&&&&& Slut på runda &&&&&&&&&&&&&&&&&&&&&')
        if has_ship and has_captain and has_mate:
            for i in range(5):
                crew += self._cup.value(i)
            return(crew-15)
        else:
            return(0)

class Die:
    def __init__(self):
        self._value = 1

    def get_value(self):
        """Returnerar värdet på tärningens värde"""
        return(self._value)

    def roll(self):
        """Slår tärningen"""
        self._value = random.randint(1,6)

class DiceCup:
    def __init__(self):
        self.banked = [False, False, False, False, False]
        self._dice = [Die(),Die(),Die(),Die(),Die()]
    
    def value(self, index):
        """Returnerar värdet på tärningen med önskat index"""
        return(self._dice[index].get_value())

    def bank(self, index):
        """Bankar önskad tärning"""
        self.banked[index] = True

    def is_banked(self, index):
        """Returnerar 'True' eller 'False' beroende på om en tärning är bankad eller inte"""
        if self.banked[index] == True:
            return(True)
        else:
            return(False)

    def release(self, index):
        """Tar bort bankad tärning med specifikt index"""
        self.banked[index] = False

    def release_all(self):
        """Tar bort alla bankade tärningar"""
        for i in range(5):
            self.banked[i] = False

    def roll(self):
        """Kastar tärningar som inte är bankade"""
        for i,j in zip(self._dice, self.banked):
            if j == False:
                i.roll()
            else:
                pass

class Player:
    def __init__(self, playernName):
        self.name = playernName
        self._score = 0

    def player_name(self):
        """Returnerr spelarens namn"""
        return(self.name)

    def current_score(self):
        """Returnerar spelarens poäng"""
        return(self._score)

    def reset_score(self):
        """Åteställer spelarens poäng"""
        self._score = 0

    def play_turn(self, game):
        """Spelar en omgång åt spelaren"""
        self._score += game.turn()

class PlayRoom:
    def __init__(self):
        self._players = []
        self._game = None

    def set_game(self, game):
        """Väljer spel"""
        self._game = game

    def add_player(self, name):
        """Lägger till en spelare i listav av spelare"""
        self._players.append(name)

    def reset_scores(self):
        """Återställer poängen för alla spelarna"""
        for index in self._players:
            index.reset_score()

    def play_round(self):
        """Spelar en runda för varje spelare"""
        for index in self._players:
            index.play_turn(self._game)

    def game_finished(self):
        """Kollar om någon spelare har uppnåt maxpoäng"""
        for index in self._players:
            if index.current_score() >= self._game.winning_score() or index.current_score() < 0:
                return(True)

    def print_scores(self):
        """Printar poängen för alla spelare"""
        for index in self._players:
            print(f"{index.player_name()}: {index.current_score()}")

    def print_winner(self):
        """Printar vinnarens namn samt poäng"""
        for index in self._players:
            if index.current_score() >= self._game.winning_score():
                print(f"Grattis {index.player_name()} du vann med {index.current_score()} poäng!")


if __name__ == "__main__":
    room = PlayRoom()
    room.set_game(ShipOfFoolsGame())
    room.add_player(Player('Elvis'))
    room.add_player(Player('Alice'))
    room.add_player(Player('Marius'))
    room.reset_scores()
    counter = 0
    while not room.game_finished():
        room.play_round()
        room.print_scores()
        counter += 1
    room.print_winner()
    print(f"{counter} rundor")