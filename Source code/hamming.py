from feature_vec import *


def hamming_check_string(str1, str2):

    '''
    Check the Hamming distance between two strings.

    Parameters
    ----------
    str1, str2: string
        The two input strings between which the Hamming 
        distance needs to be measured.

    Returns
    -------
    hamming_dist: integer
        The Hamming distance between the two strings.
    '''
    hamming_dist = 0
    for i in range(5):
        hamming_dist += int(str1[i] != str2[i])
    return hamming_dist
    

def same_person_eyes(fname1, fname2):
    #print("database iris=",fname1)
    #print("input iris=", fname2)

    '''
    Calculate the Hamming distance between all elements 
    of same indices for two faeature vectors and sum them up.
    Based on the sum of the Hamming distance calculated it is 
    determined the two images are for the same eye or not.

    Parameters
    ----------
    fname1, fname2: string
        The filenmaes of the images in string format.

    Returns
    -------
    *True* if the sum of Hamming distances==0
    (i.e. both images are for the same eye.)
    *False* if the sum of Hamming distances!=0
    (i.e. both images are for different eyes.)'''

    
    code1 = engroup(fname1)
    print("First Eye : ",fname1)
    code2 = engroup(fname2)
    print("Second Eye : ",fname2)
    hgroup1, vgroup1 = code1
    hgroup2, vgroup2 = code2
    hamming_dist = 0
    for row in range(1):

        for col in range(1):
            hamming_dist += hamming_check_string(hgroup1[row][col], hgroup2[row][col])
    for row in range(1):

        for col in range(1):
            hamming_dist += hamming_check_string(vgroup1[row][col], vgroup2[row][col])
    print("hamming_dist=",hamming_dist)
    return (hamming_dist==0)


'''verify=same_person_eyes("H://Python//VotingSystem_IRIS//venv//IRIS//TestImages//01_L.bmp","H://Python//VotingSystem_IRIS//venv//IRIS//TestImages//02_L.bmp")

if verify is True:
    print('Verified. The images belong to the same eye.')

else:
    print('Not verified. The images are of two different eyes.')'''