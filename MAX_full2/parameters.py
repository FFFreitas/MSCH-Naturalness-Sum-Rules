# This file was automatically created by FeynRules 2.3.29
# Mathematica version: 10.2.0 for Mac OS X x86 (64-bit) (July 7, 2015)
# Date: Fri 26 Jan 2018 14:12:54



from object_library import all_parameters, Parameter


from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot

# This is a default parameter object representing 0.
ZERO = Parameter(name = 'ZERO',
                 nature = 'internal',
                 type = 'real',
                 value = '0.0',
                 texname = '0')

# User-defined parameters.
aEWM1 = Parameter(name = 'aEWM1',
                  nature = 'external',
                  type = 'real',
                  value = 127.9,
                  texname = '\\text{aEWM1}',
                  lhablock = 'SMINPUTS',
                  lhacode = [ 1 ])

Gf = Parameter(name = 'Gf',
               nature = 'external',
               type = 'real',
               value = 0.0000116637,
               texname = 'G_f',
               lhablock = 'SMINPUTS',
               lhacode = [ 2 ])

aS = Parameter(name = 'aS',
               nature = 'external',
               type = 'real',
               value = 0.1184,
               texname = '\\alpha _s',
               lhablock = 'SMINPUTS',
               lhacode = [ 3 ])

ymb = Parameter(name = 'ymb',
                nature = 'external',
                type = 'real',
                value = 4.7,
                texname = '\\text{ymb}',
                lhablock = 'YUKAWA',
                lhacode = [ 5 ])

ymt = Parameter(name = 'ymt',
                nature = 'external',
                type = 'real',
                value = 172,
                texname = '\\text{ymt}',
                lhablock = 'YUKAWA',
                lhacode = [ 6 ])

ymtau = Parameter(name = 'ymtau',
                  nature = 'external',
                  type = 'real',
                  value = 1.777,
                  texname = '\\text{ymtau}',
                  lhablock = 'YUKAWA',
                  lhacode = [ 15 ])

wbtp = Parameter(name = 'wbtp',
                 nature = 'external',
                 type = 'real',
                 value = 0.047,
                 texname = '\\text{wbtp}',
                 lhablock = 'FRBlock',
                 lhacode = [ 1 ])

wbx2 = Parameter(name = 'wbx2',
                 nature = 'external',
                 type = 'real',
                 value = 0.0048,
                 texname = '\\text{wbx2}',
                 lhablock = 'FRBlock',
                 lhacode = [ 2 ])

wbt1 = Parameter(name = 'wbt1',
                 nature = 'external',
                 type = 'real',
                 value = 0.031,
                 texname = '\\text{wbt1}',
                 lhablock = 'FRBlock',
                 lhacode = [ 3 ])

htptp = Parameter(name = 'htptp',
                  nature = 'external',
                  type = 'real',
                  value = -0.0266597,
                  texname = '\\text{htptp}',
                  lhablock = 'FRBlock',
                  lhacode = [ 4 ])

htpx2 = Parameter(name = 'htpx2',
                  nature = 'external',
                  type = 'real',
                  value = 0.0116079,
                  texname = '\\text{htpx2}',
                  lhablock = 'FRBlock',
                  lhacode = [ 5 ])

htpt1 = Parameter(name = 'htpt1',
                  nature = 'external',
                  type = 'real',
                  value = 0.0157914,
                  texname = '\\text{htpt1}',
                  lhablock = 'FRBlock',
                  lhacode = [ 6 ])

htpt = Parameter(name = 'htpt',
                 nature = 'external',
                 type = 'real',
                 value = -0.0178567,
                 texname = '\\text{htpt}',
                 lhablock = 'FRBlock',
                 lhacode = [ 7 ])

hx2tp = Parameter(name = 'hx2tp',
                  nature = 'external',
                  type = 'real',
                  value = -0.849916,
                  texname = '\\text{hx2tp}',
                  lhablock = 'FRBlock',
                  lhacode = [ 8 ])

hx2x2 = Parameter(name = 'hx2x2',
                  nature = 'external',
                  type = 'real',
                  value = 0.143735,
                  texname = '\\text{hx2x2}',
                  lhablock = 'FRBlock',
                  lhacode = [ 9 ])

hx2t1 = Parameter(name = 'hx2t1',
                  nature = 'external',
                  type = 'real',
                  value = 0.109726,
                  texname = '\\text{hx2t1}',
                  lhablock = 'FRBlock',
                  lhacode = [ 10 ])

