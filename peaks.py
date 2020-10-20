# -*- coding: utf8 -*-

# peaks.py
# Dani Suarez - suarezdanieltomas@gmail.com

# First attempt on an automatic peak finder


def find_peaks(x, y, n=50):
    abs_max_y = max(y)
    abs_max_x = x[y.index(abs_max_y)]
    abs_max = (abs_max_x, abs_max_y)
    ind = list(range(len(x)))

    loc_max = []
    for i, xi, yi in zip(ind, x, y):
        if xi == abs_max_x or i in ind[:n+1] or i in ind[-n-1:]:
            pass
        else:
            if (xi, yi) in loc_max:
                continue
            elif (yi > max(y[i-n:i]) and yi > max(y[i+1:i+n])):
                # print('\nDEBUG:', xi, yi, y[i-10:i+10], '\n')
                loc_max.append((xi, yi))
    # print('DEBUG:', loc_max)
    return abs_max, loc_max



# plt.plot(x, y)
# plt.annotate('Absolute max', (abs_max_x, abs_max + abs_max*0.01))
# for lmax in loc_max:
#     plt.annotate('Local max', (lmax[0], lmax[1] + lmax[1]*0.01))
# plt.show()

