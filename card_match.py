import random


class PlayingCards:
    def __init__(self):
        self.cards = []
        self.clicks = []
        self.vals = []
        self.count = 0
        self.pcard = [
            [['X', 0, 0], ['X', 0, 1], ['X', 0, 2], ['X', 0, 3]],
            [['X', 1, 0], ['X', 1, 1], ['X', 1, 2], ['X', 1, 3]],
            [['X', 2, 0], ['X', 2, 1], ['X', 2, 2], ['X', 2, 3]],
            # [['X', 3, 0], ['X', 3, 1], ['X', 3, 2]],
        ]

    def start(self):
        cards_list = [
            1, 2, 3, 4, 5, 6,
            1, 2, 3, 4, 5, 6
        ]
        for r in range(3):
            row = []
            for c in range(4):
                num = random.choice(cards_list)
                row.append(num)
                cards_list.pop(cards_list.index(num))
            self.cards.append(row)


    def click(self, row_: int, col_: int):
        self.count = self.count + 1
        card_val = self.cards[row_][col_]
        self.vals.append(card_val)
        self.clicks.append((row_, col_))

        self.pcard[row_][col_][0] = card_val

        if len(self.vals) > 2:
            if not self.check_matching():
                self.update_display(['X', 'X'])
            else:
                self.reset_click()

        return self.pcard


    def check_matching(self):
        if self.vals[0] == self.vals[1]:
            return True
        return False

    def update_display(self, vals_):
        for r_, c_ in self.clicks[:2]:
            ind = self.clicks.index((r_, c_))
            self.pcard[r_][c_][0] = vals_[ind]
        self.reset_click()

    def reset_click(self):
        self.clicks = self.clicks[2:]
        self.vals = self.vals[2:]

    def display(self):
        return self.pcard


# if __name__ == '__main__':
#     dw = PlayingCards()
#     dw.start()
#     print(dw.cards)






