from project.decoration.base_decoration import BaseDecoration


class Ornament(BaseDecoration):
    def __init__(self):
        super().__init__(1, 5)
        self.decoration_type = 'Ornament'
