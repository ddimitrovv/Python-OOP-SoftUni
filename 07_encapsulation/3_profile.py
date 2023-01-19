class Profile:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username
    
    @username.setter
    def username(self, value):
        if not len(value) in range(5, 16):
            raise ValueError('The username must be between 5 and 15 characters.')
        self.__username = value

    @property
    def password(self):
        return self.__password
    
    @password.setter
    def password(self, value):
        len_password = 5 <= len(value) <= 15
        capital_letter = [x for x in value if x.isupper()]
        digit_symbol = [x for x in value if x.isdigit()]
        if not len_password or not digit_symbol or not capital_letter:
            raise ValueError('The password must be 8 or more characters with at least 1 digit and 1 '
                             'uppercase letter.')

        self.__password = value

    def __str__(self):
        return f'You have a profile with username: "{self.__username}" and ' \
               f'password: {"*" * len(self.__password)}'


# ------ TEST CODE ------
# test 1
profile_with_invalid_password = Profile('My_username', 'My-password')
# test 2
profile_with_invalid_username = Profile('Too_long_username', 'Any')
# test 3
correct_profile = Profile("Username", "Passw0rd")
print(correct_profile)
