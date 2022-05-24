#! /usr/bin/env python3
import matplotlib.pyplot as plt


def plotImage(Image,Num):

    plt.imshow(Image)
    plt.show()
    
def plotAfterSLADSSimulation(Im1,Im2,Im3, suptitle=None):
        
    plt.figure(1, figsize=[15, 4], constrained_layout=True)
    plt.subplot(131)          
    plt.imshow(Im1)
    plt.title('Sampled Mask')
    plt.colorbar()
    plt.subplot(132)        
    plt.imshow(Im2)
    plt.title('Reconstructed Image')
    plt.colorbar()
    plt.subplot(133)   
    plt.imshow(Im3)
    plt.title('Ground-truth Image')
    plt.colorbar()
    if suptitle is not None:
        plt.suptitle(suptitle)
    plt.show()


def plotAfterSLADS(Im1,Im2, suptitle=None):
    plt.figure(1, figsize=[7, 3.2], constrained_layout=True, dpi=300)
    plt.subplot(121)          
    plt.imshow(Im1)
    plt.title('Sampled Mask')
    plt.colorbar()
    plt.subplot(122)        
    plt.imshow(Im2)
    plt.title('Reconstructed Image')
    plt.colorbar()
    if suptitle is not None:
        plt.suptitle(suptitle)
    plt.show()


