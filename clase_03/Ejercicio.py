from datetime import date
from random import random


class Activity3:

    def find(self):

        var_list = ["almacenar", 8, "a", [1, 2, 3], True, (0, 0, 1), 85.7]
        var_find = [85.7, True, [(0,0,1)], [1,2,3], 0, [True], 85, "a"]

        self.get_find_1(var_list, var_find)
        self.get_find_2(var_list)
        self.get_find_3(var_list)


    def get_find_1(self, in_list, in_find):

        for var_found in in_find:

            var_exist = False
            var_positioned = 0

            for var_position, var_listed in enumerate (in_list):

                if var_listed == var_found:

                    var_exist = True
                    var_positioned = var_position + 1

            if var_exist:

                print(f'Value {var_found} is on list in position {var_positioned}')

            else:

                print(f'Value {var_found} is not on list')


    def get_find_2(self, in_list):

        print(f'Initial list: {in_list}')

        var_list = in_list[:-1]

        print(f'Final list: {var_list}')


    def get_find_3(self, in_list):

        var_string = ''.join(str(in_list))

        var_count = var_string.count('a')

        print(f'"a" is {var_count} times into {in_list}')


    def palindrome(self, in_word):

        var_word = in_word[::-1]

        if in_word == var_word:

            print('is palindrome')

        else:

            print('is not palindrome')


    def inverse(self):

        var_list = []
        var_range = 10

        for _ in range(var_range):

            var_list.append(str(int(random() * 1000)))

        var_inverse = var_list[::-1]

        print(var_list)
        print(var_inverse)
        print(','.join(var_inverse))

    def subjects(self):

        var_list = ['M', 'F', 'Q', 'L', 'H']
        var_value = []

        for _ in var_list:

            var_value.append(int(random() * 100))

        for var_position, var_offset in enumerate(var_list):

            print(f'ramo {var_list[var_position]} y nota {var_value[var_position]}')


    def arrays(self):

        var_matrix_1 = self.get_array(2, 3)
        var_matrix_2 = self.get_array(3, 2)

        self.get_multiplication(var_matrix_1, var_matrix_2)


    def get_array(self, in_rows, in_cols):

        var_row = []

        for _ in range(in_rows):

            var_col = []

            for _ in range(in_cols):

                var_col.append(int(random() * 100))

            var_row.append(var_col)

        print(f'Matrix 1 = {var_row}')

        return var_row


    def get_multiplication(self, in_matrix_1, in_matrix_2):

        var_row = []

        for var_cols in range(len(in_matrix_1)):

            var_col = []

            for var_rows in range(len(in_matrix_2[0])):

                var_col.append(in_matrix_1[var_rows][var_cols] * in_matrix_2[var_cols][var_rows])

            var_row.append(var_col)

        print(f'Matrix 3 = {var_row}')


    def date(self):

        var_date = date.today()
        var_day = var_date.strftime("%d")
        var_month = var_date.strftime("%B")
        var_year = var_date.strftime("%Y")

        print(f'Today is {var_date}')
        print(f'Today is {var_day} of {var_month} of {var_year}')


activity3 = Activity3()

activity3.find()
activity3.palindrome('123321')
activity3.inverse()
activity3.subjects()
activity3.date()
activity3.arrays()
