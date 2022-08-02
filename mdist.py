def manhattan_distance(location: int, home: int) -> int:
        """ Returns the direct step distance between two locations on the 8-Block board."""
        if location == home:
            return 0
        elif location == 0:
            if home in [1, 3]:
                return 1
            elif home in [2, 4, 6]:
                return 2
            elif home in  [5, 7]:
                return 3
            else:
                return 4
        elif location == 1:
            if home in [0, 2, 4]:
                return 1
            elif home in [3, 5, 7]:
                return 2
            else:
                return 3
        elif location == 2:
            if home in [1, 5]:
                return 1
            elif home in [0, 4, 8]:
                return 2
            elif home in [3, 7]:
                return 3
            else:
                return 4
        elif location == 3:
            if home in [0, 4, 6]:
                return 1
            elif home in [1, 5, 7]:
                return 2
            else:
                return 3
        elif location == 4:
            if home in [1, 3, 5, 7]:
                return 1
            else:
                return 2
        elif location == 5:
            if home in [2, 4, 8]:
                return 1
            elif home in [1, 3, 7]:
                return 2
            else:
                return 3
        elif location == 6:
            if home in [3, 7]:
                return 1
            elif home in [0, 4, 8]:
                return 2
            elif home in [1, 5]:
                return 3
            else:
                return 4
        elif location == 7:
            if home in [4, 6, 8]:
                return 1
            elif home in [1, 3, 5]:
                return 2
            else:
                return 3
        elif location == 8:
            if home in [5, 7]:
                return 1
            elif home in [2, 4, 6]:
                return 2
            elif home in [1, 3]:
                return 3
            else:
                return 4