hx2t = Parameter(name = 'hx2t',
                 nature = 'external',
                 type = 'real',
                 value = 0.250797,
                 texname = '\\text{hx2t}',
                 lhablock = 'FRBlock',
                 lhacode = [ 11 ])

ht1tp = Parameter(name = 'ht1tp',
                  nature = 'external',
                  type = 'real',
                  value = -1.11652,
                  texname = '\\text{ht1tp}',
                  lhablock = 'FRBlock',
                  lhacode = [ 12 ])

ht1x2 = Parameter(name = 'ht1x2',
                  nature = 'external',
                  type = 'real',
                  value = 0.105959,
                  texname = '\\text{ht1x2}',
                  lhablock = 'FRBlock',
                  lhacode = [ 13 ])

ht1t1 = Parameter(name = 'ht1t1',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = '\\text{ht1t1}',
                  lhablock = 'FRBlock',
                  lhacode = [ 14 ])

ht1t = Parameter(name = 'ht1t',
                 nature = 'external',
                 type = 'real',
                 value = 0.62972,
                 texname = '\\text{ht1t}',
                 lhablock = 'FRBlock',
                 lhacode = [ 15 ])

http = Parameter(name = 'http',
                 nature = 'external',
                 type = 'real',
                 value = 0.342837,
                 texname = '\\text{http}',
                 lhablock = 'FRBlock',
                 lhacode = [ 16 ])

htx2 = Parameter(name = 'htx2',
                 nature = 'external',
                 type = 'real',
                 value = 0.0657637,
                 texname = '\\text{htx2}',
                 lhablock = 'FRBlock',
                 lhacode = [ 17 ])

htt1 = Parameter(name = 'htt1',
                 nature = 'external',
                 type = 'real',
                 value = 0.170996,
                 texname = '\\text{htt1}',
                 lhablock = 'FRBlock',
                 lhacode = [ 18 ])

htt = Parameter(name = 'htt',
                nature = 'external',
                type = 'real',
                value = 0.170996,
                texname = '\\text{htt}',
                lhablock = 'FRBlock',
                lhacode = [ 19 ])

wbpt = Parameter(name = 'wbpt',
                 nature = 'external',
                 type = 'real',
                 value = 1.,
                 texname = '\\text{wbpt}',
                 lhablock = 'FRBlock',
                 lhacode = [ 20 ])

wbptp = Parameter(name = 'wbptp',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = '\\text{wbptp}',
                  lhablock = 'FRBlock',
                  lhacode = [ 21 ])

wbpx2 = Parameter(name = 'wbpx2',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = '\\text{wbpx2}',
                  lhablock = 'FRBlock',
                  lhacode = [ 22 ])

wbpt1 = Parameter(name = 'wbpt1',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = '\\text{wbpt1}',
                  lhablock = 'FRBlock',
                  lhacode = [ 23 ])

Zttp = Parameter(name = 'Zttp',
                 nature = 'external',
                 type = 'real',
                 value = 1.,
                 texname = '\\text{Zttp}',
                 lhablock = 'FRBlock',
                 lhacode = [ 24 ])

Ztx2 = Parameter(name = 'Ztx2',
                 nature = 'external',
                 type = 'real',
                 value = 1.,
                 texname = '\\text{Ztx2}',
                 lhablock = 'FRBlock',
                 lhacode = [ 25 ])

Ztt1 = Parameter(name = 'Ztt1',
                 nature = 'external',
                 type = 'real',
                 value = 1.,
                 texname = '\\text{Ztt1}',
                 lhablock = 'FRBlock',
                 lhacode = [ 26 ])

Ztptp = Parameter(name = 'Ztptp',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = '\\text{Ztptp}',
                  lhablock = 'FRBlock',
                  lhacode = [ 27 ])

Ztpx2 = Parameter(name = 'Ztpx2',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = '\\text{Ztpx2}',
                  lhablock = 'FRBlock',
                  lhacode = [ 28 ])

Ztpt1 = Parameter(name = 'Ztpt1',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = '\\text{Ztpt1}',
                  lhablock = 'FRBlock',
                  lhacode = [ 29 ])

Zx2x2 = Parameter(name = 'Zx2x2',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = '\\text{Zx2x2}',
                  lhablock = 'FRBlock',
                  lhacode = [ 30 ])

Zx2t1 = Parameter(name = 'Zx2t1',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = '\\text{Zx2t1}',
                  lhablock = 'FRBlock',
                  lhacode = [ 31 ])

