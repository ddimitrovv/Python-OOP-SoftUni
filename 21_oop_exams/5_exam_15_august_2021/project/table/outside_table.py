import os

from project.table.table import Table
from project.validators import number_in_range_validator


class OutsideTable(Table):
    MIN_TABLE_NUMBER = 51
    MAX_TABLE_NUMBER = 100
    TABLE_NUMBER_ERROR_MESSAGE = f"Outside table's number must be between {MIN_TABLE_NUMBER}" \
                                 f" and {MAX_TABLE_NUMBER} inclusive!"

    def __init__(self, table_number: int, capacity: int):
        super().__init__(table_number, capacity)

    @property
    def table_number(self):
        return self.__table_number

    @table_number.setter
    def table_number(self, value):
        if number_in_range_validator(
                value, self.MIN_TABLE_NUMBER, self.MAX_TABLE_NUMBER, self.TABLE_NUMBER_ERROR_MESSAGE):
            self.__table_number = value

    def free_table_info(self):
        if not self.is_reserved:
            return os.linesep.join([f"Table: {self.table_number}",
                                    f"Type: {self.__class__.__name__}",
                                    f"Capacity: {self.capacity}"])
