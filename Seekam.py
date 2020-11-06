#!/usr/bin/python3
#import pyximport; pyximport.install()
import subprocess
import imagehash
import shutil
import os
import sys
import vptree
import pickle
import numpy as np
from PIL import Image
from glob import glob, iglob
from profilehooks import timecall


def euclidean(p1, p2):
    try:
        return bin(p1^p2).count('1')
    except TypeError:
        p1 = int(p1)
        p2 = int(p2)
        return bin(p1^p2).count('1')



def Treetment(Template,hashtype,Dickpath,Treepath):

    if Template is TmpListSet3:
          Paf="./Datas/Templates/Set3/*"
    elif Template is TmpListSet1:
          Paf="./Datas/Templates/Set1/*"
    elif Template is TmpListSet2:
          Paf="./Datas/Templates/Set2/*"
    if (hashtype=="dhash"):
          hashfunction=imagehash.dhash

    elif (hashtype=="dhashv"):
          hashfunction=imagehash.dhash_vertical

    elif (hashtype=="ahash"):
          hashfunction=imagehash.average_hash
	        
    elif (hashtype=="phash"):
          hashfunction=imagehash.phash

    elif (hashtype=="phashimple"):
          hashfunction=imagehash.phash_simple
	    
    elif (hashtype=="whash"):
          hashfunction=imagehash.whash


    DickHead = {}
    print("Saving Hashs from " + str(Paf) + " Using " +str(hashtype)+" ...")
    for file in Template:
        sys.stdout.write("\r" + "Proceeding: "+str(file)+"                  ")
        sys.stdout.flush()
        image = Image.open(file)
        filename = file[file.rfind("/") + 1:]

        DickHead[filename] = int(str(hashfunction(image)),16)

    print("\nDone.\nWriting vptree now...")
    hashes = [int(i) for i in list(DickHead.values())]
    tree = vptree.VPTree(hashes, euclidean)
    Dick_plk = open(Dickpath,"wb")
    Tree_plk = open(Treepath, "wb")
    pickle.dump(DickHead, Dick_plk)
    pickle.dump(tree, Tree_plk)
    Dick_plk.close()
    Tree_plk.close()
    print("\n" +str(Dickpath)+" and "+str(Treepath)+" Has been saved ..\n")
    return


def Missing():



        AHASH_dict_Set3_pkl = False
        PHASH_dict_Set3_pkl = False
        PHASHS_dict_Set3_pkl = False
        DHASH_dict_Set3_pkl = False
        DHASHV_dict_Set3_pkl = False
        WHASH_dict_Set3_pkl = False


        AHASH_dict_Set1_pkl = False
        PHASH_dict_Set1_pkl = False
        PHASHS_dict_Set1_pkl = False
        DHASH_dict_Set1_pkl = False
        DHASHV_dict_Set1_pkl = False
        WHASH_dict_Set1_pkl = False

        AHASH_dict_Set2_pkl = False
        PHASH_dict_Set2_pkl = False
        PHASHS_dict_Set2_pkl = False
        DHASH_dict_Set2_pkl = False
        DHASHV_dict_Set2_pkl = False
        WHASH_dict_Set2_pkl = False


        AHASH_tree_Set3_pkl = False
        PHASH_tree_Set3_pkl = False
        PHASHS_tree_Set3_pkl = False
        DHASH_tree_Set3_pkl = False
        DHASHV_tree_Set3_pkl = False
        WHASH_tree_Set3_pkl = False


        AHASH_tree_Set1_pkl = False
        PHASH_tree_Set1_pkl = False
        PHASHS_tree_Set1_pkl = False
        DHASH_tree_Set1_pkl = False
        DHASHV_tree_Set1_pkl = False
        WHASH_tree_Set1_pkl = False

        AHASH_tree_Set2_pkl = False
        PHASH_tree_Set2_pkl = False
        PHASHS_tree_Set2_pkl = False
        DHASH_tree_Set2_pkl = False
        DHASHV_tree_Set2_pkl = False
        WHASH_tree_Set2_pkl = False



        Tmpkl = True

        CounterCheck_py = False



        if os.path.exists("./Datas/AHASH_tree_Set3.pkl"):
             AHASH_tree_Set3_pkl =True
        else:
            Tmpkl = False
            print("AHASH_tree_Set3.pkl is missing.\n")

        if os.path.exists("./Datas/PHASH_tree_Set3.pkl"):
            PHASH_tree_Set3_pkl = True
        else:
            Tmpkl = False
            print("PHASH_tree_Set3.pkl is missing.\n")

        if os.path.exists("./Datas/PHASHS_tree_Set3.pkl"):
            PHASHS_tree_Set3_pkl = True
        else:
            Tmpkl = False
            print("PHASHS_tree_Set3.pkl is missing.\n")
    
        if os.path.exists("./Datas/DHASH_tree_Set3.pkl"):
            DHASH_tree_Set3_pkl = True
        else:
            Tmpkl = False
            print("DHASH_tree_Set3.pkl is missing.\n")

        if os.path.exists("./Datas/DHASHV_tree_Set3.pkl"):
            DHASHV_tree_Set3_pkl = True
        else:
            Tmpkl = False
            print("DHASHV_tree_Set3.pkl is missing.\n")

        if os.path.exists("./Datas/WHASH_tree_Set3.pkl"):
            WHASH_tree_Set3_pkl = True
        else:
            Tmpkl = False
            print("WHASH_tree_Set3.pkl is missing.\n")


##
        if os.path.exists("./Datas/AHASH_tree_Set1.pkl"):
             AHASH_tree_Set1_pkl =True
        else:
            Tmpkl = False
            print("AHASH_tree_Set1.pkl is missing.\n")

        if os.path.exists("./Datas/PHASH_tree_Set1.pkl"):
            PHASH_tree_Set1_pkl = True
        else:
            Tmpkl = False
            print("PHASH_tree_Set1.pkl is missing.\n")

        if os.path.exists("./Datas/PHASHS_tree_Set1.pkl"):
            PHASHS_tree_Set1_pkl = True
        else:
            Tmpkl = False
            print("PHASHS_tree_Set1.pkl is missing.\n")
    
        if os.path.exists("./Datas/DHASH_tree_Set1.pkl"):
            DHASH_tree_Set1_pkl = True
        else:
            Tmpkl = False
            print("DHASH_tree_Set1.pkl is missing.\n")

        if os.path.exists("./Datas/DHASHV_tree_Set1.pkl"):
            DHASHV_tree_Set1_pkl = True
        else:
            Tmpkl = False
            print("DHASHV_tree_Set1.pkl is missing.\n")

        if os.path.exists("./Datas/WHASH_tree_Set1.pkl"):
            WHASH_tree_Set1_pkl = True
        else:
            Tmpkl = False
            print("WHASH_tree_Set1.pkl is missing.\n")
##


        if os.path.exists("./Datas/AHASH_tree_Set2.pkl"):
             AHASH_tree_Set2_pkl =True
        else:
            Tmpkl = False
            print("AHASH_tree_Set2.pkl is missing.\n")

        if os.path.exists("./Datas/PHASH_tree_Set2.pkl"):
            PHASH_tree_Set2_pkl = True
        else:
            Tmpkl = False
            print("PHASH_tree_Set1.pkl is missing.\n")

        if os.path.exists("./Datas/PHASHS_tree_Set1.pkl"):
            PHASHS_tree_Set2_pkl = True
        else:
            Tmpkl = False
            print("PHASHS_tree_Set2.pkl is missing.\n")
    
        if os.path.exists("./Datas/DHASH_tree_Set2.pkl"):
            DHASH_tree_Set2_pkl = True
        else:
            Tmpkl = False
            print("DHASH_tree_Set2.pkl is missing.\n")

        if os.path.exists("./Datas/DHASHV_tree_Set2.pkl"):
            DHASHV_tree_Set2_pkl = True
        else:
            Tmpkl = False
            print("DHASHV_tree_Set2.pkl is missing.\n")

        if os.path.exists("./Datas/WHASH_tree_Set2.pkl"):
            WHASH_tree_Set2_pkl = True
        else:
            Tmpkl = False
            print("WHASH_tree_Set2.pkl is missing.\n")

