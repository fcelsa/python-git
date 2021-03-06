#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
year_cal.py

Copyright (c) 2019 Fabio Celsalonga
MIT License

un compatto calendario, ideale per essere utilizzato con tool tipo GeekTool
visualizza il mese precedente al corrente e quelli successivi, per il totale
impostato da numm

Changelog:
Ver. 1.3 2019-04-24 code refactoring for PEP8 compliant
Ver. 1.2 2015-10-28 fix some issue on year change
"""

import calendar
import datetime
import time
import locale

locale.setlocale(locale.LC_ALL, '')

numm = 3  # total number of month to show
now = time.localtime()
curj = now[0] if now[1] > 1 else now[0]-1
curm = now[1]-1 if now[1] > 1 else 12
ddw = 1  # always set 1st day of month to calc weeks numbers.

for i in range(numm, 0, -1):
    kw = datetime.date(curj, curm, ddw).isocalendar()[1]
    print(calendar.month_name[curm], curj, "\nW |", calendar.weekheader(2))
    m = calendar.monthcalendar(curj, curm)
    for l in m:
        line = '{:2d}|'.format(kw)
        for d in l:
            if d == now[2] and curm == now[1]:
                line += '\033[1;31m'
            line = line + (' {:2d}'.format(d) if (d > 0) else '   ')
            if d == now[2] and curm == now[1]:
                line += '\033[0m'
            if (d > 1 and
                    d < 31 and
                    datetime.date(curj, curm, d).isocalendar()[2] == 4):
                ddw = d

        print(line)

        # calcolo quale sara' la prossima settimana perche' se mi limito ad
        # incrementare kw di 1 (kw +=1) al cambio di anno ho problemi...
        nextweek = datetime.date(curj, curm, ddw) + datetime.timedelta(weeks=1)
        kw = nextweek.isocalendar()[1]

    if curm < 12:
        curm += 1
        ddw = 1
    else:
        curm = 1
        curj += 1
        ddw = 1
    if i > 1:
        print()
