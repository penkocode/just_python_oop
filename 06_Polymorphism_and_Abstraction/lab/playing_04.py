# 4.Playing
def start_playing(obj):
    return obj.play()


class Guitar:
    def play(self):
        return "Playing the guitar"


guitar = Guitar()
print(start_playing(guitar))


class Children:
    def play(self):
        return "Children are playing"


piano = Children()
print(start_playing(piano))