########################################


        if os.path.exists("./Datas/AHASH_dict_Set3.pkl"):
             AHASH_dict_Set3_pkl =True
        else:
            Tmpkl = False
            print("AHASH_dict_Set3.pkl is missing.\n")

        if os.path.exists("./Datas/PHASH_dict_Set3.pkl"):
            PHASH_dict_Set3_pkl = True
        else:
            Tmpkl = False
            print("PHASH_dict_Set3.pkl is missing.\n")

        if os.path.exists("./Datas/PHASHS_dict_Set3.pkl"):
            PHASHS_dict_Set3_pkl = True
        else:
            Tmpkl = False
            print("PHASHS_dict_Set3.pkl is missing.\n")
    
        if os.path.exists("./Datas/DHASH_dict_Set3.pkl"):
            DHASH_dict_Set3_pkl = True
        else:
            Tmpkl = False
            print("DHASH_dict_Set3.pkl is missing.\n")

        if os.path.exists("./Datas/DHASHV_dict_Set3.pkl"):
            DHASHV_dict_Set3_pkl = True
        else:
            Tmpkl = False
            print("DHASHV_dict_Set3.pkl is missing.\n")

        if os.path.exists("./Datas/WHASH_dict_Set3.pkl"):
            WHASH_dict_Set3_pkl = True
        else:
            Tmpkl = False
            print("WHASH_dict_Set3.pkl is missing.\n")

##
        if os.path.exists("./Datas/AHASH_dict_Set1.pkl"):
             AHASH_dict_Set1_pkl =True
        else:
            Tmpkl = False
            print("AHASH_dict_Set1.pkl is missing.\n")

        if os.path.exists("./Datas/PHASH_dict_Set1.pkl"):
            PHASH_dict_Set1_pkl = True
        else:
            Tmpkl = False
            print("PHASH_dict_Set1.pkl is missing.\n")

        if os.path.exists("./Datas/PHASHS_dict_Set1.pkl"):
            PHASHS_dict_Set1_pkl = True
        else:
            Tmpkl = False
            print("PHASHS_dict_Set1.pkl is missing.\n")
    
        if os.path.exists("./Datas/DHASH_dict_Set1.pkl"):
            DHASH_dict_Set1_pkl = True
        else:
            Tmpkl = False
            print("DHASH_dict_Set1.pkl is missing.\n")

        if os.path.exists("./Datas/DHASHV_dict_Set1.pkl"):
            DHASHV_dict_Set1_pkl = True
        else:
            Tmpkl = False
            print("DHASHV_dict_Set1.pkl is missing.\n")

        if os.path.exists("./Datas/WHASH_dict_Set1.pkl"):
            WHASH_dict_Set1_pkl = True
        else:
            Tmpkl = False
            print("WHASH_dict_Set1.pkl is missing.\n")



        if os.path.exists("./Datas/AHASH_dict_Set2.pkl"):
             AHASH_dict_Set2_pkl =True
        else:
            Tmpkl = False
            print("AHASH_dict_Set2.pkl is missing.\n")

        if os.path.exists("./Datas/PHASH_dict_Set2.pkl"):
            PHASH_dict_Set2_pkl = True
        else:
            Tmpkl = False
            print("PHASH_dict_Set2.pkl is missing.\n")

        if os.path.exists("./Datas/PHASHS_dict_Set2.pkl"):
            PHASHS_dict_Set2_pkl = True
        else:
            Tmpkl = False
            print("PHASHS_dict_Set2.pkl is missing.\n")
    
        if os.path.exists("./Datas/DHASH_dict_Set2.pkl"):
            DHASH_dict_Set2_pkl = True
        else:
            Tmpkl = False
            print("DHASH_dict_Set2.pkl is missing.\n")

        if os.path.exists("./Datas/DHASHV_dict_Set2.pkl"):
            DHASHV_dict_Set2_pkl = True
        else:
            Tmpkl = False
            print("DHASHV_dict_Set2.pkl is missing.\n")

        if os.path.exists("./Datas/WHASH_dict_Set2.pkl"):
            WHASH_dict_Set2_pkl = True
        else:
            Tmpkl = False
            print("WHASH_dict_Set2.pkl is missing.\n")





        if os.path.exists("./Datas/CounterCheck.py"):
            CounterCheck_py = True
        else:
            Tmpkl = False
            print("\CounterCheck.py is missing.\n")




        if Tmpkl is False:

            print("\n\nSome Templates Hash files are missing ! \n\n")
            print("\nStoring Templates Pictures Hashes into lists..\nThis could take a while..\n")
            CountchkL = TmpSet1Nbr
            CountchkLNew = TmpSet2Nbr
            CountchkG = TmpSet3Nbr

            if PHASH_dict_Set3_pkl is False or PHASH_tree_Set3_pkl is False:
                  Treetment(TmpListSet3,"phash","./Datas/PHASH_dict_Set3.pkl","./Datas/PHASH_tree_Set3.pkl")

            if AHASH_dict_Set3_pkl is False or AHASH_tree_Set3_pkl is False:
                  Treetment(TmpListSet3,"ahash","./Datas/AHASH_dict_Set3.pkl","./Datas/AHASH_tree_Set3.pkl")

            if PHASHS_dict_Set3_pkl is False or PHASHS_tree_Set3_pkl is False:
                  Treetment(TmpListSet3,"phashimple","./Datas/PHASHS_dict_Set3.pkl","./Datas/PHASHS_tree_Set3.pkl")

            if DHASH_dict_Set3_pkl is False or DHASH_tree_Set3_pkl is False:
                  Treetment(TmpListSet3,"dhash","./Datas/DHASH_dict_Set3.pkl","./Datas/DHASH_tree_Set3.pkl")

            if DHASHV_dict_Set3_pkl is False or DHASHV_tree_Set3_pkl is False:
                  Treetment(TmpListSet3,"dhashv","./Datas/DHASHV_dict_Set3.pkl","./Datas/DHASHV_tree_Set3.pkl")

            if WHASH_dict_Set3_pkl is False or WHASH_tree_Set3_pkl is False:
                  Treetment(TmpListSet3,"whash","./Datas/WHASH_dict_Set3.pkl","./Datas/WHASH_tree_Set3.pkl")



            print("\n"+str(CountchkG*7)+" templates hashes loaded for "+ str(TmpSet3Nbr) +" files in Datas/Templates/Set3 's folder..\n")
##

