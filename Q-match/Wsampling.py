import numpy as np


def subW( W, opt_X, fixed_Y, fixed_C ):
    # these are indicating the *not* fixed vertices
    Xlogical = np.ones(W.shape[0])
    Xlogical[opt_X] = 0
    Ylogical = np.ones(W.shape[1])
    Ylogical[fixed_Y] = 0

    # create subW as submatrix
    smallW = W[opt_X, fixed_Y, opt_X, fixed_Y]  # submatrix of W

    # add tailing values
    for i in opt_X:
        for k in fixed_Y:
            for j in opt_X:
                for l in fixed_Y:
                    smallW[i, k, j, l] = smallW[i, k, j, l] + W[i, k, Xlogical, Ylogical].sum() + W[Xlogical, Ylogical, j, l].sum()

    # return flat version
    return flattenW(smallW)


def flattenW( W ):
    n = np.shape(W)
    return np.reshape(W, (n[0] * n[1], n[2] * n[3]), 'C')



def subproblemW( C, samplingX, samplingY, geodesicsX, geodesicsY ):
    nX = len(samplingX)
    nY = len(samplingY)
    Xgeoflat = geodesicsX.ravel()
    Ygeoflat = geodesicsY.ravel()

    # remove entries from correspondence that include samplingX, samplingY
    correspondence = []
    for c in C:
        if not((samplingX == c[0]).sum() or (samplingY == c[1]).sum()):
            correspondence.append(c)
    correspondence = np.array(correspondence)

    subW = np.zeros([nX, nY, nX, nY])
    for i in range(nX):
        indI = samplingX[i]
        I_ravel_ind = np.ravel_multi_index(np.array([indI * np.ones(len(correspondence)), correspondence[:, 0]]).astype(int), (len(geodesicsX), len(geodesicsY)))
        for k in range(nY):
            indK = samplingY[k]
            K_ravel_ind = np.ravel_multi_index(np.array([indK * np.ones(len(correspondence)), correspondence[:, 1]]).astype(int), (len(geodesicsX), len(geodesicsY)))
            for j in range(nX):
                indJ = samplingX[j]
                J_ravel_ind = np.ravel_multi_index(np.array([indJ * np.ones(len(correspondence)), correspondence[:, 0]]).astype(int), (len(geodesicsX), len(geodesicsY)))
                for l in range(nY):
                    indL = samplingY[l]
                    L_ravel_ind = np.ravel_multi_index(np.array([indL * np.ones(len(correspondence)), correspondence[:, 1]]).astype(int), (len(geodesicsX), len(geodesicsY)))
                    subW[i, k, j, l] = np.abs(geodesicsX[indI, indJ] - geodesicsY[indK, indL])
                    subW[i, k, j, l] += np.abs(Xgeoflat[I_ravel_ind] - Ygeoflat[K_ravel_ind]).sum() + np.abs(Xgeoflat[J_ravel_ind] - Ygeoflat[L_ravel_ind]).sum()
  
    return subW

