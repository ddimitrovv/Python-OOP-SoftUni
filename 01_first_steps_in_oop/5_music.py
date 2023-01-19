# Create a class named Music that receives title (string), artist (string),
# and lyrics (string) upon initialization. The class should also have two additional methods:
#     • The print_info() method should return the following: 'This is "{title}" from "{artist}"'
#     • The play() method should return the lyrics.
# Submit only the class in the judge system. Test your code with your own examples.

class Music:
    def __init__(self, title, artist, lyrics):
        self.title = title
        self.artist = artist
        self.lyrics = lyrics

    def print_info(self):
        return f'This is "{self.title}" from "{self.artist}"'

    def play(self):
        return self.lyrics


song = Music(
    "Poison",
    "Alice Cooper",
    """Your cruel device
Your blood, like ice
One look, could kill
My pain, your thrill
I wanna love you but I better not touch (don't touch)
I wanna hold you, but my senses tell me to stop
I wanna kiss you but I want it too much (too much)
I wanna taste you but your lips are venomous poison
You're poison, running through my veins
You're poison
I don't want to break these chains
Your mouth, so hot
Your web, I'm caught
Your skin, so wet
Black lace, on sweat
I hear you calling and it's needles and pins (and pins)
I wanna hurt you just to hear you screaming my name
Don't want to touch you but you're under my skin (deep in)
I wanna kiss you but your lips are venomous poison
You're poison, running through my veins
You're poison
I don't want to break these chains
Poison
One look, could kill
My pain, your thrill
I wanna love you but I better not touch (don't touch)
I wanna to hold you, but my senses tell me to stop
I wanna to kiss you but I want it too much (too much)
I wanna taste you but your lips are venomous poison
You're poison, running through my veins
You're poison
I don't want to break these chains
Poison (poison)
I wanna love you but I better not touch (don't touch)
I wanna hold you, but my senses tell me to stop
I wanna kiss you but I want it too much (too much)
I wanna taste you but your lips are venomous poison
Yeah, well I don't want to break these chains
Poison (poison)
Runnin' deep inside my veins
Burnin' deep inside my brain (poison)
Poisoning (poison)
I don't want to break these chains (poison)
Poison
(Poison) I don't want to break these chains (poison)"""
)

print(song.print_info())
print(song.play())
