import random


def possession_start(probabilities):
    """
    This function takes in a dictionary containing probabilities for each possession start method.
    The keys of the dictionary represent the start methods, and the values are the probabilities.
    The function returns a possession start method based on the provided probabilities.
    """
    methods = list(probabilities.keys())
    probs = list(probabilities.values())

    return random.choices(methods, weights=probs, k=1)[0]


# Example usage:
possession_start_probs = {
    "jump_ball": 0.02,
    "inbound_made_basket": 0.35,
    "inbound_dead_ball": 0.25,
    "inbound_missed_free_throw": 0.05,
    "inbound_timeout": 0.1,
    "turnover": 0.13,
    "rebound_after_missed_shot": 0.1
}


class Player:
    def __init__(self, name, two_point_pct, three_point_pct, fgr, ftr, pas, to_rate, to_pct, reb_rate, reb_pct, dfg, dto, pace, o_iq, d_iq):
        self.name = name
        self.two_point_pct = two_point_pct
        self.three_point_pct = three_point_pct
        self.fgr = fgr
        self.ftr = ftr
        self.pas = pas
        self.to_rate = to_rate
        self.to_pct = to_pct
        self.reb_rate = reb_rate
        self.reb_pct = reb_pct
        self.dfg = dfg
        self.dto = dto
        self.pace = pace
        self.o_iq = o_iq
        self.d_iq = d_iq

    def __repr__(self):
        return f"{self.name} (2P%: {self.two_point_pct}, 3P%: {self.three_point_pct}, FGr: {self.fgr}, FTr: {self.ftr}, PAS: {self.pas}, TO: {self.to_rate}, TO%: {self.to_pct}, REB: {self.reb_rate}, REB%: {self.reb_pct}, DFG: {self.dfg}, DTO: {self.dto}, PACE: {self.pace}, O-IQ: {self.o_iq}, D-IQ: {self.d_iq})"


player1 = Player("John Doe", 0.5, 0.35, 0.2, 0.1, 5, 0.15,
                 0.1, 0.12, 0.08, 0.05, 0.03, 100, 110, 105)
print(player1)

# start_method = possession_start(possession_start_probs)
# print(start_method)
