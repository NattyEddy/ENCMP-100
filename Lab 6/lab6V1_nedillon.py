## CORONASIMULATE  Simulate coronagraph and Gerchberg-Saxton algorithm
#
# A simulation of a coronagraph and the Gerchberg-Saxton algorithm, in the
# context of NASA's Roman Space Telescope, developed to help teach ENCMP
# 100 Computer Programming for Engineers at the University of Alberta. The
# program saves output figures to PNG files for subsequent processing.
#
# Copyright (c) 2022, University of Alberta
# Electrical and Computer Engineering
# All rights reserved.
#
# Student name: Nathan Edillon 95%
# Student CCID: nedillon
# Others: GOLDEN 2%, TOPGUN 3%
#
# To avoid plagiarism, list the names of persons, Version 0 author(s)
# excluded, whose code, words, ideas, or data you used. To avoid
# cheating, list the names of persons, excluding the ENCMP 100 lab
# instructor and TAs, who gave you compositional assistance.
#
# After each name, including your own name, enter in parentheses an
# estimate of the person's contributions in percent. Without these
# numbers, adding to 100%, follow-up questions will be asked.
#
# For anonymous sources, enter pseudonyms in uppercase, e.g., SAURON,
# followed by percentages as above. Email a link to or a copy of the
# source to the lab instructor before the assignment is due.
#
import matplotlib.pyplot as plt
import numpy as np

def main():
    im = loadImage('300_26a_big-vlt-s.jpg')
    (im,Dphi) = opticalSystem(im,300)
    images = gerchbergSaxton(im,10,Dphi)
    saveFrames(images)

def loadImage(name):
    im = plt.imread(name)/255
    if len(im.shape) > 2:
        im = (im[:,:,0]+im[:,:,1]+im[:,:,2])/3
    im[im < 0] = 0
    im[im > 1] = 1
    return im

def opticalSystem(im,width):
    im = occultSquare(im,width)
    (IMa,IMp) = dft2(im)
    rng = np.random.default_rng(12345)
    imR = rng.random(im.shape)
    (_,Dphi) = dft2(imR)
    im = idft2(IMa,IMp-Dphi)
    return (im,Dphi)

## Occult Square
#  @param im - image data
#  @param width - desired width of square
#  take an image and place a square of desired width in the center
def occultSquare(im,width):
    im[im.shape[0]//2 - width//2 : im.shape[0]//2 + width//2,
       im.shape[1]//2 - width//2 : im.shape[1]//2 + width//2] = 0
    return im

# (IMa,IMp) = dft2(im) returns the amplitude, IMa, and phase, IMp, of the
# 2D discrete Fourier transform of a grayscale image, im. The image, a 2D
# array, must have entries between 0 and 1. The phase is in radians.
def dft2(im):
    IM = np.fft.rfft2(im)
    IMa = np.abs(IM)
    IMp = np.angle(IM)
    return (IMa,IMp)

# im = idft2(IMa,IMp) returns a grayscale image, im, with entries between
# 0 and 1 that is the inverse 2D discrete Fourier transform (DFT) of a 2D
# DFT specified by its amplitude, IMa, and phase, IMp, in radians.
def idft2(IMa,IMp):
    IM = IMa*(np.cos(IMp)+1j*np.sin(IMp))
    im = np.fft.irfft2(IM)
    im[im < 0] = 0
    im[im > 1] = 1
    return im

## Gerchberg Saxton Algorithm
#  @param im - image data
#  @param maxIters - the amount of iterations to create
#  @param Dphi - phase aberration in the pupil plane of the coronagraph
#  does some math to simulate the GS algorithm, creating a set of images
#  of a desired amount of iterations
def gerchbergSaxton(im,maxIters,Dphi):
    (IMa,IMp) = dft2(im)
    images = []
    for k in range(maxIters+1):
        print("Iteration %d of %d" % (k,maxIters))
        im = idft2(IMa,IMp+(k/maxIters*Dphi))
        images.append(im)
    return images

## Save Frames
#  @param images - data of a set of images
#  takes data that forms images to form black and white photos, shows each
#  iteration of the photos in succession, and saves them as "coronograph"
#  .png files
def saveFrames(images):
    shape = (images[0].shape[0],images[0].shape[1],3)
    image = np.zeros(shape,images[0].dtype)
    maxIters = len(images)-1
    for k in range(maxIters+1):
        image[:,:,0] = images[k]
        image[:,:,1] = images[k]
        image[:,:,2] = images[k]
        plt.imshow(image)
        plt.axis('off')
        plt.title("Iteration %i of %i" % (k, maxIters))
        plt.savefig('coronagraph'+str(k)+'.png')
        plt.show()

main()
