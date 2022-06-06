'''
@author: roj-idl71
'''
#USED IN jroplot_spectra.py
RTI_CODE = 0            #Range time intensity (RTI).
SPEC_CODE = 1           #Spectra (and Cross-spectra) information.
CROSS_CODE = 2          #Cross-Correlation information.
COH_CODE = 3            #Coherence map.
BASE_CODE = 4           #Base lines graphic.
ROW_CODE = 5            #Row Spectra.
TOTAL_CODE = 6          #Total Power.
DRIFT_CODE = 7          #Drifts graphics.
HEIGHT_CODE = 8         #Height profile.
PHASE_CODE = 9          #Signal Phase.

POWER_CODE = 16
NOISE_CODE = 17
BEACON_CODE = 18

#USED IN jroplot_parameters.py
WIND_CODE = 22
MSKYMAP_CODE = 23
MPHASE_CODE = 24

MOMENTS_CODE = 25
PARMS_CODE = 26
SPECFIT_CODE = 27
EWDRIFT_CODE = 28


#COLOR TABLES

reflectivity = [
    "#000000", # -30
    "#15191d", # -25
    "#2a323b", # -20
    "#3f4c59", # -15
    "#556576", # -10
    "#6a7f94", # -5
    "#7f99b2", # 0
    "#00ffff", # 5
    "#007fff", # 10
    "#0000ff", # 15
    "#00ff00", # 20
    "#00bf00", # 25
    "#007f00", # 30
    "#ffff00", # 35
    "#ffbf00", # 40
    "#ff7f00", # 45
    "#ff0000", # 50
    "#bf0000", # 55
    "#7f0000", # 60
    "#fe00fe", # 65
    "#8e59ff", # 70
    "#f0f0f0", # 75
    "#cccccc" # 80
    ]

velocity = [
    "#003300", "#005500", "#007700", "#009900", "#00bb00", "#24ce24", "#6cd26c", "#b4d6b4",
    "#d6b4b4", "#d26c6c", "#ce2424", "#bb0000", "#980000", "#760000", "#540000", "#330000",
]

spc_width = [
    "#00ffff", "#00aaf2", "#0055e5", "#0000d8", 
    "#007f00", "#00aa00", "#00d400", "#00ff00",
    "#ffff00", "#ffd400", "#ffaa00", "#ff7f00",
    "#ff0000", "#d40000", "#aa0000", "#7f0000",
    "#ff00ff", "#d400d4", "#aa00aa", "#7f007f",
    "#9938ff", "#832ed8", "#6e25b2", "#591c8c",
    "#aaaaaa", "#8e8e8e"
]

sophy_cb_tables = [
    ('sophy_r', reflectivity),
    ('sophy_v', velocity),
    ('sophy_w', spc_width),
]