## 


            if PHASH_dict_Set2_pkl is False or PHASH_tree_Set2_pkl is False:
                  Treetment(TmpListSet2,"phash","./Datas/PHASH_dict_Set2.pkl","./Datas/PHASH_tree_Set2.pkl")

            if AHASH_dict_Set2_pkl is False or AHASH_tree_Set2_pkl is False:
                  Treetment(TmpListSet2,"ahash","./Datas/AHASH_dict_Set2.pkl","./Datas/AHASH_tree_Set2.pkl")

            if PHASHS_dict_Set2_pkl is False or PHASHS_tree_Set2_pkl is False:
                  Treetment(TmpListSet2,"phashimple","./Datas/PHASHS_dict_Set2.pkl","./Datas/PHASHS_tree_Set2.pkl")

            if DHASH_dict_Set2_pkl is False or DHASH_tree_Set2_pkl is False:
                  Treetment(TmpListSet2,"dhash","./Datas/DHASH_dict_Set2.pkl","./Datas/DHASH_tree_Set2.pkl")

            if DHASHV_dict_Set2_pkl is False or DHASHV_tree_Set2_pkl is False:
                  Treetment(TmpListSet2,"dhashv","./Datas/DHASHV_dict_Set2.pkl","./Datas/DHASHV_tree_Set2.pkl")

            if WHASH_dict_Set2_pkl is False or WHASH_tree_Set2_pkl is False:
                  Treetment(TmpListSet2,"whash","./Datas/WHASH_dict_Set2.pkl","./Datas/WHASH_tree_Set2.pkl")


            print("\n"+str(CountchkLNew*7)+" templates hashes loaded for "+ str(TmpSet2Nbr) +" files in Datas/Templates/Set1's folder..\n")
 
            if PHASH_dict_Set1_pkl is False or PHASH_tree_Set1_pkl is False:
                  Treetment(TmpListSet1,"phash","./Datas/PHASH_dict_Set1.pkl","./Datas/PHASH_tree_Set1.pkl")

            if AHASH_dict_Set1_pkl is False or AHASH_tree_Set1_pkl is False:
                  Treetment(TmpListSet1,"ahash","./Datas/AHASH_dict_Set1.pkl","./Datas/AHASH_tree_Set1.pkl")

            if PHASHS_dict_Set1_pkl is False or PHASHS_tree_Set1_pkl is False:
                  Treetment(TmpListSet1,"phashimple","./Datas/PHASHS_dict_Set1.pkl","./Datas/PHASHS_tree_Set1.pkl")

            if DHASH_dict_Set1_pkl is False or DHASH_tree_Set1_pkl is False:
                  Treetment(TmpListSet1,"dhash","./Datas/DHASH_dict_Set1.pkl","./Datas/DHASH_tree_Set1.pkl")

            if DHASHV_dict_Set1_pkl is False or DHASHV_tree_Set1_pkl is False:
                  Treetment(TmpListSet1,"dhashv","./Datas/DHASHV_dict_Set1.pkl","./Datas/DHASHV_tree_Set1.pkl")

            if WHASH_dict_Set1_pkl is False or WHASH_tree_Set1_pkl is False:
                  Treetment(TmpListSet1,"whash","./Datas/WHASH_dict_Set1.pkl","./Datas/WHASH_tree_Set1.pkl")




            print("\n"+str(CountchkL*7)+" templates hashes loaded for "+ str(TmpSet1Nbr) +" files in Datas/Templates/Set1's folder..\n")





            with open("./Datas/CounterCheck.py","w") as f:
                                f.write("#!/usr/bin/python3\n")
                                f.write("CountchkL=int("+str(CountchkL)+")\n\n")
                                f.write("CountchkLNew=int("+str(CountchkLNew)+")\n\n")
                                f.write("CountchkG=int("+str(CountchkG)+")\n\n")
    ##
            print("\nAll User Pictures Hashes as been saved to reduce loading time at next start..\n")
            return
        else:
                 return





def Hash2Test():
    global TemplatesLoaded
    global TmpSet1Hash
    global TmpSet1Phash
    global TmpSet1Phashimple
    global TmpSet1Dhash
    global TmpSet1Dhashv
    global TmpSet1Wash

    global TmpSet2Hash
    global TmpSet2Phash
    global TmpSet2Phashimple
    global TmpSet2Dhash
    global TmpSet2Dhashv
    global TmpSet2Wash

    global TmpSet3Hash
    global TmpSet3Phash
    global TmpSet3Phashimple
    global TmpSet3Dhash
    global TmpSet3Dhashv
    global TmpSet3Wash


    Missing()



    try:
              print("\nImporting TmpSet1Hash...\n")
              TmpSet1Hash = pickle.load( open( "./Datas/AHASH_tree_Set1.pkl", "rb" ) )
              print("Importing TmpSet1Phash...\n")
              TmpSet1Phash = pickle.load( open( "./Datas/PHASH_tree_Set1.pkl", "rb" ) )
              print("Importing TmpSet1Phashimple...\n")
              TmpSet1Phashimple = pickle.load( open( "./Datas/PHASHS_tree_Set1.pkl", "rb" ) )
              print("Importing TmpSet1Dhash...\n")
              TmpSet1Dhash = pickle.load( open( "./Datas/DHASH_tree_Set1.pkl", "rb" ) )
              print("Importing TmpSet1Dhash...\n")
              TmpSet1Dhashv = pickle.load( open( "./Datas/DHASHV_tree_Set1.pkl", "rb" ) )
              print("Importing TmpSet1Wash...\n")
              TmpSet1Wash = pickle.load( open( "./Datas/WHASH_tree_Set1.pkl", "rb" ) )
              print("\nDone...")



              print("\nImporting TmpSet2Hash...\n")
              TmpSet2Hash = pickle.load( open( "./Datas/AHASH_tree_Set2.pkl", "rb" ) )
              print("Importing TmpSet2Phash...\n")
              TmpSet2Phash = pickle.load( open( "./Datas/PHASH_tree_Set2.pkl", "rb" ) )
              print("Importing TmpSet2Phashimple...\n")
              TmpSet2Phashimple = pickle.load( open( "./Datas/PHASHS_tree_Set2.pkl", "rb" ) )
              print("Importing TmpSet2Dhash...\n")
              TmpSet2Dhash = pickle.load( open( "./Datas/DHASH_tree_Set2.pkl", "rb" ) )
              print("Importing TmpSet2Dhash...\n")
              TmpSet2Dhashv = pickle.load( open( "./Datas/DHASHV_tree_Set2.pkl", "rb" ) )
              print("Importing TmpSet2Wash...\n")
              TmpSet2Wash = pickle.load( open( "./Datas/WHASH_tree_Set2.pkl", "rb" ) )
              print("\nDone...")
##
              print("\nImporting TmpSet3Hash...\n")
              TmpSet3Hash = pickle.load( open( "./Datas/AHASH_tree_Set3.pkl", "rb" ) )
              print("Importing TmpSet3Phash...\n")
              TmpSet3Phash = pickle.load( open( "./Datas/PHASH_tree_Set3.pkl", "rb" ) )
              print("Importing TmpSet3Phashimple...\n")
              TmpSet3Phashimple = pickle.load( open( "./Datas/PHASHS_tree_Set3.pkl", "rb" ) )
              print("Importing TmpSet3Dhash...\n")
              TmpSet3Dhash = pickle.load( open( "./Datas/DHASH_tree_Set3.pkl", "rb" ) )
              print("Importing TmpSet3Dhashv...\n")
              TmpSet3Dhashv = pickle.load( open( "./Datas/DHASHV_tree_Set3.pkl", "rb" ) )
              print("Importing TmpSet3Wash...\n")
              TmpSet3Wash = pickle.load( open( "./Datas/WHASH_tree_Set3.pkl", "rb" ) )
              print("\nDone...")




