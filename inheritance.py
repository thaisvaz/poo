from abc import ABC

class GeneralModel(ABC):

    def fitting(self):
        
        print('training')

class Classifier(GeneralModel):

    def __init__(self):

        pass

    def fitting(self):

        print('training classifier')

class Regressor(GeneralModel):

    def __init__(self):

        pass

    def fitting(self):

        print('training regressor')


class NotSupervised(GeneralModel):

    def __init__(self):

        pass

if __name__ == '__main__':

    mc = Classifier()

    mr = Regressor()

    mnt = NotSupervised() # não tem o método especifico que sobrescreve o método principal, então ele herda o principal
    # generalModel -- classe mae / notSuperviser --> classe filha

    mc.fitting()

    mr.fitting()

    mnt.fitting()