Zt1t1 = Parameter(name = 'Zt1t1',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = '\\text{Zt1t1}',
                  lhablock = 'FRBlock',
                  lhacode = [ 32 ])

att = Parameter(name = 'att',
                nature = 'external',
                type = 'real',
                value = 0.314325,
                texname = '\\text{att}',
                lhablock = 'FRBlock',
                lhacode = [ 33 ])

wbtpR = Parameter(name = 'wbtpR',
                  nature = 'external',
                  type = 'real',
                  value = 0.047,
                  texname = '\\text{wbtpR}',
                  lhablock = 'FRBlock',
                  lhacode = [ 34 ])

wbx2R = Parameter(name = 'wbx2R',
                  nature = 'external',
                  type = 'real',
                  value = 0.0048,
                  texname = '\\text{wbx2R}',
                  lhablock = 'FRBlock',
                  lhacode = [ 35 ])

wbt1R = Parameter(name = 'wbt1R',
                  nature = 'external',
                  type = 'real',
                  value = 0.031,
                  texname = '\\text{wbt1R}',
                  lhablock = 'FRBlock',
                  lhacode = [ 36 ])

wbptR = Parameter(name = 'wbptR',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = '\\text{wbptR}',
                  lhablock = 'FRBlock',
                  lhacode = [ 37 ])

wbptpR = Parameter(name = 'wbptpR',
                   nature = 'external',
                   type = 'real',
                   value = 1.,
                   texname = '\\text{wbptpR}',
                   lhablock = 'FRBlock',
                   lhacode = [ 38 ])

wbpx2R = Parameter(name = 'wbpx2R',
                   nature = 'external',
                   type = 'real',
                   value = 1.,
                   texname = '\\text{wbpx2R}',
                   lhablock = 'FRBlock',
                   lhacode = [ 39 ])

wbpt1R = Parameter(name = 'wbpt1R',
                   nature = 'external',
                   type = 'real',
                   value = 1.,
                   texname = '\\text{wbpt1R}',
                   lhablock = 'FRBlock',
                   lhacode = [ 40 ])

ZttpR = Parameter(name = 'ZttpR',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = '\\text{ZttpR}',
                  lhablock = 'FRBlock',
                  lhacode = [ 41 ])

Ztx2R = Parameter(name = 'Ztx2R',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = '\\text{Ztx2R}',
                  lhablock = 'FRBlock',
                  lhacode = [ 42 ])

Ztt1R = Parameter(name = 'Ztt1R',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = '\\text{Ztt1R}',
                  lhablock = 'FRBlock',
                  lhacode = [ 43 ])

ZtptpR = Parameter(name = 'ZtptpR',
                   nature = 'external',
                   type = 'real',
                   value = 1.,
                   texname = '\\text{ZtptpR}',
                   lhablock = 'FRBlock',
                   lhacode = [ 44 ])

Ztpx2R = Parameter(name = 'Ztpx2R',
                   nature = 'external',
                   type = 'real',
                   value = 1.,
                   texname = '\\text{Ztpx2R}',
                   lhablock = 'FRBlock',
                   lhacode = [ 45 ])

Ztpt1R = Parameter(name = 'Ztpt1R',
                   nature = 'external',
                   type = 'real',
                   value = 1.,
                   texname = '\\text{Ztpt1R}',
                   lhablock = 'FRBlock',
                   lhacode = [ 46 ])

Zx2x2R = Parameter(name = 'Zx2x2R',
                   nature = 'external',
                   type = 'real',
                   value = 1.,
                   texname = '\\text{Zx2x2R}',
                   lhablock = 'FRBlock',
                   lhacode = [ 47 ])

Zx2t1R = Parameter(name = 'Zx2t1R',
                   nature = 'external',
                   type = 'real',
                   value = 1.,
                   texname = '\\text{Zx2t1R}',
                   lhablock = 'FRBlock',
                   lhacode = [ 48 ])

Zt1t1R = Parameter(name = 'Zt1t1R',
                   nature = 'external',
                   type = 'real',
                   value = 1.,
                   texname = '\\text{Zt1t1R}',
                   lhablock = 'FRBlock',
                   lhacode = [ 49 ])

wx5tL = Parameter(name = 'wx5tL',
                  nature = 'external',
                  type = 'real',
                  value = 0.047,
                  texname = '\\text{wx5tL}',
                  lhablock = 'FRBlock',
                  lhacode = [ 50 ])

