from project.horse_specification.horse import Horse


class Thoroughbred(Horse):

    def max_speed(self):
        return 140

    def speed_increment(self):
        return 3
