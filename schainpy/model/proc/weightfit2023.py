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

# MP febrero 2023
#    if year == 2023 and doy == 37:
#     if beam == 0 :
#      if index == 13 and h >= 9 : p0[3]=-25
#     if beam == 1 :
#      if index == 15 and h >= 9 : p0[3]=-20

    if year == 2023 and doy == 59:
     if beam == 0 :
      if index == 4 and h >= 9 : p0[3]=-5
      if index == 66 and h <= 17 : p0[3]=-5
      if index == 69 and h >= 9 : p0[3]=-8
      if index == 70 and h >= 9 : p0[3]=-8
      if index == 78 and h >= 9 : p0[3]=1
      if index == 90 and h >= 9 : p0[3]=3
      if index == 173 and h >= 9 : p0[3]=30
      if index == 174 and h >= 9 : p0[3]=35
      if index == 177 and h >= 9 : p0[3]=30
      if index >= 178 and index <= 179 and h >= 9 : p0[3]=35
      if index >= 183 and index <= 184 and h >= 9 : p0[3]=30
      if index == 195 and h >= 9 : p0[3]=33
      if index == 210 and h >= 9 : p0[3]=18
      if index == 235 and h >= 9 : p0[3]=10
      if index == 236 and h >= 9 : p0[3]=3
      if index == 237 and h >= 9 : p0[3]=0
      if index >= 238 and index <= 239 and h >= 9 : p0[3]=-5
      if index == 240 and h >= 9 : p0[3]=-10
      if index == 241 and h >= 9 : p0[3]=-15
      if index == 242 and h >= 9 : p0[3]=-10
      if index == 243 and h >= 9 : p0[3]=-15
      if index == 244 and h >= 9 : p0[3]=-18
      if index == 245 and h >= 9 : p0[3]=-20
      if index == 246 and h >= 9 : p0[3]=-25
      if index == 247 and h >= 9 : p0[3]=-30
      if index == 248 and h >= 9 : p0[3]=-32
      if index >= 249 and index <= 250 and h >= 9 : p0[3]=-35
      if index == 252 and h >= 9 : p0[3]=-30
      if index >= 254 and index <= 256 and h >= 9 : p0[3]=-30
      if index >= 257 and index <= 258 and h >= 9 : p0[3]=-35
     if beam == 1 :
      if index == 33 and h >= 9 : p0[3]=-3
      if index == 34 and h >= 9 : p0[3]=-3
      if index == 35 and h <= 19 : p0[3]=-5
      if index == 39 and h >= 9 : p0[3]=-1
      if index == 62 and h >= 9 : p0[3]=-3
      if index == 65 and h <= 17 : p0[3]=-5
      if index == 68 and h >= 9 : p0[3]=0
      if index == 72 and h >= 9 : p0[3]=-3
      if index == 99 and h >= 9 : p0[3]=0
      if index == 226 and h >= 9 : p0[3]=35
      if index >= 238 and index <= 239 and h >= 9 : p0[3]=0
      if index == 242 and h >= 9 : p0[3]=-5
      if index == 245 and h >= 9 : p0[3]=-15
      if index == 251 and h >= 9 : p0[3]=-25
      if index == 253 and h >= 9 : p0[3]=-25

    if year == 2023 and doy == 58:
     if beam == 0 :
      if index == 242 and h >= 9 : p0[3]=-10
      if index >= 243 and index <= 245 and h >= 9 : p0[3]=-12
      if index >= 246 and index <= 249 and h >= 9 : p0[3]=-20
      if index == 250 and h >= 9 : p0[3]=-15
     if beam == 1 :
      if index == 238 and h >= 9 : p0[3]=10

    if year == 2023 and doy == 44:
     if beam == 0 :
      if index == 51 and h >= 9 : p0[3]=-27
      if index == 57 and h >= 9 : p0[3]=-38
      if index == 61 and h >= 9 : p0[3]=-40
      if index == 66 and h >= 9 : p0[3]=-38
      if index == 69 and h >= 9 : p0[3]=-35
      if index == 73 and h >= 9 : p0[3]=-25
     if beam == 1 :
      if index == 56 and h >= 9 : p0[3]=-30
      if index == 60 and h >= 9 : p0[3]=-35
      if index == 62 and h >= 9 : p0[3]=-35
      if index == 68 and h >= 9 : p0[3]=-37
      if index == 69 and h >= 9 : p0[3]=-30
      if index == 70 and h >= 9 : p0[3]=-27
      if index == 71 and h >= 9 : p0[3]=-28
      if index == 73 and h >= 9 : p0[3]=-22
      if index == 74 and h >= 9 : p0[3]=-12
      if index >= 75 and index <= 76 and h >= 9 : p0[3]=-10

    if year == 2023 and doy == 43:
     if beam == 0 :
      if index == 2 and h >= 9 : p0[3]=-32
      if index == 3 and h >= 9 : p0[3]=-30
      if index == 4 and h >= 9 : p0[3]=-32
      if index >= 65 and index <= 66 and h >= 9 : p0[3]=-40
      if index == 67 and h >= 9 : p0[3]=-36
      if index == 68 and h >= 9 : p0[3]=-38
      if index == 69 and h >= 9 : p0[3]=-30
      if index >= 70 and index <= 71 and h >= 9 : p0[3]=-30
      if index == 72 and h >= 26 : p0[3]=-25
      if index >= 68 and index <= 76 and h >= 35 : p0[3]=numpy.nan
      if index == 110 and h >= 9 : p0[3]=15
      if index == 242 and h >= 9 : p0[3]=15
      if index == 243 and h >= 9 : p0[3]=5
      if index >= 244 and index <= 245 and h >= 9 : p0[3]=-10
      if index >= 249 and index <= 250 and h >= 9 : p0[3]=-20
      if index >= 251 and index <= 252 and h >= 9 : p0[3]=-10
      if index >= 253 and index <= 254 and h >= 9 : p0[3]=-20
     if beam == 1 :
      if index == 2 and h >= 9 : p0[3]=-22
      if index == 3 and h >= 9 : p0[3]=-20
      if index == 57 and h >= 9 : p0[3]=-28
      if index >= 58 and index <= 61 and h >= 9 : p0[3]=-25
      if index == 64 and h >= 9 : p0[3]=-28
      if index == 65 and h >= 9 : p0[3]=-35
      if index == 68 and h >= 9 : p0[3]=-36
      if index == 70 and h >= 9 : p0[3]=-25
      if index == 71 and h >= 9 : p0[3]=-25
      if index == 73 and h >= 9 : p0[3]=-15
      if index == 77 and h >= 9 : p0[3]=-10
      if index == 110 and h >= 9 : p0[3]=10
      if index == 147 and h >= 9 : p0[3]=10
      if index == 148 and h >= 9 : p0[3]=10
      if index == 241 and h >= 9 : p0[3]=25
      if index == 242 and h >= 9 : p0[3]=25
      if index == 243 and h >= 9 : p0[3]=15
      if index >= 244 and index <= 245 and h >= 9 : p0[3]=0
      if index == 250 and h >= 9 : p0[3]=-10
      if index >= 251 and index <= 252 and h >= 9 : p0[3]=-5
      if index == 253 and h >= 9 : p0[3]=-10
      if index == 255 and h >= 9 : p0[3]=-15
      if index == 256 and h >= 9 : p0[3]=-20
      if index == 262 and h >= 9 : p0[3]=-30
      if index == 263 and h >= 9 : p0[3]=-35
      if index == 264 and h >= 9 : p0[3]=-30

    if year == 2023 and doy == 42:
     if beam == 0 :
      if index == 28 and h <= 19 : p0[3]=-20
      if index == 30 and h <= 19 : p0[3]=-15
      if index == 68 and h >= 9 : p0[3]=-40
      if index == 71 and h >= 9 : p0[3]=-18
      if index == 72 and h >= 9 : p0[3]=-22
      if index == 130 and h >= 9 : p0[3]=10
      if index == 146 and h >= 9 : p0[3]=15
      if index == 146 and h >= 35 : p0[3]=numpy.nan
      if index == 147 and h >= 35 : p0[3]=numpy.nan
      if index >= 151 and index <= 153 and h >= 9 : p0[3]=15
      if index == 235 and h >= 9 : p0[3]=50
      if index == 236 and h >= 9 : p0[3]=55
      if index == 237 and h >= 9 : p0[3]=55
      if index == 245 and h >= 9 : p0[3]=-25
      if index == 246 and h >= 9 : p0[3]=-40
      if index == 257 and h >= 9 : p0[3]=-30
      if index == 259 and h >= 9 : p0[3]=-40
      if index == 260 and h >= 9 : p0[3]=-40
      if index == 261 and h >= 9 : p0[3]=-35
      if index == 265 and h >= 9 : p0[3]=-50
      if index == 266 and h >= 9 : p0[3]=-40
      if index == 267 and h >= 9 : p0[3]=-30
      if index == 268 and h >= 9 : p0[3]=-35
     if beam == 1 :
      if index == 20 and h <= 17 : p0[3]=-10
      if index == 23 and h <= 19 : p0[3]=-15
      if index == 67 and h >= 9 : p0[3]=-39
      if index == 71 and h >= 9 : p0[3]=-15
      if index == 76 and h >= 9 : p0[3]=-13
      if index == 121 and h >= 9 : p0[3]=5
      if index == 145 and h >= 9 : p0[3]=10
      if index == 146 and h >= 9 : p0[3]=10
      if index == 147 and h >= 9 : p0[3]=10
      if index == 148 and h >= 9 : p0[3]=8
      if index == 231 and h >= 9 : p0[3]=68
      if index == 234 and h >= 9 : p0[3]=70
      if index == 235 and h >= 9 : p0[3]=60
      if index == 236 and h >= 9 : p0[3]=65
      if index == 238 and h >= 9 : p0[3]=70
      if index == 239 and h >= 9 : p0[3]=20
      if index == 240 and h >= 9 : p0[3]=20
      if index == 241 and h >= 9 : p0[3]=-5
      if index == 244 and h >= 9 : p0[3]=-15
      if index == 245 and h >= 9 : p0[3]=-15
      if index == 246 and h >= 9 : p0[3]=-30
      if index == 247 and h >= 9 : p0[3]=-15
      if index == 249 and h >= 9 : p0[3]=-10
      if index == 252 and h >= 9 : p0[3]=-5
      if index == 253 and h >= 9 : p0[3]=-25
      if index == 254 and h >= 9 : p0[3]=-30
      if index == 255 and h >= 9 : p0[3]=-0
      if index == 256 and h >= 9 : p0[3]=-15
      if index == 257 and h >= 9 : p0[3]=-20
      if index == 259 and h >= 9 : p0[3]=-30
      if index == 265 and h >= 9 : p0[3]=-40
      if index == 266 and h >= 9 : p0[3]=-30
      if index == 268 and h >= 9 : p0[3]=-25
      if index == 269 and h >= 9 : p0[3]=-25

    if year == 2023 and doy == 41:
     if beam == 0 :
      if index == 51 and h >= 9 : p0[3]=-24
      if index == 56 and h >= 9 : p0[3]=-25
      if index == 62 and h <= 19 : p0[3]=-30
      if index == 211 and h <= 19 : p0[3]=10
      if index == 229 and h >= 9 : p0[3]=35
     if beam == 1 :
      if index == 33 and h >= 9 : p0[3]=-20
      if index == 34 and h >= 9 : p0[3]=-18
      if index == 51 and h >= 9 : p0[3]=-19
      if index == 52 and h >= 9 : p0[3]=-10
      if index == 53 and h >= 9 : p0[3]=-15
      if index == 56 and h >= 9 : p0[3]=-21
      if index == 57 and h >= 9 : p0[3]=-20
      if index == 59 and h <= 20 : p0[3]=-20
      if index == 66 and h >= 9 : p0[3]=-25
      if index == 72 and h >= 9 : p0[3]=-22
      if index == 74 and h >= 9 : p0[3]=-20
      if index == 76 and h >= 9 : p0[3]=-15

    if year == 2023 and doy == 40:
     if beam == 0 :
      if index == 46 and h >= 9 : p0[3]=-30
      if index == 56 and h >= 9 : p0[3]=-22
      if index == 61 and h >= 9 : p0[3]=-10
      if index == 72 and h >= 9 : p0[3]=-15
      if index == 208 and h >= 9 : p0[3]=10
      if index == 237 and h >= 9 : p0[3]=45
      if index == 239 and h >= 9 : p0[3]=40
      if index == 241 and h >= 9 : p0[3]=35
      if index == 242 and h >= 9 : p0[3]=30
      if index == 243 and h >= 9 : p0[3]=25
      if index == 244 and h >= 9 : p0[3]=10
      if index == 245 and h >= 9 : p0[3]=0
      if index == 246 and h >= 9 : p0[3]=-15
      if index == 247 and h >= 9 : p0[3]=-30
      if index == 248 and h >= 9 : p0[3]=-35
      if index == 249 and h >= 9 : p0[3]=-20
      if index == 250 and h >= 9 : p0[3]=-40
      if index == 251 and h >= 9 : p0[3]=-20
      if index == 255 and h >= 9 : p0[3]=-40
      if index == 258 and h >= 9 : p0[3]=-30
      if index == 260 and h >= 9 : p0[3]=-30
      if index == 262 and h >= 9 : p0[3]=-20
     if beam == 1 :
      if index == 47 and h >= 9 : p0[3]=-20
      if index == 62 and h >= 9 : p0[3]=-8
      if index == 101 and h >= 9 : p0[3]=0
      if index == 208 and h >= 9 : p0[3]=10
      if index == 236 and h >= 9 : p0[3]=50
      if index >= 237 and index <= 240 and h >= 9 : p0[3]=50
      if index == 241 and h >= 9 : p0[3]=45
      if index == 242 and h >= 9 : p0[3]=40
      if index == 243 and h >= 9 : p0[3]=35
      if index == 244 and h >= 9 : p0[3]=20
      if index == 245 and h >= 9 : p0[3]=5
      if index == 246 and h >= 9 : p0[3]=-10
      if index == 247 and h >= 9 : p0[3]=-20
      if index == 248 and h >= 9 : p0[3]=-30
      if index == 249 and h >= 9 : p0[3]=-15
      if index == 250 and h >= 9 : p0[3]=-30
      if index == 252 and h >= 9 : p0[3]=-10
      if index == 255 and h >= 9 : p0[3]=-30
      if index == 257 and h >= 9 : p0[3]=-25
      if index == 258 and h >= 9 : p0[3]=-20
      if index == 259 and h >= 9 : p0[3]=-30
      if index == 261 and h >= 9 : p0[3]=0
      if index == 262 and h >= 9 : p0[3]=-10
      if index == 263 and h >= 9 : p0[3]=-35
      if index == 264 and h >= 9 : p0[3]=-30
      if index >= 266 and index <= 267 and h >= 9 : p0[3]=-30

    if year == 2023 and doy == 39:
     if beam == 0 :
      if index == 21 and h >= 9 : p0[3]=-15
      if index == 244 and h >= 9 : p0[3]=15
      if index == 245 and h >= 9 : p0[3]=0
      if index == 246 and h >= 9 : p0[3]=-5
      if index == 247 and h >= 9 : p0[3]=-10
      if index >= 248 and index <= 249 and h >= 9 : p0[3]=-25
      if index == 250 and h >= 9 : p0[3]=-27
      if index == 251 and h >= 9 : p0[3]=-30
      if index == 278 and h >= 9 : p0[3]=-40
     if beam == 1 :
      if index == 0 and h >= 9 : p0[3]=-25
      if index == 1 and h >= 9 : p0[3]=-20
      if index == 10 and h >= 30 : p0[3]=-10
      if index == 12 and h >= 9 : p0[3]=-10
      if index == 56 and h >= 9 : p0[3]=-18
      if index == 58 and h >= 9 : p0[3]=-20
      if index == 70 and h >= 9 : p0[3]=-16
      if index == 239 and h >= 9 : p0[3]=45
      if index == 241 and h >= 9 : p0[3]=22
      if index == 242 and h >= 9 : p0[3]=28
      if index == 244 and h >= 9 : p0[3]=20
      if index == 245 and h >= 9 : p0[3]=10
      if index == 246 and h >= 9 : p0[3]=5
      if index == 247 and h >= 9 : p0[3]=-5
      if index >= 248 and index <= 249 and h >= 9 : p0[3]=-20
      if index == 251 and h >= 9 : p0[3]=-20
      if index == 252 and h >= 9 : p0[3]=-25
      if index == 253 and h >= 9 : p0[3]=-20
      if index == 254 and h >= 9 : p0[3]=-25
      if index == 255 and h >= 9 : p0[3]=-25
      if index == 267 and h >= 9 : p0[3]=-25

    if year == 2023 and doy == 38:
     if beam == 0 :
      if index == 43 and h >= 9 : p0[3]=-15
      if index == 44 and h >= 9 : p0[3]=-20
      if index == 45 and h >= 9 : p0[3]=-20
      if index == 52 and h >= 9 : p0[3]=-40
      if index == 61 and h >= 9 : p0[3]=-50
      if index >= 62 and index <= 67 and h >= 9 : p0[3]=-45
      if index == 64 and h >= 9 : p0[3]=-25
      if index == 68 and h >= 9 : p0[3]=-50
      if index >= 69 and index <= 70 and h >= 9 : p0[3]=-45
      if index == 71 and h >= 9 : p0[3]=-40
      if index == 74 and h >= 9 : p0[3]=-30
      if index == 100 and h >= 9 : p0[3]=15
      if index == 224 and h >= 9 : p0[3]=25
      if index == 227 and h <= 24 : p0[3]=35
      if index == 231 and h >= 9 : p0[3]=43
      if index == 242 and h >= 9 : p0[3]=30
      if index == 243 and h >= 9 : p0[3]=20
      if index == 244 and h >= 9 : p0[3]=25
      if index == 245 and h >= 9 : p0[3]=0
      if index == 246 and h >= 9 : p0[3]=-5
      if index == 247 and h >= 9 : p0[3]=0
      if index == 248 and h >= 9 : p0[3]=-5
      if index == 249 and h >= 9 : p0[3]=-20
      if index == 250 and h >= 9 : p0[3]=-10
      if index == 252 and h >= 9 : p0[3]=-20
      if index == 254 and h >= 9 : p0[3]=-35
      if index == 286 and h >= 9 : p0[3]=-40
     if beam == 1 :
      if index == 15 and h >= 9 : p0[3]=-15
      if index == 43 and h >= 9 : p0[3]=-5
      if index == 53 and h >= 9 : p0[3]=-28
      if index == 55 and h >= 9 : p0[3]=-50
      if index == 58 and h >= 9 : p0[3]=-40
      if index == 61 and h >= 9 : p0[3]=-45
      if index >= 62 and index <= 67 and h >= 9 : p0[3]=-40
      if index == 64 and h >= 9 : p0[3]=-20
      if index == 68 and h >= 9 : p0[3]=-45
      if index >= 69 and index <= 70 and h >= 9 : p0[3]=-40
      if index == 71 and h >= 9 : p0[3]=-35
      if index == 72 and h >= 9 : p0[3]=-40
      if index == 73 and h >= 9 : p0[3]=-35
      if index == 100 and h >= 9 : p0[3]=10
      if index == 228 and h <= 27 : p0[3]=45
      if index == 231 and h >= 9 : p0[3]=50
      if index >= 234 and index <= 235 and h >= 9 : p0[3]=60
      if index == 237 and h >= 9 : p0[3]=50
      if index >= 238 and index <= 239 and h >= 9 : p0[3]=45
      if index == 242 and h >= 9 : p0[3]=40
      if index == 243 and h >= 9 : p0[3]=30
      if index == 244 and h >= 9 : p0[3]=35
      if index == 245 and h >= 9 : p0[3]=10
      if index == 246 and h >= 9 : p0[3]=0
      if index == 247 and h >= 9 : p0[3]=5
      if index == 249 and h >= 9 : p0[3]=-10
      if index >= 250 and index <= 251 and h >= 9 : p0[3]=0
      if index == 252 and h >= 9 : p0[3]=-10
      if index == 253 and h >= 9 : p0[3]=-20
      if index == 254 and h >= 9 : p0[3]=-25
      if index == 255 and h >= 9 : p0[3]=-28
      if index == 256 and h >= 9 : p0[3]=-27
      if index == 287 and h >= 9 : p0[3]=-25

    if year == 2023 and doy == 37:
     if beam == 0 :
      if index == 38 and h >= 9 : p0[3]=-35
      if index == 44 and h >= 9 : p0[3]=-45
      if index == 47 and h >= 9 : p0[3]=-50
      if index == 50 and h >= 9 : p0[3]=-50
      if index == 54 and h >= 9 : p0[3]=-45
      if index == 55 and h >= 9 : p0[3]=-37
      if index == 56 and h >= 9 : p0[3]=-42
      if index >= 57 and index <= 59 and h >= 9 : p0[3]=-35
      if index == 60 and h >= 9 : p0[3]=-30
      if index == 61 and h >= 9 : p0[3]=-45
      if index == 62 and h >= 9 : p0[3]=-40
      if index == 63 and h >= 9 : p0[3]=-30
      if index == 64 and h >= 9 : p0[3]=-35
      if index == 66 and h >= 9 : p0[3]=-45
      if index >= 67 and index <= 68 and h >= 9 : p0[3]=-40
      if index == 69 and h >= 9 : p0[3]=-50
      if index >= 71 and index <= 72 and h >= 9 : p0[3]=-45
      if index == 75 and h >= 39 : p0[3]=numpy.nan
      if index == 76 and h >= 9 : p0[3]=-25
      if index >= 210 and index <= 211 and h >= 9 : p0[3]=13
      if index == 212 and h >= 9 : p0[3]=15
      if index == 231 and h >= 9 : p0[3]=70
      if index == 236 and h >= 9 : p0[3]=0
      if index >= 237 and index <= 238 and h >= 9 : p0[3]=-5
      if index >= 239 and index <= 240 and h >= 9 : p0[3]=-11
      if index >= 241 and index <= 243 and h >= 9 : p0[3]=-35
      if index == 244 and h >= 9 : p0[3]=-50
      if index == 253 and h >= 9 : p0[3]=-35
     if beam == 1 :
      if index == 1 and h >= 9 : p0[3]=-10
      if index == 5 and h >= 9 : p0[3]=-35
      if index == 10 and h >= 9 : p0[3]=-5
      if index == 12 and h >= 9 : p0[3]=2
      if index == 13 and h >= 9 : p0[3]=5
      if index == 14 and h >= 9 : p0[3]=-5
      if index == 25 and h >= 9 : p0[3]=8
      if index == 26 and h >= 9 : p0[3]=11
      if index == 29 and h <= 16 : p0[3]=0
      if index == 36 and h >= 9 : p0[3]=-25
      if index == 38 and h >= 9 : p0[3]=-31
      if index == 39 and h >= 9 : p0[3]=-39
      if index == 40 and h >= 9 : p0[3]=-36
      if index >= 41 and index <= 42 and h >= 9 : p0[3]=-29
      if index == 43 and h >= 9 : p0[3]=-36
      if index == 44 and h >= 9 : p0[3]=-34
      if index >= 45 and index <= 47 and h >= 9 : p0[3]=-40
      if index >= 48 and index <= 49 and h >= 9 : p0[3]=-45
      if index == 50 and h >= 9 : p0[3]=-40
      if index == 51 and h >= 9 : p0[3]=-43
      if index == 52 and h >= 9 : p0[3]=-40
      if index >= 53 and index <= 54 and h >= 9 : p0[3]=-40
      if index == 55 and h >= 9 : p0[3]=-32
      if index == 56 and h >= 9 : p0[3]=-37
      if index >= 57 and index <= 60 and h >= 9 : p0[3]=-30
      if index == 61 and h >= 9 : p0[3]=-40
      if index == 62 and h >= 9 : p0[3]=-35
      if index == 63 and h >= 9 : p0[3]=-25
      if index == 64 and h >= 9 : p0[3]=-20
      if index >= 65 and index <= 66 and h >= 9 : p0[3]=-40
      if index >= 67 and index <= 68 and h >= 9 : p0[3]=-35
      if index == 69 and h >= 9 : p0[3]=-45
      if index == 70 and h >= 9 : p0[3]=-35
      if index == 71 and h >= 9 : p0[3]=-40
      if index == 72 and h >= 9 : p0[3]=-39
      if index == 73 and h >= 9 : p0[3]=-38
      if index == 74 and h >= 9 : p0[3]=-29
      if index >= 75 and index <= 76 and h >= 9 : p0[3]=-20
      if index == 213 and h >= 9 : p0[3]=20
      if index == 231 and h >= 9 : p0[3]=75
      if index == 232 and h >= 9 : p0[3]=70
      if index == 234 and h >= 9 : p0[3]=60
      if index == 235 and h >= 9 : p0[3]=40
      if index >= 237 and index <= 238 and h >= 9 : p0[3]=7
      if index >= 239 and index <= 240 and h >= 9 : p0[3]=7
      if index == 250 and h >= 9 : p0[3]=-15
      if index == 254 and h >= 9 : p0[3]=-40
      if index == 263 and h >= 9 : p0[3]=-25      

    if year == 2023 and doy == 36: #5
     if beam == 0 :
      if index == 61 and h >= 9 : p0[3]=-45
      if index == 63 and h >= 9 : p0[3]=-45
      if index == 67 and h >= 9 : p0[3]=-50
      if index == 68 and h >= 9 : p0[3]=-46
      if index == 70 and h >= 9 : p0[3]=-35
      if index == 71 and h >= 9 : p0[3]=-30
      if index == 74 and h >= 9 : p0[3]=-20
      if index == 77 and h >= 9 : p0[3]=-10
      if index == 80 and h >= 9 : p0[3]=-1
      if index == 115 and h >= 9 : p0[3]=20
      if index == 129 and h >= 9 : p0[3]=28
      if index == 224 and h >= 9 : p0[3]=16
      if index == 248 and h >= 9 : p0[3]=-20
      if index == 250 and h >= 9 : p0[3]=-15
     if beam == 1 :
      if index == 14 and h >= 9 : p0[3]=-27
      if index == 15 and h >= 9 : p0[3]=-30
      if index == 19 and h >= 9 : p0[3]=-20
      if index == 20 and h >= 9 : p0[3]=-19
      if index == 24 and h >= 9 : p0[3]=-20
      if index == 26 and h >= 9 : p0[3]=-25
      if index == 27 and h >= 9 : p0[3]=-22
      if index == 35 and h >= 9 : p0[3]=-25
      if index == 42 and h >= 9 : p0[3]=-25
      if index == 61 and h >= 9 : p0[3]=-41
      if index == 62 and h >= 9 : p0[3]=-38
      if index == 63 and h >= 9 : p0[3]=-38
      if index == 64 and h >= 9 : p0[3]=-38
      if index >= 65 and index <= 66 and h >= 9 : p0[3]=-40
      if index == 67 and h >= 9 : p0[3]=-45
      if index == 68 and h >= 9 : p0[3]=-42
      if index == 69 and h >= 9 : p0[3]=-38
      if index == 70 and h >= 9 : p0[3]=-30
      if index == 71 and h >= 9 : p0[3]=-24
      if index == 72 and h >= 9 : p0[3]=-20
      if index == 73 and h >= 9 : p0[3]=-15
      if index == 76 and h >= 9 : p0[3]=-11
      if index == 77 and h >= 9 : p0[3]=-12
      if index >= 111 and index <= 112 and h >= 9 : p0[3]=18
      if index == 115 and h >= 9 : p0[3]=17
      if index == 116 and h >= 9 : p0[3]=16
      if index == 122 and h >= 9 : p0[3]=20
      if index == 123 and h == 15 : p0[3]=20
      if index == 223 and h <= 20 : p0[3]=20
      if index == 224 and h >= 9 : p0[3]=24
      if index == 224 and h == 16 : p0[3]=numpy.nan
      if index == 231 and h <= 25 : p0[3]=53
      if index == 233 and h >= 9 : p0[3]=55
      if index == 234 and h >= 9 : p0[3]=60
      if index == 235 and h >= 9 : p0[3]=55
      if index == 236 and h >= 9 : p0[3]=40
      if index == 237 and h >= 9 : p0[3]=40
      if index == 239 and h >= 9 : p0[3]=22
      if index == 242 and h >= 9 : p0[3]=0
      if index == 243 and h >= 9 : p0[3]=0
      if index == 244 and h >= 9 : p0[3]=-5
      if index == 248 and h >= 9 : p0[3]=-5
      if index == 249 and h >= 9 : p0[3]=-15
      if index >= 252 and index <= 254 and h >= 9 : p0[3]=-20
      if index == 257 and h >= 9 : p0[3]=-10
      if index == 261 and h >= 9 : p0[3]=-20

    if year == 2023 and doy == 35:
     if beam == 0 :
      if index == 71 and h >= 9 : p0[3]=-25
      if index == 84 and h >= 9 : p0[3]=1
      if index == 117 and h >= 9 : p0[3]=11
      if index == 218 and h >= 9 : p0[3]=22
      if index >= 233 and index <= 234 and h >= 9 : p0[3]=37
      if index == 235 and h >= 9 : p0[3]=50
      if index == 247 and h >= 29 : p0[3]=-10
      if index >= 253 and index <= 254 and h >= 9 : p0[3]=10
      if index == 262 and h >= 9 : p0[3]=-20
      if index >= 268 and index <= 269 and h >= 9 : p0[3]=-25
      if index == 273 and h >= 9 : p0[3]=-25
     if beam == 1 :
      if index == 56 and h >= 9 : p0[3]=-20
      if index >= 57 and index <= 58 and h >= 9 : p0[3]=-25
      if index == 61 and h >= 9 : p0[3]=-31
      if index == 62 and h <= 19 : p0[3]=-25
      if index == 64 and h <= 19 : p0[3]=-32
      if index == 66 and h >= 9 : p0[3]=-35
      if index == 68 and h >= 9 : p0[3]=-30
      if index == 69 and h >= 9 : p0[3]=-35
      if index == 71 and h >= 9 : p0[3]=-20
      if index == 73 and h >= 9 : p0[3]=-10
      if index == 74 and h >= 9 : p0[3]=-5
      if index == 75 and h >= 9 : p0[3]=-12
      if index == 84 and h >= 9 : p0[3]=-5
      if index == 100 and h >= 9 : p0[3]=5
      if index == 117 and h >= 9 : p0[3]=5
      if index == 163 and h >= 9 : p0[3]=8
      if index == 219 and h >= 9 : p0[3]=30
      if index == 234 and h >= 9 : p0[3]=45
      if index == 235 and h >= 9 : p0[3]=57
      if index == 236 and h >= 9 : p0[3]=62
      if index == 237 and h >= 9 : p0[3]=55
      if index == 238 and h >= 9 : p0[3]=25
      if index >= 239 and index <= 240 and h >= 9 : p0[3]=10
      if index == 243 and h >= 9 : p0[3]=5
      if index == 244 and h >= 9 : p0[3]=0
      if index == 245 and h >= 9 : p0[3]=15
      if index == 246 and h >= 9 : p0[3]=0
      if index == 247 and h <= 27 : p0[3]=80
      if index == 255 and h >= 29 : p0[3]=-18
      if index == 261 and h >= 9 : p0[3]=-5
      if index == 263 and h >= 9 : p0[3]=-5
      if index == 264 and h >= 9 : p0[3]=0
      if index == 266 and h >= 9 : p0[3]=-5
      if index == 271 and h >= 9 : p0[3]=-20
      if index == 272 and h >= 9 : p0[3]=-10
      if index == 274 and h >= 9 : p0[3]=-5

    if year == 2023 and doy == 34:
     if beam == 0 :
      if index == 40 and h >= 9 : p0[3]=-28
      if index == 50 and h >= 9 : p0[3]=-38
      if index == 51 and h >= 9 : p0[3]=-45
      if index == 52 and h >= 9 : p0[3]=-45
      if index == 56 and h >= 9 : p0[3]=-35
      if index == 57 and h >= 9 : p0[3]=-18
      if index == 59 and h >= 9 : p0[3]=-15
      if index == 60 and h >= 9 : p0[3]=-35
      if index == 62 and h >= 9 : p0[3]=-45
      if index == 63 and h >= 9 : p0[3]=-45
      if index >= 64 and index <= 68 and h >= 9 : p0[3]=-40
      if index >= 69 and index <= 70 and h >= 9 : p0[3]=-25
      if index == 74 and h >= 9 : p0[3]=-2
      if index == 235 and h >= 9 : p0[3]=70
      if index == 236 and h >= 9 : p0[3]=65
      if index == 237 and h >= 9 : p0[3]=62
      if index == 239 and h >= 9 : p0[3]=30
      if index == 241 and h >= 9 : p0[3]=2
      if index == 242 and h >= 9 : p0[3]=0
      if index == 259 and h >= 23 : p0[3]=-25
      if index == 259 and h <= 22 : p0[3]=numpy.nan
     if beam == 1 :
      if index == 48 and h >= 9 : p0[3]=-30
      if index == 51 and h >= 9 : p0[3]=-35
      if index == 52 and h >= 9 : p0[3]=-37
      if index == 53 and h >= 9 : p0[3]=-38
      if index == 55 and h >= 9 : p0[3]=-38
      if index == 56 and h >= 9 : p0[3]=-30
      if index == 57 and h >= 9 : p0[3]=-5
      if index == 58 and h >= 9 : p0[3]=-2
      if index == 59 and h >= 9 : p0[3]=-10
      if index == 60 and h >= 9 : p0[3]=-30
      if index >= 61 and index <= 63 and h >= 9 : p0[3]=-40
      if index >= 64 and index <= 68 and h >= 9 : p0[3]=-35
      if index == 69 and h >= 9 : p0[3]=-20
      if index == 71 and h >= 9 : p0[3]=-5
      if index == 72 and h >= 9 : p0[3]=-4
      if index == 73 and h >= 9 : p0[3]=-4
      if index >= 74 and index <= 75 and h >= 9 : p0[3]=0
      if index == 77 and h >= 9 : p0[3]=0
      if index == 115 and h >= 9 : p0[3]=10
      if index == 117 and h >= 9 : p0[3]=8
      if index == 199 and h >= 9 : p0[3]=-1
      if index == 200 and h >= 9 : p0[3]=3
      if index == 212 and h >= 9 : p0[3]=15
      if index >= 230 and index <= 232 and h >= 9 : p0[3]=55
      if index == 233 and h >= 9 : p0[3]=62
      if index == 234 and h >= 9 : p0[3]=65
      if index == 235 and h >= 9 : p0[3]=76
      if index == 237 and h >= 9 : p0[3]=68
      if index == 238 and h >= 9 : p0[3]=66
      if index == 239 and h >= 9 : p0[3]=45
      if index == 240 and h >= 9 : p0[3]=20
      if index == 242 and h >= 9 : p0[3]=6
      if index == 245 and h >= 9 : p0[3]=-25
      if index == 246 and h >= 9 : p0[3]=-10

    if year == 2023 and doy == 33:
     if beam == 0 :
      if index == 35 and h >= 9 : p0[3]=-25
      if index == 47 and h >= 9 : p0[3]=-25
      if index == 49 and h >= 9 : p0[3]=-23
      if index == 66 and h >= 9 : p0[3]=-25
      if index == 112 and h >= 9 : p0[3]=10
      if index == 237 and h >= 9 : p0[3]=40
      if index == 245 and h >= 9 : p0[3]=0
      if index == 248 and h >= 9 : p0[3]=-10
      if index == 249 and h >= 9 : p0[3]=-20
      if index == 252 and h >= 9 : p0[3]=-10
      if index == 255 and h >= 9 : p0[3]=-15
      if index == 266 and h >= 9 : p0[3]=-30
     if beam == 1 :
      if index == 6 and h >= 9 : p0[3]=-25
      if index == 32 and h >= 9 : p0[3]=-15
      if index == 34 and h >= 9 : p0[3]=-10
      if index == 39 and h >= 9 : p0[3]=-20
      if index == 49 and h >= 9 : p0[3]=-20
      if index >= 51 and index <= 54 and h >= 9 : p0[3]=-20
      if index == 55 and h >= 9 : p0[3]=-15
      if index == 58 and h >= 9 : p0[3]=-25
      if index == 59 and h >= 9 : p0[3]=-23
      if index == 60 and h >= 9 : p0[3]=-20
      if index == 61 and h >= 9 : p0[3]=-22
      if index >= 62 and index <= 63 and h >= 9 : p0[3]=-20
      if index == 64 and h >= 9 : p0[3]=-24
      if index == 66 and h >= 9 : p0[3]=-21
      if index == 67 and h >= 9 : p0[3]=-17
      if index == 68 and h >= 9 : p0[3]=-15
      if index >= 69 and index <= 71 and h >= 9 : p0[3]=-10
      if index == 72 and h >= 9 : p0[3]=-8
      if index == 74 and h >= 9 : p0[3]=0
      if index == 75 and h >= 9 : p0[3]=-1
      if index == 77 and h >= 9 : p0[3]=5
      if index == 95 and h >= 9 : p0[3]=5
      if index == 107 and h >= 17 : p0[3]=5
      if index == 110 and h >= 9 : p0[3]=5
      if index == 113 and h >= 9 : p0[3]=5
      if index >= 116 and index <= 119 and h >= 9 : p0[3]=5
      if index == 145 and h >= 9 : p0[3]=5
      if index == 149 and h >= 9 : p0[3]=2
      if index == 201 and h >= 9 : p0[3]=5
      if index == 217 and h >= 9 : p0[3]=25
      if index == 221 and h >= 9 : p0[3]=30
      if index == 224 and h >= 9 : p0[3]=30
      if index == 225 and h >= 9 : p0[3]=30
      if index == 228 and h >= 9 : p0[3]=45
      if index == 229 and h >= 9 : p0[3]=50
      if index == 232 and h >= 9 : p0[3]=55
      if index == 233 and h >= 9 : p0[3]=56
      if index == 234 and h >= 9 : p0[3]=51
      if index == 237 and h >= 9 : p0[3]=45
      if index == 239 and h >= 9 : p0[3]=40
      if index == 240 and h >= 9 : p0[3]=51
      if index == 241 and h >= 9 : p0[3]=50
      if index == 243 and h >= 9 : p0[3]=20
      if index == 245 and h >= 9 : p0[3]=0
      if index == 247 and h >= 9 : p0[3]=30
      if index == 256 and h >= 9 : p0[3]=0
      if index == 262 and h >= 9 : p0[3]=-5
      if index == 267 and h >= 9 : p0[3]=-5

    if year == 2023 and doy == 32:
     if beam == 0 :
      if index == 163 and h >= 9 : p0[3]=18
      if index == 168 and h >= 9 : p0[3]=15
      if index == 170 and h >= 9 : p0[3]=18
      if index == 224 and h <= 19 : p0[3]=20
      if index == 235 and h >= 9 : p0[3]=35
      if index >= 242 and index <= 243 and h >= 9 : p0[3]=20
      if index >= 244 and index <= 245 and h >= 9 : p0[3]=30
      if index >= 246 and index <= 247 and h >= 9 : p0[3]=40
      if index == 248 and h >= 9 : p0[3]=10
      if index == 249 and h >= 9 : p0[3]=-5
      if index == 250 and h >= 9 : p0[3]=-10
      if index == 271 and h >= 9 : p0[3]=-20
     if beam == 1 :
      if index == 163 and h >= 9 : p0[3]=15
      if index == 168 and h >= 9 : p0[3]=10
      if index == 170 and h >= 9 : p0[3]=12
      if index == 173 and h >= 9 : p0[3]=18
      if index >= 178 and index <= 179 and h >= 9 : p0[3]=15
      if index == 180 and h >= 9 : p0[3]=12
      if index == 184 and h >= 9 : p0[3]=15
      if index == 194 and h >= 9 : p0[3]=10
      if index == 201 and h >= 9 : p0[3]=15
      if index == 228 and h >= 9 : p0[3]=40
      if index == 231 and h >= 9 : p0[3]=55
      if index == 232 and h >= 9 : p0[3]=54
      if index == 233 and h >= 9 : p0[3]=55
      if index == 234 and h >= 9 : p0[3]=53
      if index == 238 and h >= 9 : p0[3]=35
      if index == 239 and h >= 9 : p0[3]=33
      if index == 240 and h >= 9 : p0[3]=35
      if index >= 242 and index <= 243 and h >= 9 : p0[3]=30
      if index == 244 and h >= 9 : p0[3]=40
      if index >= 246 and index <= 247 and h >= 9 : p0[3]=50
      if index == 248 and h >= 9 : p0[3]=20
      if index == 249 and h >= 9 : p0[3]=0
      if index == 252 and h >= 9 : p0[3]=-15
      if index == 253 and h >= 9 : p0[3]=-20
      if index == 255 and h >= 9 : p0[3]=-25
      if index == 256 and h >= 9 : p0[3]=-20
      if index == 257 and h >= 9 : p0[3]=-20
      if index == 258 and h >= 9 : p0[3]=-12
      if index == 259 and h >= 9 : p0[3]=-10
      if index == 277 and h >= 9 : p0[3]=-20

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
