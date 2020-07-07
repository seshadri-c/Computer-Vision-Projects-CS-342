import os
import cv2

path = "/home/seshadri_c/Image_localization/data/KITTI_sample/images/"
img_addr = os.listdir(path)
img_addr.sort()
img_list = []
for i in img_addr:
	img = cv2.imread(path + i)
	img_list.append(img)

def write_video(img_list, path = "/home/seshadri_c/kitti.avi"):

	height, width, layers = img_list[0].shape
	size = (width, height)
	out = cv2.VideoWriter(path, cv2.VideoWriter_fourcc(*'DIVX'), 8, size)
	for i in range(len(img_list)):
		out.write(img_list[i])
	out.release()

write_video(img_list)