##
##


              print("\nImporting TmpSet1DickHash...\n")
              TmpSet1DickHash = pickle.load( open( "./Datas/AHASH_dict_Set1.pkl", "rb" ) )
              print("Importing TmpSet1DickPhash...\n")
              TmpSet1DickPhash = pickle.load( open( "./Datas/PHASH_dict_Set1.pkl", "rb" ) )
              print("Importing TmpSet1DickPhashimple...\n")
              TmpSet1DickPhashimple = pickle.load( open( "./Datas/PHASHS_dict_Set1.pkl", "rb" ) )
              print("Importing TmpSet1DickDhash...\n")
              TmpSet1DickDhash = pickle.load( open( "./Datas/DHASH_dict_Set1.pkl", "rb" ) )
              print("Importing TmpSet1DickDhash...\n")
              TmpSet1DickDhashv = pickle.load( open( "./Datas/DHASHV_dict_Set1.pkl", "rb" ) )
              print("Importing TmpSet1DickWash...\n")
              TmpSet1DickWash = pickle.load( open( "./Datas/WHASH_dict_Set1.pkl", "rb" ) )
              print("\nDone...")
##
              print("\nImporting TmpSet3DickHash...\n")
              TmpSet3DickHash = pickle.load( open( "./Datas/AHASH_dict_Set3.pkl", "rb" ) )
              print("Importing TmpSet3DickPhash...\n")
              TmpSet3DickPhash = pickle.load( open( "./Datas/PHASH_dict_Set3.pkl", "rb" ) )
              print("Importing TmpSet3DickPhashimple...\n")
              TmpSet3DickPhashimple = pickle.load( open( "./Datas/PHASHS_dict_Set3.pkl", "rb" ) )
              print("Importing TmpSet3DickDhash...\n")
              TmpSet3DickDhash = pickle.load( open( "./Datas/DHASH_dict_Set3.pkl", "rb" ) )
              print("Importing TmpSet3DickDhashv...\n")
              TmpSet3DickDhashv = pickle.load( open( "./Datas/DHASHV_dict_Set3.pkl", "rb" ) )
              print("Importing TmpSet3DickWash...\n")
              TmpSet3DickWash = pickle.load( open( "./Datas/WHASH_dict_Set3.pkl", "rb" ) )
              print("\nDone...")

              print("\nImporting TmpSet2DickHash...\n")
              TmpSet2DickHash = pickle.load( open( "./Datas/AHASH_dict_Set2.pkl", "rb" ) )
              print("Importing TmpSet2DickPhash...\n")
              TmpSet2DickPhash = pickle.load( open( "./Datas/PHASH_dict_Set2.pkl", "rb" ) )
              print("Importing TmpSet2DickPhashimple...\n")
              TmpSet2DickPhashimple = pickle.load( open( "./Datas/PHASHS_dict_Set2.pkl", "rb" ) )
              print("Importing TmpSet2DickDhash...\n")
              TmpSet2DickDhash = pickle.load( open( "./Datas/DHASH_dict_Set2.pkl", "rb" ) )
              print("Importing TmpSet2DickDhash...\n")
              TmpSet2DickDhashv = pickle.load( open( "./Datas/DHASHV_dict_Set2.pkl", "rb" ) )
              print("Importing TmpSet2DickWash...\n")
              TmpSet2DickWash = pickle.load( open( "./Datas/WHASH_dict_Set2.pkl", "rb" ) )
              print("\nDone...")
##


    except Exception as e:
             print("Error : ",e)
             sys.exit(0)

    print("\nLoading Hashs done..\n\n")
##

    print("Checking Hash integrity...\n")
    sys.path.append("./Datas/")
    try:
            from CounterCheck import CountchkL,CountchkLNew,CountchkG


            if TmpSet3Nbr in (CountchkG,TmpSet3DickHash,TmpSet3DickPhash,TmpSet3DickPhashimple,TmpSet3DickDhash,TmpSet3DickDhashv,TmpSet3DickWash) and TmpSet1Nbr in (CountchkL,TmpSet1DickHash,TmpSet1DickPhash,TmpSet1DickPhashimple,TmpSet1DickDhash,TmpSet1DickDhashv,TmpSet1DickWash) and TmpSet2Nbr in (CountchkLNew,TmpSet2DickHash,TmpSet2DickPhash,TmpSet2DickPhashimple,TmpSet2DickDhash,TmpSet2DickDhashv,TmpSet2DickWash):
                print("\nIntegrity check passed !\n")
                print("Numbers of Set3  Templates = "+str(TmpSet3Nbr)+" Hashs Type Counter = "+str(CountchkG))
                print("Numbers of Set1 Templates = "+str(TmpSet1Nbr)+" Hashs Type Counter = "+str(CountchkL))
            else:
                print("\nIntegrity check failed : Number of files in Templates directory must be equal to the numbers of hashes in Templates lists ..\n")
                print("Numbers of Set3  Templates = "+str(TmpSet3Nbr)+" Hashs Type Counter = "+str(CountchkG))
                print("Numbers of Set3  Templates = "+str(TmpSet3Nbr)+" TmpSet3Hash Counter = "+str(len(TmpSet3DickHash)))
                print("Numbers of Set3  Templates = "+str(TmpSet3Nbr)+" TmpSet3Phash Counter = "+str(len(TmpSet3DickPhash)))
                print("Numbers of Set3  Templates = "+str(TmpSet3Nbr)+" TmpSet3Phashimple Counter = "+str(len(TmpSet3DickPhashimple)))
                print("Numbers of Set3  Templates = "+str(TmpSet3Nbr)+" TmpSet3Dhash Counter = "+str(len(TmpSet3DickDhash)))
                print("Numbers of Set3  Templates = "+str(TmpSet3Nbr)+" TmpSet3Dhashv Counter = "+str(len(TmpSet3DickDhashv)))
                print("Numbers of Set3  Templates = "+str(TmpSet3Nbr)+" TmpSet3Wash Counter = "+str(len(TmpSet3DickWash)))

                print("Numbers of Set1 Templates = "+str(TmpSet1Nbr)+" Hashs Type Counter = "+str(CountchkL))
                print("Numbers of Set1 Templates = "+str(TmpSet1Nbr)+" TmpSet1Hash Counter = "+str(len(TmpSet1DickHash)))
                print("Numbers of Set1 Templates = "+str(TmpSet1Nbr)+" TmpSet1Phash Counter = "+str(len(TmpSet1DickPhash)))
                print("Numbers of Set1 Templates = "+str(TmpSet1Nbr)+" TmpSet1Phashimple Counter = "+str(len(TmpSet1DickPhashimple)))
                print("Numbers of Set1 Templates = "+str(TmpSet1Nbr)+" TmpSet1Dhash Counter = "+str(len(TmpSet1DickDhash)))
                print("Numbers of Set1 Templates = "+str(TmpSet1Nbr)+" TmpSet1Dhashv Counter = "+str(len(TmpSet1DickDhashv)))
                print("Numbers of Set1 Templates = "+str(TmpSet1Nbr)+" TmpSet1Wash Counter = "+str(len(TmpSet1DickWash)))

                print("Numbers of Set2 Templates = "+str(TmpSet2Nbr)+" Hashs Type Counter = "+str(CountchkLNew))
                print("Numbers of Set2 Templates = "+str(TmpSet2Nbr)+" TmpSet2Hash Counter = "+str(len(TmpSet2DickHash)))
                print("Numbers of Set2 Templates = "+str(TmpSet2Nbr)+" TmpSet2Phash Counter = "+str(len(TmpSet2DickPhash)))
                print("Numbers of Set2 Templates = "+str(TmpSet2Nbr)+" TmpSet2Phashimple Counter = "+str(len(TmpSet2DickPhashimple)))
                print("Numbers of Set2 Templates = "+str(TmpSet2Nbr)+" TmpSet2Dhash Counter = "+str(len(TmpSet2DickDhash)))
                print("Numbers of Set2 Templates = "+str(TmpSet2Nbr)+" TmpSet2Dhashv Counter = "+str(len(TmpSet2DickDhashv)))
                print("Numbers of Set2 Templates = "+str(TmpSet2Nbr)+" TmpSet2Wash Counter = "+str(len(TmpSet2DickWash)))
                print()
                sys.exit()


    except Exception as e:
             print("\nTemplates Integrity check failed ....\n")
             print("Error : ",e)
             sys.exit(0)


