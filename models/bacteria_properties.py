class BacteriaProperties:
    """
    Represents the properties of a bacteria.

    Args:
        name (str): The name of the bacteria.
        speed (int, optional): The speed of the bacteria. Defaults to 1.
        sense (int, optional): The sense of the bacteria. Defaults to 1.
    """

    def __init__(self, name: str, speed: int = 1, sense: int = 1):
        """
        Initializes a new instance of the BacteriaProperties class.

        Args:
            name (str): The name of the bacteria.
            speed (int, optional): The speed of the bacteria. Defaults to 1.
            sense (int, optional): The sense of the bacteria. Defaults to 1.
        """
        self.name = name
        self.speed = speed
        self.sense = sense