wx5tpL = Parameter(name = 'wx5tpL',
                   nature = 'external',
                   type = 'real',
                   value = 0.0048,
                   texname = '\\text{wx5tpL}',
                   lhablock = 'FRBlock',
                   lhacode = [ 51 ])

wx5x2L = Parameter(name = 'wx5x2L',
                   nature = 'external',
                   type = 'real',
                   value = 0.031,
                   texname = '\\text{wx5x2L}',
                   lhablock = 'FRBlock',
                   lhacode = [ 52 ])

wx5t1L = Parameter(name = 'wx5t1L',
                   nature = 'external',
                   type = 'real',
                   value = 0.031,
                   texname = '\\text{wx5t1L}',
                   lhablock = 'FRBlock',
                   lhacode = [ 53 ])

wx5tR = Parameter(name = 'wx5tR',
                  nature = 'external',
                  type = 'real',
                  value = 0.047,
                  texname = '\\text{wx5tR}',
                  lhablock = 'FRBlock',
                  lhacode = [ 54 ])

wx5tpR = Parameter(name = 'wx5tpR',
                   nature = 'external',
                   type = 'real',
                   value = 0.0048,
                   texname = '\\text{wx5tpR}',
                   lhablock = 'FRBlock',
                   lhacode = [ 55 ])

wx5x2R = Parameter(name = 'wx5x2R',
                   nature = 'external',
                   type = 'real',
                   value = 0.031,
                   texname = '\\text{wx5x2R}',
                   lhablock = 'FRBlock',
                   lhacode = [ 56 ])

wx5t1R = Parameter(name = 'wx5t1R',
                   nature = 'external',
                   type = 'real',
                   value = 0.031,
                   texname = '\\text{wx5t1R}',
                   lhablock = 'FRBlock',
                   lhacode = [ 57 ])

MZ = Parameter(name = 'MZ',
               nature = 'external',
               type = 'real',
               value = 91.1876,
               texname = '\\text{MZ}',
               lhablock = 'MASS',
               lhacode = [ 23 ])

MTA = Parameter(name = 'MTA',
                nature = 'external',
                type = 'real',
                value = 1.777,
                texname = '\\text{MTA}',
                lhablock = 'MASS',
                lhacode = [ 15 ])

MT = Parameter(name = 'MT',
               nature = 'external',
               type = 'real',
               value = 172,
               texname = '\\text{MT}',
               lhablock = 'MASS',
               lhacode = [ 6 ])

MB = Parameter(name = 'MB',
               nature = 'external',
               type = 'real',
               value = 4.7,
               texname = '\\text{MB}',
               lhablock = 'MASS',
               lhacode = [ 5 ])

MH = Parameter(name = 'MH',
               nature = 'external',
               type = 'real',
               value = 125,
               texname = '\\text{MH}',
               lhablock = 'MASS',
               lhacode = [ 25 ])

MTP = Parameter(name = 'MTP',
                nature = 'external',
                type = 'real',
                value = 1800,
                texname = '\\text{MTP}',
                lhablock = 'MASS',
                lhacode = [ 6000002 ])

MXTWO = Parameter(name = 'MXTWO',
                  nature = 'external',
                  type = 'real',
                  value = 1300,
                  texname = '\\text{MXTWO}',
                  lhablock = 'MASS',
                  lhacode = [ 6000004 ])

MTONE = Parameter(name = 'MTONE',
                  nature = 'external',
                  type = 'real',
                  value = 800,
                  texname = '\\text{MTONE}',
                  lhablock = 'MASS',
                  lhacode = [ 6000006 ])

MBP = Parameter(name = 'MBP',
                nature = 'external',
                type = 'real',
                value = 1750,
                texname = '\\text{MBP}',
                lhablock = 'MASS',
                lhacode = [ 6000001 ])

Mx5 = Parameter(name = 'Mx5',
                nature = 'external',
                type = 'real',
                value = 800,
                texname = '\\text{Mx5}',
                lhablock = 'MASS',
                lhacode = [ 7000001 ])

WZ = Parameter(name = 'WZ',
               nature = 'external',
               type = 'real',
               value = 2.4952,
               texname = '\\text{WZ}',
               lhablock = 'DECAY',
               lhacode = [ 23 ])

WW = Parameter(name = 'WW',
               nature = 'external',
               type = 'real',
               value = 2.085,
               texname = '\\text{WW}',
               lhablock = 'DECAY',
               lhacode = [ 24 ])

