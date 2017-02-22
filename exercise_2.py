# Zadanie 2

def football_win(Ag, Bw, Aw, Bg):
    if (Ag + Aw > Bw + Bg) or (Ag + Aw == Bw + Bg and Aw > Bw):
        return "1"
    elif (Ag + Aw < Bw + Bg) or (Ag + Aw == Bw + Bg and Aw < Bw):
        return "2"
    else:
        return "x"

print(football_win(0, 3, 4, 1))