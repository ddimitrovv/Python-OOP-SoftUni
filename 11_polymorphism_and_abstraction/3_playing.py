# Create a function called start_playing which will receive an instance and will return its play() method.


class Guitar:
    def play(self):
        return "Playing the guitar"


guitar = Guitar()


class Children:
    def play(self):
        return "Children are playing"


children = Children()


def start_playing(obj):
    return obj.play()


print(start_playing(children))
print(start_playing(guitar))
