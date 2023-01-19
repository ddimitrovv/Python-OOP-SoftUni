# Create a class called PhotoAlbum. Upon initialization, it should receive pages (int).
# It should also have one more attribute: photos (empty matrix) representing the album
# with its pages where you should put the photos. Each page can contain only 4 photos.
# The class should also have 3 more methods:
#     • from_photos_count(photos_count: int) - creates a new instance of PhotoAlbum.
#       Note: Each page can contain 4 photos.
#     • add_photo(label:str) - adds the photo in the first possible page and slot and return:
#       "{label} photo added successfully on page {page_number(starting from 1)}
#           slot {slot_number(starting from 1)}". If there are no free slots left, return "No more free slots"
#     • display() - returns a string representation of each page and the photos in it.
#       Each photo is marked with "[]", and the page separation is made using 11 dashes (-).
#       For example, if we have 1 page and 2 photos:
# -----------
# [] []
# -----------
# and if we have 2 empty pages:
# -----------
#
# -----------
#
# -----------
from math import ceil


class PhotoAlbum:
    photos_per_page = 4

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        pages = ceil(photos_count / PhotoAlbum.photos_per_page)
        return cls(pages)

    def add_photo(self, label: str):
        for i in range(len(self.photos)):
            if len(self.photos[i]) < self.photos_per_page:
                self.photos[i].append(label)
                return f'{label} photo added successfully on page {i + 1} ' \
                       f'slot {len(self.photos[i])}'
        return 'No more free slots'

    def display(self):
        result = list()
        pages_separator = 11 * '-'
        result.append(pages_separator)

        for i in range(len(self.photos)):
            photos_per_page = ' '.join(["[]" for x in range(len(self.photos[i]) + 1) if x])
            result.append(photos_per_page)
            result.append(pages_separator)

        return '\n'.join(result)


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
