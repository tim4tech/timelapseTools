class Camera:
    """
    An easy container for tracking video4linux camera name and index
    """
    
    name: str
    index: int

    def __init__(self, n: str, i: int):
        self.name = n
        self.index = i

    def __str__(self):
        return "-- {} has index {}".format(self.name, self.index)