##
    if 1 == 1:
        NbrCamToTest = len(glob(UnknownCam+"*"))
        kamlst = iglob(UnknownCam+"*")

        filecnt = 0
        for camfile in kamlst:
              filecnt = filecnt + 1
              sys.stdout.write("\r" + "Proceeding: "+str(filecnt)+"/"+str(NbrCamToTest))
              sys.stdout.flush()
              Whicham(camfile)


    #except Exception as e:
          #print(e)



def Hashing(filename):

  phash = int(str(imagehash.phash(Image.open(filename))),16)
  ahash = int(str(imagehash.average_hash(Image.open(filename))),16)
  phashimple = int(str(imagehash.phash_simple(Image.open(filename))),16)
  dhash = int(str(imagehash.dhash(Image.open(filename))),16)
  dhashv = int(str(imagehash.dhash_vertical(Image.open(filename))),16)
  wash = int(str(imagehash.whash(Image.open(filename))),16)
  return phash,ahash,phashimple,dhash,dhashv,wash




def Queue(filename,id,bonusdbg):
     global ToMoveFile
     global ToMoveId
     global ToMoveBonus

     ToMoveFile.append(filename)
     ToMoveId.append(id)
     ToMoveBonus.append(bonusdbg)
     return

     

def Move(ToMoveFile,ToMoveId,ToMoveBonus):

  global TotalCams
  global TotalSet3
  global TotalSet2
  global Total_IpCam
  global TotalOther
  global TotalFailed

  print("\n\n Moving Pictures to their respective folders..\n\n")
  for filename,id,bonusdbg in zip(ToMoveFile,ToMoveId,ToMoveBonus):
     if id == UnknownCam:
          print("Filename : ",filename)
          print("Camera Generated file detected.")
          print("BonusDbg: ",str(bonusdbg))
          if not os.path.exists(str(UnknownCam)):
               os.makedirs(str(UnknownCam))
          shutil.copy(filename,UnknownCam)
          print("Moved to folder:"+UnknownCam)
          TotalCams= TotalCams + 1 
     if id == Set3 :
          print("Filename : ",filename)
          print("Motion Set3  Generated file detected.")
          print("BonusDbg: ",str(bonusdbg))
          if not os.path.exists(str(Set3 )):
               os.makedirs(str(Set3 ))
          shutil.copy(filename,Set3 )
          print("Moved to folder:"+Set3 )
          TotalSet3 = TotalSet3 + 1
     if id == Set1:
          print("Filename : ",filename)
          print("Motion Set1 Generated file detected.")
          print("BonusDbg: ",str(bonusdbg))
          if not os.path.exists(str(Set1)):
               os.makedirs(str(Set1))
          shutil.copy(filename,Set1)
          print("Moved to folder:"+Set1)
          TotalSet2 = TotalSet2 +1
     if id == IpCam:
          print("Filename : ",filename)
          print("Ipcam Generated file detected.")
          print("BonusDbg: ",str(bonusdbg))
          if not os.path.exists(str(IpCam)):
               os.makedirs(str(IpCam))
          shutil.copy(filename,IpCam)
          print("Moved to folder:"+IpCam)
          Total_IpCam = Total_IpCam +1
     if id == Picture:
          print("Filename : ",filename)
          print("Other Generated file detected.")
          print("BonusDbg: ",str(bonusdbg))
          if not os.path.exists(str(Picture)):
               os.makedirs(str(Picture))
          shutil.copy(filename,Picture)
          print("Moved to folder:"+Picture)
          TotalOther = TotalOther +1
     if id == Bogus:
          print("Filename : ",filename)
          print("Failed Generated file detected.")
          print("BonusDbg: ",str(bonusdbg))
          if not os.path.exists(str(Bogus)):
               os.makedirs(str(Bogus))
          shutil.copy(filename,Bogus)
          print("Moved to folder:"+Bogus)
          TotalFailed = TotalFailed + 1
     print()
  return

def Question(mode):
  if mode == "resume": 

    if os.path.exists(str(UnknownCam)):
        NbrCamToTest = len(glob(UnknownCam+"*"))
        kamlst = iglob(UnknownCam+"*")
        print("\n---- Warning!! ---- \nIt looks like the programe has been interrupted while attempting to sort  era files\nor you choose to keep the folder ./Datas/UnknownCam/ instead of deleting it for some reason\n")
        SkipPartOne = input("Do you want to resume from this part ?\nOr to start from the begining ?\n(y to resume/n to starting over again) : ").lower().strip()
        print()
        while not(SkipPartOne == "y" or SkipPartOne == "yes" or SkipPartOne == "n" or SkipPartOne == "no"):
              SkipPartOne = input("Do you want to resume from this part ?\nOr to start from the begining ?\n(y to resume/n to starting over again) : ").lower().strip()
              print()
        if "n" in SkipPartOne:
            print("\nStarting over again ..\n")
            print("\n Deleting previous ./Datas/UnknownCam/ folder.\n")
            shutil.rmtree("./Datas/UnknownCam/")
            return False
        elif "y" in SkipPartOne:
            return True
    else: 
          return False

  if mode == "delete":

            Deletefolder = input("The programe has finished all its tasks.\ndo you want to deleted ./Datas/UnknownCam/ folder?\nAnswering yes will delete all pictures identified as   files in the temporary folder.\n(y/n): ").lower().strip()
            print()
            while not(Deletefolder == "y" or Deletefolder == "yes" or Deletefolder == "n" or Deletefolder == "no"):
                  Deletefolder = input("The programe has finished all its tasks.\ndo you want to deleted ./Datas/UnknownCam/ folder?\nAnswering yes will delete all pictures from the pictures identified as   files in the temporary folder.\n(y/n): ").lower().strip()
                  print()
            if "n" in Deletefolder:
                print("\nOk keeping the folder where it is.")
                print("\nexiting now...\n")
                sys.exit(0)
            else:

                print("\nFine\nDeleting previous ./Datas/UnknownCam/ folder.\n")
                shutil.rmtree("./Datas/UnknownCam/")
                print("\nexiting now...\n")
                sys.exit(0)





def Bonus(Sortlist):
  Bonus=0
 # limit = 200
  iter = 0
  Minimal = 0

  for score,h in Sortlist:
               Minimal = score
               break
  for score,h in Sortlist:
                if score != 0:
                    Bonus = Bonus + int((1000/score))
                else:
                    Bonus = Bonus + 1000
  return Bonus,Minimal


def Scoring(filename,mlNew,mlpNew,mlpsNew,mldhNew,mldhvNew,mlwhNew,ml,mg,mlp,mgp,mlps,mgps,mldh,mgdh,mldhv,mgdhv,mlwh,mgwh,BonusSet1, BonusSet3,BonusSet1P, BonusSet3P,BonusSet1PS, BonusSet3PS,BonusSet1DH, BonusSet3DH,BonusSet1DHV, BonusSet3DHV,BonusSet1WH, BonusSet3WH, BonusSet2, BonusSet2P, BonusSet2PS, BonusSet2DH, BonusSet2DHV, BonusSet2WH):

  
  ScoreSet1 = 0
  ScoreSet3  = 0


