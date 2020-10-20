# -*- coding: utf8 -*-

# plot_cg.py
# Dani Suarez - suarezdanieltomas@gmail.com

import matplotlib.pyplot as plt

from fileparse import parse_csv
from peaks import find_peaks

def plot_cg(filepath, separator, title='Espectro CG', N=None):
    with open(filepath, 'rt') as f:
        data = parse_csv(f, types=[float, float],
                         has_headers=False, parse=separator.lower())
    x = [row[0] for row in data]
    y = [row[1] for row in data]
    if not N:
        abs_max, loc_max = find_peaks(x, y)
    else:
        abs_max, loc_max = find_peaks(x, y, n=int(N))
    plt.plot(x, y)
    plt.title(title)
    plt.xlabel('Tiempo (seg)')
    plt.ylabel('Intensidad')
    plt.annotate(f'{abs_max[0]:.3f}', (abs_max[0], abs_max[1] + abs_max[1]*0.01))
    for lmax in loc_max:
        plt.annotate(f'{lmax[0]:.3f}', (lmax[0], lmax[1] + lmax[1]*0.01))
    plt.show()


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 3:
        # print('DEBUG: Input:', ' '.join(sys.argv))
        print('\n' + '#'*71)
        print('Correct usage: "python plot_cg.py filepath separator title(opt) N(opt)"')
        print('#'*71)
        print(' '*60 + 'Dani Suarez\n')
    elif len(sys.argv) == 3:
        plot_cg(sys.argv[1], sys.argv[2])
    elif len(sys.argv) == 4:
        plot_cg(sys.argv[1], sys.argv[2], title=sys.argv[3])
    elif len(sys.argv) == 5:
        plot_cg(sys.argv[1], sys.argv[2], title=sys.argv[3], N=sys.argv[4])
