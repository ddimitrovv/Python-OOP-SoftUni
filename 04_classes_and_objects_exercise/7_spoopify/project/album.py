from project1.song import Song


class Album:

    def __init__(self, name, *songs):
        self.name = name
        self.songs = list(songs)
        self.published = False

    def add_song(self, song):
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        if self.published:
            return f'Cannot add songs. Album is published.'
        if song in self.songs:
            return f'Song is already in the album.'
        self.songs.append(song)
        return f'Song {song.name} has been added to the album {self.name}.'

    def remove_song(self, song_name):
        if self.published:
            return f"Cannot remove songs. Album is published."
        for song in self.songs:
            if song.name == song_name:
                self.songs.remove(song)
                return f"Removed song {song_name} from album {self.name}."
        return "Song is not in the album."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        output = list()
        output.append(f'Album {self.name}')
        for song in self.songs:
            output.append(f'== {song.get_info()}')
        return '\n'.join(output)
        # output = f'Album {self.name}\n'
        # for song in self.songs:
        #     output += f'== {song.get_info()}\n'
        # return output.strip()
