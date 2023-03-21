class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
        return f"{self.name}, {self.score}"

    def get_score(self):
        return self.score


players = [
    Player("Alex", 700),
    Player("Mary", 950),
    Player("Ann", 890),
]


def total_score():
    return sum([pl.get_score() for pl in players])


def avg_score():
    new_score = total_score() / len(players)
    return new_score


the_score = total_score()
print(the_score)

the_average = avg_score()
print(round(the_average))