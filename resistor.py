from PIL import Image, ImageDraw

import os.path

package_directory = os.path.dirname(os.path.abspath(__file__))


class Resistor:
    """
    class Resistor

    A simple class to define a resistance.

    Properties:
        resistance - the resistance value of the resistor (ex. 12000)
        tolerance - the percentage of tolerance for the resistor (0.1 or 0.05)
        code - a tuple of colors representing the resistance.
               Ex. (brown, black, red, gold)
    """
    _five_pct_standards = [(1, 0), (1, 1), (1, 2),
                           (1, 3), (1, 5), (1, 6),
                           (1, 8), (2, 0), (2, 2),
                           (2, 4), (2, 7), (3, 0),
                           (3, 3), (3, 6), (3, 9),
                           (4, 3), (4, 7), (5, 1),
                           (5, 6), (6, 2), (6, 8),
                           (8, 2), (9, 1)]

    _ten_pct_standards = [(1, 0), (1, 2), (1, 5),
                          (1, 8), (2, 2), (2, 7),
                          (3, 3), (3, 9), (4, 7),
                          (5, 6), (6, 8), (8, 2)]

    _colors = ['black', 'brown', 'red', 'orange',
               'yellow', 'green', 'blue', 'purple', 'gray', 'white']

    _tolerance_code = {0.1: 'silver', 0.05: 'gold',
                       'silver': 0.1, 'gold': 0.05}

    """ bidict for color code lookups """
    _color_code = {0: 'black',
                   1: 'brown',
                   2: 'red',
                   3: 'orange',
                   4: 'yellow',
                   5: 'green',
                   6: 'blue',
                   7: 'purple',
                   8: 'gray',
                   9: 'white',
                   -1: 'gold',
                   -2: 'silver',
                   'black': 0,
                   'brown': 1,
                   'red': 2,
                   'orange': 3,
                   'yellow': 4,
                   'green': 5,
                   'blue': 6,
                   'purple': 7,
                   'gray': 8,
                   'white': 9,
                   'gold': -1,
                   'silver': -2}

    @property
    def ten_pct_standards(self):
        return self._ten_pct_standards

    @property
    def five_pct_standards(self):
        return self._five_pct_standards

    @property
    def colors(self):
        return self._colors

    @property
    def resistance(self):
        return self._resistance

    @resistance.setter
    def resistance(self, r):
        if r < 0:
            raise ValueError('Invalid value provided for resistance')
        self._resistance = r
        r_str = str(self._resistance)

        exponent = int('{:e}'.format(self.resistance)[-3:])
        
        digits = ''
        if self.resistance >= 10:
            digits = r_str[:2]
            band_3 = self._color_code[exponent-1]
        else:
            if r_str[0] == '0':
                # check for instance where digit two is zero
                if len(r_str.split('.')[-1]) == 1:
                    r_str += '0'
                digits = r_str[2:4]
                band_3 = self._color_code[-2]
            else:
                digits = r_str[0] + r_str[2]
                band_3 = self._color_code[-1]

        band_1 = self._color_code[int(digits[0])]
        band_2 = self._color_code[int(digits[1])]
        band_4 = self._tolerance_code[self._tolerance]

        self._code = (band_1, band_2, band_3, band_4)
        self._min_resistance = self._resistance * (1-self._tolerance)
        self._max_resistance = self._resistance * (1+self._tolerance)

    @property
    def tolerance(self):
        return self._tolerance

    @tolerance.setter
    def tolerance(self, t):
        self._tolerance = t

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, code):
        if type(code) is not tuple:
            raise TypeError('Expected a tuple: ex. ("red","red","red","gold")')
        elif len(code) is not 4:
            raise ValueError('Expected tuple of colors with len(code)==4')
        else:
            self._code = code
            digits = self._color_code[code[0]]*10 + self._color_code[code[1]]
            exponent = self._color_code[code[2]]
            self.resistance = digits*10**exponent
            self.tolerance = self._tolerance_code[code[3]]

    def __init__(self, resistance=None, tolerance=None):
        self._code = None
        self._min_resistance = None
        self._max_resistance = None
        self._tolerance = tolerance or 0.05
        if resistance is not None:
            self.resistance = resistance

    def __str__(self):
        s = "R=" + str(self.resistance) + ", CODE=" + '-'.join(self.code)
        s = s + ", R_MIN=" + str(self._min_resistance)
        s = s + ", R_MAX=" + str(self._max_resistance)
        return s

    def to_image(self, filename=None):
        band_rects = {0: [(118, 6), (138, 72)],
                      1: [(153, 6), (173, 72)],
                      2: [(188, 6), (208, 72)],
                      3: [(238, 6), (258, 72)]}
        
        band_colors = {'black': '#000000',
                       'brown': '#A05A2C',
                       'red':   '#DA0000',
                       'orange': '#FF6600',
                       'yellow': '#FFCC00',
                       'green': '#008000',
                       'blue':  '#000080',
                       'purple': '#800080',
                       'gray':   '#666666',
                       'white':  '#FFFFFF',
                       'gold':   '#D4A017',
                       'silver': '#B3B3B3'}

        im = Image.open(os.path.join(package_directory, 'resbody.png'))
        draw = ImageDraw.Draw(im)
        for n, color in enumerate(self._code):
            draw.rectangle(band_rects[n], fill=band_colors[color])

        if filename:
            im.save(filename)
        else:
            im.show()