WT = Parameter(name = 'WT',
               nature = 'external',
               type = 'real',
               value = 1.50833649,
               texname = '\\text{WT}',
               lhablock = 'DECAY',
               lhacode = [ 6 ])

WH = Parameter(name = 'WH',
               nature = 'external',
               type = 'real',
               value = 0.00407,
               texname = '\\text{WH}',
               lhablock = 'DECAY',
               lhacode = [ 25 ])

WTP = Parameter(name = 'WTP',
                nature = 'external',
                type = 'real',
                value = 1.,
                texname = '\\text{WTP}',
                lhablock = 'DECAY',
                lhacode = [ 6000002 ])

WXTWO = Parameter(name = 'WXTWO',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = '\\text{WXTWO}',
                  lhablock = 'DECAY',
                  lhacode = [ 6000004 ])

WTONE = Parameter(name = 'WTONE',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = '\\text{WTONE}',
                  lhablock = 'DECAY',
                  lhacode = [ 6000006 ])

WBP = Parameter(name = 'WBP',
                nature = 'external',
                type = 'real',
                value = 1,
                texname = '\\text{WBP}',
                lhablock = 'DECAY',
                lhacode = [ 6000001 ])

Wx5 = Parameter(name = 'Wx5',
                nature = 'external',
                type = 'real',
                value = 1,
                texname = '\\text{Wx5}',
                lhablock = 'DECAY',
                lhacode = [ 7000001 ])

aEW = Parameter(name = 'aEW',
                nature = 'internal',
                type = 'real',
                value = '1/aEWM1',
                texname = '\\alpha _{\\text{EW}}')

G = Parameter(name = 'G',
              nature = 'internal',
              type = 'real',
              value = '2*cmath.sqrt(aS)*cmath.sqrt(cmath.pi)',
              texname = 'G')

htt2 = Parameter(name = 'htt2',
                 nature = 'internal',
                 type = 'real',
                 value = '1.',
                 texname = '\\text{htt2}')

MW = Parameter(name = 'MW',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(MZ**2/2. + cmath.sqrt(MZ**4/4. - (aEW*cmath.pi*MZ**2)/(Gf*cmath.sqrt(2))))',
               texname = 'M_W')

ee = Parameter(name = 'ee',
               nature = 'internal',
               type = 'real',
               value = '2*cmath.sqrt(aEW)*cmath.sqrt(cmath.pi)',
               texname = 'e')

sw2 = Parameter(name = 'sw2',
                nature = 'internal',
                type = 'real',
                value = '1 - MW**2/MZ**2',
                texname = '\\text{sw2}')

cw = Parameter(name = 'cw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(1 - sw2)',
               texname = 'c_w')

sw = Parameter(name = 'sw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(sw2)',
               texname = 's_w')

g1 = Parameter(name = 'g1',
               nature = 'internal',
               type = 'real',
               value = 'ee/cw',
               texname = 'g_1')

gw = Parameter(name = 'gw',
               nature = 'internal',
               type = 'real',
               value = 'ee/sw',
               texname = 'g_w')

vev = Parameter(name = 'vev',
                nature = 'internal',
                type = 'real',
                value = '(2*MW*sw)/ee',
                texname = '\\text{vev}')

lam = Parameter(name = 'lam',
                nature = 'internal',
                type = 'real',
                value = 'MH**2/(2.*vev**2)',
                texname = '\\text{lam}')

yb = Parameter(name = 'yb',
               nature = 'internal',
               type = 'real',
               value = '(ymb*cmath.sqrt(2))/vev',
               texname = '\\text{yb}')

yt = Parameter(name = 'yt',
               nature = 'internal',
               type = 'real',
               value = '(ymt*cmath.sqrt(2))/vev',
               texname = '\\text{yt}')

ytau = Parameter(name = 'ytau',
                 nature = 'internal',
                 type = 'real',
                 value = '(ymtau*cmath.sqrt(2))/vev',
                 texname = '\\text{ytau}')

muH = Parameter(name = 'muH',
                nature = 'internal',
                type = 'real',
                value = 'cmath.sqrt(lam*vev**2)',
                texname = '\\mu')

I1a33 = Parameter(name = 'I1a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yb',
                  texname = '\\text{I1a33}')

I2a33 = Parameter(name = 'I2a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yt',
                  texname = '\\text{I2a33}')

I3a33 = Parameter(name = 'I3a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yt',
                  texname = '\\text{I3a33}')

I4a33 = Parameter(name = 'I4a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yb',
                  texname = '\\text{I4a33}')

