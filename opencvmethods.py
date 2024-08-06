import numpy as np
import cv2
import math
#cap = cv2.VideoCapture(0)
#print(cap.isOpened())
#colorofblock = "empty"
#image_path = "C:\\Users\\sriva\\Downloads\\1000_F_506725496_kvJPVTdPAdmjHO6b9TOkHzm3Zqn5cILX.jpg"
#file_path = 'C:\\Users\\sriva\\Downloads\\IMG_1487 (1).jpg'
#path = "C:\\Users\\sriva\\Downloads\\b0425646-409b-480a-82da-db8f987658f6.png"
#image_path = "C:\\Users\\sriva\\Downloads\\download.jpg"
#image_path = r"C:\Users\sriva\Downloads\Green_equilateral_triangle_point_up.svg.png"
#frame = cv2.imread(image_path)

#works well for all shapes other than triangles
def find_yellow_block(cap):
    
    print(cap.isOpened())
    colorofblock = "empty"
    coordinates = None
    while True:

    # Capture frame-by-frame
        
        ret, frame = cap.read()

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lower_yellow = np.array([20, 100, 100])
        upper_yellow = np.array([30, 255, 255])
        maskmask = cv2.inRange(hsv, lower_yellow, upper_yellow)

        contours, _ = cv2.findContours(maskmask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        if contours:
            largest_contour = max(contours, key=cv2.contourArea)
            mask = np.zeros_like(maskmask)
            cv2.drawContours(mask, [largest_contour], -1, 255, thickness=cv2.FILLED)
            corners = cv2.goodFeaturesToTrack(mask, 100, 0.2, 4)

            result = cv2.bitwise_and(frame, frame, mask=mask)
        
        if corners is not None:
            corners = corners.astype(int)
            if len(corners) > 1:  # Ensure there are at least two corners
                for count, corner in enumerate(corners, start=1):
                    x,y = corner.ravel()
                    cv2.circle(result, (x,y), 5, (0,0,255), -1)
                    label = f"Corner {count}"
                    cv2.putText(result, label, (x + 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1, cv2.LINE_AA)
                    #print(f"Corner {count}: (x: {x}, y: {y})")  # Print each corner's coordinates

            max_distance = 0
            corner_one = None
            corner_two = None
            coordinateone = None
            coordinatetwo = None
            
            # Find the pair of corners with the maximum distance between them
            for i in range(len(corners) - 1):
                for j in range(i + 1, len(corners)):
                    corner_one = corners[i, 0]  # Extract the coordinates
                    corner_two = corners[j, 0]  # Extract the coordinates
                    distance = math.sqrt((corner_two[0] - corner_one[0])**2 + (corner_two[1] - corner_one[1])**2)
                    if distance > max_distance:
                        max_distance = distance
                        coordinateone = corner_one
                        coordinatetwo = corner_two

            if coordinateone is not None and coordinatetwo is not None:
            # Compute the midpoint of this pair
                center_x = int((coordinateone[0] + coordinatetwo[0]) / 2)
                center_y = int((coordinateone[1] + coordinatetwo[1]) / 2)
                coordinates = (center_x, center_y)
                cv2.circle(result, (center_x, center_y), 5, (0, 255, 0), -1)

        cv2.imshow('frame', result)
        cv2.imshow('mask', mask)
        #cv2.imshow('frame', frame)

        white_pixel_count = cv2.countNonZero(mask)
        

        if(cv2.countNonZero(mask) > 1000):
            colorofblock = "yellow"

        if(white_pixel_count < 1000):
            colorofblock = "empty"
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            
            return colorofblock,coordinates

#works for all shapes other than triangles
def find_green_block(cap):
    colorofblock = "empty"
    coordinates = None
    print(cap.isOpened())

    while True:
    # Capture frame-by-frame
        ret, frame = cap.read()

        
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lower_green = np.array([35, 100, 100])
        upper_green = np.array([85, 255, 255])
        maskmask = cv2.inRange(hsv, lower_green, upper_green)
        contours, _ = cv2.findContours(maskmask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        corners = None
        
        if contours:
            largest_contour = max(contours, key=cv2.contourArea)
            mask = np.zeros_like(maskmask)
            cv2.drawContours(mask, [largest_contour], -1, 255, thickness=cv2.FILLED)
            corners = cv2.goodFeaturesToTrack(mask, 100, 0.2, 4) #edit the amt of corners as needed

            result = cv2.bitwise_and(frame, frame, mask=mask)
        
        if corners is not None:
            corners = corners.astype(int)
            if len(corners) > 1:  # Ensure there are at least two corners
                for count, corner in enumerate(corners, start=1):
                    x,y = corner.ravel()
                    cv2.circle(result, (x,y), 5, (0,0,255), -1)
                    label = f"Corner {count}"
                    cv2.putText(result, label, (x + 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1, cv2.LINE_AA)
                    #comment or uncomment the 3 above lines of code as needed
                    #print(f"Corner {count}: (x: {x}, y: {y})")  # Print each corner's coordinates"""

            max_distance = 0
            corner_one = None
            corner_two = None
            coordinateone = None
            coordinatetwo = None
            
    
            # Find the pair of corners with the maximum distance between them
            for i in range(len(corners) - 1):
                for j in range(i + 1, len(corners)):
                    corner_one = corners[i, 0]  # Extract the coordinates
                    corner_two = corners[j, 0]  # Extract the coordinates
                    distance = math.sqrt((corner_two[0] - corner_one[0])**2 + (corner_two[1] - corner_one[1])**2)
                    if distance > max_distance:
                        max_distance = distance
                        coordinateone = corner_one
                        coordinatetwo = corner_two

            if coordinateone is not None and coordinatetwo is not None:
            # Compute the midpoint of this pair
                center_x = int((coordinateone[0] + coordinatetwo[0]) / 2)
                center_y = int((coordinateone[1] + coordinatetwo[1]) / 2)
                coordinates = (center_x, center_y)
                cv2.circle(result, (center_x, center_y), 5, (0, 255, 0), -1)
        
        cv2.imshow('frame', result)
        cv2.imshow('mask', mask)
        #cv2.imshow('camera', frame)
        
        white_pixel_count = cv2.countNonZero(mask)

        if(white_pixel_count > 1000):
            colorofblock = "green"
        
        if(white_pixel_count < 1000):
            colorofblock = "empty"

        if cv2.waitKey(1) & 0xFF == ord('q'):
            
            return colorofblock, coordinates
"""
def findcenter_block():
    maxdistance = 0
    distance = 0
    distance1 = 0
    coordinateone=0
    coordinatetwo=0
    max_distance = 0
    colorofblock = "empty"
    #print(cap.isOpened())

    while True:
        #ret, frame = cap.read()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lower_green = np.array([35, 100, 100])
        upper_green = np.array([85, 255, 255])
        mask = cv2.inRange(hsv, lower_green, upper_green)
        result = cv2.bitwise_and(frame, frame, mask=mask)
    #corners = cv2.goodFeaturesToTrack(mask, 4, 0.2, 4)
    # Find the coordinates where the mask is white (255)
        coordinates = np.column_stack(np.where(mask == 255))
        coordinates = coordinates.astype(int)
        for i in range(len(coordinates) - 1):
            for j in range(i + 1, len(coordinates)):
                corner_one = coordinates[i]  # Extract the coordinates
                corner_two = coordinates[j]  # Extract the coordinates
                distance = math.sqrt((corner_two[0] - corner_one[0])**2 + (corner_two[1] - corner_one[1])**2)
                if distance > max_distance:
                    max_distance = distance
                    coordinateone = corner_one
                    coordinatetwo = corner_two
    
        if coordinateone is not None and coordinatetwo is not None:
            # Compute the midpoint of this pair
                center_x = int((coordinateone[0] + coordinatetwo[0]) / 2)
                center_y = int((coordinateone[1] + coordinatetwo[1]) / 2)
                coordinates = (center_x, center_y)
                cv2.circle(result, (center_x, center_y), 5, (0, 255, 0), -1)
                #cv2.line(result, coordinateone, coordinatetwo, [0,0,255], thickness = 2)
        
        cv2.imshow('frame', result)
        cv2.imshow('mask', mask)
    """
#works universally for all shapes but this is less accurate... for dobot better to use previous two
def find_center_block_green(cap):
    colorofblock = "empty"
    sumX = 0
    sumY = 0
    centerX = None
    centerY = None
    while True:
        ret, frame = cap.read()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lower_green = np.array([35, 100, 100])
        upper_green = np.array([85, 255, 255])
        maskmask = cv2.inRange(hsv, lower_green, upper_green)
        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #_, maskmask = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
        contours, hierarchy = cv2.findContours(maskmask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        mask = np.zeros_like(maskmask)
        #result = cv2.bitwise_and(frame, frame, mask=mask)
        if contours:
            largest_contour = max(contours, key=cv2.contourArea)
            mask = np.zeros_like(maskmask)
            cv2.drawContours(mask, [largest_contour], -1, 255, thickness = cv2.FILLED)
            coordinates = np.column_stack(np.where(mask == 255))
            coordinates = coordinates.astype(int)
            numpoints = len(coordinates)

            if numpoints != 0:

                sumX = np.sum(coordinates[:, 0])
                sumY = np.sum(coordinates[:, 1])
        
                centerX = (1/numpoints) * sumX
                centerY = (1/numpoints) * sumY
                centerX = int(centerX)
                centerY = int(centerY)

                cv2.circle(frame, (centerX, centerY), 5, (0, 0, 255), -1)
        
        white_pixel_count = cv2.countNonZero(mask)

        if(white_pixel_count > 1000):
            colorofblock = "green"
        
        if(white_pixel_count < 200):
            colorofblock = "empty"
        
        cv2.imshow('frame', frame)
        cv2.imshow('mask', mask)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            return (centerX, centerY), colorofblock
        
#works universally for all shapes but this is less accurate... for dobot better to use previous two
def find_center_block_yellow(cap):
    sumX = 0
    sumY = 0
    centerX = None
    centerY = None
    while True:
        ret, frame = cap.read()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lower_yellow = np.array([20, 100, 100])
        upper_yellow = np.array([30, 255, 255])
        maskmask = cv2.inRange(hsv, lower_yellow, upper_yellow)
        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #_, maskmask = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
        contours, hierarchy = cv2.findContours(maskmask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        mask = np.zeros_like(maskmask)
        #result = cv2.bitwise_and(frame, frame, mask=mask)
        if contours:
            largest_contour = max(contours, key=cv2.contourArea)
            mask = np.zeros_like(maskmask)
            cv2.drawContours(mask, [largest_contour], -1, 255, thickness = cv2.FILLED)
            coordinates = np.column_stack(np.where(mask == 255))
            coordinates = coordinates.astype(int)
            numpoints = len(coordinates)

            if numpoints != 0:

                sumX = np.sum(coordinates[:, 0])
                sumY = np.sum(coordinates[:, 1])
        
                centerX = (1/numpoints) * sumX
                centerY = (1/numpoints) * sumY
                centerX = int(centerX)
                centerY = int(centerY)

                cv2.circle(frame, (centerX, centerY), 5, (0, 0, 255), -1)
        
        white_pixel_count = cv2.countNonZero(mask)

        if(white_pixel_count > 1000):
            colorofblock = "yellow"
        
        if(white_pixel_count < 1000):
            colorofblock = "empty"
        
        cv2.imshow('frame', frame)
        cv2.imshow('mask', mask)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            return (centerX, centerY), colorofblock
    

# Call the function
#result = find_yellow_block(cap)
#print(result)
#result1 = find_green_block()
#print(result1)
# Release the camera and close OpenCV windows"""
#result2 = find_center_block()
#result = find_center_block_green()
#print(result)
#cap.release()
#cv2.destroyAllWindows()