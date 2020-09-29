import cv2
import glob

from histMatch import histMatch

images_walking = [cv2.imread(file) for file in sorted(glob.glob("./DAVIS-JPEGImages/JPEGImages/walking/*.jpg"))]
images_disc_jockey = [cv2.imread(file) for file in sorted(glob.glob("./DAVIS-JPEGImages/JPEGImages/disc-jockey/*.jpg"))]
images_night_race = [cv2.imread(file) for file in sorted(glob.glob("./DAVIS-JPEGImages/JPEGImages/night-race/*.jpg"))]

target = cv2.imread("target.jpg")

for i in range(len(images_walking)):                                        #Image resizing for 3 image sequences
    images_walking[i] = cv2.resize(images_walking[i], (960,540))
    
for i in range(len(images_disc_jockey)):
    images_disc_jockey[i] = cv2.resize(images_disc_jockey[i], (960,540))
    
for i in range(len(images_night_race)):
    images_night_race[i] = cv2.resize(images_night_race[i], (960,540)) 
    
    
    
    
for i in range(len(images_walking)):                                        #And histogram matching for 3 image sequences
    images_walking[i] = histMatch(images_walking[i], target)
    
for i in range(len(images_disc_jockey)):
    images_disc_jockey[i] = histMatch(images_disc_jockey[i], target)
 
for i in range(len(images_night_race)):
    images_night_race[i] = histMatch(images_night_race[i], target)    



out = cv2.VideoWriter('part2_video_walking.mp4', 0x00000021, 25.0, (960,540))

for i in range(len(images_walking)):
    out.write(images_walking[i])
out.release()


out = cv2.VideoWriter('part2_video_disc_jockey.mp4', 0x00000021, 25.0, (960,540))

for i in range(len(images_disc_jockey)):
    out.write(images_disc_jockey[i])
out.release()


out = cv2.VideoWriter('part2_video_night_race.mp4', 0x00000021, 25.0, (960,540))

for i in range(len(images_night_race)):
    out.write(images_night_race[i])
out.release()
    

    
