from abc import abstractmethod, ABC
class Band:
    members = []

    class Musician(ABC):
        def __init__(self,name):
            self.name = name
            Band.members.append(self.name)
        @classmethod
        def play_solos(self):

            for i in members:
                print(f'{i} play a solo')
        @abstractmethod
        def __str__(self):
            return f"Musician <{self.name}>"
        @abstractmethod
        def __repr__(self):
            return f" '{self.name}' "
        def to_list(self):
            return Band.members

    class Guitarist(Musician):
        def __init__(self,name):
            super().__init__(name)
        def __str__(self):
            return f"Guitarist <{self.name}>"
        def __repr__(self):
            return f" '{self.name}' "
        def get_instrument(self):
            return 'Guitarist'
        def play_solo(self):
            return 'Play Guitar'

    class Bassist(Musician):
        def __init__(self,name):
            # self.name = name
            super().__init__(name)
        def __str__(self):
            return f"Bassist <{self.name}>"
        def __repr__(self):
            return f" '{self.name}' "
        def get_instrument(self):
            return 'Bassist'
        def play_solo(self):
            return 'Play Bassist'
    
    class Drummer(Musician):
        def __init__(self,name):
            # self.name = name
            super().__init__(name)
        def __str__(self):
            return f"Drummer <{self.name}>"
        def __repr__(self):
            return f" '{self.name}' "
        def get_instrument(self):
            return 'Drummer'
        def play_solo(self):
            return 'Dom Dum Dom Dum'

if __name__ == "__main__":
    aziz = Band.Guitarist('aziz')
    saleh = Band.Drummer('saleh')
    emad = Band.Bassist('emad')
    print(saleh.__str__())
    # # print(saleh.get_instrument())
    # print(Band.members)