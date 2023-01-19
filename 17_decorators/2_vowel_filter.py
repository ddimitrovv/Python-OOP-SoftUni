def vowel_filter(function):

    def wrapper():
        vowels = ["e", "y", "u", "i", "o", "a"]
        letters = function()
        to_return = [x for x in letters if x.lower() in vowels]
        return to_return

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]

print(get_letters())
