import os
for files in os.listdir("./"):
    if files=="0":
        new="./"+files
        print new
        os.rename(new,"./Normal")
    if files=="1":
        new="./"+files
        print new
        os.rename(new,"./Emboli")
    if files=="2":
        new="./"+files
        print new
        os.rename(new,"./BRAO")
    if files=="3":
        new="./"+files
        print new
        os.rename(new,"./CRAO")
    if files=="4":
        new="./"+files
        print new
        os.rename(new,"./BRVO")
    if files=="5":
        new="./"+files
        print new
        os.rename(new,"./CRVO")
    if files=="6":
        new="./"+files
        print new
        os.rename(new,"./Hemi-CRVO")
    if files=="7":
        new="./"+files
        print new
        os.rename(new,"./BDR-NPDR")
    if files=="8":
        new="./"+files
        print new
        os.rename(new,"./PDR")
    if files=="9":
        new="./"+files
        print new
        os.rename(new,"./ASR")
    if files=="10":
        new="./"+files
        print new
        os.rename(new,"./HTR")
    if files=="11":
        new="./"+files
        print new
        os.rename(new,"./Coat's")
    if files=="12":
        new="./"+files
        print new
        os.rename(new,"./Macroaneurism")
    if files=="13":
        new="./"+files
        print new
        os.rename(new,"./CNV")
    if files=="14":
        new="./"+files
        print new
        os.rename(new,"./Other")