##

  if min(ml,mlNew,mg) == ml:
       if max(BonusSet1, BonusSet2, BonusSet3) == BonusSet1:
            try:
                ScoreSet1 = ScoreSet1 + (BonusSet1/ml)
            except:
                ScoreSet1 = ScoreSet1 + BonusSet1

       if max(BonusSet1, BonusSet2, BonusSet3) ==  BonusSet2:
            try:
                ScoreSet1 = ScoreSet1 + ( BonusSet2/mlNew)
            except:
                ScoreSet1 = ScoreSet1 +  BonusSet2




  if min(ml,mlNew,mg) == mlNew:
       if max(BonusSet1, BonusSet2, BonusSet3) == BonusSet1:
            try:
                ScoreSet1 = ScoreSet1 + (BonusSet1/ml)
            except:
                ScoreSet1 = ScoreSet1 + BonusSet1

       if max(BonusSet1, BonusSet2, BonusSet3) ==  BonusSet2:
            try:
                ScoreSet1 = ScoreSet1 + ( BonusSet2/mlNew)
            except:
                ScoreSet1 = ScoreSet1 +  BonusSet2



  if min(ml,mlNew,mg) == mg:
  
       if max(BonusSet1, BonusSet2, BonusSet3) ==  BonusSet3:
            try:
                ScoreSet3  = ScoreSet3  + ( BonusSet3/mg)
            except:
                ScoreSet3  = ScoreSet3  +  BonusSet3
##


  if min(mlp,mlpNew,mgp) == mlp:
       if max(BonusSet1P, BonusSet2P, BonusSet3P) == BonusSet1P:
            try:
                ScoreSet1 = ScoreSet1 + (BonusSet1P/mlp)
            except:
                ScoreSet1 = ScoreSet1 + BonusSet1P
       if max(BonusSet1P, BonusSet2P, BonusSet3P) ==  BonusSet2P:
           try:
               ScoreSet1 = ScoreSet1 + ( BonusSet2P/mlpNew)
           except:
               ScoreSet1 = ScoreSet1 +  BonusSet2P



  if min(mlp,mlpNew,mgp) == mlpNew:
       if max(BonusSet1P, BonusSet2P, BonusSet3P) == BonusSet1P:
            try:
                ScoreSet1 = ScoreSet1 + (BonusSet1P/mlp)
            except:
                ScoreSet1 = ScoreSet1 + BonusSet1P
       if max(BonusSet1P, BonusSet2P, BonusSet3P) ==  BonusSet2P:
           try:
               ScoreSet1 = ScoreSet1 + ( BonusSet2P/mlpNew)
           except:
               ScoreSet1 = ScoreSet1 +  BonusSet2P



  if min(mlp,mlpNew,mgp) == mgp:
       if max(BonusSet1P, BonusSet2P, BonusSet3P) ==  BonusSet3P:
          try:
             ScoreSet3  = ScoreSet3  + ( BonusSet3P/mgp)
          except:
             ScoreSet3  = ScoreSet3  +  BonusSet3P


###
  if min(mlps,mlpsNew,mgps) == mlps:
     if max(BonusSet1PS, BonusSet2PS, BonusSet3PS) == BonusSet1PS:
         try:
           ScoreSet1 = ScoreSet1 + (BonusSet1PS/mlps)
         except:
           ScoreSet1 = ScoreSet1 + BonusSet1PS
     if max(BonusSet1PS, BonusSet2PS, BonusSet3PS) ==  BonusSet2PS:
        try:
           ScoreSet1 = ScoreSet1 + ( BonusSet2PS/mlpsNew)
        except:
           ScoreSet1 = ScoreSet1 +  BonusSet2PS



  if min(mlps,mlpsNew,mgps) == mlpsNew:
     if max(BonusSet1PS, BonusSet2PS, BonusSet3PS) == BonusSet1PS:
         try:
           ScoreSet1 = ScoreSet1 + (BonusSet1PS/mlps)
         except:
           ScoreSet1 = ScoreSet1 + BonusSet1PS
     if max(BonusSet1PS, BonusSet2PS, BonusSet3PS) ==  BonusSet2PS:
        try:
           ScoreSet1 = ScoreSet1 + ( BonusSet2PS/mlpsNew)
        except:
           ScoreSet1 = ScoreSet1 +  BonusSet2PS


  if min(mlps,mlpsNew,mgps) == mgps:
     if max(BonusSet1PS, BonusSet2PS, BonusSet3PS) ==  BonusSet3PS:
         try:
           ScoreSet3  = ScoreSet3  + ( BonusSet3PS/mgps)
         except:
           ScoreSet3  = ScoreSet3  +  BonusSet3PS
##

  if min(mldh,mldhNew,mgdh) == mldh:
      if max(BonusSet1DH, BonusSet2DH, BonusSet3DH) == BonusSet1DH:
         try:
               ScoreSet1 = ScoreSet1 + (BonusSet1DH/mldh)
         except:
               ScoreSet1 = ScoreSet1 + BonusSet1DH
      if max(BonusSet1DH, BonusSet2DH, BonusSet3DH) ==  BonusSet2DH:
         try:
               ScoreSet1 = ScoreSet1 + ( BonusSet2DH/mldhNew)
         except:
               ScoreSet1 = ScoreSet1 +  BonusSet2DH


  if min(mldh,mldhNew,mgdh) == mldhNew:
      if max(BonusSet1DH, BonusSet2DH, BonusSet3DH) == BonusSet1DH:
         try:
               ScoreSet1 = ScoreSet1 + (BonusSet1DH/mldh)
         except:
               ScoreSet1 = ScoreSet1 + BonusSet1DH
      if max(BonusSet1DH, BonusSet2DH, BonusSet3DH) ==  BonusSet2DH:
         try:
               ScoreSet1 = ScoreSet1 + ( BonusSet2DH/mldhNew)
         except:
               ScoreSet1 = ScoreSet1 +  BonusSet2DH

    


  if min(mldh,mldhNew,mgdh) == mgdh:
      if max(BonusSet1DH, BonusSet2DH, BonusSet3DH) ==  BonusSet3DH:
         try:
               ScoreSet3  = ScoreSet3  + ( BonusSet3DH/mgdh)
         except:
               ScoreSet3  = ScoreSet3  +  BonusSet3DH



