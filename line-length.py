import cv2 as cv
import numpy as np
import math

p=0

def dist(a2,b2,a1,b1):
	d = math.sqrt((a2-a1)**2 + (b2-b1)**2)
	return d

def length(event,x,y,flags,param):
	global p,d,x1,y1,x2,y2,x3,y3,x4,y4,r1,l,ac1,bd1,bc1,ad1

	if event == cv.EVENT_LBUTTONDOWN:
		if p==0:
			x1,y1 = x,y
			print ('x1 = %d, y1 = %d' %(x1,y1))
		elif p==1:
			x3,y3 = x,y
			print ('x3 = %d, y3 = %d' %(x3,y3))

		elif p==2:
			ac1 = dist(x3,y3,x1,y1)
			print ("A'C' = %d" % ac1)

			ad1 = dist(x4,y4,x1,y1)
			print ("A'D' = %d" % ad1)

			bc1 = dist(x3,y3,x2,y2)
			print ("B'C' = %d" % bc1)

			bd1 = dist(x4,y4,x2,y2)
			print ("B'D' = %d" % bd1)

			r1 = ((ac1 * bd1)/(bc1 * ad1))
			l = ((1 - r1)*50/(5*r1 - 10))
			l = l/100
			#l = ((1 - r1)*1800/(30*r1 - 60))
			print r1
			print "Length of the remaining portion = %f cm." % l
			p = 0

	elif event == cv.EVENT_LBUTTONUP:
		if p==0:
			p = 1
			x2,y2 = x,y
			print ('x2 = %d, y2 = %d' %(x2,y2))
		elif p==1:
			x4,y4 = x,y
			print ('x4 = %d, y4 = %d' %(x4,y4))
			p = 2


#	return d

img = cv.imread('Calibe32.jpg')
cv.namedWindow('Image')
cv.setMouseCallback('Image',length)

while(1):
	cv.imshow('Image',img)

	k = cv.waitKey(10) & 0xFF
	if k == ord('q'):
		cv.destroyAllWindows()
		break

