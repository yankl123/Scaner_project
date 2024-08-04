import cv2
import numpy as np 

def calculate_blur(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    laplacian_var = cv2.Laplacian(gray, cv2.CV_64F).var()
    return laplacian_var

def select_best_image(images):
    best_image = None
    max_blur = 0
    for image in images:
        blur = calculate_blur(image)
        if blur > max_blur:
            max_blur = blur
            best_image = image
    return best_image


def detect_complete_frame(img, min_area) :

	# converting image into grayscale image 
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

	# setting threshold of gray image 
	_, threshold = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY) 

	# using a findContours() function 
	contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 
	
	#filter the contours to find the bigest frame 
	fcontours = [cnt for cnt in contours if cv2.contourArea(cnt) >= min_area]

	if len(fcontours) > 1 :

		approx = cv2.approxPolyDP( 
			fcontours[1], 0.01 * cv2.arcLength(fcontours[1], True), True) 
			
		if len(approx) == 4 :
			return True
	else :
		return False 


def find_shape_in_corners(img, cornerSize, shape, minSize) :

	h = img.shape[0]
	w = img.shape[1]

	corners = [img[0:cornerSize, 0:cornerSize], img[0:cornerSize, w-cornerSize:w-1],
           img[h-cornerSize:h-1,0:cornerSize],img[h-cornerSize:h-1,w-cornerSize:w-1]]
	count = 0
	
	for i in range(0,4) :
	
		gray = cv2.cvtColor(corners[i], cv2.COLOR_BGR2GRAY)

		blurred = cv2.GaussianBlur(gray, (5, 5), 0)
		
		edges = cv2.Canny(blurred, 80, 150)

		contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

		fcontours = [cnt for cnt in contours if cv2.contourArea(cnt) > minSize]
		
		for cont in fcontours :
			# Approximate the contour to a polygon
			epsilon = 0.02 * cv2.arcLength(cont, True)
			approx = cv2.approxPolyDP(cont, epsilon, True)
			# If the polygon has 4 vertices, it is a quadrilateral
			
			if len(approx) > shape :
				count+=1
    
	return True if count == 4 else False