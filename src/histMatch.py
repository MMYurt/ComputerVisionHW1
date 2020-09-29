import numpy as np
import copy

def histMatch(source_image, target_image):
    source_image = copy.deepcopy(source_image)
    result_image = copy.deepcopy(source_image)
    
    for i in range(3):
        #Bin number is selected 255.
        source_histogram ,bin_edges = np.histogram(source_image[:,:,i].flatten(),255)   #Histogram creating for source image
        
        target_histogram,bin_edges = np.histogram(target_image[:,:,i].flatten(),255)    #Histogram creating for target image
    
        cumdistSource = source_histogram.cumsum() #Cumulative Distribution Function for histogram matching
        cumdistSource = (255 * cumdistSource / cumdistSource[-1]).astype(np.uint8) #Normalization
    
        cumdistTarget = target_histogram.cumsum() #Cumulative Distribution Function for histogram matching
        cumdistTarget = (255 * cumdistTarget / cumdistTarget[-1]).astype(np.uint8) #Normalization
    
    
        x = np.interp(source_image[:,:,i].flatten(),bin_edges[:-1],cumdistSource)     #interpolation      
        y = np.interp(x,cumdistTarget, bin_edges[:-1])                              #interpolation
    
        result_image[:,:,i] = y.reshape((source_image.shape[0],source_image.shape[1] ))
        
    return result_image