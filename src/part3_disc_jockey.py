import cv2
import glob
import copy

from histMatch import histMatch

images_original = [cv2.imread(file) for file in sorted(glob.glob("./DAVIS-JPEGImages/JPEGImages/disc-jockey/*.jpg"))]

images_seg_original = [cv2.imread(file, cv2.IMREAD_GRAYSCALE) for file in sorted(glob.glob("./DAVIS-JPEGImages/Annotations/disc-jockey/*.png"))]

target = cv2.imread("./target3.jpg")

target2 = cv2.imread("./target2.jpeg")

target3 = cv2.imread("./target.jpg")

images_seg = copy.deepcopy(images_seg_original)

for i in range(len(images_original)):
    images_seg[i] = cv2.resize(images_seg[i], (960,540))
    images_original[i] = cv2.resize(images_original[i], (960,540))
  

images = copy.deepcopy(images_original)
images_matched_guy1 = copy.deepcopy(images_original)
images_matched_guy2 = copy.deepcopy(images_original)
images_matched_background = copy.deepcopy(images_original)
total_matched = copy.deepcopy(images_original)


for k in range(len(images_original)):
    for i in range(len(images_original[k])):                         #Segmentation for guy1
        for j in range(len(images_original[k][i])):
            
            if(images_seg[k][i][j]) != 38:
                images[k][i][j][0] = 0
                images[k][i][j][1] = 0
                images[k][i][j][2] = 0
    
           
    
    images_matched_guy1[k] = histMatch(images[k], target)         #Histogram matching for guy1
        
    
    
    for i in range(len(images_matched_guy1[k])):                  #Background correction
        for j in range(len(images_matched_guy1[k][i])):
            
            if(images_seg[k][i][j]) != 38:
                images_matched_guy1[k][i][j][0] = 0            
                images_matched_guy1[k][i][j][1] = 0
                images_matched_guy1[k][i][j][2] = 0
                
    images = copy.deepcopy(images_original)
       
    
        
    for i in range(len(images[k])):                         #Segmentation for guy2
        for j in range(len(images[k][i])):
            
            if(images_seg[k][i][j]) != 75:
                images[k][i][j][0] = 0
                images[k][i][j][1] = 0
                images[k][i][j][2] = 0
    
    
    images_matched_guy2[k] = histMatch(images[k], target2)   #histogram matching for guy2        
    
    for i in range(len(images_matched_guy2[k])):                  #Background correction
        for j in range(len(images_matched_guy2[k][i])):
            
            if(images_seg[k][i][j]) != 75:
                images_matched_guy2[k][i][j][0] = 0            
                images_matched_guy2[k][i][j][1] = 0
                images_matched_guy2[k][i][j][2] = 0
                
    
    
    images = copy.deepcopy(images_original)
    
    
        
    for i in range(len(images[k])):                         #Segmentation for background
        for j in range(len(images[k][i])):
            
            if(images_seg[k][i][j] == 75 or images_seg[k][i][j] == 38):
                images[k][i][j][0] = 0
                images[k][i][j][1] = 0
                images[k][i][j][2] = 0
                
    
    images_matched_background[k] = histMatch(images[k], target3)
    
    
    
    for i in range(len(images_matched_background[k])):                  #Background correction
        for j in range(len(images_matched_background[k][i])):
            
            if(images_seg[k][i][j] == 75 or images_seg[k][i][j] == 38):
                images_matched_background[k][i][j][0] = 0            
                images_matched_background[k][i][j][1] = 0
                images_matched_background[k][i][j][2] = 0
                
    total_matched[k] = images_matched_guy2[k] + images_matched_guy1[k] + images_matched_background[k] 


out = cv2.VideoWriter('part3_video_disc_jockey.mp4', 0x00000021, 25.0, (960,540))

for i in range(len(total_matched)):
    out.write(total_matched[i])
out.release()