##
  if min(mldhv,mldhvNew,mgdhv) == mldhv:
      if max(BonusSet1DHV, BonusSet2DHV, BonusSet3DHV) == BonusSet1DHV:
         try:
               ScoreSet1 = ScoreSet1 + (BonusSet1DHV/mldhv)
         except:
               ScoreSet1 = ScoreSet1 + BonusSet1DHV
      if max(BonusSet1DHV, BonusSet2DHV, BonusSet3DHV) ==  BonusSet2DHV:
         try:
               ScoreSet1 = ScoreSet1 + ( BonusSet2DHV/mldhvNew)
         except:
               ScoreSet1 = ScoreSet1 +  BonusSet2DHV



  if min(mldhv,mldhvNew,mgdhv) == mldhvNew:
      if max(BonusSet1DHV, BonusSet2DHV, BonusSet3DHV) == BonusSet1DHV:
         try:
               ScoreSet1 = ScoreSet1 + (BonusSet1DHV/mldhv)
         except:
               ScoreSet1 = ScoreSet1 + BonusSet1DHV
      if max(BonusSet1DHV, BonusSet2DHV, BonusSet3DHV) ==  BonusSet2DHV:
         try:
               ScoreSet1 = ScoreSet1 + ( BonusSet2DHV/mldhvNew)
         except:
               ScoreSet1 = ScoreSet1 +  BonusSet2DHV



  if min(mldhv,mldhvNew,mgdhv) == mgdhv:
      if max(BonusSet1DHV, BonusSet2DHV, BonusSet3DHV) ==  BonusSet3DHV:
         try:
               ScoreSet3  = ScoreSet3  + ( BonusSet3DHV/mgdhv)
         except:
               ScoreSet3  = ScoreSet3  +  BonusSet3DHV     

       

  if min(mlwh,mlwhNew,mgwh) == mlwh:
      if max(BonusSet1WH, BonusSet2WH, BonusSet3WH) == BonusSet1WH:
         try:
               ScoreSet1 = ScoreSet1 + (BonusSet1WH/mlwh)
         except:
               ScoreSet1 = ScoreSet1 + BonusSet1WH
      if max(BonusSet1WH, BonusSet2WH,mgwh) ==  BonusSet2WH:
         try:
               ScoreSet1 = ScoreSet1 + ( BonusSet2WH/mlwhNew)
         except:
               ScoreSet1 = ScoreSet1 +  BonusSet2WH 


  if min(mlwh,mlwhNew,mgwh) == mlwhNew:
      if max(BonusSet1WH, BonusSet2WH, BonusSet3WH) == BonusSet1WH:
         try:
               ScoreSet1 = ScoreSet1 + (BonusSet1WH/mlwh)
         except:
               ScoreSet1 = ScoreSet1 + BonusSet1WH
      if max(BonusSet1WH, BonusSet2WH,mgwh) ==  BonusSet2WH:
         try:
               ScoreSet1 = ScoreSet1 + ( BonusSet2WH/mlwhNew)
         except:
               ScoreSet1 = ScoreSet1 +  BonusSet2WH 

  if min(mlwh,mlwhNew,mgwh) == mgwh:
      if max(BonusSet1WH, BonusSet2WH, BonusSet3WH) ==  BonusSet3WH:
         try:
               ScoreSet3  = ScoreSet3  + ( BonusSet3WH/mgwh)
         except:
               ScoreSet3  = ScoreSet3  +  BonusSet3WH


#  DbgBonus= ""
  DbgBonus = f"\n-- ML:{ml}/MlNew:{mlNew}/Mg:{mg}  BL:{BonusSet1}/BlNew:{ BonusSet2}/Bg:{ BonusSet3} --\n-- MLP:{mlp}/MLPNew:{mlpNew}/Mgp:{mgp}  BLP:{BonusSet1P}/BLPNew:{ BonusSet2P}/BGP:{ BonusSet3P} --\n-- MLPS:{mlps}/MlPSNew:{mlpsNew}/MGPS:{mgps}  BLPS:{BonusSet1PS}/BLPSNew:{ BonusSet2PS}/BGPS:{ BonusSet3PS} --\n-- MLDH:{mldh}/MLDHNew:{mldhNew}/MGDH:{mgdh}  BLDH:{BonusSet1DH}/BLDHNew:{ BonusSet2DH}/BGDH:{ BonusSet3DH} --\n-- MLDHV:{mldhv}/MLDHVNew:{mldhvNew}/MGDHV:{mgdhv} BLDHV:{BonusSet1DHV}/BLDHVNew{ BonusSet2DHV}/BGDHV:{ BonusSet3DHV} --\n-- MLWH:{mlwh}/MLWHNew:{mlwhNew}/MGDH:{mgwh}  BLWH:{BonusSet1WH}/BLWHNew{ BonusSet2WH}/BGWH:{ BonusSet3WH} --\n-- ScoreSet1 ={ScoreSet1} / ScoreSet3 ={ScoreSet3 } --" 

  if ScoreSet3  > ScoreSet1:
         Queue(filename,Set3 ,DbgBonus)
         return
  elif ScoreSet1 > ScoreSet3 :
         Queue(filename,Set1,DbgBonus)
         return
  else:

                   DbgBonus += "## failed ##"
                   Queue(filename,Bogus,DbgBonus)
                   return



@timecall
def Whicham(filename):
  
  phash,ahash,phashimple,dhash,dhashv,wash= Hashing(filename)

  SortlistG = sorted(TmpSet3Hash.get_n_nearest_neighbors(ahash,200))
  SortlistGP = sorted(TmpSet3Phash.get_n_nearest_neighbors(phash,200))
  SortlistGPS = sorted(TmpSet3Phashimple.get_n_nearest_neighbors(phashimple,200))
  SortlistGDH = sorted(TmpSet3Dhash.get_n_nearest_neighbors(dhash,200))
  SortlistGDHV = sorted(TmpSet3Dhashv.get_n_nearest_neighbors(dhashv,200))
  SortlistGWH = sorted(TmpSet3Wash.get_n_nearest_neighbors(wash,200))

  SortlistSet1 = sorted(TmpSet1Hash.get_n_nearest_neighbors(ahash,200))
  SortlistSet1P = sorted(TmpSet1Phash.get_n_nearest_neighbors(phash,200))
  SortlistSet1PS = sorted(TmpSet1Phashimple.get_n_nearest_neighbors(phashimple,200))
  SortlistSet1DH = sorted(TmpSet1Dhash.get_n_nearest_neighbors(dhash,200))
  SortlistSet1DHV = sorted(TmpSet1Dhashv.get_n_nearest_neighbors(dhashv,200))
  SortlistSet1WH = sorted(TmpSet1Wash.get_n_nearest_neighbors(wash,200))


  SortlistSet2 = sorted(TmpSet2Hash.get_n_nearest_neighbors(ahash,200))
  SortlistSet2P = sorted(TmpSet2Phash.get_n_nearest_neighbors(phash,200))
  SortlistSet2PS = sorted(TmpSet2Phashimple.get_n_nearest_neighbors(phashimple,200))
  SortlistSet2DH = sorted(TmpSet2Dhash.get_n_nearest_neighbors(dhash,200))
  SortlistSet2DHV = sorted(TmpSet2Dhashv.get_n_nearest_neighbors(dhashv,200))
  SortlistSet2WH = sorted(TmpSet2Wash.get_n_nearest_neighbors(wash,200))



  BonusSet1,ml = Bonus(SortlistSet1)
  BonusSet1P,mlp = Bonus(SortlistSet1P)
  BonusSet1PS,mlps = Bonus(SortlistSet1PS)
  BonusSet1DH,mldh = Bonus(SortlistSet1DH)
  BonusSet1DHV,mldhv = Bonus(SortlistSet1DHV)
  BonusSet1WH,mlwh = Bonus(SortlistSet1WH)

  BonusSet2,mlNew = Bonus(SortlistSet2)
  BonusSet2P,mlpNew = Bonus(SortlistSet2P)
  BonusSet2PS,mlpsNew = Bonus(SortlistSet2PS)
  BonusSet2DH,mldhNew = Bonus(SortlistSet2DH)
  BonusSet2DHV,mldhvNew = Bonus(SortlistSet2DHV)
  BonusSet2WH,mlwhNew = Bonus(SortlistSet2WH)



  BonusSet3,mg = Bonus(SortlistG)
  BonusSet3P,mgp = Bonus(SortlistGP)
  BonusSet3PS,mgps = Bonus(SortlistGPS)
  BonusSet3DH,mgdh = Bonus(SortlistGDH)
  BonusSet3DHV,mgdhv = Bonus(SortlistGDHV)
  BonusSet3WH,mgwh = Bonus(SortlistGWH)
