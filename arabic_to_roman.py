"""build a function that converts arabic numbers, to roman numberals

>>> arabic_to_roman(10)
'X'

>>> arabic_to_roman(3)
'III'

>>> arabic_to_roman(8)
'VIII'

>>> arabic_to_roman(5)
'V'

>>> arabic_to_roman(20)
'XX'

>>> arabic_to_roman(16)
'XVI'

>>> arabic_to_roman(6)
'VI'

>> arabic_to_roman(21)
'XXI'


"""

def arabic_to_roman(num):

    num = int(num)
    roman = ""

    while num > 0:

        if num >= 10:
            num = num - 10
            roman += "X"

        if num >= 5 and num < 10:
            num = num - 5
            roman += "V"

        if num == 4:
            num = num - 4
            roman += "VI"

        if num > 0 and num < 4:
            num = num - 1
            roman += "I"

    return roman 






if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED.\n"