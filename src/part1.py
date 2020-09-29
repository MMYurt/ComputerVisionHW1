import cv2
import glob


images_walking = [cv2.imread(file) for file in sorted(glob.glob("./DAVIS-JPEGImages/JPEGImages/walking/*.jpg"))]
images_disc_jockey = [cv2.imread(file) for file in sorted(glob.glob("./DAVIS-JPEGImages/JPEGImages/disc-jockey/*.jpg"))]
images_night_race = [cv2.imread(file) for file in sorted(glob.glob("./DAVIS-JPEGImages/JPEGImages/night-race/*.jpg"))]


images_seg_walking = [cv2.imread(file, cv2.IMREAD_GRAYSCALE) for file in sorted(glob.glob("./DAVIS-JPEGImages/Annotations/walking/*.png"))]
images_seg_disc_jockey = [cv2.imread(file, cv2.IMREAD_GRAYSCALE) for file in sorted(glob.glob("./DAVIS-JPEGImages/Annotations/disc-jockey/*.png"))]
images_seg_night_race = [cv2.imread(file, cv2.IMREAD_GRAYSCALE) for file in sorted(glob.glob("./DAVIS-JPEGImages/Annotations/night-race/*.png"))]



for i in range(len(images_walking)):                                        #Resize for images and annotations
    images_walking[i] = cv2.resize(images_walking[i], (960,540))            #and make true which have seg id=38
    images_seg_walking[i] = cv2.resize(images_seg_walking[i], (960,540))
    images_seg_walking[i] = (images_seg_walking[i] == 38)


for k in range(len(images_walking)):

    for i in range(len(images_walking[k])):
        for j in range(len(images_walking[k][i])):
            
            if(images_seg_walking[k][i][j]) == True:                        #Segmented pixels red and green channels decreased by %75
                
                images_walking[k][i][j][1] /= 4
                images_walking[k][i][j][2] /= 4
                
for i in range(len(images_disc_jockey)):
    images_disc_jockey[i] = cv2.resize(images_disc_jockey[i], (960,540))
    images_seg_disc_jockey[i] = cv2.resize(images_seg_disc_jockey[i], (960,540))
    images_seg_disc_jockey[i] = (images_seg_disc_jockey[i] == 38)


for k in range(len(images_disc_jockey)):

    for i in range(len(images_disc_jockey[k])):
        for j in range(len(images_disc_jockey[k][i])):
            
            if(images_seg_disc_jockey[k][i][j]) == True:
                
                images_disc_jockey[k][i][j][1] /= 4
                images_disc_jockey[k][i][j][2] /= 4  
                
for i in range(len(images_night_race)):
    images_night_race[i] = cv2.resize(images_night_race[i], (960,540))
    images_seg_night_race[i] = cv2.resize(images_seg_night_race[i], (960,540))
    images_seg_night_race[i] = (images_seg_night_race[i] == 38)


for k in range(len(images_night_race)):

    for i in range(len(images_night_race[k])):
        for j in range(len(images_night_race[k][i])):
            
            if(images_seg_night_race[k][i][j]) == True:
                
                images_night_race[k][i][j][1] /= 4
                images_night_race[k][i][j][2] /= 4                


out = cv2.VideoWriter('part1_video_walking.mp4', 0x00000021, 25.0, (960,540))           #Video writing. In this func, binary number is MP4 Codec.

for i in range(len(images_walking)):
    out.write(images_walking[i])
out.release()

out = cv2.VideoWriter('part1_video_disc_jockey.mp4', 0x00000021, 25.0, (960,540))

for i in range(len(images_disc_jockey)):
    out.write(images_disc_jockey[i])
out.release()

out = cv2.VideoWriter('part1_video_night_race.mp4', 0x00000021, 25.0, (960,540))

for i in range(len(images_night_race)):
    out.write(images_night_race[i])
out.release()

