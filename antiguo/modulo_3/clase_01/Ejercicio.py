import pandas as pd

class Exercise:

    def __init__(self):
        self.data = {
            'metros': [1, 2, 3, 4, 5, 6, 7, 8],
            'ninos': [2, 6, 10, 5, 10, 3, 2, 2]
        }
        self.dataframe = pd.DataFrame(self.data)

        self.dataframe['producto'] = self.dataframe.prod(axis=1)

        # print(self.data)
        # print(self.dataframe)
        # print(self.dataframe.describe())
        # print(self.dataframe['metros'].sum())
        # print(self.dataframe['ninos'].sum())

        # productoria = self.dataframe.prod(axis=1)

        print(self.dataframe['producto'].sum() / self.dataframe['ninos'].sum())

        print(self.dataframe.mode('metros'))

        self.dataframe['metros'].plot(kind='hist', bins=8)



        # print(self.dataframe['metros'].quantile(.7))



exercise = Exercise()



