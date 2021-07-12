# Demonstrate how to use set comprehensions


def main():
    # define a list of temperature data points
    # ctemps = [5, 10, 12, 14, 10, 23, 41, 30, 12, 24, 12, 18, 29]
    ctemps = set([5, 10, 12, 14, 10, 23, 41, 30, 12, 24, 12, 18, 29])
    
    ftemp1 = [t*9/5+32 for t in ctemps]
    print(ftemp1)
    

    # TODO: build a set of unique Fahrenheit temperatures
    ftemp2 = {t*9/5+32 for t in ctemps}
    print(ftemp2)

    # TODO: build a set from an input source
    s = 'The quick brown fox jumped over the lazy dog'
    chars = {c.upper() for c in s if not c.isspace()}
    print(chars)

    # frozenset()
    primaryColors = frozenset(['red', 'blue', "green"])
    
    lettes = set(['a', 'b', 'd'])
    lettes.add('e')
    print(lettes)

if __name__ == "__main__":
    main()