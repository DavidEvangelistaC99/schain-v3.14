import numpy

def esffit(esf,year,doy,index):
  esf = 0
  if year == 2026 and doy == 56 :
    if index >= 250 and index <= 254 : esf = 1
  return esf
  
def weightfit(w,year,doy,index,h,beam):
  if len(w) <= 0 : return w
  
  return w                
  
def Vrfit(p0,year,doy,index,h,beam):

# ISR mayo 2026
    if year == 2026 and doy == 151:
     if beam == 0 :
      if index == 26 and h >= 9 : p0[3]=-20
     if beam == 1 :
      if index == 26 and h >= 9 : p0[3]=-15
    if year == 2026 and doy == 147:
     if beam == 0 :
      if index == 49 and h >= 9 : p0[3]=11
      if index == 49 and h == 20 : p0[3]=numpy.nan
     if beam == 1 :
      if index == 49 and h >= 9 : p0[3]=5
      if index == 49 and h == 18 : p0[3]=0

# MP mayo 2026
#    if year == 2026 and doy == 145:
#     if beam == 0 :
#      if index == 13 and h >= 9 : p0[3]=-25
#     if beam == 1 :
#      if index == 15 and h >= 9 : p0[3]=-26

    if year == 2026 and doy == 145: #25
     if beam == 0 :
      if index == 26 and h >= 9 : p0[3]=-45
      if index == 28 and h >= 9 : p0[3]=-25
      if index == 32 and h >= 9 : p0[3]=-25
      if index == 35 and h >= 9 : p0[3]=-20
      if index == 38 and h >= 9 : p0[3]=-25
      if index == 41 and h >= 9 : p0[3]=-30
      if index == 43 and h >= 9 : p0[3]=-30
      if index == 44 and h >= 9 : p0[3]=-20
      if index == 67 and h >= 9 : p0[3]=5	
      if index == 68 and h >= 9 : p0[3]=10
      if index == 71 and h >= 9 : p0[3]=5
      if index == 72 and h >= 9 : p0[3]=0
      if index == 76 and h >= 9 : p0[3]=-1
     if beam == 1 :
      if index == 18 and h >= 9 : p0[3]=-20
      if index == 26 and h >= 9 : p0[3]=-35
      if index == 27 and h >= 9 : p0[3]=-20
      if index >= 28 and index <= 33 and h >= 9 : p0[3]=-15
      if index >= 34 and index <= 37 and h >= 9 : p0[3]=-10
      if index >= 42 and index <= 43 and h >= 9 : p0[3]=-20
      if index == 44 and h >= 9 : p0[3]=-10
      if index == 46 and h >= 9 : p0[3]=-20
      if index == 47 and h >= 9 : p0[3]=-25
      if index == 48 and h >= 9 : p0[3]=-20
      if index == 53 and h >= 9 : p0[3]=-30
      if index == 54 and h >= 9 : p0[3]=-15
      if index == 56 and h >= 9 : p0[3]=-20
      if index >= 63 and index <= 64 and h >= 9 : p0[3]=5
      if index == 70 and h >= 27 : p0[3]=20
      if index >= 72 and index <= 73 and h >= 9 : p0[3]=0
      if index == 74 and h >= 9 : p0[3]=-15
      if index == 75 and h >= 9 : p0[3]=-1

    if year == 2026 and doy == 144:
     if beam == 0 :
      if index == 0 and h >= 9 : p0[3]=-25
      if index == 25 and h >= 9 : p0[3]=-25
      if index >= 28 and index <= 38 and h >= 9 : p0[3]=-25
      if index == 31 and h >= 9 : p0[3]=-20
      if index == 33 and h >= 9 : p0[3]=-30
      if index == 37 and h >= 9 : p0[3]=-20
      if index == 40 and h >= 9 : p0[3]=-25
      if index == 41 and h >= 9 : p0[3]=-20
      if index == 44 and h >= 9 : p0[3]=-20
      if index >= 46 and index <= 48 and h >= 9 : p0[3]=-25
      if index == 50 and h >= 9 : p0[3]=-15
      if index == 58 and h >= 9 : p0[3]=-25
      if index == 59 and h >= 9 : p0[3]=-20
      if index == 60 and h >= 9 : p0[3]=-15
      if index == 62 and h >= 9 : p0[3]=-15
      if index == 64 and h >= 9 : p0[3]=-20
      if index == 66 and h >= 9 : p0[3]=-10
      if index == 67 and h >= 9 : p0[3]=-25
      if index == 69 and h >= 9 : p0[3]=-20
      if index == 70 and h >= 9 : p0[3]=-10
      if index == 71 and h >= 9 : p0[3]=-15
      if index == 72 and h >= 9 : p0[3]=-10
      if index >= 73 and index <= 74 and h >= 9 : p0[3]=0
      if index == 76 and h >= 9 : p0[3]=0
      if index == 243 and h >= 9 : p0[3]=-5
      if index == 246 and h >= 9 : p0[3]=-7
      if index == 247 and h >= 9 : p0[3]=-10
     if beam == 1 :
      if index == 18 and h >= 9 : p0[3]=-20
      if index == 19 and h >= 9 : p0[3]=-20
      if index == 21 and h >= 9 : p0[3]=-10
      if index == 22 and h >= 9 : p0[3]=-16
      if index >= 25 and index <= 30 and h >= 9 : p0[3]=-15
      if index == 31 and h >= 9 : p0[3]=-10
      if index == 34 and h >= 9 : p0[3]=-20
      if index == 35 and h >= 9 : p0[3]=-18
      if index == 36 and h >= 9 : p0[3]=-20
      if index == 37 and h >= 9 : p0[3]=-10
      if index >= 38 and index <= 41 and h >= 9 : p0[3]=-15
      if index >= 42 and index <= 44 and h >= 9 : p0[3]=-10
      if index >= 47 and index <= 48 and h >= 9 : p0[3]=-15
      if index == 49 and h >= 9 : p0[3]=-10
      if index == 50 and h >= 9 : p0[3]=-5
      if index == 53 and h >= 9 : p0[3]=-10
      if index == 56 and h >= 9 : p0[3]=-20
      if index == 57 and h >= 9 : p0[3]=-15
      if index == 58 and h >= 9 : p0[3]=-20
      if index == 59 and h >= 9 : p0[3]=-15
      if index >= 60 and index <= 64 and h >= 9 : p0[3]=-10
      if index == 66 and h >= 9 : p0[3]=-1
      if index == 67 and h >= 9 : p0[3]=-20
      if index == 68 and h >= 9 : p0[3]=-15
      if index == 69 and h >= 9 : p0[3]=-15
      if index == 70 and h >= 9 : p0[3]=-5
      if index == 71 and h >= 9 : p0[3]=-10
      if index == 72 and h >= 9 : p0[3]=-5
      if index == 73 and h >= 9 : p0[3]=5
      if index == 75 and h >= 9 : p0[3]=0
      if index == 234 and h >= 30 : p0[3]=15
      if index == 243 and h >= 9 : p0[3]=3
      if index == 246 and h >= 9 : p0[3]=-1
      if index == 248 and h >= 9 : p0[3]=-1
      if index == 267 and h >= 9 : p0[3]=-15
      if index == 268 and h >= 9 : p0[3]=-13

    if year == 2026 and doy == 143:
     if beam == 0 :
      if index == 18 and h >= 9 : p0[3]=-25
      if index == 19 and h >= 9 : p0[3]=-28
      if index == 20 and h >= 9 : p0[3]=-25
      if index == 23 and h >= 9 : p0[3]=-30
      if index == 24 and h >= 9 : p0[3]=-25
      if index >= 28 and index <= 33 and h >= 9 : p0[3]=-20
      if index == 32 and h >= 9 : p0[3]=-25
      if index >= 34 and index <= 35 and h >= 9 : p0[3]=-15
      if index == 36 and h >= 9 : p0[3]=-20
      if index >= 37 and index <= 39 and h >= 9 : p0[3]=-25
      if index == 41 and h >= 9 : p0[3]=-20
      if index == 46 and h >= 9 : p0[3]=-20
      if index == 48 and h >= 9 : p0[3]=-20
      if index == 53 and h >= 9 : p0[3]=-20
      if index == 57 and h >= 9 : p0[3]=-15
      if index == 59 and h >= 9 : p0[3]=-20
      if index == 61 and h >= 9 : p0[3]=-20
      if index >= 64 and index <= 65 and h >= 9 : p0[3]=-15
      if index == 75 and h >= 9 : p0[3]=-1
      if index == 79 and h >= 9 : p0[3]=1
      if index == 83 and h >= 21 : p0[3]=2
      if index == 168 and h >= 9 : p0[3]=11
      if index == 224 and h >= 9 : p0[3]=-5
      if index == 243 and h >= 9 : p0[3]=-15
     if beam == 1 :
      if index >= 3 and index <= 4 and h >= 20 : p0[3]=-15
      if index == 20 and h >= 9 : p0[3]=-15
      if index == 21 and h >= 9 : p0[3]=-25
      if index == 22 and h >= 9 : p0[3]=-15
      if index == 23 and h >= 9 : p0[3]=-20
      if index >= 24 and index <= 25 and h >= 9 : p0[3]=-15
      if index >= 26 and index <= 33 and h >= 9 : p0[3]=-10
      if index == 32 and h >= 9 : p0[3]=-15
      if index >= 34 and index <= 35 and h >= 9 : p0[3]=-5
      if index == 36 and h >= 9 : p0[3]=-10
      if index >= 37 and index <= 40 and h >= 9 : p0[3]=-20
      if index >= 41 and index <= 50 and h >= 9 : p0[3]=-10
      if index == 52 and h >= 9 : p0[3]=-1
      if index == 54 and h >= 9 : p0[3]=0
      if index == 55 and h >= 9 : p0[3]=-5
      if index >= 57 and index <= 58 and h >= 9 : p0[3]=-10
      if index == 61 and h >= 9 : p0[3]=-10
      if index == 62 and h >= 9 : p0[3]=-5
      if index >= 64 and index <= 65 and h >= 9 : p0[3]=-10
      if index == 67 and h >= 9 : p0[3]=-10
      if index >= 69 and index <= 70 and h >= 9 : p0[3]=0
      if index == 71 and h >= 9 : p0[3]=-3
      if index == 72 and h >= 9 : p0[3]=0
      if index == 74 and h >= 9 : p0[3]=0
      if index == 75 and h >= 9 : p0[3]=2
      if index == 154 and h >= 9 : p0[3]=11
      if index == 158 and h >= 27 : p0[3]=10
      if index == 221 and h >= 9 : p0[3]=5
      if index == 226 and h >= 9 : p0[3]=-2
      if index == 239 and h >= 9 : p0[3]=-5
      if index == 249 and h >= 9 : p0[3]=-5
      if index == 260 and h >= 27 : p0[3]=-15

    if year == 2026 and doy == 142:
     if beam == 0 :
      if index == 4 and h >= 9 : p0[3]=-22
      if index >= 23 and index <= 24 and h >= 9 : p0[3]=-15
      if index == 26 and h >= 9 : p0[3]=-15
      if index == 29 and h >= 9 : p0[3]=-20
      if index == 30 and h >= 9 : p0[3]=-15
      if index == 43 and h >= 9 : p0[3]=-20
      if index == 54 and h >= 9 : p0[3]=-12
      if index == 55 and h >= 9 : p0[3]=-10
      if index == 57 and h >= 9 : p0[3]=-16
      if index == 63 and h >= 9 : p0[3]=-23
      if index == 64 and h >= 9 : p0[3]=-20
      if index == 65 and h >= 9 : p0[3]=-22
      if index == 66 and h >= 9 : p0[3]=-15
      if index == 70 and h >= 9 : p0[3]=-10
      if index == 73 and h >= 9 : p0[3]=-5
     if beam == 1 :
      if index == 9 and h >= 9 : p0[3]=-15
      if index == 23 and h >= 9 : p0[3]=-5
      if index >= 25 and index <= 26 and h >= 9 : p0[3]=-5
      if index >= 27 and index <= 29 and h >= 9 : p0[3]=-10
      if index == 30 and h >= 9 : p0[3]=-5
      if index == 31 and h >= 9 : p0[3]=-2
      if index == 32 and h >= 9 : p0[3]=0
      if index == 33 and h >= 9 : p0[3]=2
      if index == 34 and h >= 9 : p0[3]=3
      if index == 35 and h >= 9 : p0[3]=0
      if index == 36 and h >= 9 : p0[3]=5
      if index == 37 and h >= 9 : p0[3]=0
      if index >= 38 and index <= 39 and h >= 9 : p0[3]=-5
      if index >= 40 and index <= 45 and h >= 9 : p0[3]=-10
      if index == 48 and h >= 9 : p0[3]=-5
      if index == 53 and h >= 9 : p0[3]=-5
      if index == 55 and h >= 9 : p0[3]=-5
      if index == 58 and h >= 9 : p0[3]=-10
      if index == 59 and h >= 9 : p0[3]=-14
      if index == 62 and h >= 9 : p0[3]=-18
      if index == 63 and h >= 9 : p0[3]=-20
      if index == 64 and h >= 9 : p0[3]=-16
      if index == 66 and h >= 9 : p0[3]=-10
      if index >= 70 and index <= 71 and h >= 9 : p0[3]=-5
      if index == 72 and h >= 9 : p0[3]=-2
      if index == 75 and h >= 9 : p0[3]=8
      if index == 97 and h >= 22 : p0[3]=15
      if index == 224 and h >= 9 : p0[3]=3

    if year == 2026 and doy == 141:
     if beam == 0 :
      if index == 24 and h >= 9 : p0[3]=-25
      if index == 26 and h >= 9 : p0[3]=-25
      if index == 27 and h >= 9 : p0[3]=-30
      if index == 29 and h >= 9 : p0[3]=-30
      if index == 31 and h >= 9 : p0[3]=-30
      if index == 33 and h >= 9 : p0[3]=-20
      if index >= 34 and index <= 38 and h >= 9 : p0[3]=-25
      if index == 37 and h >= 9 : p0[3]=-20
      if index == 39 and h >= 9 : p0[3]=-5
      if index >= 40 and index <= 42 and h >= 9 : p0[3]=-10
      if index >= 43 and index <= 47 and h >= 9 : p0[3]=-15
      if index >= 49 and index <= 50 and h >= 9 : p0[3]=-10
      if index >= 51 and index <= 53 and h >= 9 : p0[3]=-15
      if index == 57 and h >= 9 : p0[3]=-13
      if index == 68 and h >= 9 : p0[3]=-8
      if index == 73 and h >= 9 : p0[3]=-18
      if index == 205 and h >= 9 : p0[3]=5
      if index == 224 and h >= 27 : p0[3]=-3
     if beam == 1 :
      if index == 20 and h >= 9 : p0[3]=-10
      if index == 21 and h >= 9 : p0[3]=-15
      if index >= 23 and index <= 24 and h >= 9 : p0[3]=-20
      if index == 26 and h >= 9 : p0[3]=-20
      if index == 27 and h >= 9 : p0[3]=-25
      if index == 28 and h >= 9 : p0[3]=-20
      if index == 29 and h >= 9 : p0[3]=-25
      if index == 30 and h >= 9 : p0[3]=-17
      if index >= 32 and index <= 33 and h >= 9 : p0[3]=-15
      if index >= 34 and index <= 38 and h >= 9 : p0[3]=-20
      if index == 37 and h >= 9 : p0[3]=-15
      if index == 39 and h >= 9 : p0[3]=0
      if index >= 40 and index <= 42 and h >= 9 : p0[3]=-5
      if index >= 43 and index <= 47 and h >= 9 : p0[3]=-10
      if index >= 48 and index <= 52 and h >= 9 : p0[3]=-5
      if index >= 53 and index <= 54 and h >= 9 : p0[3]=-10
      if index == 56 and h >= 9 : p0[3]=-10
      if index == 59 and h >= 9 : p0[3]=-5
      if index == 60 and h >= 9 : p0[3]=-8
      if index >= 61 and index <= 62 and h >= 9 : p0[3]=-10
      if index == 63 and h >= 9 : p0[3]=-4
      if index == 66 and h >= 9 : p0[3]=5
      if index == 71 and h >= 9 : p0[3]=-8
      if index == 72 and h >= 9 : p0[3]=-12
      if index == 73 and h >= 9 : p0[3]=-15
      if index == 232 and h >= 9 : p0[3]=3
      if index == 269 and h >= 24 : p0[3]=-15

    if year == 2026 and doy == 140:
     if beam == 0 :
      if index == 22 and h >= 9 : p0[3]=-28
      if index == 23 and h >= 9 : p0[3]=-18
      if index == 28 and h >= 9 : p0[3]=-17
      if index >= 33 and index <= 37 and h >= 9 : p0[3]=-15
      if index == 35 and h >= 9 : p0[3]=-10
      if index >= 42 and index <= 46 and h >= 9 : p0[3]=-10
      if index == 52 and h >= 9 : p0[3]=-20
      if index == 59 and h >= 9 : p0[3]=-15
      if index == 60 and h >= 9 : p0[3]=-19
      if index == 61 and h >= 9 : p0[3]=-18
      if index == 68 and h >= 9 : p0[3]=-18
      if index == 72 and h >= 9 : p0[3]=-20
      if index == 73 and h >= 9 : p0[3]=-18
      if index == 224 and h >= 9 : p0[3]=5
      if index == 253 and h >= 9 : p0[3]=-15
      if index == 254 and h >= 9 : p0[3]=-10
      if index == 255 and h >= 9 : p0[3]=-13
      if index == 261 and h >= 9 : p0[3]=-17
      if index == 269 and h >= 9 : p0[3]=-15
     if beam == 1 :
      if index == 7 and h >= 9 : p0[3]=-10
      if index == 13 and h >= 22 : p0[3]=-10
      if index == 17 and h >= 9 : p0[3]=-10
      if index == 19 and h >= 9 : p0[3]=-5
      if index >= 20 and index <= 21 and h >= 9 : p0[3]=-5
      if index == 23 and h >= 9 : p0[3]=-13
      if index >= 24 and index <= 28 and h >= 9 : p0[3]=-10
      if index == 29 and h >= 9 : p0[3]=-5
      if index >= 30 and index <= 38 and h >= 9 : p0[3]=-10
      if index == 35 and h >= 9 : p0[3]=0
      if index == 39 and h >= 9 : p0[3]=-5
      if index == 40 and h >= 9 : p0[3]=2
      if index == 41 and h >= 9 : p0[3]=-5
      if index >= 42 and index <= 49 and h >= 9 : p0[3]=-5
      if index == 50 and h >= 9 : p0[3]=-15
      if index >= 53 and index <= 56 and h >= 9 : p0[3]=-10
      if index >= 58 and index <= 59 and h >= 9 : p0[3]=-10
      if index == 62 and h >= 9 : p0[3]=-10
      if index >= 64 and index <= 66 and h >= 9 : p0[3]=-7
      if index == 75 and h >= 9 : p0[3]=-10
      if index == 78 and h >= 9 : p0[3]=-10
      if index == 223 and h >= 9 : p0[3]=18
      if index == 224 and h >= 9 : p0[3]=10
      if index == 228 and h >= 9 : p0[3]=20
      if index == 234 and h >= 9 : p0[3]=5
      if index == 237 and h >= 9 : p0[3]=2
      if index == 238 and h >= 9 : p0[3]=3
      if index == 240 and h >= 9 : p0[3]=0
      if index == 246 and h >= 9 : p0[3]=0
      if index == 247 and h >= 9 : p0[3]=-1
      if index == 254 and h >= 9 : p0[3]=-1
      if index == 261 and h >= 9 : p0[3]=-10
      if index >= 265 and index <= 268 and h >= 9 : p0[3]=-10
      if index == 270 and h >= 9 : p0[3]=-10
      if index == 271 and h >= 9 : p0[3]=-15

    if year == 2026 and doy == 139:
     if beam == 0 :
      if index == 28 and h >= 9 : p0[3]=-35
      if index == 33 and h >= 9 : p0[3]=-25
      if index == 34 and h >= 9 : p0[3]=-35
      if index == 36 and h >= 9 : p0[3]=-40
      if index >= 37 and index <= 44 and h >= 9 : p0[3]=-30
      if index >= 45 and index <= 46 and h >= 9 : p0[3]=-25
      if index >= 49 and index <= 51 and h >= 9 : p0[3]=-35
      if index == 52 and h >= 9 : p0[3]=-40
      if index == 53 and h >= 9 : p0[3]=-30
      if index >= 54 and index <= 55 and h >= 9 : p0[3]=-35
      if index == 57 and h >= 9 : p0[3]=-25
      if index == 60 and h >= 9 : p0[3]=-25
      if index >= 61 and index <= 62 and h >= 9 : p0[3]=-15
      if index == 63 and h >= 9 : p0[3]=-25
      if index >= 66 and index <= 67 and h >= 9 : p0[3]=-10
      if index >= 68 and index <= 69 and h >= 9 : p0[3]=-5
      if index == 70 and h >= 9 : p0[3]=-10
      if index >= 71 and index <= 72 and h >= 9 : p0[3]=-20
      if index == 74 and h >= 9 : p0[3]=-20
      if index == 76 and h >= 9 : p0[3]=-16
      if index == 224 and h >= 9 : p0[3]=-5
      if index == 229 and h >= 27 : p0[3]=-2
      if index == 232 and h >= 9 : p0[3]=-5
      if index == 238 and h >= 9 : p0[3]=0
      if index == 245 and h >= 9 : p0[3]=5
      if index == 248 and h >= 9 : p0[3]=0
      if index == 250 and h >= 9 : p0[3]=-5
      if index == 252 and h >= 9 : p0[3]=-10
      if index == 253 and h >= 9 : p0[3]=-10
      if index == 258 and h >= 9 : p0[3]=-20
      if index == 260 and h >= 9 : p0[3]=-15
      if index == 262 and h >= 9 : p0[3]=-15
      if index == 266 and h >= 9 : p0[3]=-15
      if index == 267 and h >= 9 : p0[3]=-18
      if index == 272 and h >= 9 : p0[3]=-15
      if index == 286 and h >= 9 : p0[3]=-25
     if beam == 1 :
      if index == 18 and h >= 9 : p0[3]=-15
      if index == 21 and h >= 9 : p0[3]=-25
      if index == 22 and h >= 9 : p0[3]=-18
      if index == 25 and h >= 9 : p0[3]=-20
      if index == 27 and h >= 9 : p0[3]=-30
      if index == 28 and h >= 9 : p0[3]=-30
      if index == 31 and h >= 9 : p0[3]=-18
      if index == 32 and h >= 9 : p0[3]=-15
      if index == 33 and h >= 9 : p0[3]=-20
      if index == 34 and h >= 9 : p0[3]=-30
      if index >= 35 and index <= 36 and h >= 9 : p0[3]=-35
      if index >= 37 and index <= 44 and h >= 9 : p0[3]=-25
      if index >= 45 and index <= 46 and h >= 9 : p0[3]=-20
      if index >= 49 and index <= 51 and h >= 9 : p0[3]=-30
      if index == 52 and h >= 9 : p0[3]=-35
      if index == 53 and h >= 9 : p0[3]=-25
      if index >= 54 and index <= 56 and h >= 9 : p0[3]=-30
      if index == 57 and h >= 9 : p0[3]=-20
      if index == 60 and h >= 9 : p0[3]=-20
      if index >= 61 and index <= 62 and h >= 9 : p0[3]=-10
      if index == 63 and h >= 9 : p0[3]=-20
      if index >= 66 and index <= 67 and h >= 9 : p0[3]=-5
      if index >= 68 and index <= 69 and h >= 9 : p0[3]=0    
      if index == 70 and h >= 9 : p0[3]=-5
      if index == 71 and h >= 9 : p0[3]=-15
      if index == 72 and h >= 9 : p0[3]=-20
      if index == 73 and h >= 9 : p0[3]=-10
      if index == 74 and h >= 9 : p0[3]=-15
      if index == 75 and h >= 9 : p0[3]=-10
      if index == 81 and h >= 9 : p0[3]=-5
      if index == 91 and h >= 19 : p0[3]=-7
      if index == 96 and h >= 19 : p0[3]=0
      if index == 232 and h >= 9 : p0[3]=0
      if index == 234 and h >= 9 : p0[3]=5
      if index == 239 and h >= 9 : p0[3]=3
      if index == 245 and h >= 9 : p0[3]=12
      if index >= 246 and index <= 247 and h >= 9 : p0[3]=10
      if index >= 248 and index <= 249 and h >= 9 : p0[3]=2
      if index == 250 and h >= 9 : p0[3]=0
      if index == 252 and h >= 9 : p0[3]=0
      if index >= 253 and index <= 254 and h >= 9 : p0[3]=-5
      if index == 265 and h >= 9 : p0[3]=-5
      if index == 266 and h >= 9 : p0[3]=-8
      if index == 272 and h >= 9 : p0[3]=-10
      if index == 280 and h >= 9 : p0[3]=-7
      if index == 281 and h >= 9 : p0[3]=-10

    if year == 2026 and doy == 138:
     if beam == 0 :
      if index == 25 and h >= 9 : p0[3]=-20
      if index == 27 and h >= 9 : p0[3]=-20
      if index == 28 and h >= 9 : p0[3]=-15
      if index >= 33 and index <= 35 and h >= 9 : p0[3]=-20
      if index >= 36 and index <= 37 and h >= 9 : p0[3]=-15
      if index == 39 and h >= 9 : p0[3]=-10
      if index == 40 and h >= 9 : p0[3]=-5
      if index == 41 and h >= 9 : p0[3]=-10
      if index == 44 and h >= 9 : p0[3]=-10
      if index >= 45 and index <= 46 and h >= 9 : p0[3]=-15
      if index >= 48 and index <= 49 and h >= 9 : p0[3]=-10
      if index >= 50 and index <= 51 and h >= 9 : p0[3]=-5
      if index == 52 and h >= 9 : p0[3]=-15
      if index >= 53 and index <= 56 and h >= 9 : p0[3]=-10
      if index == 58 and h >= 9 : p0[3]=-10
      if index == 61 and h >= 9 : p0[3]=-10
      if index == 64 and h >= 9 : p0[3]=-10
      if index == 73 and h >= 9 : p0[3]=-10
      if index == 74 and h >= 9 : p0[3]=-5
      if index == 78 and h >= 9 : p0[3]=0
      if index == 257 and h >= 9 : p0[3]=-5
     if beam == 1 :
      if index == 19 and h >= 9 : p0[3]=-10
      if index >= 21 and index <= 22 and h >= 9 : p0[3]=-10
      if index == 27 and h >= 9 : p0[3]=-10
      if index == 28 and h >= 9 : p0[3]=-7
      if index >= 29 and index <= 30 and h >= 9 : p0[3]=-5
      if index >= 31 and index <= 35 and h >= 9 : p0[3]=-10
      if index >= 36 and index <= 37 and h >= 9 : p0[3]=-5
      if index >= 38 and index <= 39 and h >= 9 : p0[3]=-2
      if index == 40 and h >= 9 : p0[3]=5
      if index == 41 and h >= 9 : p0[3]=0
      if index == 42 and h >= 9 : p0[3]=-5
      if index == 43 and h >= 9 : p0[3]=-15
      if index == 44 and h >= 9 : p0[3]=-5
      if index >= 45 and index <= 46 and h >= 9 : p0[3]=-10
      if index == 47 and h >= 9 : p0[3]=0
      if index == 48 and h >= 9 : p0[3]=-5
      if index >= 50 and index <= 51 and h >= 9 : p0[3]=0
      if index == 52 and h >= 9 : p0[3]=-10
      if index >= 53 and index <= 58 and h >= 9 : p0[3]=-5
      if index == 59 and h >= 9 : p0[3]=0
      if index >= 61 and index <= 62 and h >= 9 : p0[3]=-5
      if index == 64 and h >= 9 : p0[3]=-5
      if index == 68 and h >= 9 : p0[3]=3
      if index >= 69 and index <= 71 and h >= 9 : p0[3]=0
      if index == 72 and h >= 9 : p0[3]=-5
      if index == 73 and h >= 9 : p0[3]=-10
      if index == 76 and h >= 9 : p0[3]=0
      if index >= 78 and index <= 79 and h >= 9 : p0[3]=0
      if index == 256 and h >= 9 : p0[3]=1
      if index >= 257 and index <= 258 and h >= 9 : p0[3]=0
      if index == 259 and h >= 9 : p0[3]=-5
      if index == 260 and h >= 9 : p0[3]=-2

    if year == 2026 and doy == 137:
     if beam == 0 :
      if index == 4 and h <= 18 : p0[3]=-25
      if index == 28 and h >= 9 : p0[3]=-8
      if index == 37 and h >= 9 : p0[3]=-17
      if index == 38 and h >= 9 : p0[3]=-25
      if index >= 46 and index <= 48 and h >= 9 : p0[3]=-20
      if index >= 50 and index <= 52 and h >= 9 : p0[3]=-25
      if index == 54 and h >= 9 : p0[3]=-35
      if index >= 55 and index <= 57 and h >= 9 : p0[3]=-25
      if index >= 58 and index <= 60 and h >= 9 : p0[3]=-40
      if index == 61 and h >= 9 : p0[3]=-30
      if index >= 62 and index <= 63 and h >= 9 : p0[3]=-25
      if index >= 64 and index <= 67 and h >= 9 : p0[3]=-30
      if index >= 68 and index <= 71 and h >= 9 : p0[3]=-40
      if index == 72 and h >= 9 : p0[3]=-35
      if index == 73 and h >= 9 : p0[3]=-30
      if index == 75 and h >= 9 : p0[3]=-25
      if index == 77 and h >= 9 : p0[3]=-15
      if index == 147 and h >= 45 : p0[3]=numpy.nan
      if index == 259 and h >= 45 : p0[3]=numpy.nan
      if index == 242 and h >= 9 : p0[3]=-8
      if index == 243 and h >= 9 : p0[3]=-10
     if beam == 1 :
      if index == 21 and h >= 9 : p0[3]=-15
      if index == 23 and h >= 9 : p0[3]=-10
      if index == 24 and h >= 9 : p0[3]=-3
      if index == 25 and h >= 9 : p0[3]=-2
      if index == 27 and h >= 9 : p0[3]=-1
      if index == 30 and h >= 9 : p0[3]=-5
      if index == 31 and h >= 9 : p0[3]=-3
      if index >= 32 and index <= 35 and h >= 9 : p0[3]=0
      if index == 38 and h >= 9 : p0[3]=-20
      if index == 39 and h >= 9 : p0[3]=-18
      if index >= 41 and index <= 42 and h >= 9 : p0[3]=-10
      if index == 43 and h >= 9 : p0[3]=-5
      if index >= 45 and index <= 47 and h >= 9 : p0[3]=-10
      if index == 48 and h >= 9 : p0[3]=-15
      if index >= 49 and index <= 52 and h >= 9 : p0[3]=-20
      if index == 53 and h >= 9 : p0[3]=-25
      if index == 54 and h >= 9 : p0[3]=-30
      if index >= 54 and index <= 57 and h >= 9 : p0[3]=-20
      if index >= 58 and index <= 60 and h >= 9 : p0[3]=-30
      if index >= 61 and index <= 63 and h >= 9 : p0[3]=-20
      if index >= 64 and index <= 67 and h >= 9 : p0[3]=-25
      if index >= 68 and index <= 71 and h >= 9 : p0[3]=-35
      if index == 72 and h >= 9 : p0[3]=-30
      if index >= 73 and index <= 74 and h >= 9 : p0[3]=-25
      if index == 75 and h >= 9 : p0[3]=-20
      if index == 76 and h >= 9 : p0[3]=-10
      if index == 221 and h <= 18 : p0[3]=15
      if index == 223 and h >= 9 : p0[3]=15
      if index == 234 and h >= 30 : p0[3]=0
      if index == 245 and h >= 9 : p0[3]=-5
      if index == 262 and h >= 9 : p0[3]=-10

    if year == 2026 and doy == 136:
     if beam == 0 :
      if index == 22 and h >= 9 : p0[3]=0
      if index == 23 and h >= 9 : p0[3]=5
      if index == 47 and h >= 9 : p0[3]=-13
      if index == 52 and h >= 9 : p0[3]=2
      if index == 53 and h >= 9 : p0[3]=5
      if index == 54 and h >= 9 : p0[3]=8
      if index == 56 and h >= 9 : p0[3]=15
      if index == 66 and h >= 9 : p0[3]=-20
      if index == 69 and h >= 9 : p0[3]=-35
      if index == 71 and h >= 9 : p0[3]=-22
      if index == 97 and h >= 19 : p0[3]=10
      if index == 219 and h >= 19 : p0[3]=-10
      if index == 237 and h >= 29 : p0[3]=-23
     if beam == 1 :
      if index == 16 and h >= 21 : p0[3]=5
      if index == 20 and h >= 9 : p0[3]=-2
      if index == 21 and h >= 9 : p0[3]=0
      if index == 26 and h >= 9 : p0[3]=10
      if index == 30 and h >= 9 : p0[3]=3
      if index == 31 and h >= 9 : p0[3]=0
      if index == 32 and h >= 9 : p0[3]=0
      if index == 34 and h >= 9 : p0[3]=-10
      if index == 35 and h >= 9 : p0[3]=-5
      if index == 36 and h >= 9 : p0[3]=-2
      if index >= 37 and index <= 41 and h >= 9 : p0[3]=-5
      if index == 40 and h >= 9 : p0[3]=-2
      if index == 43 and h >= 9 : p0[3]=-10
      if index == 44 and h >= 9 : p0[3]=-5
      if index == 45 and h >= 9 : p0[3]=-3
      if index == 48 and h >= 9 : p0[3]=-5
      if index == 49 and h >= 9 : p0[3]=0
      if index == 50 and h >= 9 : p0[3]=5
      if index >= 52 and index <= 53 and h >= 9 : p0[3]=10
      if index == 55 and h >= 9 : p0[3]=13
      if index >= 56 and index <= 57 and h >= 9 : p0[3]=20
      if index == 66 and h >= 9 : p0[3]=-15
      if index == 69 and h >= 9 : p0[3]=-30
      if index == 74 and h >= 9 : p0[3]=-15
      if index == 75 and h >= 9 : p0[3]=-18
      if index == 82 and h >= 20 : p0[3]=-5
      if index == 236 and h >= 27 : p0[3]=-15
      if index == 242 and h >= 24 : p0[3]=-13

    if year == 2026 and doy == 135:
     if beam == 0 :
      if index == 15 and h >= 9 : p0[3]=-20
      if index == 25 and h >= 9 : p0[3]=-25
      if index == 26 and h >= 9 : p0[3]=-30
      if index >= 31 and index <= 32 and h >= 9 : p0[3]=-20
      if index == 34 and h >= 9 : p0[3]=-20
      if index == 35 and h >= 9 : p0[3]=-25
      if index >= 36 and index <= 38 and h >= 9 : p0[3]=-20
      if index >= 39 and index <= 43 and h >= 9 : p0[3]=-25
      if index == 45 and h >= 9 : p0[3]=-15
      if index == 49 and h >= 9 : p0[3]=-5
      if index == 67 and h >= 9 : p0[3]=0
      if index == 72 and h >= 9 : p0[3]=10
      if index >= 73 and index <= 74 and h >= 9 : p0[3]=-5
      if index == 76 and h >= 9 : p0[3]=20
      if index == 78 and h >= 9 : p0[3]=20
      if index == 99 and h >= 35 : p0[3]=numpy.nan
      if index == 135 and h >= 35 : p0[3]=numpy.nan
      if index == 250 and h >= 9 : p0[3]=35
      if index == 251 and h >= 9 : p0[3]=45
      if index == 252 and h >= 9 : p0[3]=25
      if index == 253 and h >= 9 : p0[3]=12
      if index == 254 and h >= 9 : p0[3]=10
      if index == 259 and h >= 9 : p0[3]=-5
      if index == 261 and h >= 9 : p0[3]=-15
      if index == 262 and h >= 9 : p0[3]=-15
      if index == 269 and h >= 9 : p0[3]=-5
     if beam == 1 :
      if index == 8 and h <= 19 : p0[3]=-15
      if index == 12 and h >= 9 : p0[3]=-10
      if index == 16 and h >= 9 : p0[3]=-10
      if index == 19 and h >= 9 : p0[3]=-10
      if index == 22 and h >= 9 : p0[3]=-10
      if index == 23 and h >= 9 : p0[3]=-18
      if index == 24 and h >= 9 : p0[3]=-20
      if index == 25 and h >= 9 : p0[3]=-15
      if index == 26 and h >= 9 : p0[3]=-20
      if index == 27 and h >= 9 : p0[3]=-15
      if index == 28 and h >= 9 : p0[3]=-10
      if index == 29 and h >= 9 : p0[3]=-20
      if index == 30 and h >= 9 : p0[3]=-15
      if index >= 31 and index <= 34 and h >= 9 : p0[3]=-10
      if index == 35 and h >= 9 : p0[3]=-15
      if index >= 36 and index <= 37 and h >= 9 : p0[3]=-10
      if index == 38 and h >= 9 : p0[3]=-15
      if index >= 39 and index <= 43 and h >= 9 : p0[3]=-20
      if index == 45 and h >= 9 : p0[3]=-10
      if index == 46 and h >= 9 : p0[3]=-5
      if index == 47 and h >= 9 : p0[3]=-3
      if index >= 48 and index <= 49 and h >= 9 : p0[3]=0
      if index >= 50 and index <= 51 and h >= 9 : p0[3]=5
      if index >= 52 and index <= 53 and h >= 9 : p0[3]=0
      if index == 56 and h >= 9 : p0[3]=0
      if index == 59 and h >= 9 : p0[3]=0
      if index == 60 and h >= 9 : p0[3]=-1
      if index == 61 and h >= 9 : p0[3]=0
      if index == 64 and h >= 9 : p0[3]=-1
      if index == 65 and h >= 9 : p0[3]=0
      if index == 66 and h >= 9 : p0[3]=2
      if index == 67 and h >= 9 : p0[3]=5
      if index == 70 and h >= 9 : p0[3]=15
      if index >= 71 and index <= 72 and h >= 9 : p0[3]=10
      if index >= 73 and index <= 74 and h >= 9 : p0[3]=0
      if index == 75 and h >= 9 : p0[3]=20
      if index == 77 and h >= 9 : p0[3]=25
      if index == 127 and h >= 27 : p0[3]=15
      if index == 202 and h <= 17 : p0[3]=-2
      if index == 218 and h >= 9 : p0[3]=-10
      if index == 234 and h >= 9 : p0[3]=-10
      if index == 239 and h >= 9 : p0[3]=-10
      if index == 249 and h >= 9 : p0[3]=40
      if index == 251 and h >= 9 : p0[3]=50
      if index == 253 and h >= 9 : p0[3]=20
      if index >= 262 and index <= 263 and h >= 9 : p0[3]=-10
      if index == 265 and h >= 9 : p0[3]=-5
      if index == 267 and h >= 9 : p0[3]=2
      if index == 269 and h >= 9 : p0[3]=0
      if index == 270 and h >= 9 : p0[3]=-1
      if index == 271 and h >= 9 : p0[3]=-5
      if index == 275 and h >= 9 : p0[3]=-12
      if index == 276 and h >= 9 : p0[3]=-10

    if year == 2026 and doy == 134:
     if beam == 0 :
      if index == 41 and h >= 9 : p0[3]=-10
      if index == 44 and h >= 9 : p0[3]=-3
      if index == 45 and h >= 20 : p0[3]=0
      if index >= 53 and index <= 54 and h >= 9 : p0[3]=-5
      if index == 58 and h >= 9 : p0[3]=-10
      if index == 72 and h >= 9 : p0[3]=8
      if index == 77 and h >= 9 : p0[3]=5
      if index == 221 and h <= 18 : p0[3]=0
      if index >= 241 and index <= 242 and h >= 9 : p0[3]=-5
      if index == 243 and h >= 9 : p0[3]=-10
      if index == 248 and h >= 9 : p0[3]=-7
      if index == 260 and h >= 9 : p0[3]=-22
     if beam == 1 :
      if index == 4 and h >= 9 : p0[3]=-15
      if index == 30 and h >= 9 : p0[3]=-5
      if index == 31 and h >= 9 : p0[3]=-4
      if index == 32 and h >= 9 : p0[3]=-3
      if index == 34 and h >= 9 : p0[3]=-5
      if index >= 38 and index <= 40 and h >= 9 : p0[3]=0
      if index >= 41 and index <= 43 and h >= 9 : p0[3]=-5
      if index == 44 and h >= 9 : p0[3]=2
      if index >= 50 and index <= 55 and h >= 9 : p0[3]=0
      if index >= 57 and index <= 62 and h >= 9 : p0[3]=-5
      if index == 65 and h >= 9 : p0[3]=-3
      if index == 69 and h >= 9 : p0[3]=15
      if index >= 71 and index <= 72 and h >= 9 : p0[3]=15
      if index == 73 and h >= 9 : p0[3]=23
      if index == 74 and h >= 9 : p0[3]=20
      if index == 75 and h >= 9 : p0[3]=15
      if index == 76 and h >= 19 : p0[3]=7
      if index == 78 and h >= 9 : p0[3]=6
      if index == 80 and h >= 9 : p0[3]=5
      if index == 252 and h >= 9 : p0[3]=-5
      if index == 255 and h >= 9 : p0[3]=-10
      if index == 259 and h >= 9 : p0[3]=-10
      if index == 265 and h >= 27 : p0[3]=-20

    if year == 2026 and doy == 133:
     if beam == 0 :
      if index == 6 and h >= 19 : p0[3]=-20
      if index == 20 and h >= 19 : p0[3]=-16
      if index == 25 and h >= 9 : p0[3]=-14
      if index == 35 and h >= 9 : p0[3]=-15
      if index == 48 and h >= 9 : p0[3]=10
      if index == 50 and h >= 9 : p0[3]=3
      if index == 58 and h >= 9 : p0[3]=-10
      if index == 61 and h >= 9 : p0[3]=-15
      if index == 65 and h >= 9 : p0[3]=-20
      if index == 66 and h >= 9 : p0[3]=-22
      if index == 70 and h >= 9 : p0[3]=-20
      if index == 77 and h >= 9 : p0[3]=0
      if index == 237 and h >= 9 : p0[3]=-20
      if index == 280 and h >= 23 : p0[3]=-27
     if beam == 1 :
      if index == 5 and h >= 9 : p0[3]=-10
      if index == 15 and h >= 9 : p0[3]=-10
      if index == 20 and h >= 9 : p0[3]=-7
      if index == 22 and h >= 9 : p0[3]=-10
      if index == 23 and h >= 9 : p0[3]=-5
      if index == 25 and h >= 9 : p0[3]=-10
      if index == 26 and h >= 9 : p0[3]=-5
      if index == 27 and h >= 22 : p0[3]=-5
      if index == 28 and h >= 9 : p0[3]=-5
      if index == 30 and h >= 9 : p0[3]=-8
      if index >= 31 and index <= 33 and h >= 9 : p0[3]=-5
      if index == 34 and h >= 9 : p0[3]=-10
      if index == 36 and h >= 9 : p0[3]=-10
      if index >= 37 and index <= 38 and h >= 9 : p0[3]=-5
      if index == 40 and h >= 9 : p0[3]=0
      if index == 44 and h >= 9 : p0[3]=7
      if index == 48 and h >= 9 : p0[3]=15
      if index == 58 and h >= 9 : p0[3]=-5
      if index >= 59 and index <= 60 and h >= 9 : p0[3]=-5
      if index == 61 and h >= 9 : p0[3]=-10
      if index == 65 and h >= 9 : p0[3]=-15
      if index == 66 and h >= 9 : p0[3]=-17
      if index >= 69 and index <= 70 and h >= 9 : p0[3]=-15
      if index == 71 and h >= 9 : p0[3]=-18
      if index >= 72 and index <= 73 and h >= 9 : p0[3]=-10
      if index == 74 and h >= 9 : p0[3]=0
      if index == 76 and h >= 9 : p0[3]=1
      if index == 77 and h >= 9 : p0[3]=0
      if index == 86 and h >= 19 : p0[3]=4
      if index == 224 and h >= 26 : p0[3]=6
      if index == 235 and h >= 9 : p0[3]=-5

    if year == 2026 and doy == 132:
     if beam == 0 :
      if index == 14 and h >= 9 : p0[3]=-30
      if index == 26 and h >= 9 : p0[3]=-30
      if index == 30 and h >= 9 : p0[3]=-25
      if index == 32 and h >= 9 : p0[3]=-28
      if index == 33 and h >= 9 : p0[3]=-30
      if index == 35 and h >= 9 : p0[3]=-30
      if index == 36 and h >= 9 : p0[3]=-25
      if index == 37 and h >= 9 : p0[3]=-20
      if index == 38 and h >= 9 : p0[3]=-15
      if index == 39 and h >= 9 : p0[3]=-25
      if index == 40 and h >= 9 : p0[3]=-10
      if index >= 41 and index <= 48 and h >= 9 : p0[3]=-5
      if index == 47 and h >= 9 : p0[3]=0
      if index >= 55 and index <= 56 and h >= 9 : p0[3]=0
      if index == 62 and h >= 9 : p0[3]=-10
      if index == 73 and h >= 9 : p0[3]=-10
      if index == 79 and h >= 9 : p0[3]=-10
      if index == 221 and h >= 9 : p0[3]=0
      if index == 239 and h >= 9 : p0[3]=-8
      if index == 255 and h >= 9 : p0[3]=-23
     if beam == 1 :
      if index == 5 and h >= 9 : p0[3]=-20
      if index == 22 and h >= 9 : p0[3]=-20
      if index >= 25 and index <= 30 and h >= 9 : p0[3]=-20
      if index == 31 and h >= 9 : p0[3]=-18
      if index == 32 and h >= 9 : p0[3]=-23
      if index == 33 and h >= 9 : p0[3]=-25
      if index == 34 and h >= 9 : p0[3]=-15
      if index == 35 and h >= 9 : p0[3]=-25
      if index == 36 and h >= 9 : p0[3]=-20
      if index == 37 and h >= 9 : p0[3]=-15
      if index == 38 and h >= 9 : p0[3]=-10
      if index == 39 and h >= 9 : p0[3]=-20
      if index == 40 and h >= 9 : p0[3]=-5
      if index >= 41 and index <= 48 and h >= 9 : p0[3]=0
      if index == 47 and h >= 9 : p0[3]=5
      if index == 49 and h >= 9 : p0[3]=5
      if index == 50 and h >= 9 : p0[3]=2
      if index == 51 and h >= 9 : p0[3]=1
      if index == 52 and h >= 9 : p0[3]=0
      if index == 53 and h >= 9 : p0[3]=2
      if index == 54 and h >= 9 : p0[3]=3
      if index >= 55 and index <= 56 and h >= 9 : p0[3]=5
      if index == 57 and h >= 9 : p0[3]=1
      if index == 58 and h >= 9 : p0[3]=0
      if index >= 59 and index <= 60 and h >= 9 : p0[3]=-2
      if index >= 61 and index <= 62 and h >= 9 : p0[3]=-5
      if index >= 63 and index <= 64 and h >= 9 : p0[3]=-10
      if index == 65 and h >= 9 : p0[3]=-15
      if index == 66 and h >= 9 : p0[3]=-13
      if index >= 67 and index <= 68 and h >= 9 : p0[3]=-15
      if index >= 69 and index <= 75 and h >= 9 : p0[3]=-10
      if index >= 78 and index <= 79 and h >= 9 : p0[3]=-10
      if index == 228 and h >= 9 : p0[3]=2
      if index == 244 and h >= 9 : p0[3]=-2
      if index == 253 and h >= 26 : p0[3]=-15

    if year == 2026 and doy == 131:
     if beam == 0 :
      if index == 3 and h >= 9 : p0[3]=-25
      if index == 5 and h >= 9 : p0[3]=-25
      if index == 12 and h >= 9 : p0[3]=-23
      if index == 19 and h >= 9 : p0[3]=-25
      if index == 23 and h >= 9 : p0[3]=-20
      if index == 26 and h >= 9 : p0[3]=-22
      if index == 28 and h >= 9 : p0[3]=-20
      if index == 32 and h >= 9 : p0[3]=-20
      if index == 35 and h >= 9 : p0[3]=-25
      if index >= 36 and index <= 37 and h >= 9 : p0[3]=-20
      if index == 38 and h >= 9 : p0[3]=-25
      if index == 39 and h >= 9 : p0[3]=-23
      if index >= 40 and index <= 46 and h >= 9 : p0[3]=-25
      if index >= 47 and index <= 48 and h >= 9 : p0[3]=-20
      if index >= 49 and index <= 54 and h >= 9 : p0[3]=-25
      if index >= 56 and index <= 60 and h >= 9 : p0[3]=-20
      if index >= 63 and index <= 64 and h >= 9 : p0[3]=-25
      if index >= 66 and index <= 67 and h >= 9 : p0[3]=-20
      if index >= 69 and index <= 70 and h >= 9 : p0[3]=-15
      if index >= 71 and index <= 73 and h >= 9 : p0[3]=-10
      if index == 74 and h >= 9 : p0[3]=-3
      if index >= 75 and index <= 78 and h >= 9 : p0[3]=0
      if index == 80 and h >= 19 : p0[3]=-1
      if index == 83 and h >= 20 : p0[3]=0
      if index == 220 and h >= 29 : p0[3]=-5
      if index == 256 and h >= 25 : p0[3]=-25
     if beam == 1 :
      if index == 22 and h >= 18 : p0[3]=-12
      if index == 23 and h >= 9 : p0[3]=-13
      if index == 25 and h >= 9 : p0[3]=-12
      if index == 27 and h >= 9 : p0[3]=-11
      if index >= 28 and index <= 29 and h >= 9 : p0[3]=-10
      if index == 31 and h >= 9 : p0[3]=-15
      if index == 32 and h >= 9 : p0[3]=-10
      if index == 33 and h >= 9 : p0[3]=-15
      if index == 34 and h >= 9 : p0[3]=-16
      if index == 36 and h >= 9 : p0[3]=-10
      if index == 37 and h >= 9 : p0[3]=-15
      if index >= 38 and index <= 46 and h >= 9 : p0[3]=-20
      if index >= 47 and index <= 48 and h >= 9 : p0[3]=-15
      if index >= 49 and index <= 55 and h >= 9 : p0[3]=-20
      if index >= 56 and index <= 60 and h >= 9 : p0[3]=-15
      if index >= 61 and index <= 64 and h >= 9 : p0[3]=-20
      if index == 65 and h >= 9 : p0[3]=-15
      if index >= 67 and index <= 68 and h >= 9 : p0[3]=-15
      if index >= 69 and index <= 70 and h >= 9 : p0[3]=-10
      if index >= 71 and index <= 73 and h >= 9 : p0[3]=-5
      if index == 74 and h >= 9 : p0[3]=0
      if index == 76 and h >= 9 : p0[3]=-1
      if index == 257 and h >= 26 : p0[3]=-15

    if year == 2026 and doy == 130: #10
     if beam == 0 :
      if index == 10 and h >= 19 : p0[3]=-20
      if index == 32 and h >= 9 : p0[3]=-25
      if index >= 38 and index <= 40 and h >= 9 : p0[3]=-25
      if index >= 41 and index <= 42 and h >= 9 : p0[3]=-20
      if index >= 43 and index <= 44 and h >= 9 : p0[3]=-25
      if index >= 46 and index <= 48 and h >= 9 : p0[3]=-25
      if index == 53 and h >= 9 : p0[3]=-15
      if index == 55 and h >= 9 : p0[3]=-15
      if index == 56 and h >= 9 : p0[3]=-20
      if index >= 57 and index <= 58 and h >= 9 : p0[3]=-10
      if index == 62 and h >= 9 : p0[3]=-6
      if index == 69 and h >= 9 : p0[3]=-10
      if index == 85 and h >= 9 : p0[3]=-5
      if index == 86 and h >= 9 : p0[3]=-6
      if index == 141 and h >= 9 : p0[3]=15
      if index == 142 and h >= 9 : p0[3]=15
      if index == 228 and h >= 9 : p0[3]=13
      if index == 229 and h >= 9 : p0[3]=10
      if index == 233 and h >= 9 : p0[3]=13
      if index >= 240 and index <= 242 and h >= 9 : p0[3]=-10
      if index >= 244 and index <= 245 and h >= 9 : p0[3]=-5
      if index == 246 and h >= 9 : p0[3]=-15
      if index == 251 and h >= 9 : p0[3]=-10
      if index == 253 and h >= 9 : p0[3]=-15
      if index == 263 and h >= 9 : p0[3]=-25
     if beam == 1 :
      if index == 0 and h >= 9 : p0[3]=-10
      if index == 3 and h <= 18 : p0[3]=-12
      if index == 4 and h >= 9 : p0[3]=-12
      if index == 11 and h >= 20 : p0[3]=-20
      if index >= 34 and index <= 37 and h >= 9 : p0[3]=-20
      if index >= 38 and index <= 42 and h >= 9 : p0[3]=-15
      if index >= 43 and index <= 46 and h >= 9 : p0[3]=-20
      if index >= 48 and index <= 51 and h >= 9 : p0[3]=-20
      if index == 50 and h >= 9 : p0[3]=-15
      if index >= 53 and index <= 55 and h >= 9 : p0[3]=-10
      if index == 56 and h >= 9 : p0[3]=-15
      if index >= 57 and index <= 59 and h >= 9 : p0[3]=-5
      if index >= 60 and index <= 61 and h >= 9 : p0[3]=0
      if index == 65 and h >= 9 : p0[3]=-4
      if index >= 66 and index <= 68 and h >= 9 : p0[3]=-5
      if index == 70 and h >= 9 : p0[3]=-1
      if index == 71 and h >= 9 : p0[3]=-5
      if index == 72 and h >= 9 : p0[3]=0
      if index == 73 and h >= 9 : p0[3]=-1
      if index == 75 and h >= 9 : p0[3]=-1
      if index >= 81 and index <= 82 and h >= 9 : p0[3]=0
      if index == 225 and h >= 9 : p0[3]=25
      if index == 227 and h >= 9 : p0[3]=25
      if index == 228 and h >= 9 : p0[3]=20
      if index == 229 and h <= 25 : p0[3]=25
      if index == 236 and h >= 9 : p0[3]=5
      if index == 237 and h >= 9 : p0[3]=0
      if index == 239 and h <= 34 : p0[3]=0
      if index >= 240 and index <= 242 and h >= 9 : p0[3]=0
      if index == 245 and h >= 9 : p0[3]=5
      if index == 248 and h >= 9 : p0[3]=-5
      if index == 249 and h >= 9 : p0[3]=0
      if index == 251 and h >= 9 : p0[3]=0
      if index == 252 and h >= 9 : p0[3]=-5
      if index == 280 and h >= 20 : p0[3]=-15

    if year == 2026 and doy == 129:
     if beam == 0 :
      if index == 30 and h >= 19 : p0[3]=-20
      if index == 32 and h >= 9 : p0[3]=-25
      if index == 36 and h >= 9 : p0[3]=-20
      if index >= 38 and index <= 43 and h >= 9 : p0[3]=-20
      if index == 44 and h >= 9 : p0[3]=-25
      if index == 45 and h >= 9 : p0[3]=-22
      if index == 46 and h >= 9 : p0[3]=-25
      if index >= 47 and index <= 51 and h >= 9 : p0[3]=-20
      if index == 52 and h >= 9 : p0[3]=-15
      if index >= 53 and index <= 54 and h >= 9 : p0[3]=-10
      if index == 55 and h >= 9 : p0[3]=-5
      if index == 65 and h >= 9 : p0[3]=-10
      if index == 66 and h >= 9 : p0[3]=-15
      if index == 71 and h >= 9 : p0[3]=-10
      if index == 75 and h >= 9 : p0[3]=0
      if index == 76 and h >= 9 : p0[3]=5
      if index == 228 and h >= 9 : p0[3]=-10
      if index == 230 and h >= 9 : p0[3]=-10
      if index == 248 and h >= 9 : p0[3]=-12
      if index >= 249 and index <= 251 and h >= 9 : p0[3]=-15
      if index == 258 and h >= 9 : p0[3]=-18
     if beam == 1 :
      if index == 6 and h >= 9 : p0[3]=-10
      if index == 15 and h >= 9 : p0[3]=-10
      if index >= 28 and index <= 30 and h >= 9 : p0[3]=-10
      if index == 33 and h >= 9 : p0[3]=-15
      if index == 34 and h >= 9 : p0[3]=-13
      if index >= 35 and index <= 36 and h >= 9 : p0[3]=-15
      if index >= 37 and index <= 43 and h >= 9 : p0[3]=-10
      if index == 44 and h >= 9 : p0[3]=-15
      if index == 45 and h >= 9 : p0[3]=-17
      if index == 46 and h >= 9 : p0[3]=-20
      if index >= 47 and index <= 51 and h >= 9 : p0[3]=-15
      if index == 52 and h >= 9 : p0[3]=-10
      if index >= 53 and index <= 54 and h >= 9 : p0[3]=-5
      if index >= 55 and index <= 56 and h >= 9 : p0[3]=0
      if index >= 58 and index <= 61 and h >= 9 : p0[3]=-10
      if index == 62 and h >= 9 : p0[3]=-5
      if index == 63 and h >= 9 : p0[3]=-15
      if index == 64 and h >= 9 : p0[3]=-20
      if index == 65 and h >= 9 : p0[3]=-5
      if index >= 66 and index <= 67 and h >= 9 : p0[3]=-10
      if index >= 68 and index <= 69 and h >= 9 : p0[3]=-5
      if index == 70 and h >= 9 : p0[3]=-1
      if index == 72 and h >= 9 : p0[3]=0
      if index >= 73 and index <= 74 and h >= 9 : p0[3]=0
      if index == 75 and h >= 9 : p0[3]=1
      if index == 79 and h >= 9 : p0[3]=-1
      if index == 238 and h >= 9 : p0[3]=-3
      if index == 239 and h >= 9 : p0[3]=-2
      if index == 241 and h >= 9 : p0[3]=-5
      if index == 275 and h >= 9 : p0[3]=-10

    if year == 2026 and doy == 128:
     if beam == 0 :
      if index == 8 and h >= 9 : p0[3]=-40
      if index == 17 and h >= 9 : p0[3]=-20
      if index == 18 and h >= 9 : p0[3]=-30
      if index == 19 and h >= 9 : p0[3]=-25
      if index == 20 and h >= 9 : p0[3]=-28
      if index >= 21 and index <= 24 and h >= 9 : p0[3]=-30
      if index == 25 and h >= 9 : p0[3]=-20
      if index == 26 and h >= 9 : p0[3]=-25
      if index >= 27 and index <= 29 and h >= 9 : p0[3]=-20
      if index == 30 and h >= 9 : p0[3]=-15
      if index >= 31 and index <= 36 and h >= 9 : p0[3]=-10
      if index == 37 and h >= 9 : p0[3]=-5
      if index >= 38 and index <= 39 and h >= 9 : p0[3]=-10
      if index == 40 and h >= 9 : p0[3]=-5
      if index >= 43 and index <= 44 and h >= 9 : p0[3]=0
      if index == 45 and h >= 9 : p0[3]=-5
      if index >= 46 and index <= 50 and h >= 9 : p0[3]=-10
      if index == 51 and h >= 9 : p0[3]=0
      if index == 52 and h >= 9 : p0[3]=5
      if index == 53 and h >= 9 : p0[3]=15
      if index == 56 and h >= 9 : p0[3]=-5
      if index == 57 and h >= 9 : p0[3]=-10
      if index == 58 and h >= 9 : p0[3]=-20
      if index >= 59 and index <= 60 and h >= 9 : p0[3]=0
      if index >= 61 and index <= 64 and h >= 9 : p0[3]=15
      if index == 63 and h >= 9 : p0[3]=10
      if index == 65 and h >= 9 : p0[3]=10
      if index == 66 and h >= 9 : p0[3]=0
      if index == 67 and h >= 9 : p0[3]=-10
      if index == 68 and h >= 9 : p0[3]=-7
      if index == 69 and h >= 9 : p0[3]=-15
      if index >= 70 and index <= 72 and h >= 9 : p0[3]=-10
      if index == 73 and h >= 9 : p0[3]=-15
      if index == 74 and h >= 9 : p0[3]=-5
      if index == 75 and h >= 9 : p0[3]=0
      if index == 77 and h >= 9 : p0[3]=-5
      if index == 83 and h >= 9 : p0[3]=5
      if index == 216 and h >= 9 : p0[3]=5
      if index == 228 and h >= 9 : p0[3]=-3
      if index == 230 and h >= 9 : p0[3]=-10
      if index == 235 and h >= 9 : p0[3]=-15
     if beam == 1 :
      if index == 11 and h >= 9 : p0[3]=-30
      if index == 14 and h >= 9 : p0[3]=-25
      if index == 15 and h >= 9 : p0[3]=-20
      if index == 17 and h >= 9 : p0[3]=-15
      if index == 18 and h >= 9 : p0[3]=-25
      if index == 19 and h >= 9 : p0[3]=-20
      if index == 20 and h >= 9 : p0[3]=-23
      if index >= 21 and index <= 24 and h >= 9 : p0[3]=-25
      if index == 25 and h >= 9 : p0[3]=-15
      if index == 26 and h >= 9 : p0[3]=-20
      if index >= 27 and index <= 29 and h >= 9 : p0[3]=-15
      if index == 30 and h >= 9 : p0[3]=-10
      if index >= 31 and index <= 36 and h >= 9 : p0[3]=-5
      if index == 37 and h >= 9 : p0[3]=0
      if index >= 38 and index <= 39 and h >= 9 : p0[3]=-5
      if index == 40 and h >= 9 : p0[3]=0
      if index == 41 and h >= 9 : p0[3]=5
      if index == 42 and h >= 9 : p0[3]=8
      if index == 44 and h >= 9 : p0[3]=5
      if index >= 45 and index <= 46 and h >= 9 : p0[3]=0
      if index >= 47 and index <= 50 and h >= 9 : p0[3]=-5
      if index == 51 and h >= 9 : p0[3]=5
      if index == 52 and h >= 9 : p0[3]=10
      if index == 53 and h >= 9 : p0[3]=20
      if index == 54 and h >= 9 : p0[3]=20
      if index == 55 and h >= 9 : p0[3]=-5
      if index >= 56 and index <= 57 and h >= 9 : p0[3]=0
      if index == 58 and h >= 9 : p0[3]=-10
      if index >= 59 and index <= 60 and h >= 9 : p0[3]=5
      if index >= 61 and index <= 63 and h >= 9 : p0[3]=15
      if index == 64 and h >= 9 : p0[3]=20
      if index == 66 and h >= 9 : p0[3]=5
      if index >= 67 and index <= 72 and h >= 9 : p0[3]=-5
      if index == 69 and h >= 9 : p0[3]=-10
      if index == 73 and h >= 9 : p0[3]=-10
      if index == 74 and h >= 9 : p0[3]=0
      if index >= 75 and index <= 76 and h >= 9 : p0[3]=5
      if index == 77 and h >= 9 : p0[3]=0
      if index == 79 and h >= 9 : p0[3]=2
      if index == 81 and h >= 9 : p0[3]=0
      if index == 83 and h >= 9 : p0[3]=4
      if index == 186 and h >= 9 : p0[3]=19
      if index == 220 and h <= 18 : p0[3]=17

    if year == 2026 and doy == 127:
     if beam == 0 :
      if index == 1 and h >= 9 : p0[3]=-23
      if index == 7 and h >= 20 : p0[3]=-20
      if index == 15 and h >= 9 : p0[3]=-22
      if index == 16 and h >= 9 : p0[3]=-25
      if index == 28 and h >= 20 : p0[3]=-20
      if index >= 34 and index <= 35 and h >= 9 : p0[3]=-15
      if index >= 36 and index <= 37 and h >= 9 : p0[3]=-20
      if index >= 40 and index <= 41 and h >= 9 : p0[3]=-20
      if index >= 43 and index <= 56 and h >= 9 : p0[3]=-15
      if index >= 57 and index <= 60 and h >= 9 : p0[3]=-20
      if index == 61 and h >= 9 : p0[3]=-25
      if index >= 63 and index <= 66 and h >= 9 : p0[3]=-20
      if index >= 67 and index <= 68 and h >= 9 : p0[3]=-25
      if index == 69 and h >= 9 : p0[3]=-15
      if index == 70 and h >= 9 : p0[3]=-20
      if index == 71 and h >= 9 : p0[3]=-25
      if index == 73 and h >= 9 : p0[3]=-35
      if index == 74 and h >= 9 : p0[3]=-25
      if index == 85 and h >= 16 : p0[3]=-10
      if index == 255 and h >= 29 : p0[3]=-15
      if index == 260 and h >= 9 : p0[3]=-13
     if beam == 1 :
      if index == 4 and h >= 26 : p0[3]=-10
      if index == 25 and h >= 9 : p0[3]=-10
      if index >= 29 and index <= 37 and h >= 9 : p0[3]=-10
      if index == 31 and h >= 9 : p0[3]=-12
      if index == 38 and h >= 9 : p0[3]=-5
      if index == 39 and h >= 9 : p0[3]=-15
      if index == 40 and h >= 9 : p0[3]=-10
      if index >= 41 and index <= 42 and h >= 9 : p0[3]=-15
      if index >= 43 and index <= 56 and h >= 9 : p0[3]=-10
      if index >= 57 and index <= 60 and h >= 9 : p0[3]=-15
      if index >= 61 and index <= 62 and h >= 9 : p0[3]=-20
      if index >= 63 and index <= 66 and h >= 9 : p0[3]=-15
      if index >= 67 and index <= 68 and h >= 9 : p0[3]=-20
      if index == 69 and h >= 9 : p0[3]=-10
      if index == 70 and h >= 9 : p0[3]=-17
      if index == 71 and h >= 9 : p0[3]=-20
      if index == 72 and h >= 9 : p0[3]=-30
      if index == 73 and h >= 9 : p0[3]=-30
      if index == 74 and h >= 9 : p0[3]=-20
      if index == 75 and h >= 9 : p0[3]=-15
      if index == 76 and h >= 9 : p0[3]=-5
      if index >= 77 and index <= 78 and h >= 9 : p0[3]=-10
      if index == 84 and h >= 9 : p0[3]=-5
      if index == 86 and h >= 9 : p0[3]=-8
      if index == 229 and h >= 29 : p0[3]=5
      if index == 231 and h >= 27 : p0[3]=0
      if index == 247 and h >= 29 : p0[3]=0
      if index == 248 and h >= 30 : p0[3]=0
      if index == 260 and h >= 9 : p0[3]=-5

    if year == 2026 and doy == 126:
     if beam == 0 :
      if index == 30 and h >= 9 : p0[3]=-30
      if index == 34 and h >= 9 : p0[3]=-30
      if index == 35 and h >= 9 : p0[3]=-30
      if index == 38 and h >= 9 : p0[3]=-30
      if index >= 39 and index <= 45 and h >= 9 : p0[3]=-25
      if index >= 46 and index <= 62 and h >= 9 : p0[3]=-30
      if index == 54 and h >= 9 : p0[3]=-25
      if index == 57 and h >= 9 : p0[3]=-25
      if index == 64 and h >= 9 : p0[3]=-30
      if index == 65 and h >= 9 : p0[3]=-35
      if index == 66 and h >= 9 : p0[3]=-30
      if index == 67 and h >= 9 : p0[3]=-20
      if index == 68 and h >= 9 : p0[3]=-25
      if index >= 69 and index <= 73 and h >= 9 : p0[3]=-35
      if index == 71 and h >= 9 : p0[3]=-25
      if index == 74 and h >= 9 : p0[3]=-30
      if index == 209 and h >= 9 : p0[3]=-2
      if index == 218 and h >= 27 : p0[3]=0
      if index == 234 and h >= 9 : p0[3]=-8
      if index == 244 and h >= 9 : p0[3]=-10
      if index == 245 and h >= 9 : p0[3]=-11
      if index == 253 and h >= 9 : p0[3]=-10
      if index == 254 and h >= 9 : p0[3]=-5
     if beam == 1 :
      if index == 5 and h >= 9 : p0[3]=-15
      if index == 32 and h >= 9 : p0[3]=-20
      if index == 33 and h >= 9 : p0[3]=-25
      if index == 35 and h >= 9 : p0[3]=-25
      if index == 36 and h >= 9 : p0[3]=-30
      if index == 37 and h >= 9 : p0[3]=-23
      if index == 38 and h >= 9 : p0[3]=-25
      if index >= 39 and index <= 40 and h >= 9 : p0[3]=-20
      if index >= 42 and index <= 45 and h >= 9 : p0[3]=-20
      if index >= 46 and index <= 66 and h >= 9 : p0[3]=-25
      if index == 54 and h >= 9 : p0[3]=-20
      if index == 57 and h >= 9 : p0[3]=-20
      if index == 63 and h >= 9 : p0[3]=-30
      if index == 65 and h >= 9 : p0[3]=-30
      if index == 67 and h >= 9 : p0[3]=-20
      if index == 68 and h >= 9 : p0[3]=-25
      if index >= 69 and index <= 73 and h >= 9 : p0[3]=-30
      if index == 71 and h >= 9 : p0[3]=-20
      if index == 74 and h >= 9 : p0[3]=-25
      if index == 75 and h >= 9 : p0[3]=-15
      if index == 76 and h >= 9 : p0[3]=-10
      if index == 77 and h >= 9 : p0[3]=-10
      if index == 216 and h >= 26 : p0[3]=3
      if index == 229 and h >= 9 : p0[3]=10
      if index == 230 and h >= 9 : p0[3]=-12
      if index == 236 and h >= 9 : p0[3]=2
      if index == 249 and h >= 9 : p0[3]=-2
      if index == 262 and h >= 9 : p0[3]=-5
      if index == 270 and h >= 9 : p0[3]=-13
      if index == 272 and h >= 9 : p0[3]=-18

    if year == 2026 and doy == 125:
     if beam == 0 :
      if index == 2 and h >= 9 : p0[3]=-25
      if index == 15 and h >= 22 : p0[3]=-15
      if index == 17 and h >= 9 : p0[3]=-16
      if index == 25 and h >= 9 : p0[3]=-7
      if index == 30 and h >= 9 : p0[3]=0
      if index == 33 and h >= 9 : p0[3]=5
      if index == 34 and h >= 9 : p0[3]=5
      if index == 36 and h >= 9 : p0[3]=3
      if index >= 37 and index <= 40 and h >= 9 : p0[3]=5
      if index == 39 and h >= 9 : p0[3]=0
      if index == 53 and h >= 9 : p0[3]=-2
      if index == 58 and h >= 9 : p0[3]=0
      if index == 60 and h >= 9 : p0[3]=-5
      if index == 211 and h >= 9 : p0[3]=15
      if index == 220 and h <= 19 : p0[3]=20
      if index == 228 and h >= 9 : p0[3]=2
      if index == 229 and h >= 9 : p0[3]=5
      if index == 230 and h >= 9 : p0[3]=3
      if index == 231 and h >= 9 : p0[3]=0
      if index == 232 and h >= 9 : p0[3]=-5
      if index >= 233 and index <= 235 and h >= 9 : p0[3]=0
      if index == 251 and h >= 9 : p0[3]=-20
      if index == 252 and h >= 9 : p0[3]=-22
      if index == 255 and h >= 29 : p0[3]=-15
      if index == 260 and h >= 9 : p0[3]=-25
     if beam == 1 :
      if index == 1 and h <= 20 : p0[3]=-15
      if index == 5 and h >= 9 : p0[3]=-20
      if index == 16 and h <= 16 : p0[3]=-12
      if index == 26 and h >= 9 : p0[3]=1
      if index == 32 and h >= 9 : p0[3]=5
      if index == 34 and h >= 9 : p0[3]=8
      if index == 35 and h >= 9 : p0[3]=10
      if index == 36 and h >= 9 : p0[3]=6
      if index == 37 and h >= 9 : p0[3]=8
      if index == 38 and h >= 9 : p0[3]=5
      if index == 39 and h >= 9 : p0[3]=0
      if index == 40 and h >= 9 : p0[3]=5
      if index >= 41 and index <= 48 and h >= 9 : p0[3]=10
      if index == 49 and h >= 9 : p0[3]=5
      if index == 50 and h >= 9 : p0[3]=1
      if index == 53 and h >= 9 : p0[3]=2
      if index == 58 and h >= 9 : p0[3]=0
      if index >= 61 and index <= 63 and h >= 9 : p0[3]=-10
      if index == 66 and h >= 9 : p0[3]=-15
      if index == 67 and h >= 9 : p0[3]=-5
      if index == 69 and h >= 9 : p0[3]=-3
      if index == 70 and h >= 9 : p0[3]=-1
      if index == 74 and h >= 9 : p0[3]=-2
      if index == 211 and h >= 9 : p0[3]=15
      if index == 214 and h >= 29 : p0[3]=15
      if index == 221 and h >= 9 : p0[3]=18
      if index == 224 and h >= 9 : p0[3]=15
      if index == 233 and h >= 9 : p0[3]=5
      if index == 236 and h >= 9 : p0[3]=5
      if index == 239 and h >= 9 : p0[3]=3
      if index == 241 and h >= 9 : p0[3]=0
      if index == 247 and h >= 9 : p0[3]=-5
      if index == 250 and h >= 9 : p0[3]=-10
      if index == 255 and h >= 9 : p0[3]=-5
      if index == 263 and h >= 9 : p0[3]=-15
      if index == 285 and h >= 25 : p0[3]=-10

    if year == 2026 and doy == 124:
     if beam == 0 :
      if index == 24 and h >= 9 : p0[3]=-15
      if index == 25 and h >= 9 : p0[3]=-17
      if index == 26 and h >= 9 : p0[3]=-15
      if index == 34 and h >= 9 : p0[3]=-25
      if index == 35 and h >= 9 : p0[3]=-20
      if index == 36 and h >= 9 : p0[3]=-10
      if index >= 38 and index <= 40 and h >= 9 : p0[3]=-10
      if index == 47 and h >= 9 : p0[3]=-15
      if index >= 48 and index <= 49 and h >= 9 : p0[3]=-10
      if index == 50 and h >= 9 : p0[3]=-15
      if index == 51 and h >= 9 : p0[3]=-18
      if index >= 52 and index <= 53 and h >= 9 : p0[3]=-20
      if index == 55 and h >= 9 : p0[3]=-15
      if index == 61 and h >= 9 : p0[3]=-30
      if index == 63 and h >= 9 : p0[3]=-30
      if index == 66 and h >= 9 : p0[3]=-25
      if index >= 67 and index <= 70 and h >= 9 : p0[3]=-15
      if index == 71 and h >= 9 : p0[3]=-10
      if index == 212 and h >= 9 : p0[3]=-13
      if index == 219 and h <= 19 : p0[3]=23
      if index == 234 and h >= 9 : p0[3]=-15
      if index == 245 and h >= 9 : p0[3]=-22
     if beam == 1 :
      if index == 17 and h >= 9 : p0[3]=-25
      if index == 23 and h >= 9 : p0[3]=-17
      if index == 24 and h >= 9 : p0[3]=-10
      if index == 26 and h >= 9 : p0[3]=-10
      if index == 29 and h >= 9 : p0[3]=-20
      if index == 33 and h >= 9 : p0[3]=-20
      if index == 36 and h >= 9 : p0[3]=-5
      if index == 37 and h >= 9 : p0[3]=-1
      if index >= 38 and index <= 40 and h >= 9 : p0[3]=-5
      if index == 41 and h >= 9 : p0[3]=5
      if index == 42 and h >= 9 : p0[3]=3
      if index == 43 and h >= 9 : p0[3]=-5
      if index == 44 and h >= 9 : p0[3]=-5
      if index == 45 and h >= 9 : p0[3]=-20
      if index == 46 and h >= 9 : p0[3]=-18
      if index == 47 and h >= 9 : p0[3]=-10
      if index >= 48 and index <= 49 and h >= 9 : p0[3]=-5
      if index == 50 and h >= 9 : p0[3]=-10
      if index == 51 and h >= 9 : p0[3]=-13
      if index >= 52 and index <= 54 and h >= 9 : p0[3]=-15
      if index >= 55 and index <= 57 and h >= 9 : p0[3]=-10
      if index == 58 and h >= 9 : p0[3]=-15
      if index == 61 and h >= 9 : p0[3]=-25
      if index == 62 and h >= 9 : p0[3]=-22
      if index >= 63 and index <= 65 and h >= 9 : p0[3]=-25
      if index == 66 and h >= 9 : p0[3]=-20
      if index >= 67 and index <= 70 and h >= 9 : p0[3]=-10
      if index == 71 and h >= 9 : p0[3]=-5
      if index == 72 and h >= 9 : p0[3]=-1
      if index == 73 and h >= 9 : p0[3]=-10
      if index == 74 and h >= 9 : p0[3]=0
      if index == 75 and h >= 9 : p0[3]=2
      if index == 76 and h >= 9 : p0[3]=3
      if index == 77 and h >= 9 : p0[3]=10
      if index == 80 and h >= 9 : p0[3]=2
      if index == 230 and h >= 9 : p0[3]=15
      if index == 231 and h >= 9 : p0[3]=5
      if index == 236 and h >= 9 : p0[3]=-18
      if index >= 239 and index <= 240 and h >= 9 : p0[3]=-15

    if year == 2026 and doy == 123:
     if beam == 0 :
      if index == 18 and h >= 9 : p0[3]=-30
      if index == 23 and h >= 9 : p0[3]=-26
      if index == 28 and h >= 9 : p0[3]=-20
      if index >= 32 and index <= 34 and h >= 9 : p0[3]=-20
      if index >= 36 and index <= 39 and h >= 9 : p0[3]=-20
      if index >= 40 and index <= 48 and h >= 9 : p0[3]=-25
      if index >= 49 and index <= 50 and h >= 9 : p0[3]=-20
      if index >= 51 and index <= 52 and h >= 9 : p0[3]=-15
      if index >= 53 and index <= 66 and h >= 9 : p0[3]=-10
      if index == 67 and h >= 9 : p0[3]=-7
      if index == 72 and h >= 9 : p0[3]=-3
      if index == 74 and h >= 9 : p0[3]=-5
      if index == 76 and h >= 9 : p0[3]=0
      if index == 220 and h <= 21 : p0[3]=10
      if index == 234 and h >= 9 : p0[3]=-15
      if index == 239 and h >= 9 : p0[3]=-17
     if beam == 1 :
      if index == 9 and h >= 9 : p0[3]=-15
      if index == 24 and h >= 9 : p0[3]=-20
      if index == 30 and h >= 9 : p0[3]=-15
      if index >= 32 and index <= 35 and h >= 9 : p0[3]=-10
      if index >= 36 and index <= 39 and h >= 9 : p0[3]=-15
      if index >= 40 and index <= 48 and h >= 9 : p0[3]=-20
      if index >= 49 and index <= 50 and h >= 9 : p0[3]=-15
      if index >= 51 and index <= 52 and h >= 9 : p0[3]=-10
      if index >= 53 and index <= 66 and h >= 9 : p0[3]=-5
      if index == 67 and h >= 9 : p0[3]=-2
      if index >= 68 and index <= 74 and h >= 9 : p0[3]=-5
      if index == 72 and h >= 9 : p0[3]=-4
      if index == 75 and h >= 9 : p0[3]=-10
      if index == 77 and h >= 9 : p0[3]=-4
      if index == 80 and h >= 9 : p0[3]=2
      if index == 234 and h <= 22 : p0[3]=-5

    if year == 2026 and doy == 122:
     if beam == 0 :
      if index == 15 and h >= 30 : p0[3]=-20
      if index == 20 and h >= 9 : p0[3]=-14
      if index == 33 and h >= 9 : p0[3]=-10
      if index == 35 and h >= 9 : p0[3]=-18
      if index >= 36 and index <= 37 and h >= 9 : p0[3]=-20
      if index >= 40 and index <= 43 and h >= 9 : p0[3]=-20
      if index == 44 and h >= 9 : p0[3]=-21
      if index == 45 and h >= 9 : p0[3]=-26
      if index == 46 and h >= 9 : p0[3]=-10
      if index == 47 and h >= 9 : p0[3]=-15
      if index >= 48 and index <= 48 and h >= 9 : p0[3]=-22
      if index == 49 and h >= 9 : p0[3]=-23
      if index == 50 and h >= 9 : p0[3]=-23
      if index >= 51 and index <= 56 and h >= 9 : p0[3]=-25
      if index >= 59 and index <= 62 and h >= 9 : p0[3]=-30
      if index >= 63 and index <= 64 and h >= 9 : p0[3]=-42
      if index >= 70 and index <= 71 and h >= 9 : p0[3]=-40
      if index >= 72 and index <= 73 and h >= 9 : p0[3]=-35
      if index == 75 and h >= 9 : p0[3]=-25
      if index == 234 and h >= 9 : p0[3]=-10
      if index == 240 and h >= 9 : p0[3]=-20
     if beam == 1 :
      if index == 13 and h >= 22 : p0[3]=-15
      if index == 20 and h >= 9 : p0[3]=-8
      if index == 26 and h >= 9 : p0[3]=-8
      if index == 29 and h >= 9 : p0[3]=-6
      if index == 31 and h >= 9 : p0[3]=-5
      if index == 33 and h >= 9 : p0[3]=-6
      if index == 34 and h >= 9 : p0[3]=-10
      if index == 35 and h >= 9 : p0[3]=-9
      if index == 36 and h >= 9 : p0[3]=-17
      if index == 37 and h >= 9 : p0[3]=-15
      if index == 38 and h >= 9 : p0[3]=-10
      if index == 39 and h >= 9 : p0[3]=-9
      if index >= 40 and index <= 45 and h >= 9 : p0[3]=-15
      if index == 44 and h >= 9 : p0[3]=-10
      if index == 46 and h >= 9 : p0[3]=-3
      if index == 47 and h >= 9 : p0[3]=-10
      if index >= 48 and index <= 50 and h >= 9 : p0[3]=-16
      if index >= 51 and index <= 55 and h >= 9 : p0[3]=-20
      if index == 56 and h >= 9 : p0[3]=-19
      if index == 57 and h >= 9 : p0[3]=-25
      if index >= 60 and index <= 62 and h >= 9 : p0[3]=-25
      if index == 64 and h >= 9 : p0[3]=-38
      if index == 65 and h >= 9 : p0[3]=-30
      if index >= 66 and index <= 68 and h >= 9 : p0[3]=-21
      if index == 71 and h >= 9 : p0[3]=-30
      if index >= 72 and index <= 73 and h >= 9 : p0[3]=-23
      if index == 74 and h >= 9 : p0[3]=-30
      if index >= 75 and index <= 76 and h >= 9 : p0[3]=-20
      if index == 236 and h >= 9 : p0[3]=0

    if year == 2026 and doy == 121: #1
     if beam == 0 :
      if index == 21 and h >= 9 : p0[3]=-12
      if index == 29 and h <= 16 : p0[3]=-15
      if index == 35 and h >= 9 : p0[3]=-7
      if index == 38 and h >= 9 : p0[3]=-1
      if index == 39 and h >= 9 : p0[3]=-4
      if index == 41 and h >= 9 : p0[3]=-7
      if index == 45 and h >= 9 : p0[3]=-10
      if index == 48 and h >= 9 : p0[3]=-15
      if index == 49 and h >= 9 : p0[3]=-10
      if index == 51 and h >= 9 : p0[3]=-18
      if index == 52 and h >= 9 : p0[3]=-20
      if index == 54 and h >= 9 : p0[3]=-20
      if index >= 55 and index <= 56 and h >= 9 : p0[3]=-13
      if index == 59 and h >= 9 : p0[3]=-16
      if index >= 60 and index <= 61 and h >= 9 : p0[3]=-16
      if index >= 69 and index <= 70 and h >= 9 : p0[3]=-20
      if index == 177 and h >= 45 : p0[3]=numpy.nan
      if index == 197 and h >= 38 : p0[3]=numpy.nan
      if index == 227 and h >= 9 : p0[3]=-10
      if index == 229 and h >= 9 : p0[3]=-12
      if index == 235 and h >= 9 : p0[3]=-6
      if index == 238 and h >= 9 : p0[3]=-15
      if index == 240 and h >= 9 : p0[3]=-16
     if beam == 1 :
      if index == 1 and h >= 9 : p0[3]=-5
      if index == 4 and h >= 23 : p0[3]=-10
      if index == 6 and h <= 19 : p0[3]=-20
      if index == 12 and h >= 27 : p0[3]=-5
      if index == 16 and h >= 9 : p0[3]=-9
      if index == 17 and h >= 9 : p0[3]=-9
      if index == 20 and h >= 25 : p0[3]=-9
      if index == 27 and h >= 9 : p0[3]=-10
      if index == 31 and h >= 9 : p0[3]=-5
      if index == 37 and h >= 9 : p0[3]=0
      if index == 38 and h >= 9 : p0[3]=1
      if index == 39 and h >= 9 : p0[3]=0
      if index == 40 and h >= 9 : p0[3]=-1
      if index >= 41 and index <= 42 and h >= 9 : p0[3]=-1
      if index == 43 and h >= 9 : p0[3]=-5
      if index == 44 and h >= 9 : p0[3]=-5
      if index == 45 and h >= 9 : p0[3]=-5
      if index >= 47 and index <= 48 and h >= 9 : p0[3]=-10
      if index >= 49 and index <= 50 and h >= 9 : p0[3]=-5
      if index == 51 and h >= 9 : p0[3]=-9
      if index == 52 and h >= 9 : p0[3]=-15
      if index == 53 and h >= 9 : p0[3]=-7
      if index == 54 and h >= 9 : p0[3]=-15
      if index >= 55 and index <= 56 and h >= 9 : p0[3]=-7
      if index == 57 and h >= 9 : p0[3]=-11
      if index == 58 and h >= 9 : p0[3]=-10
      if index >= 59 and index <= 60 and h >= 9 : p0[3]=-12
      if index == 61 and h >= 9 : p0[3]=-11
      if index >= 62 and index <= 63 and h >= 9 : p0[3]=-10
      if index == 64 and h >= 9 : p0[3]=-9
      if index == 65 and h >= 9 : p0[3]=-16
      if index == 66 and h >= 9 : p0[3]=-21
      if index == 68 and h >= 9 : p0[3]=-18
      if index == 69 and h >= 9 : p0[3]=-15
      if index == 73 and h >= 9 : p0[3]=-10
      if index == 77 and h >= 9 : p0[3]=-5
      if index == 233 and h >= 27 : p0[3]=0
      if index == 286 and h >= 25 : p0[3]=-16

# MP marzo abril 2026
    if year == 2026 and doy == 120:  #30
     if beam == 0 :
      if index == 22 and h == 33 : p0[3]=numpy.nan
      if index == 37 and h >= 9 : p0[3]=-12
      if index == 42 and h >= 9 : p0[3]=-20
      if index == 47 and h >= 9 : p0[3]=-16
      if index >= 48 and index <= 49 and h >= 9 : p0[3]=-15
      if index >= 50 and index <= 51 and h >= 9 : p0[3]=-10
      if index == 52 and h >= 9 : p0[3]=-16
      if index == 53 and h >= 9 : p0[3]=-20
      if index >= 56 and index <= 58 and h >= 9 : p0[3]=-20
      if index == 56 and h == 14 : p0[3]=-25
      if index == 61 and h >= 9 : p0[3]=-30
      if index == 62 and h >= 9 : p0[3]=-26
      if index >= 66 and index <= 67 and h >= 9 : p0[3]=-21
      if index == 71 and h >= 9 : p0[3]=-20
      if index == 74 and h >= 9 : p0[3]=-5
      if index == 76 and h >= 9 : p0[3]=-10
      if index == 225 and h >= 9 : p0[3]=-12
      if index == 229 and h <= 20 : p0[3]=-9
      if index >= 24 and index <= 72 and h >= 32 : p0[3]=numpy.nan
      if index >= 204 and index <= 288 and h >= 50 : p0[3]=numpy.nan
     if beam == 1 :
      if index == 11 and h >= 9 : p0[3]=-15
      if index == 23 and h >= 9 : p0[3]=-3
      if index == 33 and h >= 9 : p0[3]=-10
      if index == 36 and h >= 9 : p0[3]=-8
      if index == 38 and h >= 9 : p0[3]=-4
      if index == 39 and h >= 9 : p0[3]=-7
      if index >= 42 and index <= 45 and h >= 9 : p0[3]=-10
      if index == 44 and h >= 9 : p0[3]=-9
      if index == 46 and h >= 9 : p0[3]=-6
      if index == 47 and h >= 9 : p0[3]=-4
      if index >= 48 and index <= 49 and h >= 9 : p0[3]=-6
      if index >= 50 and index <= 51 and h >= 9 : p0[3]=0
      if index == 52 and h >= 9 : p0[3]=-10
      if index == 53 and h >= 9 : p0[3]=-10
      if index == 54 and h >= 9 : p0[3]=-7
      if index == 55 and h >= 9 : p0[3]=-10
      if index >= 56 and index <= 58 and h >= 9 : p0[3]=-15
      if index >= 59 and index <= 59 and h >= 9 : p0[3]=-25
      if index == 60 and h >= 9 : p0[3]=-24
      if index >= 61 and index <= 63 and h >= 9 : p0[3]=-20
      if index == 64 and h >= 9 : p0[3]=-18
      if index == 66 and h >= 9 : p0[3]=-14
      if index >= 68 and index <= 69 and h >= 9 : p0[3]=-17
      if index == 70 and h >= 9 : p0[3]=-10
      if index == 71 and h >= 9 : p0[3]=-14
      if index == 72 and h >= 9 : p0[3]=-15
      if index == 73 and h >= 9 : p0[3]=-5
      if index == 75 and h >= 9 : p0[3]=0
      if index == 76 and h >= 9 : p0[3]=-2
      if index == 76 and h >= 21 : p0[3]=1
      if index == 77 and h >= 9 : p0[3]=2
      if index == 81 and h >= 18 : p0[3]=5
      if index == 245 and h <= 16 : p0[3]=-10

    if year == 2026 and doy == 119:
     if beam == 0 :
      if index == 30 and h >= 9 : p0[3]=-25
      if index == 38 and h >= 9 : p0[3]=-18
      if index == 39 and h >= 9 : p0[3]=-25
      if index >= 40 and index <= 47 and h >= 9 : p0[3]=-20
      if index == 41 and h >= 9 : p0[3]=-22
      if index == 43 and h >= 9 : p0[3]=-22
      if index == 44 and h >= 9 : p0[3]=-28
      if index == 45 and h >= 9 : p0[3]=-25
      if index >= 48 and index <= 52 and h >= 9 : p0[3]=-25
      if index == 53 and h >= 9 : p0[3]=-20
      if index == 54 and h >= 9 : p0[3]=-15
      if index >= 55 and index <= 56 and h >= 9 : p0[3]=-21
      if index == 57 and h >= 9 : p0[3]=-15
      if index == 58 and h >= 9 : p0[3]=-20
      if index == 59 and h >= 9 : p0[3]=-15
      if index >= 60 and index <= 70 and h >= 9 : p0[3]=-20
      if index == 69 and h >= 9 : p0[3]=-25
      if index == 72 and h >= 9 : p0[3]=-20
      if index == 73 and h >= 9 : p0[3]=-9
      if index == 74 and h >= 9 : p0[3]=-5
      if index == 75 and h >= 9 : p0[3]=-1
      if index == 228 and h >= 9 : p0[3]=1
      if index == 232 and h >= 9 : p0[3]=0
      if index == 234 and h >= 9 : p0[3]=0
      if index == 235 and h >= 9 : p0[3]=-8
      if index >= 278 and index <= 279 and h >= 9 : p0[3]=-30
      if index >= 0 and index <= 72 and h >= 32 : p0[3]=numpy.nan
     if beam == 1 :
      if index == 17 and h >= 9 : p0[3]=-24
      if index == 19 and h >= 9 : p0[3]=-22
      if index == 26 and h >= 9 : p0[3]=-18
      if index == 29 and h >= 9 : p0[3]=-17
      if index == 32 and h >= 9 : p0[3]=-15
      if index == 35 and h >= 9 : p0[3]=-11
      if index == 36 and h >= 9 : p0[3]=-10
      if index == 37 and h >= 9 : p0[3]=-16
      if index == 38 and h >= 9 : p0[3]=-15
      if index == 39 and h >= 9 : p0[3]=-18
      if index >= 40 and index <= 43 and h >= 9 : p0[3]=-17
      if index == 42 and h >= 9 : p0[3]=-15
      if index == 44 and h >= 9 : p0[3]=-12
      if index == 45 and h >= 9 : p0[3]=-20
      if index == 46 and h >= 9 : p0[3]=-14
      if index == 47 and h >= 9 : p0[3]=-19
      if index >= 48 and index <= 52 and h >= 9 : p0[3]=-20
      if index == 49 and h <= 17 : p0[3]=-10
      if index == 51 and h >= 9 : p0[3]=-15
      if index == 53 and h >= 9 : p0[3]=-17
      if index == 54 and h >= 9 : p0[3]=-10
      if index >= 55 and index <= 55 and h >= 9 : p0[3]=-14
      if index >= 56 and index <= 59 and h >= 9 : p0[3]=-10
      if index >= 60 and index <= 68 and h >= 9 : p0[3]=-15
      if index == 62 and h >= 9 : p0[3]=-13
      if index >= 69 and index <= 72 and h >= 9 : p0[3]=-20
      if index == 71 and h >= 9 : p0[3]=-18
      if index == 73 and h >= 9 : p0[3]=-5
      if index == 75 and h >= 9 : p0[3]=0
      if index == 76 and h >= 9 : p0[3]=2
      if index == 78 and h >= 9 : p0[3]=4
      if index == 79 and h >= 9 : p0[3]=5
      if index == 81 and h >= 22 : p0[3]=5
      if index == 83 and h >= 20 : p0[3]=6
      if index == 232 and h >= 9 : p0[3]=10
      if index == 239 and h >= 9 : p0[3]=-5
      if index >= 240 and index <= 242 and h >= 9 : p0[3]=-5
      if index == 245 and h >= 9 : p0[3]=-5
      if index == 250 and h >= 9 : p0[3]=-5
      if index == 252 and h >= 9 : p0[3]=-5
      if index >= 273 and index <= 274 and h >= 9 : p0[3]=-20

    if year == 2026 and doy == 118:
     if beam == 0 :
      if index == 11 and h >= 9 : p0[3]=-25
      if index == 15 and h >= 19 : p0[3]=-25
      if index == 21 and h >= 9 : p0[3]=-23
      if index == 25 and h >= 9 : p0[3]=-26
      if index == 31 and h >= 9 : p0[3]=-25
      if index == 36 and h >= 9 : p0[3]=-25
      if index == 39 and h >= 9 : p0[3]=-25
      if index == 45 and h >= 9 : p0[3]=-28
      if index == 48 and h >= 9 : p0[3]=-25
      if index == 49 and h >= 9 : p0[3]=-30
      if index == 51 and h >= 9 : p0[3]=-15
      if index == 52 and h >= 9 : p0[3]=-10
      if index == 53 and h >= 9 : p0[3]=-25
      if index == 54 and h >= 9 : p0[3]=-20
      if index == 55 and h >= 9 : p0[3]=-12
      if index == 56 and h >= 9 : p0[3]=-19
      if index >= 57 and index <= 57 and h >= 9 : p0[3]=-15
      if index >= 58 and index <= 59 and h >= 9 : p0[3]=-20
      if index >= 60 and index <= 66 and h >= 9 : p0[3]=-25
      if index >= 67 and index <= 67 and h >= 9 : p0[3]=-20
      if index == 68 and h >= 9 : p0[3]=-25
      if index >= 69 and index <= 70 and h >= 9 : p0[3]=-15
      if index >= 71 and index <= 72 and h >= 9 : p0[3]=-25
      if index == 73 and h >= 9 : p0[3]=-18
      if index == 76 and h >= 9 : p0[3]=-10
      if index == 77 and h >= 19 : p0[3]=-10
      if index == 218 and h >= 9 : p0[3]=10
      if index == 232 and h >= 9 : p0[3]=-8
      if index >= 24 and index <= 72 and h >= 32 : p0[3]=numpy.nan
      if index >= 204 and index <= 288 and h >= 50 : p0[3]=numpy.nan
     if beam == 1 :
      if index == 11 and h >= 9 : p0[3]=-18
      if index == 12 and h >= 9 : p0[3]=-15
      if index == 33 and h >= 9 : p0[3]=-20
      if index == 36 and h >= 9 : p0[3]=-15
      if index == 38 and h >= 9 : p0[3]=-20
      if index == 39 and h >= 9 : p0[3]=-19
      if index == 40 and h >= 9 : p0[3]=-15
      if index == 41 and h >= 9 : p0[3]=-20
      if index == 42 and h >= 9 : p0[3]=-20
      if index == 43 and h >= 9 : p0[3]=-23
      if index == 44 and h >= 9 : p0[3]=-18
      if index == 45 and h >= 9 : p0[3]=-22
      if index == 46 and h >= 9 : p0[3]=-22
      if index == 47 and h >= 9 : p0[3]=-20
      if index == 48 and h >= 9 : p0[3]=-20
      if index == 49 and h >= 9 : p0[3]=-25
      if index == 50 and h >= 9 : p0[3]=-20
      if index == 51 and h >= 9 : p0[3]=-10
      if index == 52 and h >= 9 : p0[3]=-9
      if index == 53 and h >= 9 : p0[3]=-20
      if index == 54 and h >= 9 : p0[3]=-10
      if index == 55 and h >= 9 : p0[3]=-5
      if index == 56 and h >= 9 : p0[3]=-15
      if index >= 57 and index <= 57 and h >= 9 : p0[3]=-10
      if index >= 58 and index <= 59 and h >= 9 : p0[3]=-15
      if index == 60 and h >= 9 : p0[3]=-18
      if index >= 61 and index <= 66 and h >= 9 : p0[3]=-20
      if index >= 67 and index <= 68 and h >= 9 : p0[3]=-15
      if index >= 69 and index <= 70 and h >= 9 : p0[3]=-10
      if index >= 71 and index <= 72 and h >= 9 : p0[3]=-20
      if index == 76 and h >= 9 : p0[3]=-10
      if index == 77 and h >= 9 : p0[3]=-5
      if index == 81 and h >= 19 : p0[3]=-6
      if index == 82 and h >= 19 : p0[3]=-5
      if index == 219 and h <= 19 : p0[3]=20
      if index == 222 and h <= 22 : p0[3]=20
      if index == 230 and h >= 9 : p0[3]=10
      if index == 234 and h >= 9 : p0[3]=10
      if index == 241 and h >= 9 : p0[3]=-5
      if index >= 269 and index <= 270 and h >= 9 : p0[3]=-20

    if year == 2026 and doy == 117:
     if beam == 0 :
      if index >= 39 and index <= 40 and h >= 9 : p0[3]=-30
      if index == 41 and h >= 9 : p0[3]=-40
      if index == 42 and h >= 9 : p0[3]=-30
      if index == 43 and h >= 9 : p0[3]=-25
      if index == 44 and h >= 9 : p0[3]=-20
      if index == 47 and h >= 9 : p0[3]=-27
      if index == 47 and h == 25 : p0[3]=-37
      if index == 48 and h >= 9 : p0[3]=-20
      if index == 49 and h >= 9 : p0[3]=-25
      if index == 50 and h >= 9 : p0[3]=-26
      if index >= 51 and index <= 51 and h >= 9 : p0[3]=-10
      if index >= 52 and index <= 53 and h >= 9 : p0[3]=-20
      if index >= 54 and index <= 55 and h >= 9 : p0[3]=-15
      if index == 57 and h >= 9 : p0[3]=-22
      if index >= 58 and index <= 63 and h >= 9 : p0[3]=-15
      if index == 59 and h >= 9 : p0[3]=-10
      if index >= 64 and index <= 65 and h >= 9 : p0[3]=-20
      if index >= 66 and index <= 73 and h >= 9 : p0[3]=-15
      if index == 66 and h >= 9 : p0[3]=-19
      if index == 72 and h >= 9 : p0[3]=-10
      if index == 74 and h >= 9 : p0[3]=-5
      if index == 75 and h >= 9 : p0[3]=-2
      if index == 76 and h >= 9 : p0[3]=-4
      if index == 77 and h >= 9 : p0[3]=0
      if index == 78 and h >= 9 : p0[3]=0
      if index == 81 and h >= 9 : p0[3]=0
      if index == 216 and h == 16 : p0[3]=15 #numpy.nan
      if index == 232 and h >= 9 : p0[3]=5
      if index == 233 and h >= 9 : p0[3]=2
      if index == 236 and h >= 9 : p0[3]=-6
      if index == 255 and h >= 9 : p0[3]=-30
      if index >= 0 and index <= 72 and h >= 32 : p0[3]=numpy.nan
      if index >= 204 and index <= 288 and h >= 50 : p0[3]=numpy.nan
     if beam == 1 :
      if index == 26 and h >= 9 : p0[3]=-15
      if index == 27 and h >= 9 : p0[3]=-20
      if index == 30 and h >= 9 : p0[3]=-15
      if index == 34 and h >= 9 : p0[3]=-15
      if index == 36 and h >= 9 : p0[3]=-20
      if index == 38 and h >= 9 : p0[3]=-15
      if index == 39 and h >= 9 : p0[3]=-18
      if index >= 40 and index <= 40 and h >= 9 : p0[3]=-21
      if index == 41 and h >= 9 : p0[3]=-26
      if index == 42 and h >= 9 : p0[3]=-25
      if index == 43 and h >= 9 : p0[3]=-20
      if index == 47 and h >= 9 : p0[3]=-8
      if index == 48 and h >= 9 : p0[3]=-15
      if index == 49 and h >= 9 : p0[3]=-20
      if index >= 50 and index <= 51 and h >= 9 : p0[3]=-5
      if index >= 52 and index <= 53 and h >= 9 : p0[3]=-15
      if index >= 54 and index <= 55 and h >= 9 : p0[3]=-10
      if index >= 58 and index <= 63 and h >= 9 : p0[3]=-10
      if index == 59 and h >= 9 : p0[3]=-4
      if index == 61 and h >= 9 : p0[3]=-18
      if index == 62 and h >= 9 : p0[3]=-12
      if index >= 64 and index <= 65 and h >= 9 : p0[3]=-15
      if index >= 66 and index <= 70 and h >= 9 : p0[3]=-10
      if index == 71 and h >= 9 : p0[3]=-1
      if index == 72 and h >= 9 : p0[3]=-5
      if index == 73 and h >= 9 : p0[3]=-4
      if index == 74 and h >= 9 : p0[3]=-5
      if index == 76 and h >= 9 : p0[3]=1
      if index == 77 and h >= 9 : p0[3]=2
      if index == 217 and h <= 21 : p0[3]=21
      if index == 223 and h >= 9 : p0[3]=30
      if index == 229 and h >= 9 : p0[3]=25
      if index == 233 and h >= 9 : p0[3]=10
      if index == 237 and h >= 9 : p0[3]=6
      if index == 242 and h >= 9 : p0[3]=-5
      if index == 243 and h >= 9 : p0[3]=-8
      if index == 247 and h >= 9 : p0[3]=-8
      if index == 255 and h >= 9 : p0[3]=-20

    if year == 2026 and doy == 116:
     if beam == 0 :
      if index == 30 and h >= 9 : p0[3]=-10
      if index == 33 and h >= 9 : p0[3]=-20
      if index == 43 and h >= 9 : p0[3]=-35
      if index == 45 and h >= 9 : p0[3]=-29
      if index == 46 and h >= 9 : p0[3]=-32
      if index >= 47 and index <= 47 and h >= 9 : p0[3]=-35
      if index >= 48 and index <= 51 and h >= 9 : p0[3]=-40
      if index == 50 and h >= 9 : p0[3]=-45
      if index >= 52 and index <= 53 and h >= 9 : p0[3]=-35
      if index == 54 and h >= 9 : p0[3]=-30
      if index >= 55 and index <= 56 and h >= 9 : p0[3]=-20
      if index == 57 and h >= 9 : p0[3]=-5
      if index == 58 and h >= 9 : p0[3]=-4
      if index == 59 and h >= 9 : p0[3]=-4
      if index == 60 and h >= 9 : p0[3]=0
      if index == 71 and h >= 9 : p0[3]=-4
      if index == 72 and h >= 9 : p0[3]=-4
      if index == 73 and h >= 9 : p0[3]=-5
      if index == 74 and h >= 9 : p0[3]=-3
      if index == 78 and h >= 9 : p0[3]=-5
      if index == 229 and h >= 9 : p0[3]=8
      if index == 231 and h >= 9 : p0[3]=8
      if index == 235 and h >= 9 : p0[3]=-5
      if index == 236 and h >= 9 : p0[3]=0
      if index == 239 and h >= 9 : p0[3]=-5
      if index == 241 and h >= 9 : p0[3]=-12
      if index == 242 and h >= 9 : p0[3]=-10
      if index == 243 and h >= 9 : p0[3]=-13
      if index >= 0 and index <= 72 and h >= 32 : p0[3]=numpy.nan
     if beam == 1 :
      if index == 12 and h >= 9 : p0[3]=-5
      if index == 13 and h >= 9 : p0[3]=-5
      if index == 37 and h >= 9 : p0[3]=-14
      if index == 38 and h >= 9 : p0[3]=-22
      if index == 40 and h >= 9 : p0[3]=-25
      if index == 41 and h >= 9 : p0[3]=-25
      if index >= 42 and index <= 47 and h >= 9 : p0[3]=-30
      if index == 43 and h >= 9 : p0[3]=-26
      if index == 44 and h >= 9 : p0[3]=-25
      if index == 45 and h >= 9 : p0[3]=-25
      if index == 48 and h >= 9 : p0[3]=-35
      if index == 50 and h >= 9 : p0[3]=-40
      if index == 51 and h >= 9 : p0[3]=-35
      if index >= 52 and index <= 53 and h >= 9 : p0[3]=-30
      if index == 54 and h >= 9 : p0[3]=-25
      if index >= 55 and index <= 56 and h >= 9 : p0[3]=-15
      if index >= 57 and index <= 59 and h >= 9 : p0[3]=4
      if index == 60 and h >= 9 : p0[3]=5
      if index == 63 and h >= 9 : p0[3]=-1
      if index == 67 and h >= 9 : p0[3]=-5
      if index == 68 and h >= 9 : p0[3]=-3
      if index == 69 and h >= 9 : p0[3]=-3
      if index == 70 and h >= 9 : p0[3]=-1
      if index == 74 and h >= 9 : p0[3]=-6
      if index >= 75 and index <= 77 and h >= 9 : p0[3]=0
      if index == 216 and h <= 20 : p0[3]=25
      if index == 226 and h >= 9 : p0[3]=22
      if index == 228 and h >= 9 : p0[3]=20
      if index == 230 and h >= 9 : p0[3]=20
      if index == 231 and h <= 22 : p0[3]=10
      if index == 233 and h >= 9 : p0[3]=9
      if index == 234 and h >= 9 : p0[3]=2
      if index == 239 and h >= 9 : p0[3]=0
      if index == 241 and h >= 9 : p0[3]=-5
      if index == 249 and h >= 9 : p0[3]=-10

    if year == 2026 and doy == 115:  #25
     if beam == 0 :
      if index >= 35 and index <= 36 and h >= 9 : p0[3]=-10
      if index == 38 and h >= 9 : p0[3]=-10
      if index == 39 and h >= 9 : p0[3]=-15
      if index == 46 and h >= 9 : p0[3]=-17
      if index == 47 and h >= 9 : p0[3]=-21
      if index >= 49 and index <= 50 and h >= 9 : p0[3]=-20
      if index == 52 and h >= 9 : p0[3]=-15
      if index == 55 and h >= 9 : p0[3]=-10
      if index >= 58 and index <= 59 and h >= 9 : p0[3]=-20
      if index == 61 and h >= 9 : p0[3]=-20
      if index >= 62 and index <= 63 and h >= 9 : p0[3]=-15
      if index == 65 and h >= 9 : p0[3]=-25
      if index >= 66 and index <= 66 and h >= 9 : p0[3]=-15
      if index == 68 and h >= 9 : p0[3]=-20
      if index == 69 and h >= 9 : p0[3]=-10
      if index == 70 and h >= 9 : p0[3]=-25
      if index == 71 and h >= 9 : p0[3]=-18
      if index == 72 and h >= 9 : p0[3]=-25
      if index == 74 and h >= 9 : p0[3]=-10
      if index == 75 and h >= 9 : p0[3]=-10
      if index == 220 and h <= 20 : p0[3]=5
      if index == 222 and h <= 18 : p0[3]=-1
      if index >= 0 and index <= 288 and h >= 50 : p0[3]=numpy.nan
     if beam == 1 :
      if index == 18 and h <= 18 : p0[3]=-8
      if index == 19 and h >= 18 : p0[3]=-10
      if index == 20 and h >= 9 : p0[3]=-7
      if index == 23 and h >= 9 : p0[3]=-1
      if index == 26 and h >= 9 : p0[3]=-2
      if index == 29 and h >= 9 : p0[3]=-5
      if index == 31 and h >= 9 : p0[3]=-5
      if index == 32 and h <= 19 : p0[3]=0
      if index == 34 and h >= 9 : p0[3]=-2
      if index == 35 and h >= 9 : p0[3]=-3
      if index == 36 and h >= 9 : p0[3]=-6
      if index == 37 and h >= 9 : p0[3]=-5
      if index == 41 and h >= 9 : p0[3]=-5
      if index == 42 and h >= 9 : p0[3]=-8
      if index == 44 and h >= 9 : p0[3]=-10
      if index == 45 and h >= 9 : p0[3]=-10
      if index == 46 and h >= 9 : p0[3]=-11
      if index >= 47 and index <= 50 and h >= 9 : p0[3]=-15
      if index == 49 and h >= 9 : p0[3]=-10
      if index == 50 and h >= 9 : p0[3]=-13
      if index == 51 and h >= 9 : p0[3]=-10
      if index == 52 and h >= 9 : p0[3]=-5
      if index == 53 and h >= 9 : p0[3]=-18
      if index == 55 and h >= 9 : p0[3]=-10
      if index == 56 and h >= 9 : p0[3]=-17
      if index >= 57 and index <= 58 and h >= 9 : p0[3]=-10
      if index == 59 and h >= 9 : p0[3]=-12
      if index >= 60 and index <= 61 and h >= 9 : p0[3]=-15
      if index >= 62 and index <= 66 and h >= 9 : p0[3]=-10
      if index == 63 and h >= 9 : p0[3]=-12
      if index == 64 and h >= 9 : p0[3]=-16
      if index == 67 and h >= 9 : p0[3]=-15
      if index == 68 and h >= 9 : p0[3]=-15
      if index == 69 and h >= 9 : p0[3]=-5
      if index == 70 and h >= 9 : p0[3]=-20
      if index == 71 and h >= 9 : p0[3]=-15
      if index == 72 and h >= 9 : p0[3]=-20
      if index == 75 and h >= 9 : p0[3]=-9
      if index == 206 and h >= 9 : p0[3]=10   
      if index == 221 and h <= 19 : p0[3]=5
      if index == 234 and h >= 9 : p0[3]=-2
      if index == 234 and h == 17 : p0[3]=numpy.nan

    if year == 2026 and doy == 114:
     if beam == 0 :
      if index == 33 and h <= 19 : p0[3]=-30
      if index == 36 and h >= 9 : p0[3]=-23
      if index == 44 and h >= 9 : p0[3]=-20
      if index >= 45 and index <= 46 and h >= 9 : p0[3]=-20
      if index >= 47 and index <= 48 and h >= 9 : p0[3]=-15
      if index == 49 and h >= 9 : p0[3]=-11
      if index == 50 and h >= 9 : p0[3]=-12
      if index >= 51 and index <= 52 and h >= 9 : p0[3]=-11
      if index == 55 and h >= 9 : p0[3]=-12
      if index == 64 and h >= 9 : p0[3]=-10
      if index == 65 and h >= 9 : p0[3]=-5
      if index == 69 and h >= 9 : p0[3]=0
      if index == 70 and h >= 9 : p0[3]=0
      if index == 72 and h >= 9 : p0[3]=-1
      if index == 232 and h >= 9 : p0[3]=20
      if index == 233 and h >= 9 : p0[3]=15
     if beam == 1 :
      if index == 33 and h <= 17 : p0[3]=-28
      if index == 36 and h >= 9 : p0[3]=-15
      if index == 38 and h >= 9 : p0[3]=-10
      if index == 40 and h >= 9 : p0[3]=-1
      if index == 42 and h >= 9 : p0[3]=-13
      if index == 43 and h >= 9 : p0[3]=-10
      if index >= 45 and index <= 46 and h >= 9 : p0[3]=-15
      if index >= 47 and index <= 48 and h >= 9 : p0[3]=-10
      if index == 49 and h >= 9 : p0[3]=0
      if index == 50 and h >= 9 : p0[3]=-1
      if index >= 51 and index <= 51 and h >= 9 : p0[3]=-5
      if index == 52 and h >= 9 : p0[3]=-3
      if index == 55 and h >= 9 : p0[3]=-5
      if index == 57 and h >= 9 : p0[3]=-6
      if index == 62 and h >= 9 : p0[3]=-2
      if index == 64 and h >= 9 : p0[3]=-5
      if index == 65 and h >= 9 : p0[3]=2
      if index == 69 and h >= 9 : p0[3]=0
      if index >= 70 and index <= 71 and h >= 9 : p0[3]=7
      if index >= 72 and index <= 73 and h >= 9 : p0[3]=1
      if index == 74 and h >= 9 : p0[3]=3
      if index == 75 and h >= 9 : p0[3]=5
      if index == 229 and h >= 9 : p0[3]=30
      if index == 230 and h >= 9 : p0[3]=35
      if index == 231 and h >= 9 : p0[3]=30
      if index == 232 and h >= 9 : p0[3]=35
      if index == 233 and h >= 9 : p0[3]=30
      if index == 237 and h >= 9 : p0[3]=15
      if index == 239 and h >= 9 : p0[3]=10

    if year == 2026 and doy == 113:
     if beam == 0 :
      if index == 215 and h <= 18 : p0[3]=10
      if index == 218 and h <= 21 : p0[3]=12
      if index == 220 and h <= 20 : p0[3]=20
      if index == 235 and h >= 9 : p0[3]=5
      if index == 237 and h >= 9 : p0[3]=-2
      if index == 238 and h >= 9 : p0[3]=-5
      if index == 239 and h >= 9 : p0[3]=-7
      if index == 256 and h >= 9 : p0[3]=-15
     if beam == 1 :
      if index == 254 and h >= 9 : p0[3]=-5

    if year == 2026 and doy == 110: #20
     if beam == 0 :
      if index == 10 and h >= 25 : p0[3]=-15
      if index == 17 and h >= 27 : p0[3]=-18
      if index == 35 and h >= 9 : p0[3]=-40
      if index == 37 and h >= 9 : p0[3]=-43
      if index == 38 and h >= 9 : p0[3]=-40
      if index == 42 and h >= 9 : p0[3]=-41
      if index == 44 and h >= 9 : p0[3]=-37
      if index == 45 and h >= 9 : p0[3]=-30
      if index >= 47 and index <= 49 and h >= 9 : p0[3]=-35
      if index >= 50 and index <= 52 and h >= 9 : p0[3]=-30
      if index == 53 and h >= 9 : p0[3]=-25
      if index == 53 and h >= 33 : p0[3]=numpy.nan
      if index >= 54 and index <= 67 and h >= 9 : p0[3]=-20
      if index == 55 and h >= 9 : p0[3]=-30
      if index == 56 and h >= 9 : p0[3]=-30
      if index == 57 and h >= 9 : p0[3]=-20
      if index == 59 and h >= 9 : p0[3]=-27
      if index == 68 and h >= 9 : p0[3]=-32
      if index >= 69 and index <= 71 and h >= 9 : p0[3]=-25
      if index == 70 and h >= 9 : p0[3]=-31
      if index == 72 and h >= 9 : p0[3]=-30
      if index == 74 and h >= 9 : p0[3]=-30
      if index == 75 and h >= 9 : p0[3]=-20
      if index >= 24 and index <= 120 and h >= 32 : p0[3]=numpy.nan
     if beam == 1 :
      if index == 6 and h >= 27 : p0[3]=-4
      if index == 17 and h >= 21 : p0[3]=-8
      if index == 31 and h <= 17 : p0[3]=-20
      if index == 33 and h >= 9 : p0[3]=-25
      if index == 34 and h >= 9 : p0[3]=-25
      if index == 35 and h >= 9 : p0[3]=-35
      if index == 40 and h >= 9 : p0[3]=-40
      if index == 41 and h >= 9 : p0[3]=-35
      if index == 42 and h >= 9 : p0[3]=-30
      if index == 43 and h >= 9 : p0[3]=-35
      if index == 44 and h >= 9 : p0[3]=-30
      if index == 46 and h >= 9 : p0[3]=-25
      if index >= 47 and index <= 49 and h >= 9 : p0[3]=-30
      if index >= 50 and index <= 51 and h >= 9 : p0[3]=-25
      if index >= 52 and index <= 53 and h >= 9 : p0[3]=-20
      if index >= 54 and index <= 67 and h >= 9 : p0[3]=-15
      if index == 55 and h >= 9 : p0[3]=-10
      if index == 56 and h >= 9 : p0[3]=-20
      if index == 57 and h >= 9 : p0[3]=-5
      if index == 68 and h >= 9 : p0[3]=-22
      if index >= 69 and index <= 71 and h >= 9 : p0[3]=-20
      if index == 70 and h >= 9 : p0[3]=-21
      if index == 72 and h >= 9 : p0[3]=-28
      if index == 73 and h >= 9 : p0[3]=-18
      if index == 74 and h >= 9 : p0[3]=-20
      if index == 75 and h >= 9 : p0[3]=-19
      if index == 77 and h >= 9 : p0[3]=-18
      
    if year == 2026 and doy == 109:
     if beam == 0 :
      if index == 3 and h >= 27 : p0[3]=-20
      if index == 36 and h >= 9 : p0[3]=-5
      if index == 43 and h >= 28 : p0[3]=0
      if index == 50 and h >= 9 : p0[3]=-8
      if index == 53 and h >= 9 : p0[3]=-7
      if index == 63 and h >= 9 : p0[3]=3
      if index == 64 and h >= 9 : p0[3]=0
      if index == 66 and h >= 9 : p0[3]=3
      if index == 67 and h >= 9 : p0[3]=-5
      if index == 68 and h >= 9 : p0[3]=-12
      if index >= 85 and index <= 87 and h >= 14 and h <= 17 : p0[3]=numpy.nan
      if index == 88 and h >= 14 and h <= 16 : p0[3]=numpy.nan
      if index == 229 and h >= 26 : p0[3]=-5
      if index == 235 and h >= 9 : p0[3]=-12
      if index >= 0 and index <= 288 and h >= 50 : p0[3]=numpy.nan
     if beam == 1 :
      if index == 55 and h >= 9 : p0[3]=-5
      if index == 63 and h >= 9 : p0[3]=10
      if index == 69 and h >= 9 : p0[3]=0
      if index == 217 and h <= 20 : p0[3]=20
      if index == 218 and h >= 9 : p0[3]=20

    if year == 2026 and doy == 108:
     if beam == 0 :
      if index == 20 and h >= 9 : p0[3]=-18
      if index == 24 and h <= 17 : p0[3]=-25
      if index == 31 and h >= 9 : p0[3]=-30
      if index == 32 and h >= 9 : p0[3]=-30
      if index == 33 and h >= 9 : p0[3]=-40
      if index == 34 and h >= 9 : p0[3]=-30
      if index == 41 and h >= 9 : p0[3]=-45
      if index == 42 and h >= 9 : p0[3]=-25
      if index == 43 and h >= 9 : p0[3]=-20
      if index == 46 and h >= 9 : p0[3]=8
      if index == 54 and h >= 29 : p0[3]=50
      if index == 55 and h >= 29 : p0[3]=40
      if index == 56 and h >= 29 : p0[3]=10
      if index == 57 and h >= 9 : p0[3]=-10
      if index == 58 and h >= 9 : p0[3]=-30
      if index == 59 and h >= 9 : p0[3]=-20
      if index == 60 and h >= 9 : p0[3]=-15
      if index == 61 and h >= 9 : p0[3]=-5
      if index == 64 and h >= 9 : p0[3]=30
      if index == 78 and h >= 9 : p0[3]=-15
      if index == 83 and h >= 18 : p0[3]=0
      if index == 220 and h <= 20 : p0[3]=30
      if index == 222 and h <= 22 : p0[3]=32
      if index == 224 and h >= 9 : p0[3]=32
      if index == 227 and h >= 9 : p0[3]=25
      if index == 229 and h >= 9 : p0[3]=30
      if index == 233 and h >= 9 : p0[3]=15
      if index >= 234 and index <= 235 and h >= 9 : p0[3]=15
      if index == 241 and h >= 9 : p0[3]=-15
      if index == 250 and h >= 9 : p0[3]=-25
      if index == 253 and h >= 9 : p0[3]=-5
      if index == 254 and h >= 9 : p0[3]=-10
      if index >= 255 and index <= 256 and h >= 9 : p0[3]=-10
      if index == 259 and h >= 9 : p0[3]=-25
     if beam == 1 :
      if index == 22 and h >= 9 : p0[3]=-15
      if index == 30 and h >= 9 : p0[3]=-21
      if index == 31 and h >= 9 : p0[3]=-24
      if index == 33 and h >= 9 : p0[3]=-28
      if index == 34 and h >= 9 : p0[3]=-25
      if index == 37 and h >= 9 : p0[3]=-30
      if index == 35 and h >= 9 : p0[3]=-27
      if index == 36 and h >= 9 : p0[3]=-23
      if index == 38 and h >= 9 : p0[3]=-37
      if index == 39 and h >= 9 : p0[3]=-40
      if index == 40 and h >= 9 : p0[3]=-38
      if index == 41 and h >= 9 : p0[3]=-35
      if index == 42 and h >= 9 : p0[3]=-20
      if index == 43 and h >= 9 : p0[3]=-10
      if index == 44 and h >= 9 : p0[3]=5
      if index == 46 and h >= 9 : p0[3]=11
      if index == 47 and h >= 9 : p0[3]=25
      if index == 48 and h >= 9 : p0[3]=25
      if index == 49 and h >= 9 : p0[3]=30
      if index == 50 and h >= 9 : p0[3]=65
      if index == 51 and h >= 9 : p0[3]=70
      if index == 53 and h >= 9 : p0[3]=90
      if index == 54 and h >= 29 : p0[3]=60
      if index == 54 and h <= 27 : p0[3]=100
      if index == 55 and h >= 29 : p0[3]=40
      if index == 56 and h >= 29 : p0[3]=20
      if index == 57 and h >= 9 : p0[3]=0
      if index == 58 and h >= 9 : p0[3]=-20
      if index == 59 and h >= 9 : p0[3]=-10
      if index == 60 and h >= 9 : p0[3]=-10
      if index == 61 and h >= 9 : p0[3]=0
      if index == 62 and h >= 9 : p0[3]=20
      if index == 63 and h >= 9 : p0[3]=30
      if index >= 65 and index <= 66 and h >= 9 : p0[3]=40
      if index == 75 and h >= 9 : p0[3]=-10
      if index == 76 and h >= 9 : p0[3]=-10
      if index == 79 and h >= 9 : p0[3]=-6
      if index == 227 and h >= 9 : p0[3]=36
      if index >= 229 and index <= 230 and h >= 9 : p0[3]=35
      if index == 231 and h >= 9 : p0[3]=25
      if index == 234 and h >= 9 : p0[3]=25
      if index == 240 and h >= 9 : p0[3]=2
      if index >= 241 and index <= 243 and h >= 9 : p0[3]=-5
      if index == 249 and h >= 9 : p0[3]=-10
      if index == 250 and h >= 9 : p0[3]=-16
      if index == 253 and h >= 9 : p0[3]=5
      if index == 255 and h >= 9 : p0[3]=0

    if year == 2026 and doy == 107:
     if beam == 0 :
      if index == 29 and h >= 18 : p0[3]=-38
      if index == 35 and h >= 9 : p0[3]=-40
      if index == 37 and h >= 9 : p0[3]=-40
      if index == 40 and h >= 9 : p0[3]=-30
      if index == 41 and h >= 9 : p0[3]=-42
      if index >= 42 and index <= 43 and h >= 9 : p0[3]=-35
      if index == 44 and h >= 9 : p0[3]=-30
      if index == 45 and h >= 9 : p0[3]=-40
      if index == 46 and h >= 9 : p0[3]=-35
      if index == 48 and h >= 9 : p0[3]=-30
      if index == 49 and h >= 9 : p0[3]=-35
      if index >= 50 and index <= 51 and h >= 9 : p0[3]=-15
      if index >= 52 and index <= 53 and h >= 9 : p0[3]=-20
      if index == 54 and h >= 9 : p0[3]=-25
      if index == 55 and h >= 9 : p0[3]=-30
      if index == 56 and h >= 9 : p0[3]=-30
      if index >= 57 and index <= 70 and h >= 9 : p0[3]=-25
      if index == 59 and h >= 9 : p0[3]=-26
      if index == 64 and h >= 9 : p0[3]=-30
      if index == 69 and h >= 29 : p0[3]=-22
      if index >= 71 and index <= 72 and h >= 9 : p0[3]=-6
      if index == 73 and h >= 9 : p0[3]=-15
      if index == 74 and h >= 9 : p0[3]=-11
      if index >= 75 and index <= 76 and h >= 9 : p0[3]=-10
      if index == 77 and h >= 9 : p0[3]=-5
      if index == 221 and h <= 21 : p0[3]=40
      if index == 226 and h >= 9 : p0[3]=40
      if index == 228 and h >= 9 : p0[3]=35
      if index == 229 and h >= 9 : p0[3]=30
      if index == 230 and h >= 9 : p0[3]=25
      if index == 235 and h >= 9 : p0[3]=10
      if index == 239 and h >= 9 : p0[3]=-15
      if index == 241 and h >= 9 : p0[3]=-10
      if index >= 243 and index <= 244 and h >= 9 : p0[3]=-10
      if index == 248 and h >= 9 : p0[3]=-30
      if index >= 250 and index <= 252 and h >= 9 : p0[3]=-30
      if index == 251 and h >= 9 : p0[3]=-33
      if index == 254 and h >= 9 : p0[3]=-25
      if index == 255 and h >= 9 : p0[3]=-30
      if index == 256 and h >= 9 : p0[3]=-40
      if index == 257 and h >= 9 : p0[3]=-39
      if index >= 0 and index <= 72 and h >= 32 : p0[3]=numpy.nan
     if beam == 1 :
      if index == 14 and h >= 22 : p0[3]=-20
      if index == 15 and h >= 22 : p0[3]=-22
      if index == 29 and h >= 18 : p0[3]=-25
      if index == 32 and h >= 9 : p0[3]=-32
      if index == 35 and h >= 9 : p0[3]=-30
      if index == 36 and h >= 9 : p0[3]=-25
      if index >= 38 and index <= 39 and h >= 9 : p0[3]=-30
      if index == 40 and h >= 9 : p0[3]=-20
      if index == 41 and h >= 9 : p0[3]=-30
      if index >= 42 and index <= 43 and h >= 9 : p0[3]=-25
      if index == 44 and h >= 9 : p0[3]=-20
      if index == 45 and h >= 9 : p0[3]=-35
      if index == 46 and h >= 9 : p0[3]=-30
      if index == 47 and h >= 9 : p0[3]=-33
      if index == 48 and h >= 9 : p0[3]=-25
      if index == 49 and h >= 9 : p0[3]=-20
      if index >= 50 and index <= 51 and h >= 9 : p0[3]=-8
      if index >= 52 and index <= 53 and h >= 9 : p0[3]=-15
      if index == 54 and h >= 9 : p0[3]=-20
      if index == 55 and h >= 9 : p0[3]=-25
      if index == 56 and h >= 9 : p0[3]=-25
      if index >= 57 and index <= 70 and h >= 9 : p0[3]=-20
      if index == 59 and h >= 9 : p0[3]=-5
      if index == 62 and h >= 9 : p0[3]=-18
      if index == 64 and h >= 9 : p0[3]=-25
      if index >= 71 and index <= 72 and h >= 9 : p0[3]=-4
      if index == 73 and h >= 9 : p0[3]=-10
      if index >= 74 and index <= 74 and h >= 9 : p0[3]=0
      if index == 75 and h >= 9 : p0[3]=1
      if index == 76 and h >= 9 : p0[3]=-1
      if index == 77 and h >= 9 : p0[3]=-2
      if index == 220 and h <= 20 : p0[3]=35
      if index == 225 and h >= 9 : p0[3]=48
      if index == 226 and h >= 9 : p0[3]=50
      if index == 227 and h >= 9 : p0[3]=55
      if index == 228 and h >= 9 : p0[3]=45
      if index == 233 and h >= 9 : p0[3]=25
      if index == 234 and h >= 9 : p0[3]=20
      if index == 237 and h >= 9 : p0[3]=17
      if index == 238 and h >= 9 : p0[3]=15
      if index == 240 and h >= 9 : p0[3]=-5
      if index == 241 and h >= 9 : p0[3]=-5
      if index == 247 and h >= 9 : p0[3]=-15
      if index == 248 and h >= 9 : p0[3]=-20
      if index == 249 and h >= 9 : p0[3]=-15
      if index == 254 and h >= 9 : p0[3]=-15
      if index == 255 and h >= 9 : p0[3]=-20
      if index == 257 and h >= 9 : p0[3]=-25
      if index >= 267 and index <= 268 and h >= 9 : p0[3]=-40
      if index == 269 and h >= 9 : p0[3]=-35

    if year == 2026 and doy == 106:
     if beam == 0 :
      if index == 12 and h >= 9 : p0[3]=-30
      if index == 13 and h >= 21 : p0[3]=-30
      if index == 25 and h >= 9 : p0[3]=-30
      if index == 31 and h >= 9 : p0[3]=-22
      if index == 33 and h >= 9 : p0[3]=-23
      if index >= 34 and index <= 35 and h >= 9 : p0[3]=-20
      if index >= 37 and index <= 38 and h >= 9 : p0[3]=-20
      if index == 41 and h >= 9 : p0[3]=-20
      if index == 43 and h == 18 : p0[3]=-30
      if index >= 45 and index <= 49 and h >= 9 : p0[3]=-15
      if index == 46 and h == 19 : p0[3]=numpy.nan
      if index == 47 and h >= 9 : p0[3]=-20
      if index == 51 and h >= 9 : p0[3]=-11
      if index == 52 and h >= 9 : p0[3]=-15
      if index == 53 and h >= 9 : p0[3]=-20
      if index == 54 and h >= 9 : p0[3]=-15
      if index == 55 and h >= 9 : p0[3]=-20
      if index >= 56 and index <= 66 and h >= 9 : p0[3]=-15
      if index == 60 and h >= 9 : p0[3]=-20
      if index >= 67 and index <= 68 and h >= 9 : p0[3]=-20
      if index >= 69 and index <= 70 and h >= 9 : p0[3]=-15
      if index == 71 and h >= 9 : p0[3]=-22
      if index == 71 and h >= 26 : p0[3]=-30
      if index == 72 and h >= 9 : p0[3]=-14
      if index == 73 and h >= 9 : p0[3]=-13
      if index >= 74 and index <= 76 and h >= 9 : p0[3]=-5
      if index == 77 and h >= 9 : p0[3]=-6
      if index == 79 and h >= 9 : p0[3]=-4
      if index == 83 and h >= 9 : p0[3]=-3
      if index == 219 and h >= 20 : p0[3]=18
      if index == 220 and h >= 29 : p0[3]=20
      if index == 224 and h >= 9 : p0[3]=20
      #if index == 225 and h >= 9 : p0[3]=20
      if index == 226 and h >= 9 : p0[3]=18
      if index == 242 and h >= 9 : p0[3]=-5
      if index >= 36 and index <= 72 and h >= 33 : p0[3]=numpy.nan
     if beam == 1 :
      if index == 21 and h <= 17 : p0[3]=-20
      if index == 25 and h >= 9 : p0[3]=-20
      if index == 31 and h >= 9 : p0[3]=-18
      if index >= 34 and index <= 38 and h >= 9 : p0[3]=-15
      if index == 36 and h >= 9 : p0[3]=-18
      if index == 39 and h >= 9 : p0[3]=-18
      if index == 40 and h >= 9 : p0[3]=-10
      if index == 41 and h >= 9 : p0[3]=-15
      if index >= 42 and index <= 43 and h >= 9 : p0[3]=-10
      if index == 44 and h >= 9 : p0[3]=-5
      if index >= 45 and index <= 52 and h >= 9 : p0[3]=-10
      if index == 47 and h >= 9 : p0[3]=-12
      if index == 47 and h == 17 : p0[3]=numpy.nan
      if index == 51 and h >= 9 : p0[3]=-6
      if index == 52 and h >= 9 : p0[3]=-10
      if index == 53 and h >= 9 : p0[3]=-10
      if index == 54 and h >= 9 : p0[3]=-10
      if index == 55 and h >= 9 : p0[3]=-15
      if index == 56 and h >= 9 : p0[3]=-8
      if index == 57 and h >= 9 : p0[3]=-8
      if index >= 58 and index <= 65 and h >= 9 : p0[3]=-10
      if index == 65 and h == 29 : p0[3]=-1 #0 numpy.nan
      if index == 60 and h >= 9 : p0[3]=-15
      if index == 66 and h >= 9 : p0[3]=-5
      if index >= 67 and index <= 68 and h >= 9 : p0[3]=-15
      if index >= 69 and index <= 69 and h >= 9 : p0[3]=-10
      if index == 70 and h >= 9 : p0[3]=-8
      if index == 71 and h >= 9 : p0[3]=-13
      if index == 72 and h >= 9 : p0[3]=-9
      if index == 73 and h >= 9 : p0[3]=-6
      if index == 74 and h >= 9 : p0[3]=0
      if index == 75 and h >= 9 : p0[3]=-3
      if index == 77 and h <= 25 : p0[3]=-3
      if index == 77 and h >= 26 : p0[3]=numpy.nan
      if index == 78 and h >= 9 : p0[3]=-2
      if index == 219 and h >= 9 : p0[3]=25

    if year == 2026 and doy == 105:  #15
     if beam == 0 :
      if index == 37 and h >= 9 : p0[3]=-23
      if index == 45 and h >= 19 : p0[3]=-25
      if index == 48 and h >= 9 : p0[3]=-25
      if index == 50 and h >= 9 : p0[3]=-20
      if index >= 51 and index <= 52 and h >= 9 : p0[3]=-25
      if index == 53 and h >= 9 : p0[3]=-20
      if index >= 54 and index <= 61 and h >= 9 : p0[3]=-25
      if index == 57 and h >= 9 : p0[3]=-30
      if index == 60 and h >= 9 : p0[3]=-30
      if index >= 63 and index <= 63 and h >= 9 : p0[3]=-20
      if index == 62 and h >= 9 : p0[3]=-23
      if index == 64 and h >= 9 : p0[3]=-25
      if index >= 65 and index <= 66 and h >= 9 : p0[3]=-30
      if index == 67 and h >= 9 : p0[3]=-23
      if index == 68 and h >= 9 : p0[3]=-30
      if index == 69 and h >= 9 : p0[3]=-30
      if index >= 70 and index <= 72 and h >= 9 : p0[3]=-25
      if index == 73 and h >= 9 : p0[3]=-20
      if index == 74 and h >= 9 : p0[3]=-15
      if index == 75 and h >= 9 : p0[3]=-10
      if index >= 76 and index <= 77 and h >= 9 : p0[3]=-5
      if index == 232 and h >= 9 : p0[3]=15
      if index == 233 and h >= 9 : p0[3]=10
      if index == 239 and h >= 9 : p0[3]=5
      if index == 243 and h >= 9 : p0[3]=-10
      if index == 244 and h >= 9 : p0[3]=-5
      if index >= 245 and index <= 247 and h >= 9 : p0[3]=-5
      if index == 248 and h >= 9 : p0[3]=-12
      if index == 249 and h >= 9 : p0[3]=-10
      if index == 250 and h >= 9 : p0[3]=-10
      if index == 251 and h >= 9 : p0[3]=-15
      if index == 252 and h >= 9 : p0[3]=-20
      if index == 253 and h >= 9 : p0[3]=-20
      if index >= 254 and index <= 255 and h >= 9 : p0[3]=-28
      if index == 257 and h >= 9 : p0[3]=-30
      if index == 260 and h >= 9 : p0[3]=-35
      if index == 272 and h >= 9 : p0[3]=-25
      if index >= 0 and index <= 72 and h >= 32 : p0[3]=numpy.nan
     if beam == 1 :
      if index == 28 and h >= 9 : p0[3]=-15
      if index == 30 and h >= 9 : p0[3]=-15
      if index == 33 and h >= 9 : p0[3]=-16
      if index == 34 and h >= 9 : p0[3]=-15
      if index == 36 and h >= 9 : p0[3]=-15
      if index == 37 and h >= 9 : p0[3]=-18
      if index == 38 and h >= 9 : p0[3]=-15
      if index == 40 and h >= 9 : p0[3]=-17
      if index == 44 and h >= 9 : p0[3]=-18
      if index >= 45 and index <= 46 and h >= 9 : p0[3]=-20
      if index == 45 and h >= 20 : p0[3]=-15
      if index >= 48 and index <= 49 and h >= 9 : p0[3]=-19
      if index == 52 and h >= 9 : p0[3]=-20
      if index >= 53 and index <= 54 and h >= 9 : p0[3]=-14
      if index >= 55 and index <= 61 and h >= 9 : p0[3]=-20
      if index == 57 and h >= 9 : p0[3]=-25
      if index == 60 and h >= 9 : p0[3]=-25
      if index >= 62 and index <= 63 and h >= 9 : p0[3]=-15
      if index == 64 and h >= 9 : p0[3]=-20
      if index >= 65 and index <= 66 and h >= 9 : p0[3]=-25
      if index == 67 and h >= 9 : p0[3]=-18
      if index == 68 and h >= 9 : p0[3]=-20
      if index == 69 and h >= 9 : p0[3]=-25
      if index >= 70 and index <= 72 and h >= 9 : p0[3]=-21
      if index == 71 and h >= 9 : p0[3]=-19
      if index == 73 and h >= 9 : p0[3]=-18
      if index == 74 and h >= 9 : p0[3]=-10
      if index == 75 and h >= 9 : p0[3]=-5
      if index >= 76 and index <= 77 and h >= 9 : p0[3]=1
      if index == 78 and h >= 9 : p0[3]=6
      if index == 79 and h >= 9 : p0[3]=2
      if index == 80 and h >= 9 : p0[3]=1
      if index >= 82 and index <= 83 and h >= 9 : p0[3]=5
      if index == 234 and h >= 9 : p0[3]=15
      if index == 240 and h >= 9 : p0[3]=8
      if index == 243 and h >= 9 : p0[3]=-5
      if index == 244 and h >= 9 : p0[3]=0
      if index == 249 and h >= 9 : p0[3]=0
      if index == 253 and h >= 9 : p0[3]=-10
      if index == 271 and h >= 9 : p0[3]=-10

    if year == 2026 and doy == 104:
     if beam == 0 :
      if index == 7 and h >= 9 : p0[3]=-22
      if index == 8 and h >= 9 : p0[3]=-25
      if index == 10 and h >= 9 : p0[3]=-28
      if index == 36 and h >= 27 : p0[3]=-25
      if index == 37 and h >= 9 : p0[3]=-23
      if index >= 40 and index <= 41 and h >= 9 : p0[3]=-25
      if index >= 42 and index <= 43 and h >= 9 : p0[3]=-20
      if index == 46 and h >= 9 : p0[3]=-20
      if index == 49 and h >= 9 : p0[3]=-25
      if index == 52 and h >= 9 : p0[3]=-20
      if index >= 54 and index <= 61 and h >= 9 : p0[3]=-20
      if index >= 62 and index <= 67 and h >= 9 : p0[3]=-15
      if index >= 68 and index <= 74 and h >= 9 : p0[3]=-10
      if index == 72 and h >= 9 : p0[3]=-15
      if index == 75 and h >= 9 : p0[3]=-15
      if index == 76 and h >= 9 : p0[3]=-6
      if index == 77 and h >= 9 : p0[3]=-3
      if index == 232 and h >= 9 : p0[3]=0
      if index >= 36 and index <= 72 and h >= 33 : p0[3]=numpy.nan
     if beam == 1 :
      if index == 32 and h >= 9 : p0[3]=-15
      if index >= 33 and index <= 34 and h >= 9 : p0[3]=-16
      if index == 35 and h >= 9 : p0[3]=-13
      if index == 36 and h >= 27 : p0[3]=-20
      if index == 37 and h >= 9 : p0[3]=-18
      if index == 39 and h >= 9 : p0[3]=-15
      if index == 40 and h >= 9 : p0[3]=-18
      if index >= 42 and index <= 43 and h >= 9 : p0[3]=-15
      if index >= 44 and index <= 45 and h >= 9 : p0[3]=-10
      if index == 46 and h >= 9 : p0[3]=-10
      if index >= 47 and index <= 48 and h >= 9 : p0[3]=-15
      if index >= 49 and index <= 50 and h >= 9 : p0[3]=-20
      if index >= 51 and index <= 61 and h >= 9 : p0[3]=-15
      if index >= 62 and index <= 67 and h >= 9 : p0[3]=-10
      if index >= 68 and index <= 74 and h >= 9 : p0[3]=-5
      if index == 72 and h >= 9 : p0[3]=-9 
      if index == 75 and h >= 9 : p0[3]=0
      if index == 76 and h >= 9 : p0[3]=1
      if index == 78 and h >= 19 : p0[3]=0
      if index == 224 and h >= 9 : p0[3]=25
      if index == 229 and h >= 9 : p0[3]=25
      if index == 234 and h >= 9 : p0[3]=8
      if index == 234 and h == 29 : p0[3]=13
      if index == 249 and h >= 9 : p0[3]=-5
      if index == 255 and h >= 9 : p0[3]=-8

    if year == 2026 and doy == 103:
     if beam == 0 :
      if index == 30 and h >= 25 : p0[3]=-10
      if index == 33 and h >= 9 : p0[3]=-5
      if index == 34 and h >= 9 : p0[3]=-8
      if index == 38 and h >= 9 : p0[3]=-1
      if index >= 39 and index <= 41 and h >= 9 : p0[3]=-10
      if index == 40 and h >= 9 : p0[3]=-12
      if index == 42 and h >= 9 : p0[3]=-8
      if index >= 43 and index <= 43 and h >= 9 : p0[3]=-5
      if index == 48 and h >= 9 : p0[3]=-19
      if index == 51 and h >= 9 : p0[3]=-20
      if index == 52 and h >= 9 : p0[3]=-25
      if index >= 53 and index <= 54 and h >= 9 : p0[3]=-20
      if index >= 56 and index <= 58 and h >= 9 : p0[3]=-15
      if index >= 59 and index <= 61 and h >= 9 : p0[3]=-20
      if index >= 63 and index <= 64 and h >= 9 : p0[3]=-25
      if index >= 65 and index <= 69 and h >= 9 : p0[3]=-20
      if index == 70 and h >= 9 : p0[3]=-15
      if index == 71 and h >= 9 : p0[3]=-21
      if index == 74 and h >= 9 : p0[3]=-15
      if index == 75 and h >= 9 : p0[3]=-8
      if index == 76 and h >= 9 : p0[3]=-5
      if index == 219 and h <= 19 : p0[3]=18
      if index == 233 and h >= 29 : p0[3]=-5
      if index >= 36 and index <= 72 and h >= 32 : p0[3]=numpy.nan
     if beam == 1 :
      if index == 34 and h >= 9 : p0[3]=-1
      if index == 35 and h >= 9 : p0[3]=-1
      if index == 36 and h >= 9 : p0[3]=1
      if index == 38 and h >= 9 : p0[3]=0
      if index >= 39 and index <= 40 and h >= 9 : p0[3]=-1
      if index >= 41 and index <= 41 and h >= 9 : p0[3]=-5
      if index == 42 and h >= 9 : p0[3]=-2
      if index == 44 and h >= 9 : p0[3]=-1
      if index >= 45 and index <= 46 and h >= 9 : p0[3]=-3
      if index >= 47 and index <= 47 and h >= 9 : p0[3]=-10
      if index == 48 and h >= 9 : p0[3]=-10
      if index >= 49 and index <= 53 and h >= 9 : p0[3]=-15
      if index == 52 and h >= 9 : p0[3]=-22
      if index >= 54 and index <= 57 and h >= 9 : p0[3]=-10
      if index == 55 and h >= 9 : p0[3]=-8
      if index == 58 and h >= 9 : p0[3]=-12
      if index >= 59 and index <= 61 and h >= 9 : p0[3]=-15
      if index >= 62 and index <= 64 and h >= 9 : p0[3]=-20
      if index >= 65 and index <= 71 and h >= 9 : p0[3]=-15
      if index == 70 and h >= 23 : p0[3]=-9
      if index == 70 and h <= 22 : p0[3]=-10
      if index >= 72 and index <= 74 and h >= 9 : p0[3]=-10
      if index == 75 and h >= 9 : p0[3]=-3
      if index == 76 and h >= 9 : p0[3]=4
      if index == 77 and h >= 22 : p0[3]=-1
      if index == 81 and h >= 17 : p0[3]=5
      if index == 234 and h >= 30 : p0[3]=10

    if year == 2026 and doy == 102:
     if beam == 0 :
      if index == 46 and h >= 9 : p0[3]=-15
      if index == 47 and h >= 9 : p0[3]=-21
      if index == 48 and h >= 9 : p0[3]=-18
      if index == 49 and h >= 9 : p0[3]=-12
      if index == 52 and h >= 9 : p0[3]=-20
      if index == 52 and h >= 35 : p0[3]=numpy.nan
      if index == 53 and h >= 9 : p0[3]=-22
      if index >= 55 and index <= 60 and h >= 9 : p0[3]=-20
      if index == 59 and h >= 9 : p0[3]=-22
      if index >= 61 and index <= 63 and h >= 9 : p0[3]=-15
      if index >= 64 and index <= 66 and h >= 9 : p0[3]=-10
      if index >= 67 and index <= 72 and h >= 9 : p0[3]=-15
      if index == 71 and h >= 9 : p0[3]=-18
      if index == 73 and h >= 9 : p0[3]=-13
      if index >= 74 and index <= 75 and h >= 9 : p0[3]=-5
      if index == 76 and h >= 9 : p0[3]=-14 #15
      if index == 77 and h >= 9 : p0[3]=0
      if index == 80 and h >= 9 : p0[3]=0
      if index == 109 and h >= 35 : p0[3]=numpy.nan
      if index == 198 and h >= 35 : p0[3]=numpy.nan
      if index == 224 and h >= 29 : p0[3]=20
      if index == 230 and h >= 9 : p0[3]=5
      if index == 234 and h >= 9 : p0[3]=0
      if index == 235 and h >= 9 : p0[3]=-5
      if index == 239 and h >= 9 : p0[3]=-10
      if index == 241 and h >= 9 : p0[3]=-10
      if index == 243 and h >= 9 : p0[3]=-15
      if index == 244 and h >= 9 : p0[3]=-17
      if index == 245 and h >= 9 : p0[3]=-13
      if index == 246 and h >= 9 : p0[3]=-15
      if index >= 247 and index <= 248 and h >= 9 : p0[3]=-20
      if index == 249 and h >= 9 : p0[3]=-23
      if index == 250 and h >= 9 : p0[3]=-20
      if index == 254 and h >= 9 : p0[3]=-30
      if index == 256 and h >= 29 : p0[3]=-25
      if index >= 30 and index <= 72 and h >= 32 : p0[3]=numpy.nan
     if beam == 1 :
      if index == 15 and h >= 20 : p0[3]=-20
      if index == 25 and h >= 20 : p0[3]=-18
      if index == 33 and h >= 9 : p0[3]=-20
      if index == 45 and h >= 9 : p0[3]=-20
      if index == 46 and h >= 9 : p0[3]=-9
      if index == 47 and h >= 9 : p0[3]=-12
      if index == 49 and h >= 9 : p0[3]=-5
      if index >= 50 and index <= 60 and h >= 9 : p0[3]=-15
      if index == 53 and h >= 9 : p0[3]=-15
      if index == 56 and h >= 9 : p0[3]=-18
      if index >= 61 and index <= 63 and h >= 9 : p0[3]=-10
      if index >= 64 and index <= 66 and h >= 9 : p0[3]=-5
      if index >= 67 and index <= 72 and h >= 9 : p0[3]=-10
      if index == 68 and h >= 9 : p0[3]=-5
      if index == 73 and h >= 9 : p0[3]=-10
      if index == 74 and h >= 9 : p0[3]=-5
      if index >= 75 and index <= 76 and h >= 9 : p0[3]=0
      if index == 77 and h >= 9 : p0[3]=0
      if index >= 79 and index <= 80 and h >= 9 : p0[3]=0
      if index == 245 and h >= 9 : p0[3]=-5
      if index == 257 and h >= 9 : p0[3]=-15

    if year == 2026 and doy == 101:
     if beam == 0 :
      if index == 14 and h >= 19 : p0[3]=-15
      if index == 20 and h >= 21 : p0[3]=-25
      if index == 34 and h >= 9 : p0[3]=-12
      if index == 53 and h >= 9 : p0[3]=-15
      if index == 54 and h >= 9 : p0[3]=-25
      if index == 58 and h >= 9 : p0[3]=-29
      if index == 59 and h >= 9 : p0[3]=-25
      if index >= 62 and index <= 64 and h >= 9 : p0[3]=-20
      if index >= 65 and index <= 67 and h >= 9 : p0[3]=-25
      if index >= 68 and index <= 70 and h >= 9 : p0[3]=-10
      if index == 72 and h >= 9 : p0[3]=-20
      if index == 75 and h >= 9 : p0[3]=-5
      if index == 76 and h >= 9 : p0[3]=-3
      if index == 256 and h >= 9 : p0[3]=-30
      if index == 257 and h >= 9 : p0[3]=-28
      if index >= 263 and index <= 265 and h >= 9 : p0[3]=-32
      if index >= 0 and index <= 288 and h >= 51 : p0[3]=numpy.nan
     if beam == 1 :
      if index == 30 and h >= 9 : p0[3]=0
      if index == 35 and h >= 9 : p0[3]=0
      if index == 36 and h >= 9 : p0[3]=-2
      if index == 42 and h >= 9 : p0[3]=0
      if index == 43 and h >= 9 : p0[3]=3
      if index == 44 and h >= 9 : p0[3]=5
      if index == 49 and h >= 9 : p0[3]=2
      if index == 50 and h >= 9 : p0[3]=3
      if index == 51 and h >= 9 : p0[3]=-5
      if index >= 52 and index <= 53 and h >= 9 : p0[3]=-10
      if index >= 54 and index <= 55 and h >= 9 : p0[3]=-20
      if index >= 56 and index <= 57 and h >= 9 : p0[3]=-25
      if index == 58 and h >= 9 : p0[3]=-20
      if index >= 59 and index <= 60 and h >= 9 : p0[3]=-20
      if index >= 61 and index <= 64 and h >= 9 : p0[3]=-15
      if index == 62 and h >= 9 : p0[3]=-10
      if index >= 65 and index <= 67 and h >= 9 : p0[3]=-20
      if index >= 68 and index <= 70 and h >= 9 : p0[3]=-5
      if index == 71 and h >= 9 : p0[3]=-10
      if index == 77 and h >= 9 : p0[3]=-8
      if index == 78 and h >= 9 : p0[3]=-5

    if year == 2026 and doy == 100:  #10
     if beam == 0 :
      if index == 32 and h >= 9 : p0[3]=-8
      if index == 35 and h >= 35 : p0[3]=numpy.nan
      if index == 36 and h >= 22 : p0[3]=-3
      if index == 41 and h >= 9 : p0[3]=-12
      if index == 44 and h <= 16 : p0[3]=-15
      if index == 49 and h >= 9 : p0[3]=-20
      if index == 52 and h >= 9 : p0[3]=-15
      if index == 53 and h <= 16 : p0[3]=-18
      if index == 55 and h == 18 : p0[3]=numpy.nan
      if index == 56 and h >= 9 : p0[3]=-10
      if index == 58 and h >= 9 : p0[3]=0
      if index == 62 and h >= 9 : p0[3]=5
      if index == 63 and h >= 9 : p0[3]=5
      if index == 74 and h >= 9 : p0[3]=-5
      if index == 76 and h >= 9 : p0[3]=-1
      if index == 233 and h >= 27 : p0[3]=5
      if index == 234 and h >= 9 : p0[3]=4
      if index == 239 and h >= 9 : p0[3]=0
      if index == 240 and h >= 9 : p0[3]=-5
      if index >= 36 and index <= 72 and h >= 32 : p0[3]=numpy.nan
     if beam == 1 :
      if index == 34 and h == 24 : p0[3]=numpy.nan
      if index == 45 and h >= 9 : p0[3]=-7
      if index == 50 and h >= 9 : p0[3]=-1
      if index == 51 and h >= 9 : p0[3]=-10
      if index == 52 and h >= 9 : p0[3]=-7
      if index == 53 and h >= 9 : p0[3]=-10
      if index == 54 and h <= 19 : p0[3]=-3
      if index >= 55 and index <= 55 and h >= 9 : p0[3]=-5
      if index == 56 and h >= 9 : p0[3]=-2
      if index == 57 and h >= 9 : p0[3]=1
      if index == 58 and h >= 9 : p0[3]=5
      if index == 59 and h >= 9 : p0[3]=5
      if index >= 60 and index <= 64 and h >= 9 : p0[3]=10
      if index == 61 and h >= 9 : p0[3]=-2
      if index == 65 and h >= 9 : p0[3]=2
      if index == 67 and h >= 9 : p0[3]=5
      if index >= 68 and index <= 69 and h >= 9 : p0[3]=0
      if index == 73 and h >= 9 : p0[3]=-1
      if index >= 74 and index <= 75 and h >= 9 : p0[3]=-5
      if index >= 77 and index <= 78 and h >= 9 : p0[3]=-5
      if index == 215 and h <= 18 : p0[3]=20
      if index == 239 and h >= 9 : p0[3]=10
      if index == 241 and h >= 9 : p0[3]=6
      if index == 245 and h >= 9 : p0[3]=-5

    if year == 2026 and doy == 99:
     if beam == 0 :
      if index == 40 and h >= 9 : p0[3]=-23
      if index == 47 and h >= 9 : p0[3]=-8
      if index == 51 and h >= 9 : p0[3]=-5
      if index == 53 and h >= 24 : p0[3]=0
      if index == 54 and h >= 9 : p0[3]=-4
      if index == 61 and h >= 9 : p0[3]=-5
      if index == 62 and h >= 9 : p0[3]=-5
      if index == 64 and h >= 9 : p0[3]=-6
      if index >= 66 and index <= 68 and h >= 9 : p0[3]=-5
      if index == 69 and h >= 9 : p0[3]=-6
      if index == 70 and h >= 9 : p0[3]=-6
      if index >= 71 and index <= 72 and h >= 9 : p0[3]=-4
      if index >= 73 and index <= 75 and h >= 9 : p0[3]=-7
      if index == 74 and h >= 9 : p0[3]=-10
      if index == 76 and h >= 9 : p0[3]=-11
      if index == 78 and h >= 9 : p0[3]=-10
      if index == 221 and h <= 19 : p0[3]=20
      if index == 223 and h <= 21 : p0[3]=20
      if index >= 229 and index <= 230 and h >= 9 : p0[3]=5
      if index == 234 and h >= 9 : p0[3]=-6
      if index == 235 and h >= 9 : p0[3]=-9
      if index == 247 and h >= 9 : p0[3]=-15
      if index >= 12 and index <= 72 and h >= 32 : p0[3]=numpy.nan
     if beam == 1 :
      if index == 32 and h >= 9 : p0[3]=-16
      if index == 37 and h >= 9 : p0[3]=-20
      if index == 42 and h >= 9 : p0[3]=-18
      if index == 44 and h >= 9 : p0[3]=-9
      if index == 45 and h >= 9 : p0[3]=-10
      if index >= 50 and index <= 51 and h >= 9 : p0[3]=0
      if index >= 52 and index <= 59 and h >= 9 : p0[3]=5
      if index == 53 and h >= 9 : p0[3]=3
      if index == 56 and h >= 9 : p0[3]=6
      if index == 58 and h >= 9 : p0[3]=6
      if index == 60 and h >= 9 : p0[3]=3
      if index >= 61 and index <= 63 and h >= 9 : p0[3]=0
      if index == 64 and h >= 9 : p0[3]=-2
      if index == 65 and h >= 9 : p0[3]=-1
      if index >= 66 and index <= 68 and h >= 9 : p0[3]=0
      if index == 69 and h >= 9 : p0[3]=-6
      if index >= 71 and index <= 72 and h >= 9 : p0[3]=0
      if index >= 73 and index <= 75 and h >= 9 : p0[3]=-5
      if index == 76 and h >= 9 : p0[3]=-7
      if index == 77 and h >= 9 : p0[3]=-5
      if index == 78 and h >= 9 : p0[3]=-8
      if index == 79 and h >= 9 : p0[3]=-6
      if index == 82 and h >= 9 : p0[3]=-10
      if index == 83 and h >= 9 : p0[3]=-11
      if index == 219 and h <= 22 : p0[3]=20
      if index == 222 and h <= 19 : p0[3]=25
      if index == 225 and h <= 22 : p0[3]=20
      if index == 229 and h >= 9 : p0[3]=15
      if index == 231 and h >= 9 : p0[3]=15

    if year == 2026 and doy == 98:
     if beam == 0 :
      if index == 34 and h >= 9 : p0[3]=-15
      if index == 39 and h >= 9 : p0[3]=-15
      if index == 41 and h >= 9 : p0[3]=-13
      if index == 43 and h >= 9 : p0[3]=-10
      if index >= 46 and index <= 47 and h >= 9 : p0[3]=-16
      if index == 48 and h >= 9 : p0[3]=-20
      if index == 50 and h >= 9 : p0[3]=-20
      if index >= 51 and index <= 56 and h >= 9 : p0[3]=-10
      if index == 53 and h >= 9 : p0[3]=-13
      if index == 57 and h >= 9 : p0[3]=-15
      if index >= 58 and index <= 76 and h >= 9 : p0[3]=-20
      if index == 67 and h == 25 : p0[3]=numpy.nan
      if index == 62 and h >= 9 : p0[3]=-15
      if index == 78 and h >= 9 : p0[3]=-13
      if index == 80 and h >= 9 : p0[3]=-10
      if index >= 30 and index <= 72 and h >= 32 : p0[3]=numpy.nan
      if index >= 216 and index <= 288 and h >= 51 : p0[3]=numpy.nan
     if beam == 1 :
      if index == 18 and h >= 9 : p0[3]=-15
      if index == 24 and h >= 9 : p0[3]=-15
      if index == 30 and h >= 9 : p0[3]=-10
      if index == 32 and h >= 9 : p0[3]=-10
      if index >= 35 and index <= 36 and h >= 9 : p0[3]=-10
      if index == 37 and h >= 9 : p0[3]=-8
      if index == 38 and h >= 9 : p0[3]=-3
      if index == 42 and h >= 9 : p0[3]=-10
      if index == 43 and h >= 9 : p0[3]=-5
      if index >= 45 and index <= 47 and h >= 9 : p0[3]=-10
      if index == 48 and h >= 9 : p0[3]=-15
      if index == 49 and h >= 9 : p0[3]=-12
      if index == 50 and h >= 9 : p0[3]=-15
      if index >= 51 and index <= 56 and h >= 9 : p0[3]=-5
      if index == 53 and h >= 9 : p0[3]=-2
      if index == 57 and h >= 9 : p0[3]=-10
      if index >= 58 and index <= 75 and h >= 9 : p0[3]=-15
      if index == 62 and h >= 9 : p0[3]=-10
      if index == 76 and h >= 9 : p0[3]=-12
      if index == 77 and h >= 9 : p0[3]=-10
      if index == 78 and h >= 9 : p0[3]=-8
      if index == 81 and h == 15 : p0[3]=5 #numpy.nan
      if index == 266 and h >= 29 : p0[3]=-17

    if year == 2026 and doy == 97:
     if beam == 0 :
      if index == 5 and h >= 19 : p0[3]=-30
      if index == 29 and h >= 9 : p0[3]=-20
      if index == 30 and h >= 9 : p0[3]=-20
      if index == 35 and h >= 9 : p0[3]=-22
      if index == 36 and h >= 9 : p0[3]=-16
      if index == 43 and h >= 9 : p0[3]=-9
      if index == 44 and h >= 9 : p0[3]=-9
      if index == 45 and h >= 9 : p0[3]=-10
      if index >= 48 and index <= 49 and h >= 9 : p0[3]=-10
      if index == 52 and h >= 9 : p0[3]=-10
      if index >= 54 and index <= 60 and h >= 9 : p0[3]=-20
      if index == 58 and h >= 9 : p0[3]=-25
      if index >= 61 and index <= 63 and h >= 9 : p0[3]=-25
      if index == 65 and h >= 9 : p0[3]=-25
      if index >= 66 and index <= 74 and h >= 9 : p0[3]=-20
      if index == 72 and h >= 9 : p0[3]=-14
      if index == 75 and h >= 9 : p0[3]=-15
      if index == 76 and h >= 9 : p0[3]=-10
      if index == 82 and h >= 9 : p0[3]=-7
      if index == 228 and h >= 9 : p0[3]=5
      if index == 235 and h >= 9 : p0[3]=-20
      if index >= 12 and index <= 72 and h >= 32 : p0[3]=numpy.nan
     if beam == 1 :
      if index == 13 and h >= 19 : p0[3]=-20
      if index == 34 and h >= 9 : p0[3]=-15
      if index == 35 and h >= 9 : p0[3]=-10
      if index == 42 and h >= 9 : p0[3]=-5
      if index == 43 and h >= 9 : p0[3]=-4
      if index >= 44 and index <= 45 and h >= 9 : p0[3]=-3
      if index == 49 and h >= 9 : p0[3]=-3
      if index >= 51 and index <= 52 and h >= 9 : p0[3]=-5
      if index == 53 and h >= 9 : p0[3]=-8
      if index == 54 and h >= 9 : p0[3]=-10
      if index >= 55 and index <= 63 and h >= 9 : p0[3]=-15
      if index == 58 and h >= 9 : p0[3]=-12
      if index == 62 and h >= 9 : p0[3]=-20
      if index == 65 and h >= 9 : p0[3]=-20
      if index >= 66 and index <= 74 and h >= 9 : p0[3]=-15
      if index == 72 and h >= 9 : p0[3]=-2
      if index == 75 and h >= 9 : p0[3]=-10
      if index >= 76 and index <= 77 and h >= 9 : p0[3]=-6
      if index == 81 and h >= 9 : p0[3]=-5
      if index == 224 and h >= 9 : p0[3]=41
      if index == 226 and h >= 9 : p0[3]=25
      if index == 228 and h >= 9 : p0[3]=10

    if year == 2026 and doy == 96: #6 abr
     if beam == 0 :
      if index == 224 and h >= 9 : p0[3]=25
      if index == 225 and h == 20 : p0[3]=numpy.nan #15
      if index == 232 and h >= 9 : p0[3]=-5
      if index == 243 and h >= 9 : p0[3]=-25
      if index >= 0 and h >= 50 : p0[3]=numpy.nan
     if beam == 1 :
      if index == 224 and h >= 9 : p0[3]=32
      if index == 234 and h >= 9 : p0[3]=12

    if year == 2026 and doy == 89: #30
     if beam == 0 :
      if index == 36 and h >= 9 : p0[3]=-15
      if index == 46 and h >= 9 : p0[3]=-25
      if index >= 54 and index <= 56 and h >= 9 : p0[3]=-45
      if index == 60 and h >= 9 : p0[3]=-45
      if index >= 62 and index <= 63 and h >= 9 : p0[3]=-45
      if index == 64 and h >= 9 : p0[3]=-43
      if index >= 65 and index <= 66 and h >= 9 : p0[3]=-35
      if index >= 67 and index <= 69 and h >= 9 : p0[3]=-30
      if index == 70 and h >= 9 : p0[3]=-25
      if index == 71 and h >= 9 : p0[3]=-15
      if index == 72 and h >= 9 : p0[3]=-10
      if index == 73 and h >= 9 : p0[3]=-7
      if index == 74 and h >= 9 : p0[3]=-11
      if index == 75 and h >= 9 : p0[3]=-20
      if index == 76 and h >= 9 : p0[3]=-15
      if index == 77 and h >= 9 : p0[3]=-8
      if index == 78 and h >= 9 : p0[3]=-15
      if index == 79 and h >= 9 : p0[3]=-5
      if index == 85 and h >= 9 : p0[3]=-2
     if beam == 1 :
      if index == 36 and h >= 9 : p0[3]=-9
      if index == 38 and h >= 9 : p0[3]=-5
      if index == 43 and h >= 9 : p0[3]=-7
      if index == 44 and h >= 9 : p0[3]=-8
      if index == 47 and h >= 9 : p0[3]=-25
      if index == 51 and h >= 9 : p0[3]=-17
      if index == 52 and h >= 9 : p0[3]=-35
      if index == 55 and h >= 9 : p0[3]=-39
      if index == 56 and h >= 9 : p0[3]=-38
      if index == 57 and h >= 9 : p0[3]=-39
      if index >= 58 and index <= 63 and h >= 9 : p0[3]=-40
      if index == 61 and h >= 9 : p0[3]=-41
      if index == 64 and h >= 9 : p0[3]=-37
      if index >= 65 and index <= 66 and h >= 9 : p0[3]=-30
      if index >= 67 and index <= 69 and h >= 9 : p0[3]=-25
      if index == 70 and h >= 9 : p0[3]=-20
      if index >= 71 and index <= 72 and h >= 9 : p0[3]=-10
      if index == 73 and h >= 9 : p0[3]=-1
      if index == 74 and h >= 9 : p0[3]=-3
      if index == 75 and h >= 9 : p0[3]=-15
      if index == 76 and h >= 9 : p0[3]=-8
      if index == 77 and h >= 9 : p0[3]=-2
      if index == 78 and h >= 9 : p0[3]=-8

    if year == 2026 and doy == 88:
     if beam == 0 :
      if index == 6 and h >= 9 : p0[3]=-35
      if index == 11 and h >= 9 : p0[3]=-35
      if index == 12 and h >= 9 : p0[3]=-35
      if index == 16 and h >= 9 : p0[3]=-27
      if index == 25 and h >= 9 : p0[3]=-18
      if index == 26 and h >= 9 : p0[3]=-17
      if index == 48 and h >= 9 : p0[3]=-6
      if index == 52 and h >= 9 : p0[3]=-10
      if index == 53 and h >= 9 : p0[3]=-13
      if index == 54 and h >= 9 : p0[3]=-6
      if index == 56 and h >= 9 : p0[3]=-15
      if index == 59 and h >= 27 : p0[3]=-10
      if index == 62 and h >= 9 : p0[3]=-15
      if index == 63 and h >= 9 : p0[3]=-21
      if index == 64 and h >= 9 : p0[3]=-13
      if index == 65 and h >= 9 : p0[3]=-10
      if index == 66 and h >= 9 : p0[3]=-6
      if index == 67 and h >= 9 : p0[3]=-2
      if index == 68 and h >= 9 : p0[3]=-5
      if index == 70 and h >= 9 : p0[3]=-5
      if index == 71 and h >= 9 : p0[3]=-4
      if index == 72 and h >= 9 : p0[3]=-10
      if index == 73 and h >= 9 : p0[3]=-5
      if index == 74 and h >= 9 : p0[3]=-5
      if index == 75 and h >= 9 : p0[3]=-5
      if index == 79 and h >= 9 : p0[3]=0
      if index == 245 and h >= 9 : p0[3]=-15
     if beam == 1 :
      if index == 8 and h >= 9 : p0[3]=-27
      if index == 10 and h >= 27 : p0[3]=-30
      if index == 12 and h >= 9 : p0[3]=-30
      if index == 14 and h >= 9 : p0[3]=-20
      if index == 43 and h >= 9 : p0[3]=-8
      if index == 46 and h >= 9 : p0[3]=-10
      if index == 47 and h >= 9 : p0[3]=-5
      if index == 49 and h >= 9 : p0[3]=2
      if index == 53 and h >= 9 : p0[3]=-5
      if index == 55 and h >= 9 : p0[3]=-1
      if index == 56 and h >= 9 : p0[3]=-10
      if index == 57 and h >= 9 : p0[3]=-1
      if index == 58 and h >= 9 : p0[3]=-4
      if index == 59 and h >= 9 : p0[3]=-3
      if index == 60 and h >= 9 : p0[3]=0
      if index >= 61 and index <= 61 and h >= 9 : p0[3]=0
      if index == 62 and h >= 9 : p0[3]=-10
      if index == 63 and h >= 9 : p0[3]=-18
      if index == 64 and h >= 9 : p0[3]=-5
      if index == 65 and h >= 9 : p0[3]=0
      if index == 66 and h >= 9 : p0[3]=0
      if index == 67 and h >= 9 : p0[3]=0
      if index == 68 and h >= 9 : p0[3]=0
      if index == 69 and h >= 9 : p0[3]=-15
      if index >= 70 and index <= 70 and h >= 9 : p0[3]=-3
      if index == 71 and h >= 9 : p0[3]=0
      if index == 72 and h >= 9 : p0[3]=-10
      if index == 73 and h >= 9 : p0[3]=-2
      if index == 74 and h >= 9 : p0[3]=-4
      if index == 75 and h >= 9 : p0[3]=-3
      if index == 76 and h >= 9 : p0[3]=-6
      if index >= 78 and index <= 78 and h >= 9 : p0[3]=-5
      if index == 79 and h >= 9 : p0[3]=-6
      if index == 231 and h >= 9 : p0[3]=20
      if index == 223 and h >= 27 : p0[3]=35
      if index == 225 and h >= 9 : p0[3]=30
      if index == 227 and h >= 9 : p0[3]=30
      if index == 228 and h >= 9 : p0[3]=35
      if index == 229 and h >= 9 : p0[3]=25

    if year == 2026 and doy == 87:
     if beam == 0 :
      if index == 30 and h >= 19 : p0[3]=-25
      if index == 33 and h >= 9 : p0[3]=-27
      if index >= 37 and index <= 38 and h >= 9 : p0[3]=-25
      if index == 41 and h >= 9 : p0[3]=-26
      if index == 43 and h >= 9 : p0[3]=-20
      if index == 44 and h >= 9 : p0[3]=-21
      if index >= 45 and index <= 46 and h >= 9 : p0[3]=-15
      if index >= 47 and index <= 52 and h >= 9 : p0[3]=-20
      if index >= 53 and index <= 54 and h >= 9 : p0[3]=-10
      if index >= 55 and index <= 57 and h >= 9 : p0[3]=-5
      if index >= 58 and index <= 60 and h >= 9 : p0[3]=0
      if index >= 61 and index <= 66 and h >= 9 : p0[3]=5
      if index == 64 and h >= 9 : p0[3]=-1
      if index == 65 and h >= 9 : p0[3]=10
      if index == 67 and h >= 9 : p0[3]=0
      if index == 68 and h >= 9 : p0[3]=-5
      if index == 69 and h >= 9 : p0[3]=-7
      if index >= 70 and index <= 76 and h >= 9 : p0[3]=-10
      if index == 73 and h >= 9 : p0[3]=-5
      if index == 74 and h >= 9 : p0[3]=-12
      if index >= 77 and index <= 78 and h >= 9 : p0[3]=-5
      if index == 83 and h >= 9 : p0[3]=-3
      if index == 85 and h >= 22 : p0[3]=8
      if index == 221 and h >= 9 : p0[3]=45
      if index == 222 and h >= 9 : p0[3]=33
      if index == 224 and h >= 9 : p0[3]=45
      if index == 226 and h >= 9 : p0[3]=55
      if index == 228 and h >= 9 : p0[3]=45
      if index == 229 and h >= 9 : p0[3]=60
      if index == 230 and h >= 9 : p0[3]=35
      if index == 231 and h >= 27 : p0[3]=15
      if index == 233 and h >= 27 : p0[3]=15
      if index == 234 and h >= 9 : p0[3]=20
      if index == 235 and h >= 27 : p0[3]=-5
      if index == 236 and h >= 9 : p0[3]=-8
      if index == 238 and h >= 27 : p0[3]=-20
      if index == 239 and h >= 9 : p0[3]=-27
      if index == 242 and h >= 9 : p0[3]=-25
      if index == 243 and h >= 9 : p0[3]=-26
      if index == 244 and h >= 9 : p0[3]=-45
      if index == 245 and h >= 9 : p0[3]=-27
      if index == 246 and h >= 9 : p0[3]=-30
      if index == 247 and h >= 9 : p0[3]=-32
      if index == 248 and h >= 9 : p0[3]=-25
      if index == 274 and h >= 27 : p0[3]=-35
      if index == 286 and h >= 27 : p0[3]=-35
      if index == 287 and h >= 9 : p0[3]=-35
     if beam == 1 :
      if index == 10 and h >= 9 : p0[3]=-30
      if index == 22 and h >= 9 : p0[3]=-30
      if index == 30 and h >= 9 : p0[3]=-21
      if index >= 31 and index <= 32 and h >= 9 : p0[3]=-20
      if index == 33 and h >= 9 : p0[3]=-22
      if index == 35 and h >= 9 : p0[3]=-21
      if index == 37 and h >= 9 : p0[3]=-23
      if index == 38 and h >= 9 : p0[3]=-18
      if index >= 39 and index <= 41 and h >= 9 : p0[3]=-20
      if index == 41 and h >= 9 : p0[3]=-21
      if index >= 43 and index <= 44 and h >= 9 : p0[3]=-15
      if index >= 45 and index <= 46 and h >= 9 : p0[3]=-10
      if index >= 47 and index <= 52 and h >= 9 : p0[3]=-15
      if index >= 53 and index <= 54 and h >= 9 : p0[3]=-5
      if index >= 55 and index <= 57 and h >= 9 : p0[3]=0
      if index >= 58 and index <= 59 and h >= 9 : p0[3]=5
      if index >= 60 and index <= 66 and h >= 9 : p0[3]=5
      if index == 65 and h >= 9 : p0[3]=10
      if index == 67 and h >= 9 : p0[3]=0
      if index == 68 and h >= 9 : p0[3]=-3
      if index >= 71 and index <= 75 and h >= 9 : p0[3]=-5
      if index == 73 and h >= 9 : p0[3]=2
      if index == 76 and h >= 9 : p0[3]=0
      if index >= 79 and index <= 79 and h >= 9 : p0[3]=-1
      if index == 77 and h >= 9 : p0[3]=-2
      if index == 78 and h >= 9 : p0[3]=-3
      if index == 81 and h >= 9 : p0[3]=0
      if index == 219 and h <= 20 : p0[3]=45
      if index == 222 and h >= 9 : p0[3]=45
      if index == 223 and h >= 9 : p0[3]=50
      if index == 224 and h >= 9 : p0[3]=55
      if index == 225 and h >= 9 : p0[3]=75
      if index == 226 and h >= 9 : p0[3]=65
      if index == 227 and h >= 9 : p0[3]=45
      if index == 228 and h >= 9 : p0[3]=52
      if index == 229 and h >= 9 : p0[3]=60
      if index == 230 and h >= 9 : p0[3]=50
      if index == 231 and h >= 26 : p0[3]=60
      if index == 233 and h >= 29 : p0[3]=30
      if index == 234 and h >= 29 : p0[3]=30
      if index == 235 and h >= 9 : p0[3]=15
      if index == 238 and h >= 29 : p0[3]=-8
      if index == 239 and h >= 26 : p0[3]=-18
      if index == 243 and h >= 9 : p0[3]=-18
      if index == 244 and h >= 9 : p0[3]=-35
      if index == 247 and h >= 9 : p0[3]=-22
      if index == 248 and h >= 9 : p0[3]=-18
      if index == 260 and h >= 9 : p0[3]=-25
      if index == 266 and h >= 27 : p0[3]=-30
      if index == 274 and h >= 27 : p0[3]=-30
      if index == 284 and h >= 9 : p0[3]=-30

    if year == 2026 and doy == 86:
     if beam == 0 :
      if index == 31 and h >= 9 : p0[3]=-23
      if index == 36 and h >= 9 : p0[3]=-20
      if index == 37 and h <= 17 : p0[3]=-20
      if index == 40 and h >= 9 : p0[3]=-18
      if index == 43 and h >= 9 : p0[3]=-15
      if index == 44 and h >= 9 : p0[3]=-22
      if index == 45 and h >= 9 : p0[3]=-21
      if index == 48 and h >= 9 : p0[3]=-21
      if index == 49 and h >= 9 : p0[3]=-15
      if index >= 50 and index <= 52 and h >= 9 : p0[3]=-20
      if index == 54 and h >= 9 : p0[3]=-23
      if index == 55 and h >= 9 : p0[3]=-25
      if index == 59 and h >= 9 : p0[3]=-20
      if index == 60 and h >= 18 : p0[3]=-21
      if index >= 61 and index <= 65 and h >= 9 : p0[3]=-20
      if index == 63 and h >= 9 : p0[3]=-15
      if index == 66 and h >= 9 : p0[3]=-25
      if index == 67 and h >= 9 : p0[3]=-20
      if index == 68 and h >= 9 : p0[3]=-10
      if index == 69 and h >= 9 : p0[3]=-1
      if index == 70 and h >= 9 : p0[3]=-15
      if index == 71 and h >= 9 : p0[3]=-10
      if index == 72 and h >= 9 : p0[3]=-10
      if index == 73 and h >= 9 : p0[3]=-2
      if index == 75 and h >= 9 : p0[3]=-10
      if index == 76 and h >= 9 : p0[3]=-8
      if index == 78 and h >= 9 : p0[3]=-12
      if index == 79 and h >= 9 : p0[3]=-10
      if index == 243 and h >= 9 : p0[3]=-20
     if beam == 1 :
      if index == 20 and h == 15 : p0[3]=-20 #numpy.nan
      if index == 25 and h == 13 : p0[3]=numpy.nan
      if index == 26 and h >= 9 : p0[3]=-17
      if index == 30 and h >= 9 : p0[3]=-17
      if index >= 31 and index <= 32 and h >= 9 : p0[3]=-15
      if index == 35 and h >= 9 : p0[3]=-19
      if index == 36 and h >= 9 : p0[3]=-18
      if index == 37 and h >= 9 : p0[3]=-12
      if index == 38 and h >= 9 : p0[3]=-12
      if index == 39 and h >= 9 : p0[3]=-14
      if index == 40 and h >= 9 : p0[3]=-16
      if index >= 41 and index <= 43 and h >= 9 : p0[3]=-10
      if index == 44 and h >= 9 : p0[3]=-15
      if index == 45 and h >= 9 : p0[3]=-15
      if index >= 46 and index <= 47 and h >= 9 : p0[3]=-15
      if index == 48 and h >= 9 : p0[3]=-15
      if index == 49 and h >= 9 : p0[3]=-10
      if index >= 50 and index <= 52 and h >= 9 : p0[3]=-15
      if index == 51 and h >= 9 : p0[3]=-16
      if index == 53 and h >= 9 : p0[3]=-19
      if index == 54 and h >= 9 : p0[3]=-13
      if index == 55 and h >= 9 : p0[3]=-15
      if index == 56 and h >= 9 : p0[3]=-16
      if index == 57 and h >= 9 : p0[3]=-18
      if index == 58 and h >= 9 : p0[3]=-19
      if index == 59 and h >= 9 : p0[3]=-16
      if index == 60 and h >= 9 : p0[3]=-10
      if index >= 61 and index <= 65 and h >= 9 : p0[3]=-15
      if index == 63 and h >= 9 : p0[3]=-10
      if index == 66 and h >= 9 : p0[3]=-20
      if index == 67 and h >= 9 : p0[3]=-13
      if index == 68 and h >= 9 : p0[3]=-5
      if index == 69 and h >= 9 : p0[3]=-2
      if index == 70 and h >= 9 : p0[3]=-8
      if index == 71 and h >= 9 : p0[3]=-10
      if index == 72 and h >= 9 : p0[3]=5
      if index == 73 and h >= 9 : p0[3]=1
      if index == 74 and h >= 9 : p0[3]=-3
      if index == 75 and h >= 9 : p0[3]=-3
      if index == 76 and h >= 9 : p0[3]=0
      if index == 80 and h >= 9 : p0[3]=-10
      if index == 243 and h >= 9 : p0[3]=-10

    if year == 2026 and doy == 85:
     if beam == 0 :
      if index == 29 and h >= 22 : p0[3]=-20
      if index == 33 and h <= 18 : p0[3]=-17
      if index == 56 and h >= 9 : p0[3]=-17
      if index == 56 and h == 20 : p0[3]=-15 #numpy.nan
      if index == 60 and h >= 9 : p0[3]=-20
      if index == 61 and h >= 9 : p0[3]=-20
      if index == 62 and h >= 9 : p0[3]=-22
      if index == 63 and h >= 9 : p0[3]=-6
      if index == 64 and h >= 9 : p0[3]=-7
      if index == 66 and h >= 9 : p0[3]=-10
      if index == 67 and h >= 9 : p0[3]=-5
      if index == 68 and h >= 9 : p0[3]=-3
      if index == 73 and h >= 9 : p0[3]=-20
      if index == 78 and h >= 9 : p0[3]=-5
      if index == 79 and h >= 9 : p0[3]=-8
      if index == 206 and h >= 35 : p0[3]=numpy.nan
      if index == 219 and h >= 29 : p0[3]=16
      if index == 229 and h >= 9 : p0[3]=15
      if index == 237 and h >= 9 : p0[3]=-6
      if index == 239 and h >= 9 : p0[3]=-10
      if index == 244 and h >= 9 : p0[3]=-15
     if beam == 1 :
      if index == 29 and h >= 9 : p0[3]=-11
      if index == 33 and h <= 17 : p0[3]=-10
      if index == 45 and h <= 18 : p0[3]=-5
      if index == 56 and h >= 9 : p0[3]=-10
      if index == 59 and h >= 9 : p0[3]=-10
      if index == 62 and h >= 9 : p0[3]=-16
      if index == 63 and h >= 9 : p0[3]=0
      if index >= 64 and index <= 65 and h >= 9 : p0[3]=-1
      if index == 66 and h >= 9 : p0[3]=-5
      if index == 67 and h >= 9 : p0[3]=-2
      if index == 68 and h >= 9 : p0[3]=0
      if index == 69 and h >= 9 : p0[3]=-18
      if index == 70 and h >= 9 : p0[3]=-2
      if index == 71 and h >= 9 : p0[3]=-15
      if index == 72 and h >= 9 : p0[3]=-20
      if index == 73 and h >= 9 : p0[3]=-15
      if index == 74 and h >= 9 : p0[3]=-10
      if index >= 75 and index <= 76 and h >= 9 : p0[3]=-10
      if index == 77 and h >= 9 : p0[3]=-7
      if index == 78 and h >= 9 : p0[3]=-1
      if index == 79 and h >= 9 : p0[3]=-4
      if index == 81 and h >= 9 : p0[3]=-2
      if index == 221 and h == 18 : p0[3]=22 #numpy.nan
      if index == 229 and h == 22 : p0[3]=20 #numpy.nan
      if index == 230 and h >= 9 : p0[3]=20
      if index == 231 and h >= 9 : p0[3]=18
      if index == 239 and h >= 9 : p0[3]=-2
      if index == 241 and h >= 9 : p0[3]=0

    if year == 2026 and doy == 84: #25
     if beam == 0 :
      if index == 44 and h >= 9 : p0[3]=-15
      if index == 45 and h >= 9 : p0[3]=-7
      if index >= 47 and index <= 48 and h >= 9 : p0[3]=-5
      if index == 49 and h >= 9 : p0[3]=-3
      if index == 51 and h >= 9 : p0[3]=-0
      if index == 52 and h >= 9 : p0[3]=2
      if index == 56 and h >= 9 : p0[3]=-18
      if index == 57 and h >= 9 : p0[3]=-30
      if index == 58 and h >= 9 : p0[3]=-35
      if index == 59 and h >= 9 : p0[3]=-25
      if index == 60 and h >= 9 : p0[3]=-23
      if index == 62 and h >= 9 : p0[3]=-12
      if index >= 65 and index <= 66 and h >= 9 : p0[3]=30
      if index == 67 and h >= 9 : p0[3]=35
      if index == 74 and h >= 9 : p0[3]=0
      if index == 75 and h >= 9 : p0[3]=-5
      if index == 78 and h >= 9 : p0[3]=-15
      if index == 79 and h >= 9 : p0[3]=-10
      if index == 231 and h >= 9 : p0[3]=5
      if index == 235 and h >= 9 : p0[3]=-5
      if index == 236 and h >= 9 : p0[3]=-10
     if beam == 1 :
      if index == 37 and h >= 9 : p0[3]=-36
      if index >= 38 and index <= 40 and h >= 9 : p0[3]=-39
      if index == 42 and h >= 9 : p0[3]=-25
      if index == 43 and h >= 9 : p0[3]=-15
      if index == 45 and h >= 9 : p0[3]=-1
      if index == 47 and h >= 9 : p0[3]=1
      if index == 48 and h >= 9 : p0[3]=0
      if index >= 49 and index <= 50 and h >= 9 : p0[3]=0
      if index == 51 and h >= 9 : p0[3]=5
      if index == 52 and h >= 9 : p0[3]=10
      if index == 53 and h >= 9 : p0[3]=0
      if index == 55 and h >= 9 : p0[3]=-18
      if index == 56 and h >= 9 : p0[3]=-10
      if index == 57 and h >= 9 : p0[3]=-25
      if index == 58 and h >= 9 : p0[3]=-30
      if index == 59 and h >= 9 : p0[3]=-19
      if index == 62 and h >= 9 : p0[3]=0
      if index == 63 and h >= 9 : p0[3]=-1
      if index == 64 and h >= 9 : p0[3]=15
      if index >= 65 and index <= 66 and h >= 9 : p0[3]=35
      if index == 67 and h >= 9 : p0[3]=40
      if index >= 73 and index <= 74 and h >= 9 : p0[3]=-2
      if index == 75 and h >= 9 : p0[3]=-5
      if index >= 76 and index <= 77 and h >= 9 : p0[3]=-10
      if index == 79 and h >= 9 : p0[3]=-10
      if index == 80 and h >= 9 : p0[3]=-20
      if index == 81 and h >= 9 : p0[3]=-10
      if index == 83 and h >= 9 : p0[3]=-8
      if index == 86 and h >= 9 : p0[3]=-5
      if index == 224 and h >= 9 : p0[3]=35
      if index == 235 and h >= 9 : p0[3]=0

    if year == 2026 and doy == 83:
     if beam == 0 :
      if index == 20 and h >= 25 : p0[3]=-10
      if index == 50 and h >= 20 : p0[3]=-20
      if index == 64 and h >= 9 : p0[3]=-35
      if index == 69 and h >= 9 : p0[3]=-35
      if index == 71 and h >= 9 : p0[3]=-28
      if index >= 72 and index <= 73 and h >= 9 : p0[3]=-20
      if index == 74 and h >= 9 : p0[3]=-15
      if index == 75 and h >= 9 : p0[3]=-23
      if index == 76 and h >= 9 : p0[3]=-20
      if index == 81 and h >= 9 : p0[3]=-17
      if index == 84 and h >= 19 : p0[3]=-10
      if index == 85 and h >= 9 : p0[3]=-7
      if index == 232 and h >= 9 : p0[3]=15
      if index == 236 and h >= 9 : p0[3]=3
      if index >= 237 and index <= 238 and h >= 9 : p0[3]=0
      if index == 239 and h >= 9 : p0[3]=-6
      if index == 240 and h >= 9 : p0[3]=-13
      if index == 243 and h >= 9 : p0[3]=-20
      if index == 245 and h >= 9 : p0[3]=-20
      if index == 250 and h >= 9 : p0[3]=-35
      if index == 251 and h >= 9 : p0[3]=-30
      if index == 256 and h >= 9 : p0[3]=-25
     if beam == 1 :
      if index == 8 and h >= 9 : p0[3]=-12
      if index == 14 and h >= 22 : p0[3]=-10
      if index == 20 and h >= 9 : p0[3]=-5
      if index == 30 and h >= 9 : p0[3]=-8
      if index == 31 and h >= 9 : p0[3]=-8
      if index == 45 and h >= 9 : p0[3]=-20
      if index == 49 and h >= 9 : p0[3]=-12
      if index == 50 and h <= 16 : p0[3]=-13
      if index == 51 and h >= 9 : p0[3]=-17
      if index == 58 and h >= 9 : p0[3]=-33
      if index == 62 and h >= 9 : p0[3]=-20
      if index >= 63 and index <= 66 and h >= 9 : p0[3]=-30
      if index == 65 and h >= 9 : p0[3]=-24
      if index == 67 and h >= 9 : p0[3]=-30
      if index == 68 and h >= 9 : p0[3]=-28
      if index == 69 and h >= 9 : p0[3]=-24
      if index == 70 and h >= 9 : p0[3]=-22
      if index == 71 and h >= 9 : p0[3]=-23
      if index >= 73 and index <= 73 and h >= 9 : p0[3]=-18
      if index == 72 and h >= 9 : p0[3]=-16
      if index == 74 and h >= 9 : p0[3]=-14
      if index == 75 and h >= 9 : p0[3]=-21
      if index == 76 and h >= 9 : p0[3]=-15
      if index == 77 and h >= 9 : p0[3]=-18
      if index == 78 and h >= 9 : p0[3]=-7
      if index == 84 and h >= 9 : p0[3]=-15
      if index == 232 and h >= 9 : p0[3]=20
      if index == 237 and h >= 9 : p0[3]=5
      if index == 238 and h >= 9 : p0[3]=7
      if index == 244 and h >= 9 : p0[3]=-10

    if year == 2026 and doy == 82:
     if beam == 0 :
      if index == 222 and h >= 35 : p0[3]=numpy.nan
     if beam == 1 :
      if index == 231 and h >= 9 : p0[3]=18
      if index == 232 and h >= 9 : p0[3]=15
      if index == 233 and h >= 9 : p0[3]=10

    if year == 2026 and doy == 68:
     if beam == 0 :
      if index == 13 and h >= 9 : p0[3]=-25
      if index == 35 and h >= 9 : p0[3]=-25
      if index == 61 and h <= 16 : p0[3]=-20
      if index == 71 and h >= 9 : p0[3]=-22
      if index == 89 and h >= 9 : p0[3]=-3
     if beam == 1 :
      if index == 25 and h <= 19 : p0[3]=-10
      if index == 29 and h >= 19 : p0[3]=-13
      if index == 35 and h >= 9 : p0[3]=-15
      if index == 37 and h >= 9 : p0[3]=-13
      if index == 46 and h >= 9 : p0[3]=-15
      if index == 48 and h >= 9 : p0[3]=-17
      if index == 55 and h >= 9 : p0[3]=-18
      if index == 60 and h >= 9 : p0[3]=-20
      if index == 67 and h >= 9 : p0[3]=-20
      if index == 69 and h >= 9 : p0[3]=-20
      if index == 70 and h >= 9 : p0[3]=-22
      if index == 71 and h >= 9 : p0[3]=-16
      if index == 73 and h >= 9 : p0[3]=-18
      if index == 74 and h >= 9 : p0[3]=-15
      if index == 75 and h >= 9 : p0[3]=-10
      if index >= 76 and index <= 77 and h >= 9 : p0[3]=-5
      if index == 78 and h >= 9 : p0[3]=-10
      if index == 81 and h >= 9 : p0[3]=-5
      if index == 85 and h >= 9 : p0[3]=0
      if index >= 87 and index <= 88 and h >= 9 : p0[3]=0
      if index == 89 and h >= 9 : p0[3]=2
      if index == 91 and h >= 9 : p0[3]=1
      if index == 94 and h >= 9 : p0[3]=10

    if year == 2026 and doy == 67:
     if beam == 0 :
      if index == 32 and h >= 9 : p0[3]=-10
      if index == 49 and h >= 9 : p0[3]=18
      if index == 60 and h >= 9 : p0[3]=-10
      if index == 62 and h >= 9 : p0[3]=-23
      if index == 64 and h >= 9 : p0[3]=-25
      if index == 66 and h >= 9 : p0[3]=-28
      if index == 229 and h >= 9 : p0[3]=25
      if index == 232 and h >= 9 : p0[3]=17
      if index >= 233 and index <= 234 and h >= 9 : p0[3]=8
      if index == 235 and h >= 9 : p0[3]=5
      if index == 236 and h >= 9 : p0[3]=0
      if index == 257 and h >= 9 : p0[3]=-30
     if beam == 1 :
      if index == 26 and h >= 9 : p0[3]=-15
      if index == 27 and h >= 9 : p0[3]=-8
      if index == 33 and h >= 9 : p0[3]=-5
      if index == 34 and h >= 9 : p0[3]=-10
      if index == 35 and h >= 9 : p0[3]=-20
      if index == 38 and h >= 9 : p0[3]=-3
      if index == 40 and h >= 22 : p0[3]=0
      if index == 43 and h >= 9 : p0[3]=5
      if index == 44 and h >= 9 : p0[3]=10
      if index == 45 and h >= 19 : p0[3]=15
      if index == 47 and h >= 9 : p0[3]=20
      if index == 54 and h >= 9 : p0[3]=8
      if index == 56 and h >= 9 : p0[3]=10
      if index >= 57 and index <= 58 and h >= 9 : p0[3]=8
      if index == 60 and h >= 9 : p0[3]=-5
      if index >= 61 and index <= 62 and h >= 9 : p0[3]=-18
      if index >= 63 and index <= 65 and h >= 9 : p0[3]=-20
      if index == 68 and h >= 9 : p0[3]=-30
      if index == 73 and h >= 9 : p0[3]=-15
      if index == 77 and h >= 9 : p0[3]=-1
      if index >= 82 and index <= 84 and h >= 9 : p0[3]=0
      if index >= 87 and index <= 88 and h >= 9 : p0[3]=1
      if index == 204 and h >= 9 : p0[3]=17
      if index >= 217 and index <= 218 and h >= 9 : p0[3]=25
      if index == 226 and h >= 9 : p0[3]=38
      if index >= 228 and index <= 230 and h >= 9 : p0[3]=30
      if index == 232 and h >= 9 : p0[3]=20
      if index >= 233 and index <= 234 and h >= 9 : p0[3]=15
      if index == 235 and h >= 9 : p0[3]=10
      if index == 240 and h >= 9 : p0[3]=-5
      if index == 241 and h >= 9 : p0[3]=-3
      if index >= 243 and index <= 244 and h >= 9 : p0[3]=-8
      if index == 245 and h >= 9 : p0[3]=-10
      if index == 249 and h >= 9 : p0[3]=-15
      if index == 252 and h >= 9 : p0[3]=-18

    if year == 2026 and doy == 66:
     if beam == 0 :
      if index == 26 and h >= 9 : p0[3]=0
      if index == 58 and h >= 9 : p0[3]=-22
      if index == 70 and h >= 9 : p0[3]=-20
      if index == 92 and h >= 9 : p0[3]=2
      if index == 229 and h >= 9 : p0[3]=30
      if index == 237 and h >= 9 : p0[3]=5
      if index == 241 and h >= 9 : p0[3]=-20
      if index == 245 and h >= 9 : p0[3]=-25
      if index == 246 and h >= 9 : p0[3]=-30
      if index == 247 and h >= 9 : p0[3]=-40
      if index == 248 and h >= 9 : p0[3]=-40
      if index == 254 and h >= 9 : p0[3]=-35
     if beam == 1 :
      if index == 15 and h >= 9 : p0[3]=-5
      if index == 22 and h >= 9 : p0[3]=0
      if index == 29 and h >= 9 : p0[3]=5
      if index == 35 and h >= 9 : p0[3]=-18
      if index == 40 and h >= 9 : p0[3]=-2
      if index == 41 and h >= 9 : p0[3]=-5
      if index == 43 and h >= 9 : p0[3]=1
      if index == 45 and h >= 9 : p0[3]=-10
      if index == 46 and h >= 9 : p0[3]=-5
      if index == 48 and h >= 9 : p0[3]=10
      if index == 50 and h >= 9 : p0[3]=0
      if index == 51 and h >= 9 : p0[3]=1
      if index == 53 and h >= 9 : p0[3]=-5
      if index == 54 and h >= 9 : p0[3]=-20
      if index == 55 and h >= 9 : p0[3]=-20
      if index == 56 and h >= 9 : p0[3]=-10
      if index == 66 and h >= 9 : p0[3]=-20
      if index == 70 and h >= 9 : p0[3]=-15
      if index == 72 and h >= 9 : p0[3]=-15
      if index == 75 and h >= 9 : p0[3]=-15
      if index == 76 and h >= 9 : p0[3]=-18
      if index == 77 and h >= 9 : p0[3]=-10
      if index == 89 and h >= 9 : p0[3]=-2
      if index == 110 and h >= 9 : p0[3]=10
      if index == 113 and h >= 9 : p0[3]=15
      if index == 137 and h >= 9 : p0[3]=35
      if index == 149 and h >= 9 : p0[3]=20
      if index == 168 and h >= 9 : p0[3]=8
      if index == 199 and h >= 9 : p0[3]=6
      if index == 227 and h >= 9 : p0[3]=50
      if index == 228 and h >= 9 : p0[3]=45
      if index == 232 and h >= 9 : p0[3]=40
      if index == 233 and h >= 9 : p0[3]=28
      if index == 234 and h >= 9 : p0[3]=10
      if index == 237 and h >= 9 : p0[3]=15
      if index == 238 and h >= 9 : p0[3]=15
      if index == 239 and h >= 9 : p0[3]=10
      if index == 240 and h >= 9 : p0[3]=0
      if index == 242 and h >= 9 : p0[3]=-5
      if index == 244 and h >= 9 : p0[3]=-20
      if index == 246 and h >= 9 : p0[3]=-20
      if index == 250 and h >= 9 : p0[3]=-30
      if index == 268 and h >= 9 : p0[3]=-25

    if year == 2026 and doy == 65:
     if beam == 0 :
      if index == 30 and h >= 22 : p0[3]=-25
      if index == 39 and h >= 9 : p0[3]=-25
      if index == 42 and h >= 9 : p0[3]=-27
      if index == 44 and h >= 9 : p0[3]=-30
      if index == 46 and h >= 9 : p0[3]=-23
      if index >= 47 and index <= 71 and h >= 9 : p0[3]=-30
      if index == 50 and h >= 9 : p0[3]=-32
      if index == 54 and h >= 9 : p0[3]=-32
      if index == 55 and h >= 9 : p0[3]=-35
      if index == 56 and h >= 9 : p0[3]=-38
      if index == 65 and h >= 9 : p0[3]=-32
      if index == 66 and h >= 9 : p0[3]=-20
      if index == 72 and h >= 9 : p0[3]=-25
      if index == 74 and h >= 9 : p0[3]=-25
      if index == 234 and h >= 9 : p0[3]=25
      if index == 235 and h >= 9 : p0[3]=20
      if index >= 237 and index <= 238 and h >= 9 : p0[3]=15
      if index == 239 and h >= 9 : p0[3]=10
      if index == 242 and h >= 9 : p0[3]=-15
     if beam == 1 :
      if index == 7 and h >= 9 : p0[3]=-25
      if index == 31 and h <= 16 : p0[3]=-20
      if index == 33 and h >= 9 : p0[3]=-17
      if index == 34 and h >= 9 : p0[3]=-20
      if index == 35 and h >= 9 : p0[3]=-22
      if index == 37 and h >= 9 : p0[3]=-25
      if index >= 39 and index <= 41 and h >= 9 : p0[3]=-20
      if index == 42 and h >= 9 : p0[3]=-17
      if index == 43 and h >= 9 : p0[3]=-21
      if index == 44 and h >= 9 : p0[3]=-25
      if index >= 45 and index <= 46 and h >= 9 : p0[3]=-20
      if index >= 47 and index <= 71 and h >= 9 : p0[3]=-25
      if index == 55 and h >= 9 : p0[3]=-27
      if index == 56 and h >= 9 : p0[3]=-35
      if index == 59 and h >= 9 : p0[3]=-22
      if index >= 72 and index <= 73 and h >= 9 : p0[3]=-20
      if index == 74 and h >= 9 : p0[3]=-12
      if index >= 75 and index <= 78 and h >= 9 : p0[3]=-5
      if index == 77 and h >= 9 : p0[3]=-10
      if index == 79 and h >= 9 : p0[3]=-8
      if index == 81 and h >= 9 : p0[3]=0
      if index == 83 and h >= 9 : p0[3]=-5
      if index == 87 and h >= 9 : p0[3]=0
      if index >= 88 and index <= 89 and h >= 9 : p0[3]=0
      if index == 90 and h >= 9 : p0[3]=4
      if index == 92 and h >= 9 : p0[3]=10
      if index == 94 and h >= 9 : p0[3]=10
      if index == 95 and h >= 9 : p0[3]=5
      if index == 97 and h >= 9 : p0[3]=10
      if index == 98 and h >= 9 : p0[3]=15
      if index == 105 and h >= 9 : p0[3]=18
      if index == 122 and h >= 9 : p0[3]=30
      if index == 217 and h >= 9 : p0[3]=22
      if index == 223 and h >= 9 : p0[3]=42
      if index == 224 and h >= 9 : p0[3]=40
      if index == 226 and h >= 9 : p0[3]=40
      if index == 227 and h >= 9 : p0[3]=35
      if index == 229 and h >= 9 : p0[3]=30
      if index == 230 and h >= 9 : p0[3]=33
      if index == 231 and h >= 9 : p0[3]=40
      if index == 234 and h >= 9 : p0[3]=38
      if index == 235 and h >= 9 : p0[3]=28
      if index == 236 and h >= 9 : p0[3]=32
      if index == 237 and h >= 9 : p0[3]=22
      if index >= 238 and index <= 238 and h >= 9 : p0[3]=20
      if index == 239 and h >= 9 : p0[3]=22
      if index == 240 and h >= 9 : p0[3]=10
      if index == 241 and h >= 9 : p0[3]=-3
      if index == 243 and h >= 9 : p0[3]=-22
      if index == 244 and h >= 9 : p0[3]=-20
      if index == 245 and h >= 9 : p0[3]=-25
      if index >= 246 and index <= 247 and h >= 9 : p0[3]=-25
      if index >= 249 and index <= 251 and h >= 9 : p0[3]=-25
      if index == 252 and h >= 9 : p0[3]=-30
      if index == 254 and h >= 9 : p0[3]=-20
      if index == 255 and h >= 9 : p0[3]=-25

    if year == 2026 and doy == 64:  #5
     if beam == 0 :
      if index == 227 and h >= 9 : p0[3]=40
      if index == 232 and h >= 9 : p0[3]=25
      if index >= 233 and index <= 234 and h >= 9 : p0[3]=12
      if index == 235 and h >= 9 : p0[3]=25
      if index >= 236 and index <= 238 and h >= 9 : p0[3]=10
      if index == 239 and h >= 9 : p0[3]=15
      if index == 240 and h >= 9 : p0[3]=0
      if index == 244 and h >= 9 : p0[3]=-15
      if index >= 245 and index <= 246 and h >= 9 : p0[3]=-25
      if index == 247 and h >= 9 : p0[3]=-35
      if index == 248 and h >= 9 : p0[3]=-25
      if index == 257 and h >= 9 : p0[3]=-35
      if index == 258 and h >= 9 : p0[3]=-25
      if index == 259 and h >= 9 : p0[3]=-20
      if index == 260 and h >= 9 : p0[3]=-25
     if beam == 1 :
      if index == 208 and h >= 9 : p0[3]=10
      if index == 231 and h >= 9 : p0[3]=45
      if index == 232 and h >= 9 : p0[3]=30
      if index >= 233 and index <= 234 and h >= 9 : p0[3]=22
      if index >= 235 and index <= 236 and h >= 9 : p0[3]=25
      if index == 237 and h >= 9 : p0[3]=20
      if index == 239 and h >= 9 : p0[3]=25
      if index == 240 and h >= 9 : p0[3]=10
      if index >= 241 and index <= 242 and h >= 9 : p0[3]=-8
      if index == 244 and h >= 9 : p0[3]=-6
      if index == 245 and h >= 9 : p0[3]=-10
      if index == 246 and h >= 9 : p0[3]=-15
      if index == 248 and h >= 9 : p0[3]=-15
      if index >= 249 and index <= 251 and h >= 9 : p0[3]=-25
      if index == 252 and h >= 9 : p0[3]=-10
      if index >= 253 and index <= 254 and h >= 9 : p0[3]=-20
      if index == 256 and h >= 9 : p0[3]=-20
      if index == 257 and h >= 9 : p0[3]=-25
      if index == 258 and h >= 9 : p0[3]=-15

    if year == 2026 and doy == 62:
     if beam == 0 :
      if index >= 61 and index <= 69 and h >= 9 : p0[3]=-40
      if index == 64 and h >= 9 : p0[3]=-45
      if index == 68 and h >= 9 : p0[3]=-35
      if index == 70 and h >= 9 : p0[3]=-40
      if index >= 71 and index <= 71 and h >= 9 : p0[3]=-35
      if index == 72 and h >= 9 : p0[3]=-30
      if index == 73 and h >= 9 : p0[3]=-20
      if index == 76 and h >= 19 : p0[3]=-10
      if index == 77 and h >= 9 : p0[3]=-4
     if beam == 1 :
      if index >= 61 and index <= 68 and h >= 9 : p0[3]=-35
      if index == 64 and h >= 9 : p0[3]=-40
      if index == 69 and h >= 9 : p0[3]=-33
      if index == 70 and h >= 9 : p0[3]=-20
      if index >= 71 and index <= 71 and h >= 9 : p0[3]=-30
      if index == 72 and h >= 9 : p0[3]=-25
      if index == 73 and h >= 9 : p0[3]=-15
      if index == 74 and h >= 9 : p0[3]=-5
      if index == 75 and h >= 9 : p0[3]=-4
      if index == 77 and h >= 9 : p0[3]=-5
      if index == 78 and h >= 9 : p0[3]=-4
      if index == 82 and h >= 9 : p0[3]=1

    if year == 2026 and doy == 61:
     if beam == 0 :
      if index >= 70 and index <= 71 and h >= 9 : p0[3]=-25
      if index == 73 and h >= 9 : p0[3]=-20
      if index == 76 and h >= 9 : p0[3]=-5
      if index == 192 and h >= 9 : p0[3]=10
      if index == 227 and h >= 9 : p0[3]=38
      if index == 235 and h >= 9 : p0[3]=16
      if index == 236 and h >= 9 : p0[3]=15
      if index == 237 and h >= 9 : p0[3]=10
      if index >= 239 and index <= 240 and h >= 9 : p0[3]=-2
      if index == 241 and h >= 9 : p0[3]=-15
      if index == 242 and h >= 9 : p0[3]=-15
      if index == 243 and h >= 9 : p0[3]=-20
      if index >= 244 and index <= 245 and h >= 9 : p0[3]=-15
      if index >= 246 and index <= 247 and h >= 9 : p0[3]=-30
      if index == 250 and h >= 9 : p0[3]=-35
      if index == 251 and h >= 9 : p0[3]=-30
      if index == 255 and h >= 9 : p0[3]=-40
      if index == 261 and h >= 9 : p0[3]=-35   
     if beam == 1 :
      if index == 59 and h >= 9 : p0[3]=-30
      if index == 60 and h >= 9 : p0[3]=-25
      if index == 62 and h >= 9 : p0[3]=-28
      if index == 63 and h >= 9 : p0[3]=-25
      if index == 74 and h >= 9 : p0[3]=-15
      if index == 76 and h >= 9 : p0[3]=-7
      if index == 77 and h >= 9 : p0[3]=-8
      if index == 192 and h >= 9 : p0[3]=10
      if index == 234 and h >= 9 : p0[3]=25
      if index == 236 and h >= 9 : p0[3]=20
      if index == 238 and h >= 9 : p0[3]=22
      if index == 239 and h >= 9 : p0[3]=5
      if index == 240 and h >= 9 : p0[3]=0
      if index == 241 and h >= 9 : p0[3]=-10
      if index == 242 and h >= 9 : p0[3]=-5
      if index >= 243 and index <= 244 and h >= 9 : p0[3]=-10
      if index == 245 and h >= 9 : p0[3]=-2
      if index >= 246 and index <= 248 and h >= 9 : p0[3]=-18
      if index == 249 and h >= 9 : p0[3]=-35
      if index == 250 and h >= 9 : p0[3]=-20
      if index == 251 and h >= 9 : p0[3]=-15
      if index == 252 and h >= 9 : p0[3]=-20
      if index >= 253 and index <= 254 and h >= 9 : p0[3]=-40
      if index == 257 and h >= 9 : p0[3]=-28
      if index == 260 and h >= 9 : p0[3]=-25
      if index == 266 and h >= 9 : p0[3]=-20
      if index >= 269 and index <= 270 and h >= 9 : p0[3]=-25
      if index == 280 and h >= 9 : p0[3]=-10

    if year == 2026 and doy == 60:  #1 mar
     if beam == 0 :
      if index == 71 and h >= 9 : p0[3]=-25
      if index == 230 and h >= 9 : p0[3]=50
      if index == 231 and h >= 9 : p0[3]=40
      if index == 232 and h >= 9 : p0[3]=40
      if index >= 233 and index <= 234 and h >= 9 : p0[3]=40
      if index == 235 and h >= 9 : p0[3]=32
      if index == 236 and h >= 9 : p0[3]=20
      if index == 238 and h >= 9 : p0[3]=38
      if index == 239 and h >= 9 : p0[3]=33
      if index == 240 and h >= 9 : p0[3]=5
      if index >= 241 and index <= 242 and h >= 9 : p0[3]=5
      if index >= 244 and index <= 245 and h >= 9 : p0[3]=5
      if index == 248 and h >= 9 : p0[3]=-5
      if index == 251 and h >= 9 : p0[3]=-10
      if index == 252 and h >= 9 : p0[3]=-25
      if index == 255 and h >= 9 : p0[3]=-25
      if index == 256 and h >= 9 : p0[3]=-30
      if index == 258 and h >= 9 : p0[3]=-38
     if beam == 1 :
      if index == 65 and h >= 9 : p0[3]=-25
      if index == 91 and h >= 9 : p0[3]=3
      if index == 231 and h >= 9 : p0[3]=50
      if index == 232 and h >= 9 : p0[3]=52
      if index == 233 and h >= 9 : p0[3]=50
      if index == 234 and h >= 9 : p0[3]=55
      if index == 235 and h >= 9 : p0[3]=35
      if index == 236 and h >= 9 : p0[3]=30
      if index == 237 and h >= 9 : p0[3]=35
      if index == 240 and h >= 9 : p0[3]=15
      if index >= 241 and index <= 242 and h >= 9 : p0[3]=12
      if index == 244 and h >= 9 : p0[3]=15
      if index == 246 and h >= 9 : p0[3]=5
      if index == 248 and h >= 9 : p0[3]=0
      if index == 249 and h >= 9 : p0[3]=3
      if index == 250 and h >= 9 : p0[3]=2
      if index == 251 and h >= 9 : p0[3]=0
      if index == 252 and h >= 9 : p0[3]=-20
      if index == 254 and h >= 9 : p0[3]=-20
      if index >= 256 and index <= 257 and h >= 9 : p0[3]=-20
      if index == 258 and h >= 9 : p0[3]=-30
      if index >= 260 and index <= 261 and h >= 9 : p0[3]=-20

# ISCOD febrero 2026  (13 14 10 min) 5 min
    if year == 2026 and doy == 54:
     if beam == 1 :
      if index == 37 and h >= 9 : p0[3]=8

    if year == 2026 and doy == 51:
     if beam == 0 :
      if index == 240 and h >= 9 : p0[3]=-15
      if index == 242 and h >= 9 : p0[3]=-35
      if index >= 250 and index <= 251 and h >= 9 : p0[3]=-40
     if beam == 1 :
      if index == 240 and h >= 9 : p0[3]=-10
      if index == 241 and h >= 9 : p0[3]=-10
      if index == 264 and h >= 9 : p0[3]=-15

    if year == 2026 and doy == 50:
     if beam == 0 :
      if index == 5 and h >= 9 : p0[3]=-30
      if index == 132 and h >= 9 : p0[3]=25
     if beam == 1 :
      if index == 132 and h >= 9 : p0[3]=20

    if year == 2026 and doy == 49:
     if beam == 0 :
      if index == 114 and h >= 9 : p0[3]=19
      if index == 248 and h >= 9 : p0[3]=-20
      if index == 250 and h >= 9 : p0[3]=-25
      if index == 253 and h >= 9 : p0[3]=-12
      if index == 254 and h >= 9 : p0[3]=-18
     if beam == 1 :
      if index == 114 and h >= 9 : p0[3]=15
      if index == 246 and h >= 9 : p0[3]=5
      if index == 247 and h >= 9 : p0[3]=-15
      if index == 258 and h >= 9 : p0[3]=-15
      if index >= 261 and index <= 262 and h >= 9 : p0[3]=-15

    if year == 2026 and doy == 48:
     if beam == 0 :
      if index == 51 and h >= 9 : p0[3]=-45
      if index == 66 and h >= 9 : p0[3]=-50
      if index == 68 and h >= 9 : p0[3]=-55
      if index == 70 and h >= 9 : p0[3]=-45
      if index == 83 and h >= 23 : p0[3]=-3
      if index == 84 and h >= 26 : p0[3]=-3
      if index >= 151 and index <= 161 and h >= 45 : p0[3]=numpy.nan
      if index == 237 and h >= 9 : p0[3]=35
      if index == 238 and h >= 9 : p0[3]=10
      if index == 239 and h >= 9 : p0[3]=0
      if index >= 240 and index <= 241 and h >= 9 : p0[3]=-25
      if index == 245 and h >= 9 : p0[3]=-35
      if index == 246 and h >= 9 : p0[3]=-30
      if index == 252 and h >= 9 : p0[3]=-10
      if index == 254 and h >= 9 : p0[3]=-30
      if index == 256 and h >= 9 : p0[3]=-35
     if beam == 1 :
      if index == 51 and h >= 9 : p0[3]=-40
      if index == 53 and h >= 9 : p0[3]=-45
      if index == 54 and h >= 9 : p0[3]=-40
      if index >= 58 and index <= 60 and h >= 9 : p0[3]=-38
      if index == 62 and h >= 9 : p0[3]=-42
      if index == 65 and h >= 9 : p0[3]=-43
      if index >= 66 and index <= 67 and h >= 9 : p0[3]=-45
      if index == 69 and h >= 9 : p0[3]=-30
      if index == 70 and h >= 9 : p0[3]=-40
      if index == 237 and h >= 9 : p0[3]=40
      if index == 242 and h >= 9 : p0[3]=-15

    if year == 2026 and doy == 47:
     if beam == 0 :
      if index == 246 and h >= 9 : p0[3]=0

    if year == 2026 and doy == 46:
     if beam == 0 :
      if index == 9 and h >= 50 : p0[3]=numpy.nan
      if index == 22 and h >= 9 : p0[3]=-10
      if index == 29 and h >= 9 : p0[3]=-15
      if index == 31 and h >= 9 : p0[3]=-15
      if index == 236 and h >= 9 : p0[3]=30
      if index == 237 and h >= 9 : p0[3]=28
      if index == 239 and h >= 9 : p0[3]=40
      if index == 240 and h >= 9 : p0[3]=60
      if index == 242 and h >= 9 : p0[3]=40
      if index == 243 and h >= 9 : p0[3]=45
      if index >= 244 and index <= 245 and h >= 9 : p0[3]=35
      if index == 246 and h >= 9 : p0[3]=40
      if index == 247 and h >= 29 : p0[3]=0
      if index >= 252 and index <= 253 and h >= 9 : p0[3]=-20
      if index >= 255 and index <= 256 and h >= 9 : p0[3]=-20
      if index == 257 and h >= 9 : p0[3]=-10
      if index == 259 and h >= 9 : p0[3]=-10
      if index == 263 and h >= 9 : p0[3]=-23
      if index >= 264 and index <= 265 and h >= 9 : p0[3]=-25
      if index == 270 and h >= 9 : p0[3]=-20
      if index == 271 and h >= 9 : p0[3]=-15
      if index == 272 and h >= 29 : p0[3]=-30
     if beam == 1 :
      if index == 237 and h >= 9 : p0[3]=35
      if index == 238 and h >= 9 : p0[3]=58
      if index == 239 and h >= 9 : p0[3]=45
      if index == 240 and h >= 9 : p0[3]=70
      if index == 241 and h >= 9 : p0[3]=65
      if index == 242 and h >= 9 : p0[3]=50
      if index == 243 and h >= 9 : p0[3]=50
      if index == 246 and h >= 9 : p0[3]=45
      if index == 247 and h <= 29 : p0[3]=35
      if index == 251 and h >= 9 : p0[3]=-5
      if index >= 252 and index <= 256 and h >= 9 : p0[3]=-10
      if index == 257 and h >= 9 : p0[3]=0
      if index >= 260 and index <= 262 and h >= 9 : p0[3]=0

    if year == 2026 and doy == 45:
     if beam == 0 :
      if index == 47 and h >= 9 : p0[3]=5
      if index == 81 and h >= 9 : p0[3]=15
      if index == 125 and h >= 9 : p0[3]=35
      if index == 126 and h >= 9 : p0[3]=40
      if index == 127 and h >= 9 : p0[3]=10
      if index == 128 and h >= 9 : p0[3]=10
      if index == 132 and h >= 9 : p0[3]=-15
      if index >= 133 and index <= 135 and h >= 9 : p0[3]=-25
      if index == 138 and h >= 9 : p0[3]=-60
     if beam == 1 :
      if index == 47 and h >= 9 : p0[3]=5
      if index == 81 and h >= 9 : p0[3]=8
      if index == 127 and h >= 9 : p0[3]=20
      if index == 128 and h >= 9 : p0[3]=15
      if index == 129 and h >= 9 : p0[3]=0
      if index == 135 and h >= 9 : p0[3]=-15
      if index == 137 and h >= 9 : p0[3]=-40

    if year == 2026 and doy == 44:
     if beam == 0 :
      if index == 123 and h >= 9 : p0[3]=-10
      if index == 128 and h >= 9 : p0[3]=-10

# MP enero febrero 2026
#    if year == 2026 and doy == 59:
#     if beam == 0 :
#      if index == 13 and h >= 9 : p0[3]=-25
#     if beam == 1 :
#      if index == 15 and h >= 9 : p0[3]=-20

    if year == 2026 and doy == 59:
     if beam == 0 :
      if index == 13 and h >= 9 : p0[3]=-30
      if index == 66 and h >= 9 : p0[3]=-45
      if index == 68 and h >= 9 : p0[3]=-30
      if index == 69 and h >= 9 : p0[3]=-40
      if index == 74 and h >= 9 : p0[3]=-10
      if index == 234 and h >= 9 : p0[3]=15
      if index == 235 and h >= 9 : p0[3]=5
      if index == 237 and h >= 9 : p0[3]=-5
      if index == 238 and h >= 9 : p0[3]=-10
      if index == 266 and h >= 9 : p0[3]=-30
      if index == 271 and h >= 9 : p0[3]=-25
     if beam == 1 :
      if index == 48 and h >= 9 : p0[3]=-23
      if index == 65 and h >= 9 : p0[3]=-40
      if index == 66 and h >= 9 : p0[3]=-40
      if index == 68 and h >= 9 : p0[3]=-25
      if index == 71 and h >= 9 : p0[3]=-20
      if index == 227 and h >= 9 : p0[3]=45
      if index == 232 and h >= 9 : p0[3]=35
      if index == 234 and h >= 9 : p0[3]=20
      if index == 235 and h >= 9 : p0[3]=10
      if index == 236 and h >= 9 : p0[3]=7
      if index == 237 and h >= 9 : p0[3]=0
      if index == 239 and h >= 9 : p0[3]=0
      if index == 248 and h >= 9 : p0[3]=-15
      if index == 251 and h >= 9 : p0[3]=-15
      if index == 267 and h >= 9 : p0[3]=-20
      if index == 272 and h >= 9 : p0[3]=-25

    if year == 2026 and doy == 58:
     if beam == 0 :
      if index == 62 and h >= 9 : p0[3]=-30
      if index == 65 and h >= 9 : p0[3]=-25
      if index == 92 and h >= 9 : p0[3]=0
      if index == 104 and h >= 9 : p0[3]=15
      if index == 240 and h >= 9 : p0[3]=13
      if index >= 242 and index <= 243 and h >= 9 : p0[3]=-5
      if index == 245 and h >= 9 : p0[3]=-10
      if index >= 249 and index <= 250 and h >= 9 : p0[3]=-10
      if index >= 252 and index <= 253 and h >= 9 : p0[3]=-15
      if index == 256 and h >= 9 : p0[3]=-25
      if index == 257 and h >= 9 : p0[3]=-30
      if index == 267 and h >= 9 : p0[3]=-35
      if index == 268 and h >= 9 : p0[3]=-20
      if index == 274 and h >= 9 : p0[3]=-35
     if beam == 1 :
      if index == 30 and h >= 9 : p0[3]=-15
      if index == 63 and h >= 9 : p0[3]=-25
      if index == 65 and h >= 9 : p0[3]=-20
      if index == 66 and h >= 9 : p0[3]=-20
      if index == 69 and h >= 9 : p0[3]=-30
      if index >= 71 and index <= 72 and h >= 9 : p0[3]=-25
      if index == 77 and h >= 9 : p0[3]=-12
      if index == 83 and h >= 9 : p0[3]=-3
      if index == 92 and h >= 9 : p0[3]=0
      if index == 93 and h >= 19 : p0[3]=0
      if index == 102 and h >= 9 : p0[3]=10
      if index == 137 and h >= 9 : p0[3]=9
      if index == 239 and h >= 9 : p0[3]=20
      if index >= 242 and index <= 243 and h >= 9 : p0[3]=0
      if index == 245 and h >= 9 : p0[3]=-2
      if index >= 247 and index <= 248 and h >= 9 : p0[3]=-5
      if index == 249 and h >= 9 : p0[3]=-5
      if index == 265 and h >= 9 : p0[3]=-15
      if index == 267 and h >= 9 : p0[3]=-30

    if year == 2026 and doy == 57:
     if beam == 0 :
      if index == 52 and h >= 9 : p0[3]=-23
      if index == 67 and h >= 9 : p0[3]=-15
      if index == 232 and h >= 9 : p0[3]=50
      if index == 233 and h >= 9 : p0[3]=35
      if index == 234 and h >= 9 : p0[3]=30
      if index == 236 and h >= 9 : p0[3]=20
      if index >= 237 and index <= 238 and h >= 9 : p0[3]=10
      if index == 239 and h >= 9 : p0[3]=3
      if index == 240 and h >= 9 : p0[3]=0
      if index == 241 and h >= 9 : p0[3]=-17
      if index == 242 and h >= 9 : p0[3]=-30
      if index >= 245 and index <= 247 and h >= 9 : p0[3]=-10
      if index == 248 and h >= 9 : p0[3]=0
      if index == 249 and h >= 9 : p0[3]=-15
      if index == 251 and h >= 9 : p0[3]=-25
      if index == 253 and h >= 9 : p0[3]=-10
      if index == 254 and h >= 9 : p0[3]=-30
      if index == 255 and h >= 9 : p0[3]=-20
      if index == 256 and h >= 9 : p0[3]=-22
      if index == 257 and h >= 9 : p0[3]=-20
      if index == 258 and h >= 9 : p0[3]=-25
      if index == 259 and h >= 9 : p0[3]=-30
      if index == 260 and h >= 9 : p0[3]=-30
      if index >= 261 and index <= 262 and h >= 9 : p0[3]=-25
      if index == 268 and h >= 9 : p0[3]=-30
     if beam == 1 :
      if index == 11 and h >= 26 : p0[3]=-10
      if index == 12 and h >= 24 : p0[3]=-5
      if index == 48 and h >= 9 : p0[3]=-1
      if index == 49 and h >= 9 : p0[3]=-10
      if index == 51 and h >= 9 : p0[3]=-10
      if index == 59 and h >= 9 : p0[3]=-17
      if index == 60 and h >= 9 : p0[3]=-20
      if index == 61 and h >= 9 : p0[3]=-20
      if index == 62 and h >= 9 : p0[3]=-23
      if index == 64 and h >= 9 : p0[3]=-19
      if index == 69 and h >= 9 : p0[3]=-15
      if index == 75 and h >= 9 : p0[3]=-13
      if index == 226 and h >= 9 : p0[3]=42
      if index == 232 and h >= 9 : p0[3]=60
      if index == 233 and h >= 9 : p0[3]=42
      if index >= 234 and index <= 235 and h >= 9 : p0[3]=40
      if index == 236 and h >= 9 : p0[3]=25
      if index == 237 and h >= 9 : p0[3]=20
      if index == 238 and h >= 9 : p0[3]=15
      if index == 240 and h >= 9 : p0[3]=5
      if index == 241 and h >= 9 : p0[3]=-5
      if index == 242 and h >= 9 : p0[3]=-20
      if index == 243 and h >= 9 : p0[3]=-10
      if index == 245 and h >= 9 : p0[3]=0
      if index == 246 and h >= 9 : p0[3]=-5
      if index == 247 and h >= 9 : p0[3]=-5
      if index == 249 and h >= 9 : p0[3]=-5
      if index == 252 and h >= 9 : p0[3]=-10
      if index == 254 and h >= 9 : p0[3]=-20
      if index == 255 and h >= 9 : p0[3]=-10
      if index == 256 and h >= 9 : p0[3]=0
      if index == 257 and h >= 9 : p0[3]=-10
      if index == 259 and h >= 9 : p0[3]=-20
      if index == 261 and h >= 9 : p0[3]=-15
      if index == 262 and h >= 9 : p0[3]=-13
      if index == 269 and h >= 9 : p0[3]=-10
      if index == 275 and h >= 9 : p0[3]=-20

    if year == 2026 and doy == 56:
     if beam == 0 :
      if index == 231 and h >= 9 : p0[3]=30
      if index == 234 and h >= 9 : p0[3]=15
      if index == 238 and h >= 9 : p0[3]=-5
      if index == 239 and h >= 9 : p0[3]=0
      if index >= 240 and index <= 241 and h >= 9 : p0[3]=5
      if index == 243 and h >= 9 : p0[3]=0
      if index == 244 and h >= 9 : p0[3]=-10
      if index == 247 and h >= 9 : p0[3]=-20
      if index == 249 and h <= 35 : p0[3]=40
      if index == 251 and h >= 35 : p0[3]=-20
      if index == 252 and h >= 35 : p0[3]=0
      if index == 253 and h >= 35 : p0[3]=-30
      if index == 253 and h <= 34 : p0[3]=80
      if index == 254 and h >= 35 : p0[3]=-20
      if index == 255 and h >= 29 : p0[3]=-25
      if index == 255 and h <= 28 : p0[3]=30
      if index == 256 and h >= 9 : p0[3]=-20
      if index == 258 and h >= 25 : p0[3]=-10
      if index == 259 and h <= 24 : p0[3]=30
      if index == 263 and h >= 9 : p0[3]=-30
      if index == 266 and h >= 9 : p0[3]=-10
     if beam == 1 :
      if index >= 231 and index <= 232 and h >= 9 : p0[3]=35
      if index == 234 and h >= 9 : p0[3]=20
      if index == 240 and h >= 9 : p0[3]=10
      if index == 241 and h >= 9 : p0[3]=15
      if index == 243 and h >= 9 : p0[3]=10
      if index >= 244 and index <= 245 and h >= 9 : p0[3]=-2
      if index == 246 and h >= 9 : p0[3]=-5
      if index == 249 and h >= 35 : p0[3]=-5
      if index == 249 and h <= 34 : p0[3]=30
      if index == 250 and h <= 34 : p0[3]=40
      if index == 251 and h <= 34 : p0[3]=60
      if index == 252 and h >= 35 : p0[3]=0
      if index == 252 and h <= 34 : p0[3]=70
      if index == 253 and h <= 34 : p0[3]=60
      if index == 254 and h >= 35 : p0[3]=-10
      if index == 254 and h <= 34 : p0[3]=-40
      if index == 255 and h >= 29 : p0[3]=-20
      if index == 255 and h <= 28 : p0[3]=40
      if index == 257 and h >= 9 : p0[3]=10
      if index == 259 and h >= 25 : p0[3]=-10
      if index == 260 and h >= 27 : p0[3]=-15
      if index == 277 and h >= 9 : p0[3]=-40
      if index == 278 and h >= 9 : p0[3]=-38

    if year == 2026 and doy == 42:
     if beam == 0 :
      if index >= 9 and index <= 10 and h >= 9 : p0[3]=-35
      if index == 24 and h >= 9 : p0[3]=-25
      if index == 26 and h >= 9 : p0[3]=-30
      if index == 41 and h >= 9 : p0[3]=-5
      if index == 42 and h >= 9 : p0[3]=0
      if index == 45 and h >= 9 : p0[3]=5
      if index == 47 and h >= 9 : p0[3]=-7
      if index == 48 and h >= 9 : p0[3]=-1
      if index == 52 and h >= 9 : p0[3]=40
      if index == 53 and h >= 9 : p0[3]=45
      if index == 56 and h >= 9 : p0[3]=40
      if index == 57 and h >= 9 : p0[3]=40
      if index == 58 and h >= 29 : p0[3]=40
      if index == 64 and h >= 9 : p0[3]=-5
      if index == 65 and h >= 9 : p0[3]=0
      if index == 72 and h >= 9 : p0[3]=13
      if index == 73 and h >= 9 : p0[3]=5
     if beam == 1 :
      if index == 25 and h >= 9 : p0[3]=-20
      if index == 40 and h >= 9 : p0[3]=-5
      if index == 42 and h >= 9 : p0[3]=5
      if index == 43 and h >= 9 : p0[3]=5
      if index == 45 and h >= 9 : p0[3]=10
      if index == 46 and h >= 9 : p0[3]=0
      if index == 47 and h >= 9 : p0[3]=-5
      if index == 48 and h >= 9 : p0[3]=0
      if index == 54 and h >= 9 : p0[3]=50
      if index == 55 and h >= 9 : p0[3]=62
      if index == 57 and h >= 9 : p0[3]=45
      if index == 59 and h >= 29 : p0[3]=70
      if index == 60 and h >= 9 : p0[3]=55
      if index == 71 and h >= 9 : p0[3]=0
      if index == 73 and h >= 9 : p0[3]=5
      if index == 74 and h >= 9 : p0[3]=-1
      if index == 78 and h >= 9 : p0[3]=-2
      if index == 81 and h >= 9 : p0[3]=-3

    if year == 2026 and doy == 41:
     if beam == 0 :
      if index == 62 and h >= 9 : p0[3]=-35
      if index >= 66 and index <= 67 and h >= 9 : p0[3]=-48
      if index == 68 and h >= 9 : p0[3]=-50
      if index == 71 and h >= 9 : p0[3]=-40
      if index == 72 and h >= 9 : p0[3]=-40
      if index == 75 and h >= 9 : p0[3]=-18
      if index == 80 and h >= 9 : p0[3]=-10
      if index == 85 and h >= 35 : p0[3]=numpy.nan
      if index == 234 and h >= 9 : p0[3]=38
      if index == 236 and h >= 9 : p0[3]=8
      if index >= 237 and index <= 238 and h >= 9 : p0[3]=0
      if index >= 239 and index <= 241 and h >= 9 : p0[3]=-10
      if index == 242 and h >= 9 : p0[3]=0
      if index == 243 and h >= 9 : p0[3]=20
      if index == 244 and h >= 9 : p0[3]=40
      if index == 245 and h >= 9 : p0[3]=40
      if index == 246 and h >= 9 : p0[3]=35
      if index == 247 and h >= 9 : p0[3]=50
      if index == 249 and h >= 9 : p0[3]=20
      if index == 255 and h >= 9 : p0[3]=-30
      if index == 257 and h >= 9 : p0[3]=-20
      if index == 258 and h >= 9 : p0[3]=-15
      if index == 259 and h >= 9 : p0[3]=-20
      if index == 260 and h >= 29 : p0[3]=-25
      if index == 262 and h >= 9 : p0[3]=-40
      if index == 268 and h >= 9 : p0[3]=-45
      if index >= 273 and index <= 274 and h >= 9 : p0[3]=-50
     if beam == 1 :
      if index == 20 and h >= 9 : p0[3]=-25
      if index == 45 and h >= 9 : p0[3]=-18
      if index == 60 and h >= 9 : p0[3]=-30
      if index >= 62 and index <= 63 and h >= 9 : p0[3]=-30
      if index == 64 and h >= 9 : p0[3]=-40
      if index == 66 and h >= 9 : p0[3]=-42
      if index >= 67 and index <= 70 and h >= 9 : p0[3]=-45
      if index == 71 and h >= 9 : p0[3]=-38
      if index == 72 and h >= 9 : p0[3]=-37
      if index == 73 and h >= 9 : p0[3]=-30
      if index == 74 and h >= 9 : p0[3]=-25
      if index == 78 and h >= 9 : p0[3]=-20
      if index == 79 and h >= 9 : p0[3]=-10
      if index == 81 and h >= 9 : p0[3]=-10
      if index == 231 and h >= 9 : p0[3]=50
      if index == 236 and h >= 9 : p0[3]=15
      if index == 237 and h >= 9 : p0[3]=5
      if index == 238 and h >= 9 : p0[3]=10
      if index == 239 and h >= 9 : p0[3]=0
      if index == 241 and h >= 9 : p0[3]=0
      if index == 242 and h >= 9 : p0[3]=5
      if index == 243 and h >= 9 : p0[3]=30
      if index == 244 and h >= 9 : p0[3]=45
      if index == 245 and h >= 9 : p0[3]=45
      if index == 247 and h >= 9 : p0[3]=60
      if index == 248 and h >= 9 : p0[3]=50
      if index == 250 and h >= 9 : p0[3]=25
      if index == 257 and h >= 9 : p0[3]=-10
      if index == 259 and h >= 9 : p0[3]=-8
      if index == 260 and h >= 29 : p0[3]=-15
      if index == 261 and h >= 29 : p0[3]=-25
      if index == 275 and h >= 9 : p0[3]=-40

    if year == 2026 and doy == 40:
     if beam == 0 :
      if index == 25 and h >= 9 : p0[3]=-15
      if index == 28 and h >= 9 : p0[3]=-10
      if index == 39 and h >= 9 : p0[3]=0
      if index == 41 and h >= 9 : p0[3]=0
      if index == 46 and h >= 9 : p0[3]=5
      if index == 47 and h >= 9 : p0[3]=15
      if index == 58 and h >= 9 : p0[3]=0
      if index == 61 and h >= 9 : p0[3]=5
      if index == 62 and h >= 9 : p0[3]=3
      if index == 63 and h >= 9 : p0[3]=10
      if index == 64 and h >= 9 : p0[3]=5
      if index >= 66 and index <= 67 and h >= 9 : p0[3]=-10
      if index >= 68 and index <= 69 and h >= 9 : p0[3]=-25
      if index == 116 and h >= 19 : p0[3]=15
      if index == 151 and h >= 9 : p0[3]=20
      if index == 152 and h >= 9 : p0[3]=20
      if index == 241 and h >= 9 : p0[3]=-5
      if index == 243 and h >= 9 : p0[3]=-20
      if index == 245 and h >= 9 : p0[3]=-15
      if index == 252 and h >= 9 : p0[3]=-20
      if index == 253 and h >= 9 : p0[3]=-10
      if index == 254 and h >= 9 : p0[3]=-25
      if index == 257 and h >= 9 : p0[3]=-15
      if index == 260 and h >= 9 : p0[3]=-5
      if index == 268 and h >= 9 : p0[3]=-15
      if index == 269 and h >= 9 : p0[3]=-30
      if index == 270 and h >= 9 : p0[3]=-25
     if beam == 1 :
      if index == 28 and h >= 9 : p0[3]=-5
      if index == 32 and h >= 9 : p0[3]=-1
      if index >= 35 and index <= 36 and h >= 9 : p0[3]=0
      if index == 37 and h >= 9 : p0[3]=5
      if index == 40 and h >= 9 : p0[3]=5
      if index == 42 and h >= 9 : p0[3]=15
      if index == 44 and h >= 9 : p0[3]=20
      if index == 46 and h >= 9 : p0[3]=15
      if index == 46 and h >= 9 : p0[3]=25
      if index == 48 and h >= 9 : p0[3]=17
      if index == 52 and h >= 9 : p0[3]=13
      if index == 53 and h >= 9 : p0[3]=10
      if index == 54 and h >= 9 : p0[3]=1
      if index == 56 and h >= 9 : p0[3]=4
      if index == 57 and h >= 9 : p0[3]=0
      if index >= 58 and index <= 60 and h >= 9 : p0[3]=3
      if index == 61 and h >= 9 : p0[3]=5
      if index == 63 and h >= 9 : p0[3]=15
      if index == 64 and h >= 9 : p0[3]=10
      if index >= 66 and index <= 67 and h >= 9 : p0[3]=-5
      if index == 71 and h >= 9 : p0[3]=-10
      if index == 72 and h >= 9 : p0[3]=-6
      if index == 73 and h >= 9 : p0[3]=-5
      if index == 123 and h >= 9 : p0[3]=10
      if index == 229 and h >= 9 : p0[3]=42
      if index == 234 and h >= 9 : p0[3]=50
      if index == 238 and h >= 9 : p0[3]=18
      if index == 242 and h >= 9 : p0[3]=-5
      if index == 243 and h >= 9 : p0[3]=-10
      if index == 244 and h >= 9 : p0[3]=-5
      if index == 245 and h >= 9 : p0[3]=-5
      if index == 246 and h >= 9 : p0[3]=0
      if index == 252 and h >= 9 : p0[3]=-10
      if index == 253 and h >= 9 : p0[3]=-5
      if index == 255 and h >= 9 : p0[3]=10
      if index == 256 and h >= 9 : p0[3]=25
      if index == 260 and h >= 9 : p0[3]=5

    if year == 2026 and doy == 39:
     if beam == 0 :
      if index == 15 and h >= 22 : p0[3]=-25
      if index == 150 and h >= 9 : p0[3]=37
      if index == 151 and h >= 9 : p0[3]=35
      if index == 152 and h >= 9 : p0[3]=38
      if index == 153 and h >= 9 : p0[3]=40
      if index == 153 and h >= 35 : p0[3]=numpy.nan
      if index == 159 and h >= 9 : p0[3]=35
      if index == 163 and h >= 25 : p0[3]=35
      if index == 168 and h >= 9 : p0[3]=29
      if index == 225 and h >= 9 : p0[3]=20
      if index == 227 and h >= 9 : p0[3]=35
      if index == 230 and h >= 9 : p0[3]=50
      if index == 231 and h >= 9 : p0[3]=25
      if index >= 233 and index <= 233 and h >= 9 : p0[3]=50
      if index == 234 and h >= 9 : p0[3]=45
      if index == 235 and h >= 9 : p0[3]=40
      if index == 236 and h >= 9 : p0[3]=30
      if index == 238 and h >= 9 : p0[3]=25
      if index == 239 and h >= 9 : p0[3]=20
      if index == 240 and h >= 9 : p0[3]=15
      if index == 242 and h >= 9 : p0[3]=0
      if index == 243 and h >= 9 : p0[3]=-15
      if index >= 244 and index <= 245 and h >= 9 : p0[3]=-25
      if index == 248 and h >= 9 : p0[3]=-20
      if index == 251 and h >= 9 : p0[3]=-10
      if index == 256 and h >= 9 : p0[3]=-15
      if index == 257 and h >= 9 : p0[3]=-10
      if index == 258 and h >= 9 : p0[3]=-15
      if index == 263 and h >= 9 : p0[3]=-25
      if index == 264 and h >= 9 : p0[3]=-20
      if index == 265 and h >= 9 : p0[3]=-15
      if index == 266 and h >= 9 : p0[3]=-10
      if index == 268 and h >= 9 : p0[3]=-20
      if index == 269 and h >= 9 : p0[3]=-30
      if index == 273 and h >= 9 : p0[3]=-35
      if index == 274 and h >= 9 : p0[3]=-40
     if beam == 1 :
      if index == 21 and h >= 9 : p0[3]=-10
      if index == 45 and h >= 9 : p0[3]=0
      if index == 108 and h >= 9 : p0[3]=15
      if index == 148 and h >= 9 : p0[3]=33
      if index == 153 and h >= 9 : p0[3]=33
      if index == 229 and h >= 9 : p0[3]=48
      if index == 230 and h >= 9 : p0[3]=55
      if index == 232 and h >= 9 : p0[3]=38
      if index >= 233 and index <= 233 and h >= 9 : p0[3]=55
      if index == 234 and h >= 9 : p0[3]=50
      if index == 235 and h >= 9 : p0[3]=45
      if index == 236 and h >= 9 : p0[3]=45
      if index == 238 and h >= 9 : p0[3]=30
      if index == 239 and h >= 9 : p0[3]=30
      if index == 242 and h >= 9 : p0[3]=10
      if index == 243 and h >= 9 : p0[3]=-5
      if index == 244 and h >= 9 : p0[3]=-20
      if index == 246 and h >= 9 : p0[3]=-10
      if index == 250 and h >= 9 : p0[3]=0
      if index == 251 and h >= 9 : p0[3]=-5
      if index == 253 and h >= 9 : p0[3]=-15
      if index == 255 and h >= 9 : p0[3]=-15
      if index == 256 and h >= 9 : p0[3]=-5
      if index == 257 and h >= 9 : p0[3]=0
      if index == 258 and h >= 9 : p0[3]=-5
      if index == 260 and h >= 9 : p0[3]=-10
      if index == 261 and h >= 9 : p0[3]=-15
      if index == 262 and h >= 9 : p0[3]=-20
      if index == 263 and h >= 9 : p0[3]=-15
      if index >= 264 and index <= 265 and h >= 9 : p0[3]=-10
      if index == 267 and h >= 9 : p0[3]=0
      if index == 274 and h >= 9 : p0[3]=-30
      if index == 280 and h >= 9 : p0[3]=-40

    if year == 2026 and doy == 38:
     if beam == 0 :
      if index == 26 and h >= 9 : p0[3]=-18
      if index == 34 and h >= 9 : p0[3]=-15
      if index == 39 and h >= 9 : p0[3]=-20
      if index == 40 and h >= 9 : p0[3]=-16
      if index == 50 and h >= 9 : p0[3]=-8
      if index == 54 and h >= 9 : p0[3]=-1
      if index == 55 and h >= 9 : p0[3]=0
      if index == 56 and h >= 9 : p0[3]=0
      if index == 57 and h >= 9 : p0[3]=1
      if index == 58 and h >= 9 : p0[3]=5
      if index == 59 and h >= 9 : p0[3]=0
      if index == 60 and h >= 9 : p0[3]=0
      if index == 63 and h >= 9 : p0[3]=3
      if index == 64 and h >= 9 : p0[3]=0
      if index == 65 and h >= 9 : p0[3]=-5
      if index == 69 and h >= 9 : p0[3]=-30
      if index == 72 and h >= 9 : p0[3]=-25
      if index == 111 and h >= 9 : p0[3]=15
      if index == 121 and h >= 9 : p0[3]=25
      if index == 122 and h >= 9 : p0[3]=22
      if index == 148 and h >= 9 : p0[3]=30
      if index == 148 and h >= 35 : p0[3]=numpy.nan
      if index == 150 and h >= 9 : p0[3]=30
      if index == 151 and h >= 35 : p0[3]=numpy.nan
      if index == 153 and h >= 35 : p0[3]=numpy.nan
      if index == 158 and h >= 26 : p0[3]=27
      if index == 230 and h >= 9 : p0[3]=45
      if index == 231 and h >= 9 : p0[3]=50
      if index == 233 and h >= 9 : p0[3]=55
      if index == 234 and h >= 9 : p0[3]=42
      if index >= 235 and index <= 235 and h >= 9 : p0[3]=42
      if index == 236 and h >= 27 : p0[3]=30
      if index == 237 and h >= 27 : p0[3]=17
      if index == 238 and h >= 27 : p0[3]=12
      if index == 239 and h >= 9 : p0[3]=10
      if index >= 240 and index <= 241 and h >= 9 : p0[3]=-25
      if index == 242 and h >= 9 : p0[3]=-20
      if index >= 243 and index <= 244 and h >= 9 : p0[3]=-15
      if index == 245 and h >= 9 : p0[3]=-5
      if index == 247 and h >= 9 : p0[3]=-30
      if index >= 249 and index <= 250 and h >= 9 : p0[3]=-10
      if index == 251 and h >= 9 : p0[3]=-20
      if index == 252 and h >= 9 : p0[3]=-15
      if index == 254 and h >= 9 : p0[3]=-25
      if index >= 255 and index <= 256 and h >= 9 : p0[3]=-20
      if index == 260 and h >= 9 : p0[3]=-25
      if index == 262 and h >= 9 : p0[3]=-35
      if index == 269 and h >= 9 : p0[3]=-25
      if index == 271 and h >= 9 : p0[3]=-35
     if beam == 1 :
      if index == 5 and h >= 9 : p0[3]=-15
      if index == 8 and h >= 9 : p0[3]=-23
      if index == 17 and h >= 9 : p0[3]=-15
      if index == 31 and h >= 9 : p0[3]=5
      if index == 32 and h >= 9 : p0[3]=-4
      if index == 34 and h >= 9 : p0[3]=-8
      if index == 40 and h >= 9 : p0[3]=-10
      if index == 41 and h >= 9 : p0[3]=-10
      if index == 43 and h >= 9 : p0[3]=-18
      if index == 48 and h >= 9 : p0[3]=-10
      if index == 49 and h >= 9 : p0[3]=-5
      if index == 51 and h >= 9 : p0[3]=0
      if index == 52 and h >= 9 : p0[3]=-2
      if index == 53 and h >= 9 : p0[3]=0
      if index == 55 and h >= 9 : p0[3]=5
      if index == 61 and h >= 9 : p0[3]=0
      if index == 62 and h >= 9 : p0[3]=0
      if index == 70 and h >= 9 : p0[3]=-35
      if index == 71 and h >= 9 : p0[3]=-30
      if index == 73 and h >= 9 : p0[3]=-25
      if index == 74 and h >= 9 : p0[3]=-20
      if index == 104 and h >= 9 : p0[3]=10
      if index == 153 and h >= 9 : p0[3]=30
      if index == 192 and h >= 25 : p0[3]=10
      if index == 229 and h >= 9 : p0[3]=50
      if index >= 231 and index <= 233 and h >= 9 : p0[3]=55
      if index == 234 and h >= 9 : p0[3]=60
      if index == 237 and h >= 9 : p0[3]=23
      if index == 238 and h >= 9 : p0[3]=25
      if index == 240 and h >= 9 : p0[3]=-15
      if index == 242 and h >= 9 : p0[3]=-10
      if index == 244 and h >= 9 : p0[3]=-5
      if index == 245 and h >= 9 : p0[3]=0
      if index == 249 and h >= 9 : p0[3]=-5
      if index == 250 and h >= 9 : p0[3]=-1
      if index == 253 and h >= 9 : p0[3]=-10
      if index == 257 and h >= 9 : p0[3]=-20
      if index == 258 and h >= 9 : p0[3]=-30
      if index == 259 and h >= 9 : p0[3]=-10
      if index == 261 and h >= 9 : p0[3]=-25
      if index == 266 and h >= 9 : p0[3]=-10
      if index >= 267 and index <= 268 and h >= 9 : p0[3]=-20

    if year == 2026 and doy == 37:
     if beam == 0 :
      if index == 70 and h >= 9 : p0[3]=-40
      if index == 150 and h >= 9 : p0[3]=36
      if index == 151 and h >= 9 : p0[3]=35
      if index == 151 and h >= 35 : p0[3]=numpy.nan
      if index == 152 and h >= 9 : p0[3]=40
      if index == 153 and h >= 19 : p0[3]=40
      if index == 217 and h >= 9 : p0[3]=25
      if index == 224 and h >= 9 : p0[3]=30
      if index == 226 and h >= 9 : p0[3]=25
      if index >= 227 and index <= 228 and h >= 9 : p0[3]=35
      if index == 231 and h >= 9 : p0[3]=40
      if index == 232 and h >= 9 : p0[3]=30
      if index == 233 and h >= 9 : p0[3]=28
      if index == 234 and h >= 9 : p0[3]=20
      if index == 237 and h >= 9 : p0[3]=5
      if index == 238 and h >= 9 : p0[3]=-1
      if index >= 241 and index <= 242 and h >= 9 : p0[3]=20
      if index == 248 and h >= 29 : p0[3]=25
      if index == 251 and h >= 9 : p0[3]=25
      if index == 261 and h >= 9 : p0[3]=-40
      if index == 265 and h >= 9 : p0[3]=-15
      if index == 267 and h >= 9 : p0[3]=-30
      if index == 268 and h <= 29 : p0[3]=0
      if index == 272 and h >= 9 : p0[3]=-30
      if index >= 273 and index <= 274 and h >= 9 : p0[3]=-40
      if index == 275 and h >= 9 : p0[3]=-25
      if index == 280 and h >= 9 : p0[3]=-25
      if index == 281 and h >= 35 : p0[3]=-30
     if beam == 1 :
      if index == 53 and h >= 9 : p0[3]=-20
      if index == 62 and h >= 9 : p0[3]=-30
      if index == 70 and h >= 9 : p0[3]=-35
      if index == 71 and h >= 9 : p0[3]=-30
      if index == 79 and h >= 9 : p0[3]=-15
      if index == 115 and h >= 9 : p0[3]=15
      if index == 142 and h >= 9 : p0[3]=40
      if index >= 154 and index <= 155 and h >= 9 : p0[3]=35
      if index == 214 and h >= 9 : p0[3]=20
      if index == 216 and h >= 9 : p0[3]=22
      if index == 220 and h >= 9 : p0[3]=28
      if index == 225 and h >= 9 : p0[3]=35
      if index == 228 and h >= 9 : p0[3]=40
      if index >= 229 and index <= 230 and h >= 9 : p0[3]=50
      if index == 231 and h >= 9 : p0[3]=45
      if index == 232 and h >= 9 : p0[3]=35
      if index == 235 and h >= 25 : p0[3]=30
      if index == 236 and h >= 9 : p0[3]=25
      if index == 237 and h >= 9 : p0[3]=15
      if index == 238 and h >= 9 : p0[3]=10
      if index == 239 and h >= 9 : p0[3]=20
      if index == 240 and h >= 9 : p0[3]=23
      if index >= 241 and index <= 242 and h >= 9 : p0[3]=30
      if index == 243 and h >= 9 : p0[3]=35
      if index == 246 and h >= 9 : p0[3]=20
      if index == 250 and h >= 29 : p0[3]=40
      if index == 251 and h >= 9 : p0[3]=30
      if index == 252 and h >= 29 : p0[3]=20
      if index == 254 and h >= 9 : p0[3]=10
      if index == 257 and h >= 9 : p0[3]=-5
      if index == 259 and h >= 9 : p0[3]=-20
      if index == 264 and h >= 9 : p0[3]=-15
      if index == 265 and h >= 9 : p0[3]=-5
      if index == 268 and h >= 29 : p0[3]=-25
      if index == 269 and h >= 29 : p0[3]=-20
      if index == 271 and h >= 9 : p0[3]=-30
      if index == 272 and h >= 9 : p0[3]=-20

    if year == 2026 and doy == 36:
     if beam == 0 :
      if index == 11 and h >= 9 : p0[3]=-7
      if index == 24 and h >= 9 : p0[3]=5
      if index == 28 and h >= 9 : p0[3]=3
      if index == 38 and h >= 9 : p0[3]=-10
      if index == 40 and h >= 9 : p0[3]=-15
      if index >= 42 and index <= 44 and h >= 9 : p0[3]=-10
      if index == 49 and h >= 9 : p0[3]=-13
      if index >= 50 and index <= 51 and h >= 9 : p0[3]=-15
      if index == 52 and h >= 9 : p0[3]=-25
      if index == 54 and h >= 9 : p0[3]=-13
      if index == 56 and h >= 9 : p0[3]=-5
      if index == 66 and h >= 9 : p0[3]=-22
      if index == 67 and h >= 9 : p0[3]=-30
      if index >= 71 and index <= 72 and h >= 9 : p0[3]=-10
      if index == 76 and h >= 9 : p0[3]=-5
      if index == 124 and h >= 9 : p0[3]=15
      if index == 127 and h >= 9 : p0[3]=15
      if index == 141 and h >= 9 : p0[3]=15
      if index == 141 and h >= 35 : p0[3]=numpy.nan
      if index >= 149 and index <= 151 and h >= 9 : p0[3]=15
      if index == 153 and h >= 9 : p0[3]=16
      if index >= 147 and index <= 155 and h >= 35 : p0[3]=numpy.nan
      if index == 175 and h >= 9 : p0[3]=3
      if index == 175 and h >= 35 : p0[3]=numpy.nan
      if index == 232 and h >= 9 : p0[3]=45
      if index == 236 and h >= 9 : p0[3]=13
      if index == 238 and h >= 9 : p0[3]=20
      if index == 239 and h >= 9 : p0[3]=10
      if index == 242 and h >= 9 : p0[3]=-10
      if index == 243 and h >= 9 : p0[3]=-20
      if index == 246 and h >= 9 : p0[3]=0
      if index == 247 and h >= 9 : p0[3]=3
      if index == 248 and h >= 9 : p0[3]=-15
      if index == 249 and h >= 9 : p0[3]=-10
      if index == 252 and h >= 9 : p0[3]=-10
      if index == 255 and h >= 9 : p0[3]=0
      if index >= 256 and index <= 257 and h >= 9 : p0[3]=-20
      if index == 259 and h >= 9 : p0[3]=-5
      if index == 260 and h >= 9 : p0[3]=0
      if index == 261 and h >= 9 : p0[3]=-15
      if index == 265 and h >= 9 : p0[3]=-25
      if index == 267 and h >= 9 : p0[3]=-30
      if index == 272 and h >= 9 : p0[3]=-35
      if index == 274 and h >= 9 : p0[3]=-20
      if index == 276 and h >= 9 : p0[3]=-30
     if beam == 1 :
      if index == 27 and h >= 9 : p0[3]=18
      if index == 38 and h >= 9 : p0[3]=-5
      if index == 40 and h >= 9 : p0[3]=-10
      if index == 47 and h >= 9 : p0[3]=-7
      if index == 51 and h >= 9 : p0[3]=-10
      if index == 52 and h >= 9 : p0[3]=-20
      if index == 53 and h >= 9 : p0[3]=-35
      if index == 55 and h >= 9 : p0[3]=-5
      if index == 59 and h >= 9 : p0[3]=-35
      if index == 70 and h >= 9 : p0[3]=-8
      if index == 72 and h >= 9 : p0[3]=-10
      if index == 117 and h >= 9 : p0[3]=5
      if index == 120 and h >= 9 : p0[3]=5
      if index == 132 and h >= 9 : p0[3]=8
      if index == 144 and h >= 9 : p0[3]=8
      if index == 145 and h >= 9 : p0[3]=10
      if index == 146 and h >= 9 : p0[3]=10
      if index >= 147 and index <= 151 and h >= 9 : p0[3]=10
      if index == 148 and h >= 9 : p0[3]=7
      if index >= 153 and index <= 153 and h >= 9 : p0[3]=10
      if index == 154 and h >= 9 : p0[3]=8
      if index == 155 and h >= 9 : p0[3]=7
      if index >= 178 and index <= 179 and h >= 9 : p0[3]=0
      if index == 229 and h >= 9 : p0[3]=50
      if index == 233 and h >= 9 : p0[3]=50
      if index >= 234 and index <= 235 and h >= 9 : p0[3]=40
      if index == 237 and h >= 9 : p0[3]=30
      if index == 238 and h >= 9 : p0[3]=25
      if index == 246 and h >= 9 : p0[3]=5
      if index == 248 and h >= 9 : p0[3]=-4
      if index == 249 and h >= 29 : p0[3]=-5
      if index == 249 and h <= 28 : p0[3]=5
      if index == 250 and h >= 9 : p0[3]=-10
      if index == 255 and h >= 9 : p0[3]=5
      if index == 257 and h >= 9 : p0[3]=-15
      if index == 265 and h >= 9 : p0[3]=-15
      if index == 266 and h >= 9 : p0[3]=-16
      if index == 270 and h >= 9 : p0[3]=-25
      if index == 271 and h >= 9 : p0[3]=-25

    if year == 2026 and doy == 35:
     if beam == 0 :
      if index == 30 and h >= 9 : p0[3]=-30
      if index == 31 and h >= 9 : p0[3]=-28
      if index == 44 and h >= 9 : p0[3]=-23
      if index == 45 and h >= 9 : p0[3]=-25
      if index == 53 and h >= 9 : p0[3]=-20
      if index == 54 and h >= 9 : p0[3]=-10
      if index == 56 and h >= 9 : p0[3]=-15
      if index == 60 and h >= 9 : p0[3]=-30
      if index == 64 and h >= 9 : p0[3]=-35
      if index == 65 and h >= 9 : p0[3]=-35
      if index == 70 and h >= 9 : p0[3]=-30
      if index == 71 and h >= 9 : p0[3]=-25
      if index >= 75 and index <= 76 and h >= 9 : p0[3]=-5
      if index == 77 and h >= 9 : p0[3]=-3
      if index == 78 and h >= 9 : p0[3]=-2
      if index == 117 and h >= 9 : p0[3]=17
      if index == 143 and h >= 9 : p0[3]=35
      if index == 146 and h >= 9 : p0[3]=20
      if index >= 147 and index <= 148 and h >= 9 : p0[3]=20
      if index >= 149 and index <= 151 and h >= 9 : p0[3]=25
      if index == 150 and h >= 9 : p0[3]=21
      if index >= 152 and index <= 153 and h >= 9 : p0[3]=15
      if index == 154 and h >= 9 : p0[3]=20
      if index >= 144 and index <= 157 and h >= 35 : p0[3]=numpy.nan
      if index >= 160 and index <= 162 and h >= 35 : p0[3]=numpy.nan
      if index >= 165 and index <= 166 and h >= 35 : p0[3]=numpy.nan
      if index == 238 and h >= 9 : p0[3]=5
      if index == 254 and h >= 9 : p0[3]=-40
      if index == 270 and h >= 9 : p0[3]=-10
     if beam == 1 :
      if index == 10 and h >= 9 : p0[3]=-20
      if index == 23 and h >= 9 : p0[3]=-20
      if index == 44 and h >= 9 : p0[3]=-20
      if index == 49 and h >= 9 : p0[3]=-15
      if index == 50 and h >= 9 : p0[3]=-5
      if index >= 51 and index <= 53 and h >= 9 : p0[3]=-10
      if index == 55 and h >= 9 : p0[3]=0
      if index == 56 and h >= 9 : p0[3]=-5
      if index == 57 and h >= 9 : p0[3]=-4
      if index == 58 and h >= 9 : p0[3]=-15
      if index >= 59 and index <= 60 and h >= 9 : p0[3]=-25
      if index == 62 and h >= 9 : p0[3]=-25
      if index == 63 and h >= 9 : p0[3]=-20
      if index == 66 and h >= 9 : p0[3]=-35
      if index == 67 and h >= 9 : p0[3]=-30
      if index >= 76 and index <= 77 and h >= 9 : p0[3]=-5
      if index >= 115 and index <= 116 and h >= 9 : p0[3]=10
      if index == 144 and h >= 9 : p0[3]=30
      if index == 145 and h >= 9 : p0[3]=19
      if index >= 146 and index <= 147 and h >= 9 : p0[3]=15
      if index == 148 and h >= 9 : p0[3]=10
      if index >= 149 and index <= 150 and h >= 9 : p0[3]=20
      if index >= 152 and index <= 153 and h >= 9 : p0[3]=10
      if index >= 154 and index <= 156 and h >= 9 : p0[3]=15
      if index == 228 and h >= 9 : p0[3]=30
      if index == 229 and h >= 9 : p0[3]=25
      if index == 230 and h >= 9 : p0[3]=33
      if index == 232 and h >= 9 : p0[3]=35
      if index == 235 and h >= 9 : p0[3]=30
      if index == 239 and h >= 9 : p0[3]=-10
      if index == 243 and h >= 9 : p0[3]=-7
      if index == 244 and h >= 9 : p0[3]=-10
      if index == 248 and h >= 9 : p0[3]=-20
      if index >= 249 and index <= 250 and h >= 9 : p0[3]=-25

    if year == 2026 and doy == 34:
     if beam == 0 :
      if index == 28 and h >= 9 : p0[3]=-20
      if index == 69 and h >= 9 : p0[3]=-16
      if index == 71 and h >= 9 : p0[3]=0
      if index == 117 and h >= 9 : p0[3]=20
      if index == 146 and h >= 9 : p0[3]=25
      if index == 147 and h >= 35 : p0[3]=numpy.nan
      if index >= 149 and index <= 151 and h >= 35 : p0[3]=numpy.nan
      if index >= 154 and index <= 156 and h >= 35 : p0[3]=numpy.nan
      if index >= 230 and index <= 233 and h >= 9 : p0[3]=60
      if index == 235 and h >= 9 : p0[3]=30
      if index == 237 and h >= 9 : p0[3]=30
      if index == 238 and h >= 9 : p0[3]=-10
      if index == 239 and h >= 9 : p0[3]=-15
      if index == 243 and h >= 9 : p0[3]=-25
      if index == 244 and h >= 9 : p0[3]=-15
      if index == 246 and h >= 9 : p0[3]=-25
      if index == 249 and h >= 9 : p0[3]=-30
      if index == 260 and h >= 9 : p0[3]=-18
      if index == 261 and h >= 9 : p0[3]=-20
      if index == 263 and h >= 9 : p0[3]=-28
     if beam == 1 :
      if index == 26 and h >= 9 : p0[3]=-20
      if index == 60 and h >= 9 : p0[3]=-17
      if index == 63 and h >= 9 : p0[3]=-15
      if index == 70 and h >= 9 : p0[3]=-3
      if index == 71 and h >= 9 : p0[3]=-5
      if index == 72 and h >= 9 : p0[3]=-5
      if index == 110 and h >= 9 : p0[3]=13
      if index == 126 and h >= 9 : p0[3]=15
      if index == 145 and h >= 9 : p0[3]=20
      if index >= 147 and index <= 148 and h >= 9 : p0[3]=20
      if index == 152 and h >= 9 : p0[3]=18
      if index == 155 and h >= 9 : p0[3]=18
      if index == 228 and h >= 9 : p0[3]=53
      if index == 229 and h >= 9 : p0[3]=55
      if index >= 230 and index <= 233 and h >= 9 : p0[3]=65
      if index == 234 and h >= 9 : p0[3]=50
      if index == 235 and h >= 9 : p0[3]=35
      if index == 236 and h >= 9 : p0[3]=25
      if index == 238 and h >= 9 : p0[3]=0
      if index == 239 and h >= 9 : p0[3]=-5
      if index == 240 and h >= 9 : p0[3]=-15
      if index == 241 and h >= 9 : p0[3]=-5
      if index == 242 and h >= 9 : p0[3]=-10
      if index >= 244 and index <= 245 and h >= 9 : p0[3]=-10
      if index == 246 and h >= 9 : p0[3]=-20
      if index == 248 and h >= 9 : p0[3]=-15
      if index == 249 and h >= 9 : p0[3]=-20
      if index == 251 and h >= 9 : p0[3]=0
      if index == 252 and h >= 9 : p0[3]=5
      if index >= 253 and index <= 254 and h >= 9 : p0[3]=0
      if index == 255 and h >= 9 : p0[3]=3
      if index == 256 and h >= 9 : p0[3]=5
      if index == 259 and h >= 9 : p0[3]=-10
      if index == 264 and h >= 9 : p0[3]=-20
      if index == 267 and h >= 9 : p0[3]=-30
      if index == 268 and h >= 9 : p0[3]=-35

    if year == 2026 and doy == 33:
     if beam == 0 :
      if index == 25 and h >= 9 : p0[3]=-20
      if index == 63 and h >= 9 : p0[3]=-23
      if index == 120 and h >= 9 : p0[3]=20
      if index == 232 and h >= 9 : p0[3]=45
      if index == 233 and h >= 9 : p0[3]=30
      if index == 238 and h >= 9 : p0[3]=8
      if index == 239 and h >= 9 : p0[3]=7
      if index >= 244 and index <= 245 and h >= 9 : p0[3]=-15
      if index == 247 and h >= 9 : p0[3]=-10
      if index == 248 and h >= 9 : p0[3]=-15
      if index == 249 and h >= 9 : p0[3]=-10
      if index == 254 and h >= 9 : p0[3]=-5
      if index == 255 and h >= 9 : p0[3]=-15
      if index == 256 and h >= 26 : p0[3]=-20
      if index >= 257 and index <= 258 and h >= 27 : p0[3]=-20
      if index == 259 and h >= 27 : p0[3]=-25
      if index == 260 and h >= 9 : p0[3]=-15
      if index == 261 and h >= 9 : p0[3]=-15
      if index == 268 and h >= 9 : p0[3]=-20
      if index == 270 and h >= 9 : p0[3]=-10
     if beam == 1 :
      if index == 30 and h >= 9 : p0[3]=-10
      if index == 61 and h >= 9 : p0[3]=-10
      if index == 70 and h >= 9 : p0[3]=-10
      if index == 118 and h >= 9 : p0[3]=15
      if index >= 230 and index <= 232 and h >= 9 : p0[3]=50
      if index == 234 and h >= 9 : p0[3]=35
      if index == 237 and h >= 9 : p0[3]=33
      if index == 243 and h >= 9 : p0[3]=0
      if index >= 244 and index <= 245 and h >= 9 : p0[3]=-10
      if index >= 246 and index <= 247 and h >= 9 : p0[3]=-5
      if index == 250 and h >= 9 : p0[3]=5
      if index == 251 and h >= 9 : p0[3]=0
      if index == 252 and h >= 9 : p0[3]=-10
      if index == 253 and h >= 9 : p0[3]=-10
      if index == 255 and h >= 9 : p0[3]=-10
      if index == 257 and h >= 27 : p0[3]=-8
      if index == 258 and h >= 27 : p0[3]=-10
      if index == 259 and h >= 27 : p0[3]=-15
      if index == 260 and h >= 9 : p0[3]=0
      if index == 261 and h >= 9 : p0[3]=-5
      if index == 262 and h >= 9 : p0[3]=0
      if index == 263 and h >= 9 : p0[3]=-13
      if index == 265 and h >= 27 : p0[3]=-10
      if index == 268 and h >= 9 : p0[3]=-10
      if index == 269 and h >= 9 : p0[3]=5
      if index == 270 and h >= 9 : p0[3]=-1
      if index == 277 and h >= 9 : p0[3]=-30
      if index == 278 and h >= 9 : p0[3]=-40

    if year == 2026 and doy == 32: #01
     if beam == 0 :
      if index == 10 and h >= 25 : p0[3]=-30
      if index == 13 and h >= 21 : p0[3]=-30
      if index == 24 and h >= 9 : p0[3]=-18
      if index == 34 and h >= 9 : p0[3]=-10
      if index == 56 and h >= 9 : p0[3]=-22
      if index == 64 and h >= 9 : p0[3]=-22
      if index == 135 and h >= 9 : p0[3]=10
      if index == 230 and h >= 9 : p0[3]=55
      if index == 232 and h >= 9 : p0[3]=40
      if index == 233 and h >= 9 : p0[3]=45
      if index == 237 and h >= 9 : p0[3]=30
      if index == 238 and h >= 9 : p0[3]=15
      if index == 239 and h >= 9 : p0[3]=-1
      if index == 240 and h >= 9 : p0[3]=5
      if index >= 241 and index <= 244 and h >= 9 : p0[3]=10
      if index == 245 and h >= 9 : p0[3]=20
      if index == 246 and h >= 9 : p0[3]=0
      if index == 247 and h >= 29 : p0[3]=0
      if index == 253 and h >= 9 : p0[3]=0
      if index == 254 and h >= 9 : p0[3]=-10
      if index == 255 and h >= 9 : p0[3]=-10
      if index == 256 and h >= 9 : p0[3]=-15
      if index >= 259 and index <= 260 and h >= 9 : p0[3]=-40
      if index == 261 and h >= 9 : p0[3]=-10
      if index == 262 and h >= 9 : p0[3]=-30
      if index >= 267 and index <= 268 and h >= 9 : p0[3]=-35
      if index == 270 and h >= 9 : p0[3]=-35
     if beam == 1 :
      if index == 12 and h >= 23 : p0[3]=-20
      if index == 35 and h >= 9 : p0[3]=-1
      if index == 51 and h >= 9 : p0[3]=-17
      if index == 54 and h >= 9 : p0[3]=-18
      if index == 55 and h >= 9 : p0[3]=-20
      if index == 63 and h >= 9 : p0[3]=-18
      if index == 66 and h >= 9 : p0[3]=-16
      if index == 100 and h >= 9 : p0[3]=5
      if index == 117 and h >= 9 : p0[3]=8
      if index == 118 and h >= 9 : p0[3]=9
      if index == 151 and h >= 9 : p0[3]=10
      if index == 227 and h >= 9 : p0[3]=50
      if index == 228 and h >= 9 : p0[3]=52
      if index == 231 and h >= 9 : p0[3]=75
      if index == 232 and h >= 9 : p0[3]=50
      if index == 233 and h >= 9 : p0[3]=50
      if index == 234 and h >= 9 : p0[3]=60
      if index == 235 and h >= 9 : p0[3]=50
      if index == 236 and h >= 9 : p0[3]=15
      if index == 237 and h >= 9 : p0[3]=35
      if index == 238 and h >= 9 : p0[3]=20
      if index == 239 and h >= 9 : p0[3]=0
      if index == 240 and h >= 9 : p0[3]=15
      if index >= 241 and index <= 244 and h >= 9 : p0[3]=20
      if index == 245 and h >= 9 : p0[3]=30
      if index == 246 and h >= 9 : p0[3]=10
      if index == 247 and h >= 29 : p0[3]=10
      if index == 247 and h <= 25 : p0[3]=100
      if index == 260 and h >= 9 : p0[3]=-30
      if index == 285 and h >= 9 : p0[3]=-35


    if year == 2026 and doy == 31:
     if beam == 0 :
      if index == 1 and h >= 39 : p0[3]=-45
      if index == 5 and h >= 39 : p0[3]=-42
      if index == 14 and h >= 9 : p0[3]=-40
      if index == 24 and h >= 9 : p0[3]=-30
      if index >= 36 and index <= 37 and h >= 9 : p0[3]=-20
      if index == 51 and h >= 9 : p0[3]=-15
      if index == 60 and h >= 9 : p0[3]=-5
      if index >= 61 and index <= 62 and h >= 9 : p0[3]=-10
      if index == 64 and h >= 9 : p0[3]=-15
      if index == 66 and h >= 9 : p0[3]=-10
      if index == 69 and h >= 9 : p0[3]=-4
      if index == 224 and h >= 9 : p0[3]=28
      if index == 231 and h >= 9 : p0[3]=45
      if index == 235 and h >= 9 : p0[3]=50
      if index == 236 and h >= 9 : p0[3]=20
      if index == 239 and h >= 9 : p0[3]=20
      if index >= 240 and index <= 242 and h >= 9 : p0[3]=0
      if index >= 243 and index <= 245 and h >= 9 : p0[3]=10
      if index == 246 and h >= 9 : p0[3]=-10
      if index == 247 and h >= 9 : p0[3]=0
      if index == 255 and h >= 9 : p0[3]=10
      if index == 259 and h >= 9 : p0[3]=2
      if index == 260 and h >= 9 : p0[3]=0
      if index == 261 and h >= 9 : p0[3]=-20
      if index == 262 and h >= 9 : p0[3]=-22
      if index == 263 and h >= 9 : p0[3]=-25
      if index == 264 and h >= 9 : p0[3]=-20
     if beam == 1 :
      if index == 15 and h >= 9 : p0[3]=-30
      if index == 24 and h >= 9 : p0[3]=-25
      if index == 34 and h >= 9 : p0[3]=-25
      if index == 35 and h >= 9 : p0[3]=-20
      if index == 36 and h >= 9 : p0[3]=-10
      if index == 38 and h >= 9 : p0[3]=-10
      if index == 39 and h >= 9 : p0[3]=-17
      if index == 40 and h >= 9 : p0[3]=-5
      if index == 59 and h >= 9 : p0[3]=-5
      if index == 60 and h >= 9 : p0[3]=0
      if index == 63 and h >= 9 : p0[3]=-5
      if index == 65 and h >= 9 : p0[3]=-5
      if index == 66 and h >= 9 : p0[3]=-8
      if index == 67 and h >= 9 : p0[3]=-9
      if index == 70 and h >= 9 : p0[3]=0
      if index >= 113 and index <= 114 and h >= 9 : p0[3]=10
      if index == 122 and h >= 9 : p0[3]=12
      if index == 154 and h >= 9 : p0[3]=20
      if index == 235 and h >= 9 : p0[3]=55
      if index == 236 and h >= 9 : p0[3]=30
      if index == 237 and h >= 9 : p0[3]=30
      if index == 238 and h >= 9 : p0[3]=28
      if index == 239 and h >= 9 : p0[3]=25
      if index >= 240 and index <= 242 and h >= 9 : p0[3]=10
      if index >= 243 and index <= 245 and h >= 9 : p0[3]=20
      if index == 246 and h >= 9 : p0[3]=0
      if index == 247 and h >= 9 : p0[3]=20
      if index == 249 and h >= 9 : p0[3]=5
      if index == 250 and h >= 9 : p0[3]=15
      if index == 251 and h >= 9 : p0[3]=0
      if index == 255 and h >= 9 : p0[3]=18
      if index == 256 and h >= 9 : p0[3]=15
      if index == 261 and h >= 9 : p0[3]=-10
      if index == 262 and h >= 9 : p0[3]=-15
      if index == 265 and h >= 9 : p0[3]=-10
      if index == 270 and h >= 9 : p0[3]=-20

    if year == 2026 and doy == 30:
     if beam == 0 :
      if index == 43 and h >= 9 : p0[3]=-20
      if index == 59 and h <= 21 : p0[3]=-20
      if index >= 237 and index <= 239 and h >= 9 : p0[3]=10
      if index == 240 and h >= 9 : p0[3]=5
      if index == 243 and h >= 9 : p0[3]=20
      if index == 244 and h >= 9 : p0[3]=20
      if index == 245 and h >= 9 : p0[3]=15
      if index == 246 and h >= 9 : p0[3]=20
      if index == 248 and h >= 9 : p0[3]=20
      if index == 249 and h >= 9 : p0[3]=25
      if index == 250 and h >= 29 : p0[3]=15
      if index == 251 and h <= 29 : p0[3]=50
      if index == 252 and h >= 9 : p0[3]=-10
      if index == 257 and h >= 9 : p0[3]=-10
      if index == 258 and h >= 9 : p0[3]=0
      if index == 259 and h >= 9 : p0[3]=-20
      if index == 263 and h >= 29 : p0[3]=0
      if index >= 270 and index <= 272 and h >= 29 : p0[3]=-35
      if index == 273 and h >= 29 : p0[3]=-25
      if index >= 274 and index <= 275 and h >= 29 : p0[3]=-40
      if index == 279 and h >= 9 : p0[3]=-35
     if beam == 1 :
      if index == 26 and h >= 9 : p0[3]=-15
      if index == 65 and h >= 21 : p0[3]=-20
      if index == 224 and h >= 9 : p0[3]=30
      if index == 225 and h >= 9 : p0[3]=30
      if index == 227 and h >= 9 : p0[3]=35
      if index == 232 and h >= 9 : p0[3]=40
      if index == 234 and h >= 9 : p0[3]=42
      if index == 235 and h >= 9 : p0[3]=25
      if index == 236 and h >= 9 : p0[3]=20
      if index >= 237 and index <= 239 and h >= 9 : p0[3]=15
      if index == 240 and h >= 9 : p0[3]=10
      if index >= 241 and index <= 242 and h >= 9 : p0[3]=8
      if index == 243 and h >= 9 : p0[3]=25
      if index == 244 and h >= 9 : p0[3]=28
      if index == 245 and h >= 9 : p0[3]=22
      if index == 247 and h >= 9 : p0[3]=30
      if index == 248 and h >= 9 : p0[3]=25
      if index == 249 and h >= 9 : p0[3]=30
      if index == 251 and h >= 29 : p0[3]=-10
      if index == 255 and h >= 9 : p0[3]=0
      if index == 266 and h >= 9 : p0[3]=-10
      if index == 273 and h >= 9 : p0[3]=-20

    if year == 2026 and doy == 29:
     if beam == 0 :
      if index == 51 and h >= 9 : p0[3]=-30
      if index == 53 and h >= 9 : p0[3]=-21
      if index == 61 and h >= 9 : p0[3]=-35
      if index == 64 and h >= 9 : p0[3]=-70
      if index == 81 and h >= 9 : p0[3]=-18
      if index == 225 and h >= 9 : p0[3]=20
      if index == 232 and h >= 9 : p0[3]=20
      if index == 233 and h >= 9 : p0[3]=18
      if index == 234 and h >= 9 : p0[3]=24
      if index == 235 and h >= 9 : p0[3]=15
      if index == 237 and h >= 9 : p0[3]=15
      if index == 238 and h >= 9 : p0[3]=0
      if index == 240 and h >= 9 : p0[3]=-7
      if index == 241 and h >= 9 : p0[3]=-10
      if index == 242 and h >= 9 : p0[3]=-15
      if index == 245 and h >= 9 : p0[3]=-25
      if index == 248 and h >= 9 : p0[3]=-22
      if index == 249 and h >= 9 : p0[3]=-25
      if index == 250 and h >= 9 : p0[3]=-26
     if beam == 1 :
      if index == 27 and h >= 9 : p0[3]=-5
      if index == 38 and h >= 9 : p0[3]=-5
      if index == 39 and h >= 9 : p0[3]=-10
      if index == 41 and h >= 9 : p0[3]=-30
      if index == 42 and h >= 9 : p0[3]=-35
      if index == 45 and h >= 9 : p0[3]=-35
      if index == 52 and h >= 9 : p0[3]=-20
      if index == 62 and h >= 9 : p0[3]=-45
      if index == 72 and h >= 9 : p0[3]=-32
      if index == 77 and h >= 9 : p0[3]=-15
      if index == 228 and h >= 9 : p0[3]=45
      if index == 229 and h >= 9 : p0[3]=50
      if index == 230 and h >= 9 : p0[3]=55
      if index == 231 and h >= 9 : p0[3]=45
      if index == 232 and h >= 9 : p0[3]=30
      if index == 233 and h >= 9 : p0[3]=25
      if index == 234 and h >= 9 : p0[3]=31
      if index == 235 and h >= 9 : p0[3]=23
      if index == 237 and h >= 9 : p0[3]=20
      if index == 239 and h >= 9 : p0[3]=10
      if index == 240 and h >= 9 : p0[3]=0
      if index == 241 and h >= 9 : p0[3]=-3
      if index == 243 and h >= 9 : p0[3]=-10
      if index == 245 and h >= 9 : p0[3]=-20
      if index >= 246 and index <= 247 and h >= 9 : p0[3]=-10
      if index == 251 and h >= 9 : p0[3]=-15
      if index == 255 and h >= 9 : p0[3]=-18

    if year == 2026 and doy == 28:
     if beam == 0 :
      if index == 230 and h >= 9 : p0[3]=35
      if index == 231 and h >= 9 : p0[3]=38
      if index == 234 and h >= 9 : p0[3]=23
      if index == 235 and h >= 9 : p0[3]=15
      if index == 236 and h >= 9 : p0[3]=0
      if index == 240 and h >= 9 : p0[3]=-25
      if index == 249 and h >= 9 : p0[3]=-20
      if index == 270 and h >= 9 : p0[3]=-35
     if beam == 1 :
      if index == 207 and h >= 9 : p0[3]=12
      if index == 233 and h >= 9 : p0[3]=40
      if index == 235 and h >= 9 : p0[3]=25
      if index == 236 and h >= 9 : p0[3]=10
      if index == 237 and h >= 9 : p0[3]=-5
      if index == 238 and h >= 9 : p0[3]=-10
      if index == 239 and h >= 9 : p0[3]=-5
      if index == 240 and h >= 9 : p0[3]=-10
      if index == 241 and h >= 9 : p0[3]=-10
      if index == 242 and h >= 9 : p0[3]=-20
      if index == 245 and h >= 9 : p0[3]=-18
      if index == 249 and h >= 9 : p0[3]=-10
      if index == 259 and h >= 9 : p0[3]=-20
      if index == 262 and h >= 9 : p0[3]=-20

    if year == 2026 and doy == 27:
     if beam == 0 :
      if index == 42 and h >= 9 : p0[3]=-25
      if index >= 44 and index <= 48 and h >= 9 : p0[3]=-30
      if index == 54 and h >= 9 : p0[3]=-30
      if index == 55 and h >= 9 : p0[3]=-32
      if index == 57 and h >= 9 : p0[3]=-38
      if index == 60 and h >= 9 : p0[3]=-40
      if index == 61 and h >= 9 : p0[3]=-38
      if index == 63 and h >= 9 : p0[3]=-25
      if index == 64 and h >= 9 : p0[3]=-38
      if index == 65 and h >= 9 : p0[3]=-40
      if index == 68 and h >= 9 : p0[3]=-35
      if index == 79 and h >= 19 : p0[3]=-12
      if index == 83 and h >= 9 : p0[3]=-15
     if beam == 1 :
      if index == 29 and h >= 9 : p0[3]=-17
      if index == 35 and h >= 9 : p0[3]=-22
      if index == 42 and h >= 9 : p0[3]=-20
      if index == 44 and h >= 9 : p0[3]=-25
      if index >= 45 and index <= 46 and h >= 9 : p0[3]=-20
      if index == 47 and h >= 9 : p0[3]=-25
      if index == 52 and h >= 9 : p0[3]=-30
      if index == 62 and h >= 9 : p0[3]=-40
      if index == 65 and h >= 9 : p0[3]=-40
      if index == 68 and h >= 9 : p0[3]=-38
      if index == 69 and h >= 9 : p0[3]=-40
      if index == 73 and h >= 9 : p0[3]=-25

    if year == 2026 and doy == 26:
     if beam == 0 :
      if index == 41 and h >= 9 : p0[3]=-30
      if index >= 46 and index <= 47 and h >= 9 : p0[3]=-45
      if index == 51 and h >= 9 : p0[3]=-45
      if index == 57 and h >= 9 : p0[3]=-35
      if index >= 58 and index <= 59 and h >= 9 : p0[3]=-30
      if index >= 61 and index <= 71 and h >= 9 : p0[3]=-20
      if index == 64 and h >= 9 : p0[3]=-28
      if index == 69 and h >= 9 : p0[3]=-25
      if index == 74 and h >= 9 : p0[3]=-10
      if index == 214 and h >= 21 : p0[3]=18
      if index == 232 and h >= 9 : p0[3]=55
      if index == 234 and h >= 9 : p0[3]=40
      if index == 235 and h >= 9 : p0[3]=40
      if index == 236 and h >= 9 : p0[3]=35
      if index == 237 and h >= 9 : p0[3]=35
      if index == 241 and h >= 9 : p0[3]=20
      if index >= 242 and index <= 245 and h >= 9 : p0[3]=10
      if index == 246 and h >= 9 : p0[3]=40
      if index == 248 and h >= 9 : p0[3]=40
      if index == 250 and h >= 9 : p0[3]=10
      if index >= 251 and index <= 252 and h >= 9 : p0[3]=30
      if index == 253 and h >= 9 : p0[3]=10
      if index == 254 and h >= 9 : p0[3]=0
      if index == 255 and h >= 9 : p0[3]=10
      if index == 257 and h >= 9 : p0[3]=0
      if index == 270 and h >= 9 : p0[3]=-35
      if index == 271 and h >= 9 : p0[3]=-30
      if index == 273 and h >= 9 : p0[3]=-40
      if index == 274 and h >= 9 : p0[3]=-25
      if index == 275 and h >= 9 : p0[3]=-20
      if index == 277 and h >= 9 : p0[3]=-30
      if index >= 278 and index <= 279 and h >= 9 : p0[3]=-40
      if index == 281 and h >= 9 : p0[3]=-30
      if index == 286 and h >= 9 : p0[3]=-45
     if beam == 1 :
      if index >= 46 and index <= 47 and h >= 9 : p0[3]=-40
      if index == 48 and h >= 9 : p0[3]=-45
      if index == 50 and h >= 9 : p0[3]=-45
      if index == 51 and h >= 9 : p0[3]=-40
      if index == 52 and h >= 9 : p0[3]=-30
      if index == 56 and h >= 9 : p0[3]=-30
      if index >= 57 and index <= 59 and h >= 9 : p0[3]=-25
      if index >= 61 and index <= 68 and h >= 9 : p0[3]=-15
      if index == 66 and h >= 9 : p0[3]=-10
      if index == 69 and h >= 9 : p0[3]=-20
      if index == 71 and h >= 9 : p0[3]=-15
      if index == 72 and h >= 9 : p0[3]=-16
      if index == 120 and h >= 9 : p0[3]=2
      if index == 184 and h >= 9 : p0[3]=18
      if index == 233 and h >= 9 : p0[3]=45
      if index == 234 and h >= 9 : p0[3]=50
      if index == 235 and h >= 9 : p0[3]=50
      if index == 236 and h >= 9 : p0[3]=40
      if index == 237 and h >= 9 : p0[3]=45
      if index == 238 and h >= 9 : p0[3]=42
      if index == 245 and h >= 9 : p0[3]=15
      if index == 251 and h >= 9 : p0[3]=40
      if index == 254 and h >= 9 : p0[3]=10
      if index == 255 and h >= 9 : p0[3]=20
      if index == 256 and h >= 9 : p0[3]=10
      if index == 272 and h >= 9 : p0[3]=-20
      if index == 276 and h >= 9 : p0[3]=-10
      if index == 277 and h >= 9 : p0[3]=-20
      if index == 279 and h >= 9 : p0[3]=-30
      
    if year == 2026 and doy == 25:
     if beam == 0 :
      if index == 13 and h >= 9 : p0[3]=-27
      if index == 50 and h >= 9 : p0[3]=-27
      if index == 55 and h >= 9 : p0[3]=-25
      if index == 56 and h >= 9 : p0[3]=-22
      if index == 57 and h >= 9 : p0[3]=-23
      if index == 58 and h >= 9 : p0[3]=-25
      if index == 60 and h >= 9 : p0[3]=-20
      if index >= 61 and index <= 62 and h >= 9 : p0[3]=-30
      if index == 65 and h >= 9 : p0[3]=-15
      if index == 66 and h >= 9 : p0[3]=-5
      if index >= 67 and index <= 69 and h >= 9 : p0[3]=-20
      if index == 96 and h >= 19 : p0[3]=10
      if index == 232 and h >= 9 : p0[3]=45
      if index >= 233 and index <= 234 and h >= 9 : p0[3]=50
      if index == 235 and h >= 9 : p0[3]=40
      if index == 236 and h >= 9 : p0[3]=45
      if index == 237 and h >= 9 : p0[3]=35
      if index == 239 and h >= 9 : p0[3]=30
      if index == 240 and h >= 9 : p0[3]=25
      if index == 241 and h >= 9 : p0[3]=0
      if index == 243 and h >= 9 : p0[3]=20
      if index == 244 and h >= 9 : p0[3]=30
      if index >= 245 and index <= 247 and h >= 9 : p0[3]=40
      if index == 252 and h >= 9 : p0[3]=20
      if index == 258 and h >= 29 : p0[3]=-15
      if index == 259 and h >= 29 : p0[3]=-5
      if index == 260 and h >= 29 : p0[3]=-20
      if index == 261 and h >= 9 : p0[3]=-20
      if index == 262 and h >= 29 : p0[3]=-20
      if index >= 266 and index <= 267 and h >= 9 : p0[3]=-20
      if index == 268 and h >= 9 : p0[3]=-25
      if index == 279 and h >= 9 : p0[3]=-35
      if index == 284 and h >= 9 : p0[3]=-40
      if index == 285 and h >= 9 : p0[3]=-42
      if index == 287 and h >= 9 : p0[3]=-40
     if beam == 1 :
      if index == 13 and h >= 9 : p0[3]=-20
      if index == 35 and h >= 9 : p0[3]=-40
      if index == 55 and h >= 9 : p0[3]=-10
      if index == 56 and h >= 9 : p0[3]=-15
      if index == 57 and h >= 9 : p0[3]=-15
      if index == 58 and h >= 9 : p0[3]=-20
      if index == 59 and h >= 9 : p0[3]=-15
      if index == 61 and h >= 9 : p0[3]=-20
      if index == 63 and h >= 9 : p0[3]=-10
      if index >= 64 and index <= 65 and h >= 9 : p0[3]=-15
      if index == 66 and h >= 9 : p0[3]=-5
      if index == 76 and h >= 9 : p0[3]=-10
      if index == 86 and h >= 9 : p0[3]=-10
      if index == 118 and h >= 9 : p0[3]=10
      if index == 132 and h >= 9 : p0[3]=10
      if index == 165 and h >= 9 : p0[3]=10
      if index == 166 and h >= 9 : p0[3]=10
      if index == 226 and h >= 9 : p0[3]=35
      if index >= 228 and index <= 229 and h >= 9 : p0[3]=40
      if index == 230 and h >= 9 : p0[3]=45
      if index == 234 and h >= 9 : p0[3]=60
      if index == 235 and h >= 9 : p0[3]=45
      if index == 236 and h >= 9 : p0[3]=50
      if index == 237 and h >= 9 : p0[3]=45
      if index == 238 and h >= 9 : p0[3]=50
      if index == 240 and h >= 9 : p0[3]=30
      if index == 242 and h >= 9 : p0[3]=15
      if index == 244 and h >= 9 : p0[3]=40
      if index == 245 and h >= 9 : p0[3]=50
      if index == 246 and h >= 9 : p0[3]=40
      if index == 247 and h >= 9 : p0[3]=45
      if index == 250 and h >= 9 : p0[3]=40
      if index >= 265 and index <= 266 and h >= 9 : p0[3]=-10
      if index == 267 and h >= 9 : p0[3]=-12
      if index == 268 and h >= 9 : p0[3]=-20

    if year == 2026 and doy == 24:
     if beam == 0 :
      if index == 40 and h >= 9 : p0[3]=-25
      if index == 41 and h >= 9 : p0[3]=-30
      if index == 48 and h >= 9 : p0[3]=-38
      if index == 49 and h >= 9 : p0[3]=-35
      if index == 52 and h >= 9 : p0[3]=-23
      if index == 53 and h >= 9 : p0[3]=-25
      if index == 59 and h >= 9 : p0[3]=-40
      if index == 60 and h >= 9 : p0[3]=-45
      if index == 62 and h >= 9 : p0[3]=-40
      if index == 63 and h >= 9 : p0[3]=-35
      if index >= 67 and index <= 68 and h >= 9 : p0[3]=-30
      if index == 69 and h >= 9 : p0[3]=-20
      if index == 71 and h >= 9 : p0[3]=-20
      if index == 123 and h >= 9 : p0[3]=20
      if index == 125 and h >= 9 : p0[3]=20
      if index == 148 and h >= 19 : p0[3]=35
      if index == 152 and h >= 9 : p0[3]=35
      if index == 163 and h >= 9 : p0[3]=26
      if index == 224 and h >= 9 : p0[3]=20
      if index == 234 and h >= 9 : p0[3]=50
      if index == 243 and h >= 9 : p0[3]=0
      if index == 244 and h >= 9 : p0[3]=-5
      if index == 245 and h >= 9 : p0[3]=-20
      if index == 246 and h >= 9 : p0[3]=-25
      if index == 247 and h >= 9 : p0[3]=-15
      if index == 248 and h >= 9 : p0[3]=-20
      if index == 250 and h >= 9 : p0[3]=0
      if index == 251 and h >= 9 : p0[3]=5
      if index == 252 and h >= 9 : p0[3]=0
      if index == 253 and h >= 9 : p0[3]=5
      if index == 255 and h >= 9 : p0[3]=0
      if index == 259 and h >= 9 : p0[3]=0
      if index == 264 and h >= 9 : p0[3]=-25
      if index == 268 and h >= 9 : p0[3]=-30
      if index == 271 and h >= 9 : p0[3]=-25
      if index == 272 and h >= 9 : p0[3]=-30
      if index == 276 and h >= 9 : p0[3]=-50
      if index == 279 and h >= 9 : p0[3]=-40
      if index == 280 and h >= 9 : p0[3]=-45
     if beam == 1 :
      if index == 47 and h >= 9 : p0[3]=-30
      if index == 49 and h >= 9 : p0[3]=-25
      if index == 51 and h >= 9 : p0[3]=-18
      if index == 53 and h >= 9 : p0[3]=-15
      if index == 56 and h >= 9 : p0[3]=-20
      if index >= 57 and index <= 58 and h >= 9 : p0[3]=-30
      if index == 62 and h >= 9 : p0[3]=-37
      if index == 63 and h >= 9 : p0[3]=-30
      if index == 66 and h >= 9 : p0[3]=-15
      if index >= 67 and index <= 68 and h >= 9 : p0[3]=-25
      if index >= 69 and index <= 70 and h >= 9 : p0[3]=-15
      if index == 120 and h >= 9 : p0[3]=18
      if index == 121 and h >= 9 : p0[3]=16
      if index == 122 and h >= 9 : p0[3]=17
      if index >= 152 and index <= 153 and h >= 9 : p0[3]=25
      if index == 154 and h >= 9 : p0[3]=28
      if index == 156 and h >= 19 : p0[3]=23
      if index == 163 and h >= 9 : p0[3]=22
      if index == 186 and h >= 9 : p0[3]=13
      if index == 229 and h <= 21 : p0[3]=55
      if index == 234 and h >= 9 : p0[3]=55
      if index == 235 and h >= 9 : p0[3]=50
      if index == 236 and h >= 9 : p0[3]=45
      if index == 237 and h >= 9 : p0[3]=30
      if index == 239 and h >= 9 : p0[3]=22
      if index == 240 and h >= 9 : p0[3]=25
      if index == 241 and h >= 9 : p0[3]=10
      if index == 242 and h >= 9 : p0[3]=5
      if index == 243 and h >= 9 : p0[3]=8
      if index == 244 and h >= 9 : p0[3]=0
      if index == 245 and h >= 9 : p0[3]=-10
      if index >= 247 and index <= 248 and h >= 9 : p0[3]=-10
      if index == 250 and h >= 9 : p0[3]=10
      if index == 251 and h >= 9 : p0[3]=25
      if index == 252 and h >= 9 : p0[3]=7
      if index == 253 and h >= 9 : p0[3]=10
      if index == 254 and h >= 9 : p0[3]=0
      if index == 255 and h >= 9 : p0[3]=5
      if index == 257 and h >= 9 : p0[3]=5
      if index == 263 and h >= 9 : p0[3]=-15
      if index == 275 and h >= 9 : p0[3]=-30

    if year == 2026 and doy == 23:
     if beam == 0 :
      if index == 123 and h >= 9 : p0[3]=20
      if index == 129 and h >= 9 : p0[3]=25
      if index == 229 and h >= 9 : p0[3]=45
      if index == 232 and h >= 9 : p0[3]=35
      if index == 239 and h >= 9 : p0[3]=23
      if index == 240 and h >= 9 : p0[3]=25
      if index == 241 and h >= 9 : p0[3]=5
      if index >= 242 and index <= 243 and h >= 9 : p0[3]=8
      if index == 246 and h >= 9 : p0[3]=-15
      if index == 247 and h >= 9 : p0[3]=-20
      if index >= 248 and index <= 249 and h >= 9 : p0[3]=-20
      if index == 250 and h >= 9 : p0[3]=-27
      if index == 252 and h >= 9 : p0[3]=-18
      if index == 253 and h >= 9 : p0[3]=-20
      if index == 254 and h >= 9 : p0[3]=-25
      if index == 257 and h >= 9 : p0[3]=-20
      if index == 258 and h >= 9 : p0[3]=-30
      if index >= 259 and index <= 260 and h >= 9 : p0[3]=-35
      if index == 264 and h >= 9 : p0[3]=-30
      if index == 271 and h >= 9 : p0[3]=-35
     if beam == 1 :
      if index == 124 and h >= 9 : p0[3]=16
      if index == 133 and h >= 9 : p0[3]=25
      if index == 153 and h >= 9 : p0[3]=20
      if index == 174 and h >= 9 : p0[3]=5
      if index == 233 and h >= 9 : p0[3]=50
      if index == 236 and h >= 9 : p0[3]=38
      if index >= 237 and index <= 238 and h >= 9 : p0[3]=40
      if index == 239 and h >= 9 : p0[3]=32
      if index == 240 and h >= 9 : p0[3]=30
      if index >= 241 and index <= 244 and h >= 9 : p0[3]=15
      if index == 242 and h >= 9 : p0[3]=18
      if index == 245 and h >= 9 : p0[3]=0
      if index == 246 and h >= 9 : p0[3]=-5
      if index == 247 and h >= 9 : p0[3]=-10
      if index == 251 and h >= 9 : p0[3]=-5
      if index == 254 and h >= 9 : p0[3]=-15
      if index >= 255 and index <= 256 and h >= 9 : p0[3]=-10
      if index == 258 and h >= 9 : p0[3]=-20
      if index == 259 and h >= 9 : p0[3]=-25
      if index == 261 and h >= 9 : p0[3]=-25
      if index == 264 and h >= 9 : p0[3]=-20
      if index >= 270 and index <= 272 and h >= 9 : p0[3]=-25
      if index == 279 and h >= 9 : p0[3]=-25
      if index == 280 and h >= 9 : p0[3]=-23

    if year == 2026 and doy == 22:
     if beam == 0 :
      if index == 4 and h >= 9 : p0[3]=-30
      if index == 10 and h >= 9 : p0[3]=-25
      if index == 231 and h >= 9 : p0[3]=30
      if index == 233 and h >= 9 : p0[3]=25
      if index == 235 and h >= 9 : p0[3]=38
      if index == 236 and h >= 9 : p0[3]=35
      if index >= 239 and index <= 240 and h >= 9 : p0[3]=25
      if index == 241 and h >= 9 : p0[3]=15
      if index == 242 and h >= 9 : p0[3]=-5
      if index >= 244 and index <= 245 and h >= 9 : p0[3]=-20
      if index == 247 and h >= 9 : p0[3]=-15
      if index == 249 and h >= 9 : p0[3]=-25
     if beam == 1 :
      if index == 0 and h >= 9 : p0[3]=-20
      if index == 2 and h >= 9 : p0[3]=-15
      if index == 52 and h >= 9 : p0[3]=0
      if index == 58 and h >= 9 : p0[3]=-15
      if index == 59 and h >= 9 : p0[3]=-20
      if index == 60 and h >= 9 : p0[3]=-17
      if index == 225 and h >= 9 : p0[3]=30
      if index == 231 and h >= 9 : p0[3]=33
      if index == 232 and h >= 9 : p0[3]=50
      if index == 233 and h >= 9 : p0[3]=30
      if index == 234 and h >= 9 : p0[3]=50
      if index == 235 and h >= 9 : p0[3]=45
      if index == 238 and h >= 9 : p0[3]=45
      if index == 239 and h >= 9 : p0[3]=30
      if index == 243 and h >= 9 : p0[3]=0
      if index == 244 and h >= 9 : p0[3]=-10
      if index == 246 and h >= 29 : p0[3]=0

    if year == 2026 and doy == 21:
     if beam == 0 :
      if index == 6 and h >= 9 : p0[3]=-8
      if index == 31 and h >= 9 : p0[3]=0
      if index >= 32 and index <= 33 and h >= 9 : p0[3]=5
      if index >= 34 and index <= 35 and h >= 9 : p0[3]=10
      if index == 40 and h >= 9 : p0[3]=20
      if index == 42 and h >= 9 : p0[3]=25
      if index == 43 and h >= 9 : p0[3]=15
      if index == 44 and h >= 9 : p0[3]=25
      if index == 45 and h >= 9 : p0[3]=15
      if index == 46 and h >= 9 : p0[3]=0
      if index == 48 and h >= 9 : p0[3]=15
      if index == 51 and h >= 9 : p0[3]=0
      if index == 52 and h >= 9 : p0[3]=5
      if index == 61 and h >= 9 : p0[3]=-15
      if index == 62 and h >= 9 : p0[3]=-10
      if index == 68 and h >= 9 : p0[3]=-45
      if index == 229 and h >= 9 : p0[3]=30
      if index == 234 and h >= 9 : p0[3]=40
      if index == 236 and h >= 9 : p0[3]=30
      if index >= 237 and index <= 238 and h >= 9 : p0[3]=25
      if index == 239 and h >= 9 : p0[3]=18
      if index >= 240 and index <= 241 and h >= 9 : p0[3]=15
      if index == 242 and h >= 9 : p0[3]=10
      if index == 243 and h >= 9 : p0[3]=5
      if index >= 246 and index <= 247 and h >= 9 : p0[3]=-5
      if index == 248 and h >= 9 : p0[3]=30
      if index == 250 and h >= 9 : p0[3]=20
      if index == 251 and h >= 9 : p0[3]=10
      if index == 258 and h >= 9 : p0[3]=-20
      if index == 260 and h >= 9 : p0[3]=-20
      if index == 270 and h >= 9 : p0[3]=-35
      if index == 274 and h >= 9 : p0[3]=-30
     if beam == 1 :
      if index == 8 and h >= 9 : p0[3]=0
      if index == 10 and h >= 9 : p0[3]=0
      if index == 29 and h >= 9 : p0[3]=20
      if index == 35 and h >= 9 : p0[3]=15
      if index == 36 and h >= 9 : p0[3]=20
      if index == 39 and h >= 9 : p0[3]=20
      if index == 41 and h >= 9 : p0[3]=20
      if index == 43 and h >= 9 : p0[3]=15
      if index == 44 and h >= 9 : p0[3]=20
      if index == 45 and h >= 9 : p0[3]=15
      if index == 47 and h >= 9 : p0[3]=5
      if index == 48 and h >= 9 : p0[3]=20
      if index == 49 and h >= 9 : p0[3]=5
      if index == 52 and h >= 9 : p0[3]=5
      if index == 54 and h >= 9 : p0[3]=20
      if index == 59 and h >= 9 : p0[3]=-15
      if index == 63 and h >= 9 : p0[3]=-10
      if index == 66 and h >= 9 : p0[3]=-20
      if index == 67 and h >= 9 : p0[3]=-40
      if index == 72 and h >= 9 : p0[3]=-40
      if index == 152 and h >= 9 : p0[3]=5
      if index == 228 and h >= 9 : p0[3]=30
      if index == 230 and h >= 9 : p0[3]=40
      if index == 231 and h >= 9 : p0[3]=38
      if index == 238 and h >= 9 : p0[3]=30
      if index == 244 and h >= 9 : p0[3]=15
      if index == 248 and h >= 9 : p0[3]=35
      if index == 249 and h >= 9 : p0[3]=45
      if index == 250 and h >= 9 : p0[3]=30
      if index == 252 and h >= 9 : p0[3]=15
      if index == 253 and h >= 32 : p0[3]=10
      if index == 254 and h >= 32 : p0[3]=15
      if index == 260 and h >= 9 : p0[3]=-10
      if index == 273 and h >= 9 : p0[3]=-20
      if index == 287 and h >= 9 : p0[3]=-20

    if year == 2026 and doy == 20:
     if beam == 0 :
      if index == 6 and h >= 9 : p0[3]=-8
      if index == 8 and h >= 9 : p0[3]=-5
      if index == 21 and h >= 9 : p0[3]=-40
      if index == 22 and h >= 9 : p0[3]=-40
      if index == 24 and h >= 9 : p0[3]=-40
      if index == 30 and h >= 9 : p0[3]=-15
      if index == 31 and h >= 9 : p0[3]=-25
      if index == 32 and h >= 9 : p0[3]=-42
      if index >= 34 and index <= 35 and h >= 9 : p0[3]=-50
      if index == 37 and h >= 9 : p0[3]=-50
      if index == 38 and h >= 9 : p0[3]=-45
      if index == 39 and h >= 9 : p0[3]=-50
      if index >= 40 and index <= 41 and h >= 9 : p0[3]=-80
      if index == 43 and h >= 9 : p0[3]=-75
      if index == 46 and h >= 9 : p0[3]=-60
      if index == 48 and h >= 9 : p0[3]=-45
      if index == 49 and h >= 9 : p0[3]=-45
      if index == 51 and h >= 9 : p0[3]=-40
      if index == 52 and h >= 9 : p0[3]=-70
      if index == 53 and h >= 9 : p0[3]=-70
      if index == 54 and h >= 9 : p0[3]=-65
      if index == 55 and h >= 9 : p0[3]=-70
      if index >= 56 and index <= 57 and h >= 9 : p0[3]=-50
      if index >= 58 and index <= 59 and h >= 9 : p0[3]=-35
      if index == 60 and h >= 9 : p0[3]=-20
      if index == 61 and h >= 9 : p0[3]=-25
      if index == 62 and h >= 9 : p0[3]=-10
      if index >= 63 and index <= 68 and h >= 9 : p0[3]=-5
      if index == 71 and h >= 9 : p0[3]=-75
      if index == 73 and h >= 9 : p0[3]=-50
      if index == 80 and h >= 9 : p0[3]=-65
      if index == 126 and h >= 9 : p0[3]=48
      if index == 129 and h >= 9 : p0[3]=40
      if index == 160 and h >= 9 : p0[3]=45
      if index == 166 and h >= 9 : p0[3]=45
      if index == 168 and h >= 9 : p0[3]=45
      if index == 169 and h >= 9 : p0[3]=40
      if index == 170 and h >= 9 : p0[3]=45
      if index >= 176 and index <= 177 and h >= 9 : p0[3]=35
      if index == 184 and h >= 9 : p0[3]=35
      if index == 188 and h >= 9 : p0[3]=32
      if index == 217 and h >= 9 : p0[3]=28
      if index == 218 and h >= 9 : p0[3]=25
      if index == 223 and h >= 9 : p0[3]=45
      if index >= 228 and index <= 229 and h >= 9 : p0[3]=20
      if index == 232 and h >= 9 : p0[3]=25
      if index == 233 and h >= 9 : p0[3]=30
      if index == 234 and h >= 9 : p0[3]=30
      if index == 236 and h >= 9 : p0[3]=10
      if index == 238 and h >= 9 : p0[3]=-15
      if index == 239 and h >= 9 : p0[3]=-5
      if index >= 241 and index <= 242 and h >= 9 : p0[3]=-20
      if index == 243 and h >= 9 : p0[3]=-18
      if index >= 244 and index <= 245 and h >= 9 : p0[3]=-25
      if index == 247 and h >= 9 : p0[3]=-30
      if index == 248 and h >= 9 : p0[3]=-35
      if index == 249 and h >= 9 : p0[3]=-30
      if index == 256 and h >= 9 : p0[3]=-30
     if beam == 1 :
      if index == 2 and h >= 9 : p0[3]=0
      if index == 4 and h >= 9 : p0[3]=0
      if index == 6 and h >= 9 : p0[3]=-1
      if index == 7 and h >= 9 : p0[3]=5
      if index == 8 and h >= 9 : p0[3]=5
      if index == 9 and h >= 9 : p0[3]=0
      if index == 11 and h >= 9 : p0[3]=18
      if index == 15 and h >= 9 : p0[3]=0
      if index == 21 and h >= 9 : p0[3]=-30
      if index >= 24 and index <= 25 and h >= 9 : p0[3]=-30
      if index == 30 and h >= 9 : p0[3]=-1
      if index == 34 and h >= 9 : p0[3]=-40
      if index == 36 and h >= 9 : p0[3]=-50
      if index == 37 and h >= 9 : p0[3]=-40
      if index == 38 and h >= 9 : p0[3]=-35
      if index == 39 and h >= 9 : p0[3]=-40
      if index >= 40 and index <= 41 and h >= 9 : p0[3]=-75
      if index == 44 and h >= 9 : p0[3]=-75
      if index == 45 and h >= 9 : p0[3]=-80
      if index == 46 and h >= 9 : p0[3]=-50
      if index == 49 and h >= 9 : p0[3]=-40
      if index == 50 and h >= 9 : p0[3]=-30
      if index == 51 and h >= 9 : p0[3]=-30
      if index == 52 and h >= 9 : p0[3]=-60
      if index == 53 and h >= 9 : p0[3]=-60
      if index == 54 and h >= 9 : p0[3]=-58
      if index == 55 and h >= 9 : p0[3]=-60
      if index >= 56 and index <= 57 and h >= 9 : p0[3]=-40
      if index >= 58 and index <= 59 and h >= 9 : p0[3]=-25
      if index == 60 and h >= 9 : p0[3]=-10
      if index == 61 and h >= 9 : p0[3]=-15
      if index == 62 and h >= 9 : p0[3]=-5
      if index >= 63 and index <= 68 and h >= 9 : p0[3]=0
      if index >= 69 and index <= 70 and h >= 9 : p0[3]=-70
      if index == 71 and h >= 9 : p0[3]=-70
      if index == 73 and h >= 9 : p0[3]=-40
      if index == 74 and h >= 9 : p0[3]=-50
      if index == 75 and h >= 9 : p0[3]=-55
      if index == 76 and h >= 9 : p0[3]=-45
      if index == 77 and h >= 9 : p0[3]=-35
      if index == 129 and h >= 9 : p0[3]=35
      if index == 130 and h >= 9 : p0[3]=30
      if index == 133 and h >= 9 : p0[3]=30
      if index == 148 and h >= 9 : p0[3]=35
      if index == 149 and h >= 9 : p0[3]=40
      if index == 150 and h >= 9 : p0[3]=45
      if index == 152 and h >= 9 : p0[3]=35
      if index == 157 and h >= 9 : p0[3]=37
      if index == 159 and h >= 9 : p0[3]=45
      if index == 160 and h >= 9 : p0[3]=40
      if index == 167 and h >= 9 : p0[3]=40
      if index >= 170 and index <= 171 and h >= 9 : p0[3]=40
      if index == 175 and h >= 9 : p0[3]=30
      if index == 178 and h >= 9 : p0[3]=35
      if index == 180 and h >= 9 : p0[3]=30
      if index == 182 and h >= 9 : p0[3]=30
      if index == 183 and h >= 9 : p0[3]=25
      if index == 185 and h >= 9 : p0[3]=25
      if index == 186 and h >= 9 : p0[3]=22
      if index == 223 and h >= 9 : p0[3]=50
      if index >= 224 and index <= 225 and h >= 9 : p0[3]=25
      if index == 227 and h >= 9 : p0[3]=35
      if index >= 228 and index <= 229 and h >= 9 : p0[3]=25
      if index == 230 and h >= 9 : p0[3]=35
      if index == 231 and h >= 9 : p0[3]=30
      if index == 232 and h >= 9 : p0[3]=35
      if index == 234 and h >= 9 : p0[3]=35
      if index == 235 and h >= 9 : p0[3]=20
      if index == 236 and h >= 9 : p0[3]=15
      if index >= 237 and index <= 238 and h >= 9 : p0[3]=-5
      if index == 239 and h >= 9 : p0[3]=5
      if index >= 240 and index <= 241 and h >= 9 : p0[3]=-10
      if index == 242 and h >= 9 : p0[3]=-15
      if index == 243 and h >= 9 : p0[3]=-10
      if index >= 244 and index <= 245 and h >= 9 : p0[3]=-20
      if index == 246 and h >= 9 : p0[3]=-30
      if index == 247 and h >= 9 : p0[3]=-20
      if index == 249 and h >= 9 : p0[3]=-20
      if index == 250 and h >= 9 : p0[3]=-30
      if index == 251 and h >= 9 : p0[3]=-35
      if index == 257 and h >= 9 : p0[3]=-30
      if index == 259 and h >= 9 : p0[3]=-30

    if year == 2026 and doy == 19:
     if beam == 0 :
      if index == 56 and h >= 9 : p0[3]=-40
      if index == 65 and h >= 9 : p0[3]=-35
      if index == 66 and h >= 9 : p0[3]=-38
      if index == 126 and h >= 9 : p0[3]=20
      if index == 158 and h >= 9 : p0[3]=2
      if index == 183 and h >= 9 : p0[3]=50
      if index == 192 and h >= 9 : p0[3]=65
      if index == 193 and h >= 9 : p0[3]=60
      if index == 194 and h >= 9 : p0[3]=60
      if index == 195 and h >= 9 : p0[3]=60
      if index == 196 and h >= 9 : p0[3]=40
      if index == 200 and h >= 9 : p0[3]=30
      if index == 204 and h >= 9 : p0[3]=20
      if index == 205 and h >= 9 : p0[3]=10
      if index == 260 and h >= 9 : p0[3]=-18
      if index == 281 and h >= 9 : p0[3]=-15
      if index == 283 and h >= 9 : p0[3]=0
      if index == 285 and h >= 9 : p0[3]=20
      if index == 286 and h >= 9 : p0[3]=0
     if beam == 1 :
      if index == 56 and h >= 9 : p0[3]=-30
      if index == 58 and h >= 9 : p0[3]=-23
      if index == 64 and h >= 9 : p0[3]=-35
      if index == 65 and h >= 9 : p0[3]=-30
      if index == 67 and h >= 19 : p0[3]=-30
      if index == 69 and h >= 9 : p0[3]=-20
      if index == 70 and h >= 9 : p0[3]=-14
      if index == 72 and h >= 9 : p0[3]=-10
      if index == 125 and h >= 9 : p0[3]=15
      if index == 127 and h >= 9 : p0[3]=15
      if index == 128 and h >= 9 : p0[3]=15
      if index == 131 and h >= 9 : p0[3]=15
      if index == 153 and h >= 9 : p0[3]=10
      if index == 191 and h >= 9 : p0[3]=45
      if index == 192 and h >= 9 : p0[3]=60
      if index == 195 and h >= 9 : p0[3]=50
      if index == 197 and h >= 9 : p0[3]=25
      if index == 198 and h >= 9 : p0[3]=15
      if index == 201 and h >= 9 : p0[3]=10
      if index == 206 and h >= 9 : p0[3]=5
      if index == 220 and h >= 9 : p0[3]=-10
      if index == 235 and h >= 9 : p0[3]=-35
      if index == 247 and h >= 9 : p0[3]=-15
      if index == 265 and h >= 9 : p0[3]=-20
      if index == 270 and h >= 9 : p0[3]=-15
      if index == 271 and h >= 9 : p0[3]=-10
      if index == 274 and h >= 9 : p0[3]=2
      if index == 275 and h >= 9 : p0[3]=0
      if index == 278 and h >= 9 : p0[3]=10
      if index == 280 and h >= 9 : p0[3]=10
      if index == 281 and h >= 9 : p0[3]=-5
      if index == 282 and h >= 9 : p0[3]=5
      if index == 283 and h >= 9 : p0[3]=10
      if index == 284 and h >= 9 : p0[3]=35
      if index == 285 and h >= 9 : p0[3]=30

    if year == 2026 and doy == 18:
     if beam == 0 :
      if index == 44 and h >= 9 : p0[3]=-15
      if index == 57 and h >= 9 : p0[3]=-20
      if index == 61 and h >= 9 : p0[3]=-30
      if index == 65 and h >= 9 : p0[3]=-25
      if index >= 66 and index <= 67 and h >= 9 : p0[3]=-15
      if index >= 68 and index <= 69 and h >= 9 : p0[3]=-10
      if index >= 70 and index <= 71 and h >= 9 : p0[3]=-15
      if index == 130 and h >= 9 : p0[3]=23
      if index == 146 and h >= 9 : p0[3]=15
      if index == 154 and h >= 35 : p0[3]=numpy.nan
      if index == 157 and h >= 9 : p0[3]=10
      if index == 161 and h >= 9 : p0[3]=4
      if index == 161 and h >= 35 : p0[3]=numpy.nan
      if index == 162 and h >= 25 : p0[3]=5
      if index == 167 and h >= 9 : p0[3]=10
      if index == 229 and h >= 9 : p0[3]=45
      if index == 232 and h >= 9 : p0[3]=30
      if index == 233 and h >= 9 : p0[3]=37
      if index == 234 and h >= 9 : p0[3]=18
      if index == 235 and h >= 9 : p0[3]=40
      if index == 237 and h >= 9 : p0[3]=30
      if index == 238 and h >= 9 : p0[3]=25
      if index == 239 and h >= 9 : p0[3]=35
      if index == 240 and h >= 9 : p0[3]=20
      if index == 241 and h >= 9 : p0[3]=5
      if index == 242 and h >= 9 : p0[3]=-15
      if index == 243 and h >= 9 : p0[3]=0
      if index == 244 and h >= 9 : p0[3]=0
      if index == 245 and h >= 9 : p0[3]=-10
      if index == 247 and h >= 9 : p0[3]=18
      if index == 249 and h >= 9 : p0[3]=20
      if index == 250 and h >= 9 : p0[3]=35
      if index == 251 and h >= 9 : p0[3]=40
      if index == 252 and h >= 9 : p0[3]=5
      if index == 253 and h >= 9 : p0[3]=15
      if index == 269 and h >= 9 : p0[3]=-40
     if beam == 1 :
      if index == 14 and h >= 9 : p0[3]=-14
      if index == 15 and h >= 9 : p0[3]=-18
      if index == 47 and h >= 9 : p0[3]=-10
      if index == 58 and h >= 9 : p0[3]=-15
      if index == 63 and h >= 9 : p0[3]=-25
      if index == 64 and h >= 9 : p0[3]=-23
      if index == 65 and h >= 9 : p0[3]=-20
      if index >= 66 and index <= 67 and h >= 9 : p0[3]=-10
      if index >= 68 and index <= 69 and h >= 9 : p0[3]=-5
      if index == 70 and h >= 9 : p0[3]=-10
      if index >= 71 and index <= 72 and h >= 9 : p0[3]=-8
      if index == 126 and h >= 9 : p0[3]=15
      if index == 129 and h >= 9 : p0[3]=14
      if index >= 130 and index <= 131 and h >= 9 : p0[3]=19
      if index == 139 and h >= 9 : p0[3]=15
      if index == 145 and h >= 9 : p0[3]=10
      if index == 146 and h >= 9 : p0[3]=10
      if index == 161 and h >= 9 : p0[3]=0
      if index == 162 and h >= 9 : p0[3]=1
      if index == 225 and h >= 9 : p0[3]=42
      if index == 229 and h >= 9 : p0[3]=50
      if index >= 230 and index <= 231 and h >= 9 : p0[3]=55
      if index == 232 and h >= 9 : p0[3]=40
      if index == 233 and h >= 9 : p0[3]=45
      if index == 235 and h >= 9 : p0[3]=50
      if index == 237 and h >= 9 : p0[3]=45
      if index == 238 and h >= 9 : p0[3]=35
      if index == 239 and h >= 9 : p0[3]=40
      if index == 240 and h >= 9 : p0[3]=30
      if index == 243 and h >= 9 : p0[3]=5
      if index >= 246 and index <= 249 and h >= 9 : p0[3]=25
      if index == 250 and h >= 9 : p0[3]=40
      if index == 253 and h >= 9 : p0[3]=25
      if index == 255 and h >= 9 : p0[3]=10
      if index == 262 and h >= 9 : p0[3]=-10
      if index == 263 and h >= 9 : p0[3]=-10

    if year == 2026 and doy == 17:
     if beam == 0 :
      if index == 3 and h >= 9 : p0[3]=-10
      if index == 5 and h >= 25 : p0[3]=-20
      if index == 18 and h >= 9 : p0[3]=-3
      if index == 19 and h >= 9 : p0[3]=-15
      if index == 63 and h >= 9 : p0[3]=-10
      if index == 64 and h >= 9 : p0[3]=-3
      if index == 65 and h >= 9 : p0[3]=-5
      if index == 66 and h >= 9 : p0[3]=10
      if index == 67 and h >= 9 : p0[3]=5
      if index == 68 and h >= 9 : p0[3]=10
      if index == 74 and h >= 9 : p0[3]=12
      if index == 124 and h >= 9 : p0[3]=15
      if index == 234 and h >= 9 : p0[3]=22
      if index == 237 and h >= 9 : p0[3]=5
      if index == 244 and h >= 9 : p0[3]=-20
      if index == 246 and h >= 9 : p0[3]=-5
      if index >= 248 and index <= 251 and h >= 9 : p0[3]=0
      if index == 256 and h >= 9 : p0[3]=-5
      if index == 257 and h >= 9 : p0[3]=-15
      if index == 258 and h >= 9 : p0[3]=-10
      if index == 259 and h >= 9 : p0[3]=-7
      if index == 260 and h >= 9 : p0[3]=-10
      if index == 283 and h >= 9 : p0[3]=-16
     if beam == 1 :
      if index >= 2 and index <= 3 and h >= 9 : p0[3]=0
      if index == 18 and h >= 9 : p0[3]=5
      if index == 66 and h >= 9 : p0[3]=15
      if index == 67 and h >= 9 : p0[3]=5
      if index == 68 and h >= 9 : p0[3]=10
      if index == 69 and h >= 9 : p0[3]=30
      if index == 72 and h >= 9 : p0[3]=15
      if index == 73 and h >= 9 : p0[3]=12
      if index == 76 and h >= 9 : p0[3]=18
      if index == 86 and h <= 19 : p0[3]=5
      if index >= 122 and index <= 123 and h >= 9 : p0[3]=10
      if index >= 130 and index <= 131 and h >= 9 : p0[3]=18
      if index == 133 and h >= 9 : p0[3]=12
      if index == 234 and h >= 9 : p0[3]=32
      if index == 237 and h >= 9 : p0[3]=10
      if index == 239 and h >= 9 : p0[3]=5
      if index == 240 and h >= 9 : p0[3]=-2
      if index == 244 and h >= 9 : p0[3]=-15
      if index == 245 and h >= 9 : p0[3]=0
      if index == 247 and h >= 9 : p0[3]=5
      if index == 256 and h >= 9 : p0[3]=10
      if index == 257 and h >= 9 : p0[3]=-5
      if index == 258 and h >= 9 : p0[3]=0
      if index == 260 and h >= 9 : p0[3]=0

    if year == 2026 and doy == 16:
     if beam == 0 :
      if index == 31 and h >= 9 : p0[3]=20
      if index >= 32 and index <= 33 and h >= 9 : p0[3]=15
      if index == 34 and h >= 9 : p0[3]=20
      if index == 35 and h >= 9 : p0[3]=10
      if index == 36 and h >= 9 : p0[3]=25
      if index == 38 and h >= 9 : p0[3]=5
      if index == 39 and h >= 9 : p0[3]=0
      if index == 41 and h >= 9 : p0[3]=0
      if index == 43 and h >= 9 : p0[3]=-15
      if index == 45 and h >= 9 : p0[3]=-25
      if index >= 46 and index <= 47 and h >= 9 : p0[3]=-20
      if index == 48 and h >= 9 : p0[3]=-15
      if index == 49 and h >= 9 : p0[3]=-5
      if index == 50 and h >= 9 : p0[3]=-25
      if index == 53 and h >= 9 : p0[3]=-30
      if index >= 61 and index <= 62 and h >= 9 : p0[3]=-5
      if index >= 63 and index <= 64 and h >= 9 : p0[3]=-15
      if index == 65 and h >= 9 : p0[3]=-11
      if index >= 66 and index <= 67 and h >= 9 : p0[3]=-5
      if index == 69 and h >= 9 : p0[3]=0
      if index == 71 and h >= 9 : p0[3]=0
      if index == 226 and h >= 9 : p0[3]=20
      if index == 238 and h >= 9 : p0[3]=20
      if index == 241 and h >= 9 : p0[3]=10
      if index >= 245 and index <= 246 and h >= 9 : p0[3]=-5
      if index == 247 and h >= 9 : p0[3]=-10
      if index == 248 and h >= 9 : p0[3]=-20
      if index == 250 and h >= 9 : p0[3]=-15
      if index >= 251 and index <= 252 and h >= 9 : p0[3]=0
      if index == 254 and h >= 9 : p0[3]=5
      if index == 255 and h >= 9 : p0[3]=10
      if index == 256 and h >= 9 : p0[3]=0
      if index == 257 and h >= 9 : p0[3]=-1
      if index == 258 and h >= 9 : p0[3]=-20
      if index == 270 and h >= 9 : p0[3]=-20
      if index == 271 and h >= 9 : p0[3]=-10
      if index == 274 and h >= 9 : p0[3]=-5
      if index >= 275 and index <= 276 and h >= 9 : p0[3]=-20
      if index == 285 and h >= 9 : p0[3]=-33
     if beam == 1 :
      if index == 11 and h >= 9 : p0[3]=-10
      if index == 31 and h >= 9 : p0[3]=30
      if index == 37 and h >= 9 : p0[3]=25
      if index == 39 and h >= 9 : p0[3]=10
      if index == 40 and h >= 9 : p0[3]=0
      if index == 41 and h >= 9 : p0[3]=10
      if index == 42 and h >= 9 : p0[3]=0
      if index == 43 and h >= 9 : p0[3]=-10
      if index == 44 and h >= 9 : p0[3]=-5
      if index == 45 and h >= 9 : p0[3]=-20
      if index == 46 and h >= 9 : p0[3]=-15
      if index == 47 and h >= 9 : p0[3]=-10
      if index == 48 and h >= 9 : p0[3]=-5
      if index == 49 and h >= 9 : p0[3]=0
      if index == 50 and h >= 9 : p0[3]=-20
      if index == 51 and h >= 9 : p0[3]=-25
      if index == 56 and h >= 9 : p0[3]=-15
      if index == 57 and h >= 9 : p0[3]=-19
      if index == 58 and h >= 9 : p0[3]=-15
      if index == 59 and h >= 9 : p0[3]=-10
      if index == 60 and h >= 9 : p0[3]=-5
      if index >= 61 and index <= 62 and h >= 9 : p0[3]=0
      if index >= 63 and index <= 65 and h >= 9 : p0[3]=-10
      if index == 66 and h >= 9 : p0[3]=-4
      if index == 68 and h >= 9 : p0[3]=0
      if index == 121 and h >= 9 : p0[3]=40
      if index == 131 and h >= 9 : p0[3]=10
      if index == 130 and h >= 9 : p0[3]=13
      if index == 133 and h >= 9 : p0[3]=2
      if index == 134 and h >= 9 : p0[3]=0
      if index == 228 and h >= 9 : p0[3]=25
      if index == 229 and h >= 9 : p0[3]=30
      if index == 230 and h >= 9 : p0[3]=32
      if index >= 231 and index <= 232 and h >= 9 : p0[3]=30
      if index == 233 and h >= 9 : p0[3]=43
      if index >= 234 and index <= 235 and h >= 9 : p0[3]=32
      if index == 238 and h >= 9 : p0[3]=25
      if index == 239 and h >= 9 : p0[3]=20
      if index == 240 and h >= 9 : p0[3]=15
      if index == 242 and h >= 9 : p0[3]=10
      if index == 246 and h >= 9 : p0[3]=0
      if index == 247 and h >= 9 : p0[3]=-5
      if index >= 249 and index <= 250 and h >= 9 : p0[3]=-5
      if index == 252 and h >= 9 : p0[3]=10
      if index == 255 and h >= 9 : p0[3]=20
      if index == 259 and h >= 9 : p0[3]=-20
      if index == 269 and h >= 9 : p0[3]=15
      if index == 273 and h >= 9 : p0[3]=5      

    if year == 2026 and doy == 15:
     if beam == 0 :
      if index == 33 and h >= 9 : p0[3]=-25
      if index == 36 and h >= 9 : p0[3]=-35
      if index == 54 and h >= 9 : p0[3]=-40
      if index == 55 and h >= 9 : p0[3]=-40
      if index >= 56 and index <= 61 and h >= 9 : p0[3]=-35
      if index >= 62 and index <= 64 and h >= 9 : p0[3]=-40
      if index == 65 and h >= 9 : p0[3]=-30
      if index == 66 and h >= 9 : p0[3]=-25
      if index == 67 and h >= 9 : p0[3]=-27
      if index == 69 and h >= 9 : p0[3]=-30
      if index == 70 and h >= 9 : p0[3]=-20
      if index == 73 and h >= 9 : p0[3]=-22
      if index == 78 and h >= 9 : p0[3]=5
      if index == 237 and h >= 9 : p0[3]=15
      if index == 239 and h >= 9 : p0[3]=15
      if index == 241 and h >= 9 : p0[3]=20
      if index >= 243 and index <= 244 and h >= 9 : p0[3]=10
      if index == 253 and h >= 9 : p0[3]=-10
      if index == 255 and h >= 9 : p0[3]=-20
      if index == 256 and h >= 9 : p0[3]=-25
      if index == 257 and h >= 9 : p0[3]=-30
      if index >= 258 and index <= 260 and h >= 9 : p0[3]=-20
      if index >= 261 and index <= 262 and h >= 9 : p0[3]=-15
      if index == 265 and h >= 9 : p0[3]=-25
      if index == 268 and h >= 9 : p0[3]=-25
      if index == 269 and h >= 9 : p0[3]=-30
     if beam == 1 :
      if index == 5 and h >= 9 : p0[3]=-25
      if index == 23 and h >= 9 : p0[3]=-15
      if index == 33 and h >= 9 : p0[3]=-20
      if index >= 37 and index <= 38 and h >= 9 : p0[3]=-35
      if index == 41 and h >= 9 : p0[3]=-35
      if index == 44 and h >= 9 : p0[3]=-40
      if index == 49 and h >= 9 : p0[3]=-40
      if index == 52 and h >= 9 : p0[3]=-38
      if index == 53 and h >= 9 : p0[3]=-40
      if index == 54 and h >= 9 : p0[3]=-30
      if index == 55 and h >= 9 : p0[3]=-25
      if index >= 56 and index <= 61 and h >= 9 : p0[3]=-30
      if index >= 62 and index <= 64 and h >= 9 : p0[3]=-35
      if index >= 65 and index <= 68 and h >= 9 : p0[3]=-25
      if index == 70 and h >= 9 : p0[3]=-18
      if index == 72 and h >= 9 : p0[3]=-10
      if index == 73 and h >= 9 : p0[3]=-2
      if index == 234 and h >= 9 : p0[3]=34
      if index >= 241 and index <= 242 and h >= 9 : p0[3]=25
      if index == 244 and h >= 9 : p0[3]=30
      if index == 248 and h >= 9 : p0[3]=30
      if index == 250 and h >= 9 : p0[3]=0
      if index >= 251 and index <= 252 and h >= 9 : p0[3]=-5
      if index == 255 and h >= 9 : p0[3]=-5
      if index == 256 and h >= 9 : p0[3]=-10
      if index == 257 and h >= 9 : p0[3]=-15
      if index == 260 and h >= 9 : p0[3]=-10
      if index == 263 and h >= 9 : p0[3]=-10

    if year == 2026 and doy == 14:
     if beam == 0 :
      if index == 52 and h >= 9 : p0[3]=-25
      if index == 53 and h >= 9 : p0[3]=-32
      if index >= 55 and index <= 65 and h >= 9 : p0[3]=-30
      if index == 64 and h >= 9 : p0[3]=-35
      if index == 59 and h >= 9 : p0[3]=-25
      if index >= 66 and index <= 67 and h >= 9 : p0[3]=-25
      if index == 68 and h >= 9 : p0[3]=-15
      if index == 69 and h >= 9 : p0[3]=-10
      if index == 70 and h >= 9 : p0[3]=5
      if index == 229 and h >= 9 : p0[3]=40
      if index == 230 and h >= 9 : p0[3]=50
      if index == 231 and h >= 9 : p0[3]=45
      if index == 232 and h >= 9 : p0[3]=50
      if index == 233 and h >= 9 : p0[3]=50
      if index == 234 and h >= 9 : p0[3]=30
      if index == 239 and h >= 9 : p0[3]=25
      if index == 242 and h >= 29 : p0[3]=15
      if index == 244 and h >= 29 : p0[3]=45
      if index == 248 and h >= 9 : p0[3]=10
      if index >= 255 and index <= 256 and h >= 9 : p0[3]=-5
      if index == 266 and h >= 9 : p0[3]=20
     if beam == 1 :
      if index == 50 and h >= 9 : p0[3]=-23
      if index == 51 and h >= 9 : p0[3]=-25
      if index == 52 and h >= 9 : p0[3]=-20
      if index == 56 and h >= 9 : p0[3]=-30
      if index >= 57 and index <= 65 and h >= 9 : p0[3]=-25
      if index == 59 and h >= 9 : p0[3]=-20
      if index == 62 and h >= 9 : p0[3]=-20
      if index >= 66 and index <= 67 and h >= 9 : p0[3]=-20
      if index == 68 and h >= 9 : p0[3]=-10
      if index == 69 and h >= 9 : p0[3]=-5
      if index == 75 and h >= 9 : p0[3]=18
      if index == 76 and h >= 9 : p0[3]=15
      if index == 229 and h >= 9 : p0[3]=45
      if index == 231 and h >= 9 : p0[3]=53
      if index == 232 and h >= 9 : p0[3]=55
      if index == 233 and h >= 9 : p0[3]=55
      if index >= 234 and index <= 235 and h >= 9 : p0[3]=43
      if index >= 236 and index <= 237 and h >= 9 : p0[3]=20
      if index == 238 and h >= 9 : p0[3]=40
      if index >= 240 and index <= 241 and h >= 29 : p0[3]=50
      if index == 244 and h >= 29 : p0[3]=50
      if index == 261 and h >= 9 : p0[3]=0
      if index == 265 and h >= 9 : p0[3]=25
      if index == 267 and h >= 9 : p0[3]=5
      if index == 273 and h >= 9 : p0[3]=-15

    if year == 2026 and doy == 13:
     if beam == 0 :
      if index == 18 and h >= 9 : p0[3]=-22
      if index >= 55 and index <= 55 and h >= 9 : p0[3]=-20
      if index == 56 and h >= 9 : p0[3]=-22
      if index == 57 and h >= 9 : p0[3]=-15
      if index == 58 and h >= 9 : p0[3]=-2
      if index == 60 and h >= 9 : p0[3]=4
      if index == 61 and h >= 9 : p0[3]=4
      if index == 64 and h >= 9 : p0[3]=-2
      if index == 65 and h >= 9 : p0[3]=-5
      if index == 66 and h >= 9 : p0[3]=5
      if index >= 68 and index <= 70 and h >= 9 : p0[3]=5
      if index == 72 and h >= 9 : p0[3]=10
      if index == 73 and h >= 9 : p0[3]=10
      if index == 76 and h >= 9 : p0[3]=5
      if index == 233 and h >= 9 : p0[3]=35
      if index == 239 and h >= 9 : p0[3]=25
      if index == 241 and h >= 9 : p0[3]=10
      if index == 244 and h >= 9 : p0[3]=0
      if index == 245 and h >= 9 : p0[3]=-5
      if index == 248 and h >= 9 : p0[3]=-15
      if index >= 250 and index <= 251 and h >= 9 : p0[3]=-5
      if index == 252 and h >= 9 : p0[3]=10
      if index == 256 and h >= 9 : p0[3]=10
      if index == 267 and h >= 9 : p0[3]=0
      if index == 271 and h >= 9 : p0[3]=-20
      if index == 272 and h >= 9 : p0[3]=-28
      if index == 275 and h >= 29 : p0[3]=-40
      if index >= 276 and index <= 277 and h >= 29 : p0[3]=-40
      if index >= 281 and index <= 284 and h >= 29 : p0[3]=-45
      if index == 282 and h >= 29 : p0[3]=-42
      if index == 285 and h >= 19 : p0[3]=-45
      if index == 286 and h >= 19 : p0[3]=-45
     if beam == 1 :
      if index == 45 and h >= 9 : p0[3]=-28
      if index == 54 and h >= 9 : p0[3]=-25
      if index >= 55 and index <= 56 and h >= 9 : p0[3]=-15
      if index == 57 and h >= 9 : p0[3]=-10
      if index == 59 and h >= 9 : p0[3]=0
      if index == 61 and h >= 9 : p0[3]=5
      if index == 62 and h >= 9 : p0[3]=3
      if index == 64 and h >= 9 : p0[3]=1
      if index == 65 and h >= 9 : p0[3]=0
      if index == 66 and h >= 9 : p0[3]=3
      if index >= 67 and index <= 70 and h >= 9 : p0[3]=0
      if index == 69 and h >= 9 : p0[3]=-3
      if index == 71 and h >= 9 : p0[3]=3
      if index == 233 and h >= 9 : p0[3]=40
      if index == 236 and h <= 29 : p0[3]=42
      if index == 239 and h >= 9 : p0[3]=32
      if index == 240 and h >= 9 : p0[3]=20
      if index == 241 and h >= 9 : p0[3]=20
      if index == 244 and h >= 9 : p0[3]=10
      if index == 247 and h >= 9 : p0[3]=5
      if index == 250 and h >= 9 : p0[3]=0
      if index == 273 and h >= 9 : p0[3]=-20
      if index == 274 and h >= 9 : p0[3]=-30
      if index == 283 and h >= 29 : p0[3]=-35

    if year == 2026 and doy == 12:
     if beam == 0 :
      if index == 4 and h >= 9 : p0[3]=-15
      if index == 32 and h >= 9 : p0[3]=18
      if index == 36 and h >= 9 : p0[3]=0
      if index == 39 and h >= 9 : p0[3]=0
      if index == 40 and h >= 9 : p0[3]=20
      if index == 41 and h >= 9 : p0[3]=15
      if index == 42 and h >= 9 : p0[3]=5
      if index == 43 and h >= 9 : p0[3]=-5
      if index >= 44 and index <= 47 and h >= 9 : p0[3]=0
      if index == 66 and h <= 28 : p0[3]=-5
      if index == 72 and h >= 9 : p0[3]=5
      if index == 73 and h <= 27 : p0[3]=10
      if index == 245 and h >= 9 : p0[3]=15
      if index == 250 and h >= 9 : p0[3]=15
      if index == 257 and h >= 9 : p0[3]=-10
      if index == 258 and h >= 9 : p0[3]=-15
      if index == 266 and h >= 9 : p0[3]=-10
      if index == 268 and h >= 9 : p0[3]=-20
      if index == 269 and h >= 9 : p0[3]=-25
     if beam == 1 :
      if index == 31 and h >= 9 : p0[3]=40
      if index == 33 and h >= 9 : p0[3]=35
      if index == 37 and h >= 9 : p0[3]=25
      if index == 41 and h >= 9 : p0[3]=20
      if index == 49 and h >= 9 : p0[3]=5
      if index == 50 and h >= 9 : p0[3]=0
      if index == 77 and h >= 9 : p0[3]=0
      if index == 78 and h >= 9 : p0[3]=5
      if index == 133 and h >= 9 : p0[3]=5
      if index == 138 and h >= 9 : p0[3]=10
      if index == 208 and h >= 9 : p0[3]=15
      if index == 236 and h >= 9 : p0[3]=35
      if index == 237 and h >= 9 : p0[3]=30
      if index == 238 and h >= 9 : p0[3]=35
      if index >= 246 and index <= 248 and h >= 9 : p0[3]=20
      if index == 255 and h >= 29 : p0[3]=15
      if index == 256 and h >= 9 : p0[3]=5
      if index == 257 and h >= 9 : p0[3]=-5
      if index == 270 and h >= 9 : p0[3]=-15
      if index == 279 and h >= 29 : p0[3]=-13

    if year == 2026 and doy == 11:
     if beam == 0 :
      if index == 5 and h >= 9 : p0[3]=-35
      if index == 6 and h >= 9 : p0[3]=-30
      if index >= 7 and index <= 12 and h >= 9 : p0[3]=-25
      if index == 13 and h >= 9 : p0[3]=-20
      if index >= 14 and index <= 20 and h >= 9 : p0[3]=-25
      if index == 17 and h >= 9 : p0[3]=-22
      if index == 21 and h >= 9 : p0[3]=-20
      if index == 22 and h >= 9 : p0[3]=-20
      if index >= 23 and index <= 24 and h >= 9 : p0[3]=-10
      if index == 25 and h >= 9 : p0[3]=-5
      if index == 26 and h >= 9 : p0[3]=0
      if index == 28 and h >= 9 : p0[3]=15
      if index == 29 and h >= 9 : p0[3]=5
      if index == 30 and h >= 9 : p0[3]=10
      if index >= 31 and index <= 32 and h >= 9 : p0[3]=12
      if index == 34 and h >= 9 : p0[3]=0
      if index == 36 and h >= 9 : p0[3]=-5
      if index == 37 and h >= 9 : p0[3]=10
      if index == 38 and h >= 21 : p0[3]=5
      if index == 39 and h >= 26 : p0[3]=30
      if index >= 40 and index <= 44 and h >= 26 : p0[3]=15
      if index == 45 and h >= 9 : p0[3]=10
      if index == 50 and h >= 9 : p0[3]=-5
      if index == 51 and h >= 9 : p0[3]=0
      if index == 52 and h >= 9 : p0[3]=-1
      if index == 53 and h >= 9 : p0[3]=0
      if index == 54 and h >= 9 : p0[3]=5
      if index == 57 and h >= 9 : p0[3]=2
      if index == 58 and h >= 9 : p0[3]=5
      if index == 59 and h >= 9 : p0[3]=3
      if index == 60 and h >= 9 : p0[3]=5
      if index == 69 and h >= 9 : p0[3]=-5
      if index == 70 and h >= 9 : p0[3]=5
      if index == 71 and h >= 9 : p0[3]=-2
      if index == 72 and h >= 9 : p0[3]=5
      if index == 73 and h >= 9 : p0[3]=0
      if index == 75 and h >= 9 : p0[3]=0
      if index == 76 and h >= 9 : p0[3]=5
      if index >= 80 and index <= 81 and h >= 9 : p0[3]=-5
      if index == 132 and h >= 9 : p0[3]=5
      if index == 137 and h >= 9 : p0[3]=15
      if index == 149 and h >= 35 : p0[3]=numpy.nan
      if index == 163 and h >= 9 : p0[3]=13
      if index == 165 and h >= 29 : p0[3]=15
     if beam == 1 :
      if index == 1 and h >= 9 : p0[3]=-30
      if index == 5 and h >= 9 : p0[3]=-30
      if index >= 7 and index <= 12 and h >= 9 : p0[3]=-20
      if index == 16 and h >= 9 : p0[3]=-20
      if index >= 18 and index <= 20 and h >= 9 : p0[3]=-20
      if index == 19 and h >= 9 : p0[3]=-15
      if index == 21 and h >= 9 : p0[3]=-15
      if index == 22 and h >= 9 : p0[3]=-10
      if index == 28 and h >= 9 : p0[3]=15
      if index == 31 and h >= 9 : p0[3]=20
      if index == 35 and h >= 9 : p0[3]=20
      if index == 37 and h >= 9 : p0[3]=30
      if index == 38 and h >= 21 : p0[3]=10
      if index == 40 and h >= 19 : p0[3]=40
      if index == 56 and h >= 9 : p0[3]=5
      if index == 69 and h >= 9 : p0[3]=-10
      if index == 70 and h >= 9 : p0[3]=1
      if index == 71 and h >= 9 : p0[3]=-5
      if index == 72 and h >= 9 : p0[3]=0
      if index >= 130 and index <= 131 and h >= 9 : p0[3]=0
      if index == 133 and h >= 9 : p0[3]=0
      if index == 157 and h >= 9 : p0[3]=13
      if index == 163 and h >= 22 : p0[3]=8
      if index == 164 and h >= 9 : p0[3]=8
      if index == 168 and h >= 9 : p0[3]=11
      if index == 171 and h >= 19 : p0[3]=18

    if year == 2026 and doy == 10:
     if beam == 0 :
      if index == 14 and h >= 9 : p0[3]=-10
      if index == 18 and h >= 9 : p0[3]=-5
      if index == 24 and h >= 9 : p0[3]=-30
      if index == 30 and h >= 9 : p0[3]=-15
      if index == 31 and h >= 9 : p0[3]=-10
      if index == 34 and h >= 9 : p0[3]=-8
      if index == 38 and h >= 9 : p0[3]=-16
      if index == 39 and h >= 9 : p0[3]=-15
      if index == 50 and h >= 9 : p0[3]=-30
      if index == 52 and h >= 9 : p0[3]=-25
      if index == 53 and h >= 9 : p0[3]=-25
      if index == 54 and h >= 9 : p0[3]=-35
      if index == 66 and h >= 9 : p0[3]=-40
      if index == 70 and h >= 9 : p0[3]=-28
      if index == 85 and h >= 19 : p0[3]=-5
      if index == 168 and h >= 9 : p0[3]=23
     if beam == 1 :
      if index == 1 and h >= 9 : p0[3]=-20
      if index == 3 and h >= 9 : p0[3]=-20
      if index == 5 and h >= 9 : p0[3]=-25
      if index == 12 and h >= 9 : p0[3]=-22
      if index == 18 and h >= 9 : p0[3]=0
      if index == 25 and h >= 9 : p0[3]=-30
      if index == 51 and h >= 9 : p0[3]=-20
      if index == 53 and h >= 9 : p0[3]=-25
      if index == 54 and h >= 9 : p0[3]=-30
      if index == 55 and h >= 9 : p0[3]=-25
      if index >= 56 and index <= 58 and h >= 9 : p0[3]=-25
      if index == 59 and h >= 9 : p0[3]=-35
      if index == 62 and h >= 9 : p0[3]=-35
      if index == 63 and h >= 9 : p0[3]=-43
      if index == 69 and h >= 9 : p0[3]=-35
      if index == 70 and h >= 9 : p0[3]=-30
      if index == 71 and h >= 9 : p0[3]=-28
      if index == 72 and h >= 9 : p0[3]=-30
      if index == 73 and h >= 9 : p0[3]=-32
      if index == 74 and h >= 9 : p0[3]=-28
      if index == 132 and h >= 9 : p0[3]=7
      if index == 133 and h >= 9 : p0[3]=9
      if index == 134 and h >= 9 : p0[3]=8
      if index == 135 and h >= 9 : p0[3]=10
      if index == 138 and h >= 9 : p0[3]=15
      if index >= 174 and index <= 178 and h >= 9 : p0[3]=20
      if index == 208 and h >= 9 : p0[3]=20
      if index == 216 and h >= 9 : p0[3]=5

    if year == 2026 and doy == 9:
     if beam == 0 :
      if index >= 10 and index <= 12 and h >= 9 : p0[3]=-15
      if index == 14 and h >= 9 : p0[3]=-20
      if index == 23 and h >= 9 : p0[3]=-10
      if index == 29 and h >= 9 : p0[3]=-25
      if index == 32 and h >= 9 : p0[3]=-10
      if index >= 34 and index <= 35 and h >= 9 : p0[3]=-5
      if index >= 36 and index <= 37 and h >= 29 : p0[3]=-20
      if index == 38 and h >= 29 : p0[3]=-15
      if index == 39 and h >= 29 : p0[3]=-20
      if index == 62 and h >= 9 : p0[3]=-35
      if index == 137 and h >= 9 : p0[3]=22
      if index == 239 and h >= 9 : p0[3]=25
      if index == 240 and h >= 9 : p0[3]=17
      if index == 241 and h >= 9 : p0[3]=10
      if index == 243 and h >= 9 : p0[3]=0
      if index == 246 and h >= 9 : p0[3]=-20
      if index >= 247 and index <= 248 and h >= 9 : p0[3]=-15
      if index == 252 and h >= 9 : p0[3]=0
      if index == 259 and h >= 9 : p0[3]=-10
      if index == 260 and h >= 9 : p0[3]=-20
      if index >= 268 and index <= 269 and h >= 9 : p0[3]=-20
      if index == 273 and h >= 9 : p0[3]=-30
      if index == 275 and h >= 9 : p0[3]=-30
      if index == 285 and h >= 9 : p0[3]=-25
     if beam == 1 :
      if index >= 12 and index <= 13 and h >= 9 : p0[3]=-10
      if index == 16 and h >= 9 : p0[3]=-10
      if index == 20 and h >= 9 : p0[3]=-10
      if index == 24 and h >= 9 : p0[3]=-5
      if index == 33 and h >= 9 : p0[3]=5
      if index == 67 and h >= 9 : p0[3]=-22
      if index >= 132 and index <= 134 and h >= 9 : p0[3]=10
      if index == 135 and h >= 9 : p0[3]=15
      if index == 231 and h >= 9 : p0[3]=45
      if index >= 236 and index <= 238 and h >= 9 : p0[3]=35
      if index == 241 and h >= 9 : p0[3]=15
      if index == 242 and h >= 9 : p0[3]=18
      if index == 244 and h >= 9 : p0[3]=10
      if index == 245 and h >= 9 : p0[3]=5
      if index >= 246 and index <= 247 and h >= 9 : p0[3]=-10
      if index == 249 and h >= 9 : p0[3]=0
      if index == 252 and h >= 9 : p0[3]=5
      if index == 260 and h >= 9 : p0[3]=-10
      if index == 264 and h >= 9 : p0[3]=-15
      if index == 268 and h >= 9 : p0[3]=-15
      if index == 271 and h >= 9 : p0[3]=-15
      
    if year == 2026 and doy == 8:
     if beam == 0 :
      if index == 14 and h >= 9 : p0[3]=2
      if index == 15 and h >= 9 : p0[3]=12
      if index == 35 and h >= 9 : p0[3]=-2
      if index == 48 and h >= 9 : p0[3]=15
      if index == 49 and h >= 9 : p0[3]=10
      if index == 50 and h >= 9 : p0[3]=5
      if index == 55 and h >= 9 : p0[3]=-30
      if index == 56 and h >= 9 : p0[3]=-25
      if index == 57 and h >= 21 : p0[3]=-25
      if index >= 58 and index <= 61 and h >= 9 : p0[3]=-25
      if index == 60 and h >= 9 : p0[3]=-30
      if index == 62 and h >= 9 : p0[3]=-20
      if index == 63 and h >= 9 : p0[3]=-30
      if index >= 64 and index <= 65 and h >= 9 : p0[3]=-35
      if index >= 66 and index <= 67 and h >= 9 : p0[3]=-30
      if index >= 68 and index <= 69 and h >= 9 : p0[3]=-20
      if index == 70 and h >= 9 : p0[3]=-15
      if index == 155 and h >= 35 : p0[3]=numpy.nan
      if index == 157 and h >= 9 : p0[3]=20
      if index >= 159 and index <= 160 and h >= 9 : p0[3]=20
      if index == 160 and h >= 35 : p0[3]=numpy.nan
      if index == 161 and h >= 9 : p0[3]=17
      if index == 161 and h >= 35 : p0[3]=numpy.nan
      if index == 168 and h >= 9 : p0[3]=15
      if index == 170 and h >= 19 : p0[3]=15
      if index == 178 and h >= 9 : p0[3]=18
      if index == 239 and h >= 9 : p0[3]=-10
      if index == 241 and h >= 9 : p0[3]=-15
      if index == 242 and h >= 9 : p0[3]=-5
      if index == 243 and h >= 9 : p0[3]=0
      if index == 247 and h >= 9 : p0[3]=10
      if index == 249 and h >= 9 : p0[3]=10
      if index == 250 and h >= 9 : p0[3]=0
      if index == 251 and h >= 9 : p0[3]=-15
      if index == 252 and h >= 9 : p0[3]=-10
      if index == 256 and h >= 9 : p0[3]=10
      if index == 257 and h >= 9 : p0[3]=15
      if index == 258 and h >= 9 : p0[3]=0
      if index == 259 and h >= 9 : p0[3]=10
      if index == 263 and h >= 9 : p0[3]=10
      if index == 264 and h >= 9 : p0[3]=5
      if index == 265 and h >= 9 : p0[3]=0
      if index == 266 and h >= 9 : p0[3]=5
      if index == 268 and h >= 9 : p0[3]=20
      if index == 269 and h >= 9 : p0[3]=18
      if index == 273 and h >= 29 : p0[3]=30
      if index == 274 and h >= 9 : p0[3]=35
      if index == 277 and h >= 29 : p0[3]=50
      if index == 278 and h >= 29 : p0[3]=40
      if index == 279 and h >= 29 : p0[3]=25
     if beam == 1 :
      if index == 51 and h >= 9 : p0[3]=10
      if index == 53 and h >= 9 : p0[3]=0
      if index == 54 and h >= 9 : p0[3]=-25
      if index == 56 and h >= 9 : p0[3]=-20
      if index == 57 and h >= 21 : p0[3]=-20
      if index == 59 and h >= 9 : p0[3]=-20
      if index == 60 and h >= 9 : p0[3]=-20
      if index == 61 and h >= 9 : p0[3]=-25
      if index == 62 and h >= 9 : p0[3]=-10
      if index == 65 and h >= 9 : p0[3]=-30
      if index == 66 and h >= 9 : p0[3]=-25
      if index >= 68 and index <= 69 and h >= 9 : p0[3]=-20
      if index == 136 and h >= 9 : p0[3]=15
      if index >= 138 and index <= 139 and h >= 9 : p0[3]=15
      if index == 147 and h >= 9 : p0[3]=18
      if index == 148 and h >= 9 : p0[3]=19
      if index == 150 and h >= 9 : p0[3]=15
      if index == 151 and h >= 9 : p0[3]=17
      if index >= 157 and index <= 158 and h >= 9 : p0[3]=15
      if index == 160 and h >= 9 : p0[3]=15
      if index == 161 and h >= 9 : p0[3]=12
      if index == 169 and h >= 9 : p0[3]=12
      if index == 171 and h >= 9 : p0[3]=10
      if index == 224 and h >= 9 : p0[3]=30
      if index == 237 and h >= 9 : p0[3]=15
      if index >= 239 and index <= 240 and h >= 9 : p0[3]=-5
      if index == 244 and h >= 9 : p0[3]=10
      if index == 245 and h >= 9 : p0[3]=35
      if index == 246 and h >= 9 : p0[3]=28
      if index == 248 and h >= 9 : p0[3]=40
      if index == 249 and h >= 9 : p0[3]=15
      if index == 250 and h >= 9 : p0[3]=5
      if index >= 267 and index <= 268 and h >= 9 : p0[3]=25
      if index == 275 and h >= 29 : p0[3]=-20
      if index == 276 and h >= 9 : p0[3]=-5
      if index == 287 and h >= 9 : p0[3]=0

    if year == 2026 and doy == 7:
     if beam == 0 :
      if index == 30 and h >= 9 : p0[3]=-28
      if index == 55 and h >= 9 : p0[3]=-50
      if index == 56 and h >= 9 : p0[3]=-45
      if index >= 58 and index <= 65 and h >= 9 : p0[3]=-45
      if index == 63 and h >= 9 : p0[3]=-30
      if index == 66 and h >= 9 : p0[3]=-40
      if index == 68 and h >= 9 : p0[3]=-32
      if index == 76 and h >= 19 : p0[3]=-8
      if index == 241 and h >= 9 : p0[3]=30
      if index == 242 and h >= 9 : p0[3]=23
      if index >= 243 and index <= 244 and h >= 9 : p0[3]=20
      if index == 245 and h >= 9 : p0[3]=10
      if index == 246 and h >= 9 : p0[3]=5
      if index >= 250 and index <= 253 and h >= 9 : p0[3]=0
      if index >= 254 and index <= 256 and h >= 9 : p0[3]=-5
      if index == 257 and h >= 9 : p0[3]=10
      if index == 260 and h >= 9 : p0[3]=10
      if index == 261 and h >= 9 : p0[3]=-1
      if index == 265 and h >= 9 : p0[3]=-20
      if index == 281 and h >= 9 : p0[3]=-12
      if index == 282 and h >= 9 : p0[3]=-20
      if index == 286 and h >= 9 : p0[3]=-15
     if beam == 1 :
      if index == 36 and h >= 9 : p0[3]=-25
      if index == 44 and h >= 9 : p0[3]=-36
      if index == 55 and h >= 9 : p0[3]=-45
      if index >= 56 and index <= 66 and h >= 9 : p0[3]=-40
      if index == 63 and h >= 9 : p0[3]=-30
      if index == 234 and h >= 9 : p0[3]=35
      if index == 238 and h >= 9 : p0[3]=35
      if index == 239 and h >= 9 : p0[3]=31
      if index == 241 and h >= 9 : p0[3]=35
      if index == 242 and h >= 9 : p0[3]=30
      if index >= 243 and index <= 244 and h >= 9 : p0[3]=25
      if index == 246 and h >= 9 : p0[3]=10
      if index == 247 and h >= 9 : p0[3]=15
      if index >= 248 and index <= 250 and h >= 9 : p0[3]=5
      if index == 256 and h >= 9 : p0[3]=0
      if index == 258 and h >= 9 : p0[3]=30
      if index == 262 and h >= 9 : p0[3]=0
      if index == 263 and h >= 9 : p0[3]=-15
      if index == 283 and h >= 9 : p0[3]=-2
      if index == 284 and h >= 9 : p0[3]=-10
      if index == 285 and h >= 9 : p0[3]=-2
      if index == 287 and h >= 9 : p0[3]=0

    if year == 2026 and doy == 6:
     if beam == 0 :
      if index == 40 and h >= 9 : p0[3]=-40
      if index == 42 and h >= 9 : p0[3]=-40
      if index == 55 and h >= 9 : p0[3]=-60
      if index == 56 and h >= 9 : p0[3]=-62
      if index == 58 and h >= 9 : p0[3]=-60
      if index == 59 and h >= 9 : p0[3]=-55
      if index >= 63 and index <= 66 and h >= 9 : p0[3]=-50
      if index == 68 and h >= 9 : p0[3]=-45
      if index == 65 and h >= 9 : p0[3]=-50
      if index >= 236 and index <= 238 and h >= 9 : p0[3]=30
      if index == 239 and h >= 9 : p0[3]=15
      if index == 240 and h >= 9 : p0[3]=12
      if index == 243 and h >= 9 : p0[3]=20
      if index == 252 and h >= 9 : p0[3]=-10
      if index == 256 and h >= 9 : p0[3]=-15
      if index == 262 and h >= 9 : p0[3]=-20
      if index == 265 and h >= 9 : p0[3]=-3
      if index == 273 and h >= 39 : p0[3]=-10
      if index == 274 and h >= 29 : p0[3]=-15
      if index == 275 and h >= 29 : p0[3]=-5
      if index == 277 and h >= 29 : p0[3]=-25
      if index == 278 and h >= 29 : p0[3]=-20
      if index == 279 and h >= 29 : p0[3]=-30
      if index == 281 and h >= 29 : p0[3]=-40
      if index == 282 and h >= 29 : p0[3]=-45
      if index == 284 and h >= 29 : p0[3]=-35
      if index == 285 and h >= 29 : p0[3]=-35
     if beam == 1 :
      if index == 42 and h >= 9 : p0[3]=-30
      if index == 62 and h >= 9 : p0[3]=-38
      if index == 63 and h >= 9 : p0[3]=-40
      if index == 64 and h >= 9 : p0[3]=-45
      if index == 67 and h >= 9 : p0[3]=-45
      if index == 68 and h >= 9 : p0[3]=-40
      if index >= 236 and index <= 237 and h >= 9 : p0[3]=40
      if index == 238 and h >= 9 : p0[3]=35
      if index == 240 and h >= 9 : p0[3]=18
      if index == 241 and h >= 9 : p0[3]=15
      if index == 242 and h >= 9 : p0[3]=40
      if index == 243 and h >= 9 : p0[3]=30
      if index == 245 and h >= 9 : p0[3]=30
      if index == 246 and h >= 9 : p0[3]=20
      if index == 251 and h >= 9 : p0[3]=5
      if index == 252 and h >= 9 : p0[3]=0
      if index == 253 and h >= 9 : p0[3]=-10
      if index == 254 and h >= 9 : p0[3]=10
      if index == 255 and h >= 9 : p0[3]=-10
      if index == 257 and h >= 9 : p0[3]=0
      if index == 260 and h >= 9 : p0[3]=0
      if index == 262 and h >= 9 : p0[3]=-10
      if index >= 264 and index <= 266 and h >= 9 : p0[3]=0
      if index == 265 and h >= 9 : p0[3]=-1
      if index == 268 and h >= 9 : p0[3]=-10
      if index == 276 and h >= 29 : p0[3]=-5
      if index == 284 and h >= 29 : p0[3]=-20

    if year == 2026 and doy == 5:
     if beam == 0 :
      if index == 6 and h >= 9 : p0[3]=-40
      if index == 7 and h >= 9 : p0[3]=-45
      if index == 57 and h >= 9 : p0[3]=-25
      if index == 254 and h >= 9 : p0[3]=10
      if index == 259 and h >= 9 : p0[3]=-5
      if index == 261 and h >= 29 : p0[3]=20
      if index == 275 and h >= 9 : p0[3]=-25
      if index == 276 and h >= 9 : p0[3]=-20
      if index == 278 and h >= 9 : p0[3]=-20
     if beam == 1 :
      if index == 55 and h >= 9 : p0[3]=-10
      if index == 247 and h >= 9 : p0[3]=5
      if index == 249 and h >= 9 : p0[3]=10
      if index == 254 and h >= 9 : p0[3]=10
      if index == 270 and h >= 29 : p0[3]=0

    if year == 2026 and doy == 4:
     if beam == 0 :
      if index == 1 and h >= 9 : p0[3]=-10
      if index == 4 and h >= 9 : p0[3]=-10
      if index == 17 and h >= 9 : p0[3]=-23
      if index == 30 and h >= 9 : p0[3]=-32
      if index == 70 and h >= 9 : p0[3]=0
      if index == 71 and h >= 9 : p0[3]=2
      if index == 153 and h >= 9 : p0[3]=6
      if index == 236 and h >= 9 : p0[3]=50
      if index == 238 and h >= 9 : p0[3]=30
      if index == 239 and h >= 9 : p0[3]=25
      if index == 240 and h >= 9 : p0[3]=0
      if index == 245 and h >= 9 : p0[3]=-20
      if index >= 249 and index <= 251 and h >= 9 : p0[3]=-25
      if index == 252 and h >= 9 : p0[3]=-15
      if index == 259 and h >= 9 : p0[3]=10
      if index == 260 and h >= 9 : p0[3]=15
      if index == 261 and h >= 9 : p0[3]=10
      if index == 262 and h >= 9 : p0[3]=10
      if index >= 263 and index <= 264 and h >= 9 : p0[3]=0
      if index >= 267 and index <= 268 and h >= 9 : p0[3]=-10
      if index >= 269 and index <= 270 and h >= 9 : p0[3]=-25
      if index >= 271 and index <= 273 and h >= 29 : p0[3]=-10
      if index == 282 and h >= 9 : p0[3]=-35
     if beam == 1 :
      if index == 18 and h >= 9 : p0[3]=-15
      if index == 62 and h >= 9 : p0[3]=-35
      if index == 66 and h >= 19 : p0[3]=-22
      if index == 67 and h >= 9 : p0[3]=-10
      if index == 68 and h >= 9 : p0[3]=-5
      if index == 134 and h >= 9 : p0[3]=5
      if index == 137 and h >= 9 : p0[3]=10
      if index == 140 and h >= 9 : p0[3]=5
      if index == 150 and h >= 9 : p0[3]=0
      if index == 233 and h >= 9 : p0[3]=50
      if index == 234 and h >= 9 : p0[3]=58
      if index == 235 and h >= 9 : p0[3]=63
      if index == 236 and h >= 9 : p0[3]=55
      if index == 237 and h >= 9 : p0[3]=60
      if index == 239 and h >= 9 : p0[3]=30
      if index == 240 and h >= 9 : p0[3]=10
      if index == 241 and h >= 9 : p0[3]=0
      if index >= 242 and index <= 244 and h >= 9 : p0[3]=-10
      if index == 246 and h >= 9 : p0[3]=-15
      if index == 248 and h >= 9 : p0[3]=-20
      if index >= 249 and index <= 251 and h >= 9 : p0[3]=-20
      if index == 252 and h >= 9 : p0[3]=-10
      if index == 253 and h >= 9 : p0[3]=15
      if index == 254 and h >= 9 : p0[3]=10
      if index >= 255 and index <= 256 and h >= 9 : p0[3]=25
      if index == 257 and h >= 9 : p0[3]=15
      if index == 258 and h >= 9 : p0[3]=10
      if index == 262 and h >= 9 : p0[3]=20
      if index >= 263 and index <= 265 and h >= 9 : p0[3]=10
      if index == 267 and h >= 9 : p0[3]=0
      if index == 270 and h >= 9 : p0[3]=-15

    if year == 2026 and doy == 3:
     if beam == 0 :
      if index == 1 and h >= 9 : p0[3]=-35
      if index == 2 and h >= 9 : p0[3]=-30
      if index == 11 and h >= 9 : p0[3]=-20
      if index == 68 and h >= 9 : p0[3]=-5
      if index == 150 and h >= 35 : p0[3]=numpy.nan
      if index == 234 and h >= 9 : p0[3]=18
      if index == 237 and h >= 9 : p0[3]=22
      if index >= 238 and index <= 240 and h >= 9 : p0[3]=20
      if index >= 241 and index <= 242 and h >= 9 : p0[3]=15
      if index == 243 and h >= 9 : p0[3]=20
      if index == 244 and h >= 9 : p0[3]=10
      if index == 245 and h >= 9 : p0[3]=0
      if index >= 246 and index <= 247 and h >= 9 : p0[3]=5
      if index == 250 and h >= 9 : p0[3]=-15
      if index == 251 and h >= 9 : p0[3]=-10
      if index == 252 and h >= 9 : p0[3]=-10
      if index == 253 and h >= 9 : p0[3]=-15
      if index == 254 and h >= 9 : p0[3]=-5
      if index >= 257 and index <= 258 and h >= 9 : p0[3]=0
      if index >= 259 and index <= 260 and h >= 9 : p0[3]=-5
      if index == 261 and h >= 9 : p0[3]=0
      if index >= 262 and index <= 263 and h >= 9 : p0[3]=-10
      if index == 268 and h >= 9 : p0[3]=-10
      if index == 272 and h >= 9 : p0[3]=-12
      if index == 275 and h >= 9 : p0[3]=-15
      if index == 286 and h >= 9 : p0[3]=-5
     if beam == 1 :
      if index == 6 and h >= 9 : p0[3]=-10
      if index == 14 and h >= 9 : p0[3]=-30
      if index == 15 and h >= 9 : p0[3]=-30
      if index == 70 and h <= 17 : p0[3]=0
      if index == 71 and h <= 17 : p0[3]=-3
      if index == 125 and h >= 9 : p0[3]=20
      if index == 137 and h >= 9 : p0[3]=15
      if index == 138 and h >= 9 : p0[3]=13
      if index >= 147 and index <= 148 and h >= 9 : p0[3]=15
      if index == 149 and h >= 9 : p0[3]=13
      if index == 150 and h >= 9 : p0[3]=10
      if index >= 235 and index <= 236 and h >= 9 : p0[3]=30
      if index == 237 and h >= 9 : p0[3]=27
      if index == 238 and h >= 9 : p0[3]=25
      if index == 241 and h >= 9 : p0[3]=20
      if index == 243 and h >= 9 : p0[3]=25
      if index == 246 and h >= 9 : p0[3]=10
      if index == 247 and h >= 9 : p0[3]=15
      if index == 248 and h >= 9 : p0[3]=20
      if index == 249 and h >= 9 : p0[3]=15
      if index == 250 and h >= 9 : p0[3]=0
      if index == 253 and h >= 9 : p0[3]=-5
      if index == 254 and h >= 9 : p0[3]=0
      if index == 258 and h >= 9 : p0[3]=10
      if index >= 259 and index <= 261 and h >= 9 : p0[3]=5
      if index == 265 and h >= 9 : p0[3]=-5
      if index == 267 and h >= 9 : p0[3]=0
      if index >= 270 and index <= 271 and h >= 9 : p0[3]=10
      if index == 273 and h >= 9 : p0[3]=0
      if index == 276 and h >= 9 : p0[3]=-5
      
    if year == 2026 and doy == 2:
     if beam == 0 :
      if index == 234 and h >= 9 : p0[3]=25
      if index == 236 and h >= 9 : p0[3]=15
      if index == 237 and h >= 9 : p0[3]=10
      if index == 238 and h >= 9 : p0[3]=20
      if index == 239 and h >= 9 : p0[3]=0
      if index >= 245 and index <= 246 and h >= 9 : p0[3]=-10
      if index == 250 and h >= 9 : p0[3]=-10
      if index == 251 and h >= 9 : p0[3]=0
      if index == 252 and h >= 9 : p0[3]=-10
      if index == 253 and h >= 9 : p0[3]=-20
      if index == 254 and h >= 9 : p0[3]=-10
      if index == 262 and h >= 9 : p0[3]=-20
      if index >= 263 and index <= 264 and h >= 9 : p0[3]=-15
      if index == 269 and h >= 9 : p0[3]=-5
      if index >= 270 and index <= 273 and h >= 9 : p0[3]=-20
      if index == 276 and h >= 9 : p0[3]=-25
      if index >= 277 and index <= 278  and h >= 14 and h <= 24 : p0[3]=numpy.nan
      if index == 279 and h >= 9 : p0[3]=-20
     if beam == 1 :
      if index == 14 and h >= 9 : p0[3]=-10
      if index == 56 and h >= 9 : p0[3]=-5
      if index == 137 and h >= 9 : p0[3]=7
      if index == 140 and h >= 9 : p0[3]=3
      if index == 219 and h >= 9 : p0[3]=35
      if index == 221 and h >= 9 : p0[3]=32
      if index == 222 and h >= 9 : p0[3]=30
      if index == 226 and h >= 9 : p0[3]=30
      if index == 227 and h >= 9 : p0[3]=32
      if index == 234 and h >= 9 : p0[3]=30
      if index == 235 and h >= 9 : p0[3]=25
      if index == 238 and h >= 9 : p0[3]=30
      if index == 239 and h >= 9 : p0[3]=5
      if index == 241 and h >= 9 : p0[3]=5
      if index == 246 and h >= 9 : p0[3]=0
      if index == 247 and h >= 9 : p0[3]=5
      if index == 248 and h >= 9 : p0[3]=0
      if index == 249 and h >= 9 : p0[3]=-5
      if index == 250 and h >= 9 : p0[3]=0
      if index == 251 and h >= 9 : p0[3]=10
      if index == 254 and h >= 9 : p0[3]=0
      if index == 255 and h >= 9 : p0[3]=-10
      if index == 268 and h >= 9 : p0[3]=5
      if index == 269 and h >= 9 : p0[3]=0
      if index >= 273 and index <= 274 and h >= 9 : p0[3]=-10

    if year == 2026 and doy == 1:
     if beam == 0 :
      if index == 236 and h >= 9 : p0[3]=33
      if index == 238 and h >= 9 : p0[3]=30
      if index == 240 and h >= 26 : p0[3]=40
      if index == 244 and h >= 9 : p0[3]=36
      if index == 245 and h >= 9 : p0[3]=35
      if index == 247 and h >= 9 : p0[3]=50
      if index == 248 and h >= 29 : p0[3]=40
      if index == 255 and h >= 9 : p0[3]=0
      if index == 258 and h >= 39 : p0[3]=0
      if index == 259 and h >= 9 : p0[3]=10
      if index == 263 and h >= 9 : p0[3]=-15
      if index == 264 and h >= 9 : p0[3]=-20
      if index == 265 and h >= 9 : p0[3]=-20
      if index == 268 and h >= 9 : p0[3]=-30
      if index >= 270 and index <= 271 and h >= 9 : p0[3]=-30
      if index == 272 and h >= 9 : p0[3]=-40
      if index == 273 and h >= 9 : p0[3]=-25
      if index == 274 and h >= 9 : p0[3]=-30
      if index >= 275 and index <= 277 and h >= 9 : p0[3]=-35
      if index == 279 and h >= 9 : p0[3]=-35
     if beam == 1 :
      if index == 141 and h >= 9 : p0[3]=10
      if index == 232 and h >= 9 : p0[3]=45
      if index >= 233 and index <= 235 and h >= 9 : p0[3]=50
      if index == 236 and h >= 9 : p0[3]=41
      if index == 239 and h >= 9 : p0[3]=50
      if index == 243 and h >= 9 : p0[3]=55
      if index == 244 and h >= 9 : p0[3]=44
      if index == 245 and h >= 9 : p0[3]=45
      if index == 246 and h >= 9 : p0[3]=55
      if index == 247 and h >= 29 : p0[3]=60
      if index == 252 and h >= 29 : p0[3]=25
      if index == 265 and h >= 9 : p0[3]=-5
      if index == 267 and h >= 9 : p0[3]=-10
      if index == 268 and h >= 9 : p0[3]=-20
      if index == 271 and h >= 9 : p0[3]=-20
      if index == 272 and h >= 9 : p0[3]=-30
      if index == 274 and h >= 9 : p0[3]=-20
      if index == 275 and h >= 9 : p0[3]=-20

    if year == 2025 and doy == 365:
     if beam == 0 :
      if index >= 0 and index <= 1 and h >= 9 : p0[3]=-30
      if index == 2 and h >= 9 : p0[3]=-35
      if index >= 10 and index <= 11 and h >= 9 : p0[3]=-50
      if index >= 12 and index <= 13 and h >= 9 : p0[3]=-45
      if index == 16 and h >= 9 : p0[3]=-42
      if index >= 18 and index <= 19 and h >= 9 : p0[3]=-35
      if index >= 20 and index <= 21 and h >= 9 : p0[3]=-40
      if index == 23 and h >= 9 : p0[3]=-42
      if index == 33 and h >= 9 : p0[3]=-45
      if index == 45 and h >= 9 : p0[3]=-30
      if index == 232 and h >= 9 : p0[3]=30
      if index == 233 and h >= 9 : p0[3]=45
      if index == 236 and h >= 9 : p0[3]=55
      if index == 239 and h >= 9 : p0[3]=25
      if index == 240 and h >= 9 : p0[3]=20
      if index == 241 and h >= 9 : p0[3]=15
      if index == 242 and h >= 9 : p0[3]=10
      if index == 243 and h >= 9 : p0[3]=5
      if index == 245 and h >= 9 : p0[3]=0
      if index >= 247 and index <= 248 and h >= 9 : p0[3]=0
     if beam == 1 :
      if index == 0 and h >= 9 : p0[3]=-18
      if index == 1 and h >= 9 : p0[3]=-20
      if index == 2 and h >= 9 : p0[3]=-25
      if index == 5 and h >= 9 : p0[3]=-20
      if index == 9 and h >= 9 : p0[3]=-40
      if index >= 13 and index <= 14 and h >= 9 : p0[3]=-40
      if index == 15 and h >= 9 : p0[3]=-30
      if index == 16 and h >= 9 : p0[3]=-35
      if index >= 17 and index <= 19 and h >= 9 : p0[3]=-30
      if index >= 20 and index <= 21 and h >= 9 : p0[3]=-36
      if index == 26 and h >= 9 : p0[3]=-30
      if index == 27 and h >= 9 : p0[3]=-38
      if index == 55 and h >= 9 : p0[3]=-35
      if index == 69 and h >= 9 : p0[3]=-10
      if index == 226 and h >= 9 : p0[3]=30
      if index == 230 and h >= 9 : p0[3]=42
      if index == 232 and h >= 9 : p0[3]=38
      if index == 233 and h >= 9 : p0[3]=55
      if index == 234 and h >= 9 : p0[3]=60
      if index == 235 and h >= 9 : p0[3]=55
      if index == 237 and h >= 9 : p0[3]=30
      if index == 238 and h >= 9 : p0[3]=40
      if index == 239 and h >= 9 : p0[3]=35
      if index == 240 and h >= 9 : p0[3]=30
      if index == 242 and h >= 9 : p0[3]=20
      if index == 243 and h >= 9 : p0[3]=10
      if index == 244 and h >= 9 : p0[3]=30
      if index == 245 and h >= 9 : p0[3]=0
      if index >= 246 and index <= 247 and h >= 9 : p0[3]=5
      if index == 248 and h >= 9 : p0[3]=5
      if index == 250 and h >= 9 : p0[3]=20
      if index == 251 and h >= 9 : p0[3]=40

    return p0
