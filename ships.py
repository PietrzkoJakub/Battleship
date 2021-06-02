class Ship:
    """
    Obiekty tej klasy sa inicjalizowane w klasach Enemy oraz Player.
    size - rozmiar okretu, liczby od 1 do 4,
    quantity - laczna ilosc pol zajmowana przez okrety danego typu.
    """
    def __init__(self,size,quantity):
        self.size = size
        self.quantity = quantity*self.size
