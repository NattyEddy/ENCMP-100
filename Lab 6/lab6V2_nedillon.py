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
# Student name: Nathan Edillon 92%
# Student CCID: nedillon
# Others: GOLDEN 5%, TOPGUN 3%
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
    (im,Dphi,mask) = opticalSystem(im,300)
    (images,errors) = gerchbergSaxton(im,10,Dphi,mask)
    saveFrames(images,errors)

## Load Image
#  @param name - name of image
#  @return im - pixel data of image
#  reads an image file and converts into raw pixel data
def loadImage(name):
    im = plt.imread(name)/255
    if len(im.shape) > 2:
        im = (im[:,:,0]+im[:,:,1]+im[:,:,2])/3
    im[im < 0] = 0
    im[im > 1] = 1
    return im

## Optical System
#  @param im - image data
#  @param diameter - desired diameter of circle
#  @return im - altered image data
#  @return Dphi - phase aberration in the pupil plane of the coronagraph
#  @return mask - pixels masked by the circle
#  places a circle in the original photo data and performs some Fourier
#  transformation
def opticalSystem(im,diameter):
    (im, mask) = occultCircle(im,diameter)
    (IMa,IMp) = dft2(im)
    rng = np.random.default_rng(12345)
    imR = rng.random(im.shape)
    (_,Dphi) = dft2(imR)
    im = idft2(IMa,IMp-Dphi)
    return (im,Dphi,mask)

## Occult Circle
#  @param im - image data
#  @param diameter - desired diameter of circle
#  @return im - altered image data
#  @return mask - data of pixels altered with the black circle (boolean)
#  take an image and place a black circle of desired diameter in the center
def occultCircle(im,diameter):
    mask = np.full(im.shape, False, dtype = bool)
    radius = diameter // 2
    xCenter = im.shape[0] // 2
    yCenter = im.shape[1] // 2
    for x in range(xCenter - radius, xCenter + radius):    
        for y in range(yCenter - radius, yCenter + radius):
            if np.sqrt((x - xCenter)**2 + (y - yCenter)**2) <= radius:
                im[x, y] = 0
                mask[x, y] = True
    return (im, mask)

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

## Occult Error
#  @param im - image data
#  @param mask - masked pixel data
#  @return error - sum of squared data of masked pixels
#  the error is the sum of all squared values of masked pixels
def occultError(im,mask):
    error = np.sum(im[mask]**2)
    return error

## Gerchberg Saxton Algorithm
#  @param im - image data
#  @param maxIters - the amount of iterations to create
#  @param Dphi - phase aberration in the pupil plane of the coronagraph
#  @param mask - masked pixel data
#  @return images - image data post-algorithm
#  @return errors - data of mask error
#  does some math to simulate the GS algorithm, creating a set of images of
#  a desired amount of iterations, printing its progression in the console
def gerchbergSaxton(im,maxIters,Dphi,mask):
    (IMa,IMp) = dft2(im)
    images = []
    errors = []
    for k in range(maxIters+1):
        print("Iteration %d of %d" % (k,maxIters))
        im = idft2(IMa,IMp+(k/maxIters*Dphi))
        images.append(im)
        errors.append(occultError(im,mask))       
    return (images,errors)

## Save Frames
#  @param images - data of a set of images
#  @param errors - masked error data
#  takes data that forms black and white images to simulate a coronagraph, 
#  graphs error data per iteration on top of the simulation and saves them 
#  as "coronograph" .png files
def saveFrames(images,errors):
    shape = (images[0].shape[0],images[0].shape[1],3)
    image = np.zeros(shape,images[0].dtype)
    maxIters = len(images)-1
    iterations = []
    sumError = []
    maxError = max(errors)
    for k in range(maxIters+1):
        image[:,:,0] = images[k]
        image[:,:,1] = images[k]
        image[:,:,2] = images[k]
        iterations.append(k)
        sumError.append(errors[k])
        plt.xlabel("Iteration")
        plt.ylabel("Sum Square Error")
        plt.xlim(0, maxIters)
        plt.ylim(0, maxError)
        plt.plot(iterations, sumError, "r-")
        plt.imshow(image, extent = (0, maxIters, 0, maxError))
        plt.gca().set_aspect(maxIters/maxError)
        plt.title("Coronagraph Simulation")
        plt.savefig('coronagraph'+str(k)+'.png')
        plt.show()

main()