##
##
  Scoring(filename,mlNew,mlpNew,mlpsNew,mldhNew,mldhvNew,mlwhNew,ml,mg,mlp,mgp,mlps,mgps,mldh,mgdh,mldhv,mgdhv,mlwh,mgwh,BonusSet1, BonusSet3,BonusSet1P, BonusSet3P,BonusSet1PS, BonusSet3PS,BonusSet1DH, BonusSet3DH,BonusSet1DHV, BonusSet3DHV,BonusSet1WH, BonusSet3WH, BonusSet2, BonusSet2P, BonusSet2PS, BonusSet2DH, BonusSet2DHV, BonusSet2WH)
##
##

  



def Seekam(jpg):

     FoundMotion = False
     FoundIpCam = False
     cmd = "identify -verbose "+jpg
     try:
          jpgexif=subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True)
          jpgexif=jpgexif.decode("utf-8")
     except Exception as e:
          print('\nError:',e)
          return

     for exif in MotionExif:
          if str(exif) in str(jpgexif) and not str(exif) in str(BadExif):
               FoundMotion = True
          else:
               if str(exif) == "Quality: 42":
                      if "Quality: 50" in str(jpgexif):
                         FoundMotion = True
               else:
                    FoundMotion = False
                    break
     if FoundMotion == False:

          for exif in IpCamExif:
               if str(exif) in str(jpgexif) and not str(exif) in str(BadExif):
                    FoundIpCam = True
               else:
                    FoundIpCam =  False
                    break

     if FoundIpCam == True:
          Queue(jpg,IpCam,"NoDbg")
          return
     if FoundIpCam == False and FoundMotion == False:
          Queue(jpg,Picture,"NoDbg")
          return
     if FoundMotion == True:
          
          Queue(jpg,UnknownCam,"Unknown")


#################
###### Main #####
#################

def main():
    global ToMoveFile
    global ToMoveId
    global ToMoveBonus
    global Total_IpCam
    global TotalOther
    global TotalCams
    global TotalSet3
    global TotalSet2
    global TotalFailed



    if Question("resume") is False:
   
            print("\nSeekam files in:",Seek)

            try:
                filecnt = 0
                for camfile in Seeklst:
                      filecnt = filecnt + 1
                      sys.stdout.write("\r" + "Proceeding: "+str(filecnt)+"/"+str(NbrFilesToTest))
                      sys.stdout.flush()
                      Seekam(camfile)

            except Exception as e:
                 print(e)

            Move(ToMoveFile,ToMoveId,ToMoveBonus)



            ToMoveFile=[]
            ToMoveId=[]
            ToMoveBonus=[]

            print("\nEnd of Sorting Part 1 ... \n\n")
            print("The story so far :\n")
            print("Found " +str(Total_IpCam) +" Identified as from IpCam  .")
            print("Found " +str(TotalOther) +" Identified Random Pictures .")
            print("Found " +str(TotalCams) +" Identitied but NOT Sorted yet .")
            if TotalCams == 0:
                print("\nHaven't found any other   files to Sort.\n")
                print("\nExiting...")
                sys.exit(0)

            print("\n\nNow Attempting to sort Files....\n\n")
            TotalCams = 0
            TotalSet3 = 0
            TotalSet2 = 0
            TotalFailed = 0

            Hash2Test()

            Move(ToMoveFile,ToMoveId,ToMoveBonus)

            print("\n\nAll Done ! \n\n")


            print("The story so far :\n")
            print("Found " +str(TotalSet2) +" Identified as from Set1.")
            print("Found " +str(TotalSet3) +" Identified as from Set3 .")
            print("Found " +str(TotalFailed) +" Failed to be identidied.")

            Question("delete")


    else:


            ToMoveFile=[]
            ToMoveId=[]
            ToMoveBonus=[]

            print("\nSkipping Part 1 ... \n\n")
            print("\n\nNow Attempting to sort Files....\n\n")
            TotalCams = 0
            TotalSet3 = 0
            TotalSet2 = 0
            TotalFailed = 0
               

            Hash2Test()

            Move(ToMoveFile,ToMoveId,ToMoveBonus)

            print("\n\nAll Done ! \n\n")

            print("The story so far :\n")
            print("Found " +str(TotalSet2) +" Identified as from Set1.")
            print("Found " +str(TotalSet3) +" Identified as from Set3 .")
            print("Found " +str(TotalFailed) +" Failed to be identidied.")

            Question("delete")
            sys.exit(0)


###
###
if __name__ == '__main__':

    sys.setrecursionlimit(2323)
    #Seek ="./FAILED/Miss/"
    #Seek ="./FAILED/Miss"
    #Seek ="./FAILED/Mini"
    #Seek = "./Powerless"
    #Seek = "./FAILED/Slim"
#    Seek = "./FAILED/NewTest"
    Seek = "./FAILED/Fuck"
    #Seek = "./FAILED/Falseposif"
    if not Seek.endswith("/"):
         Seek = Seek+"/"
    Seeklst = iglob(Seek+"*")

    #Master = "./SurvCamArchive"
    Master = "./TestSurvCamArchive"
    Bogus = str(Master)+"/Failed/"
    UnknownCam = "./Datas/UnknownCam/"
    IpCam = str(Master)+"/SavedIpCam/"
    Set1 = str(Master)+"/SavedSet1/"
    Set3 = str(Master)+"/SavedSet3/"
    Picture = str(Master)+"/Other/"



    ToMoveFile=[]
    ToMoveId=[]
    ToMoveBonus=[]


    MotionExif=["Geometry: 640x480+0+0","Pixels: 307200","Compression: JPEG","Quality: 42","Units: Undefined","Orientation: Undefined","exif:ExifOffset: 50","Profile-exif: 146 bytes","jpeg:colorspace: 2"]
    IpCamExif=["Geometry: 1280x720+0+0","Pixels: 921600","Compression: JPEG","Quality: 80","Orientation: Undefined","Units: Undefined","jpeg:colorspace: 2"]
    BadExif=["Resolution:","Print size:","exif:ColorSpace:","exif:DateTimeDigitized:","exif:ExposureBiasValue:","exif:ExposureMode:","exif:ExposureTime:","exif:FocalLength:","exif:ImageDescription:","exif:Make:","exif:Model:","exif:Orientation:","exif:Software:","exif:thumbnail:","Profile-app"]


    if os.path.exists(str(UnknownCam)):
        NbrCamToTest = len(glob(UnknownCam+"*"))
        kamlst = iglob(UnknownCam+"*")


    TmpListSet3 = glob("./Datas/Templates/Set3/*")
    TmpListSet1 = glob("./Datas/Templates/Set1/*")
    TmpListSet2 = glob("./Datas/Templates/Set2/*")

    TmpSet1Nbr = len(glob("./Datas/Templates/Set1/*"))
    TmpSet2Nbr = len(glob("./Datas/Templates/Set2/*"))
    TmpSet3Nbr = len(glob("./Datas/Templates/Set3/*"))

    NbrFilesToTest = len(glob(Seek+"*"))



    TmpSet1Hash = []
    TmpSet1Phash = []
    TmpSet1Phashimple =[]
    TmpSet1Dhash = []
    TmpSet1Dhashv = []
    TmpSet1Wash = []

    TmpSet2Hash = []
    TmpSet2Phash = []
    TmpSet2Phashimple =[]
    TmpSet2Dhash = []
    TmpSet2Dhashv = []
    TmpSet2Wash = []



    TmpSet3Hash = []
    TmpSet3Phash = []
    TmpSet3Phashimple =[]
    TmpSet3Dhash = []         
    TmpSet3Dhashv = []
    TmpSet3Wash = []

    TemplatesLoaded = False
    UserLoaded = False

    TotalCams = 0
    TotalSet3 = 0
    TotalSet2 = 0
    Total_IpCam = 0
    TotalOther = 0
    TotalFailed = 0

    main()

####




