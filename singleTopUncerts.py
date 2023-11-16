
from math import sqrt

uncerts = {
    "stat": [0.19, 0.23, 0.33],
    "stat+prof": [0.32, 0.37, 0.58],
    "jes": [0.40, 0.18, 0.84],
    "ElectronEfficiency": [0.01, 0.01, 0.01],
    "Pileup": [0.14, 0.04, 0.34],
    "btagging": [0.20, 0.18, 0.22],
    "QCDbackground": [0.02, 0.01, 0.02],
    "MassCalibration": [0.11, 0.13, 0.20],
    "CR": [0.24, 0.39, 0.68],
    "FlavorJES": [0.13, 0.72, 0.46],
    "bhadronization": [0.23, 0.21, 0.28],
    "signalModel": [0.30, 0.34, 0.21],
    "ttModel": [0.20, 0.04, 0.17],
    "shapes": [0.09, 0.05, 0.07],
    "totalSYS": [0.71, 0.97, 1.39],
    "total": [0.76, 1.04, 1.51],
}


category = {
    "stat": None,
    "stat+prof": None,
    "jes": "exp",
    "ElectronEfficiency": "exp",
    "Pileup": "exp",
    "btagging": "exp",
    "QCDbackground": "exp",
    "MassCalibration": "exp",
    "CR": "model",
    "FlavorJES": "model",
    "bhadronization": "model",
    "signalModel": "model",
    "ttModel": "model",
    "shapes": "model",
    "totalSYS": None,
    "total": None,
}



for i in [0,1,2]:
    print sqrt(pow(uncerts["totalSYS"][i],2)+pow(uncerts["stat+prof"][i],2)), "=", uncerts["total"][i]

for cat in ["exp", "model"]:
    u_comb_2 = 0
    u_plus_2 = 0
    u_minus_2 = 0
    for uncert in uncerts.keys():
        if category[uncert] == cat:
            u_comb_2 += pow(uncerts[uncert][0],2)
            u_plus_2 += pow(uncerts[uncert][1],2)
            u_minus_2 += pow(uncerts[uncert][2],2)
    print "Mtop", cat, ":", sqrt(u_comb_2)
    print "Delta", cat, ":", sqrt(u_plus_2+u_minus_2)
