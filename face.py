import cv2
import mediapipe as mp
mp_face_detection = mp.solutions.face_detection
face = mp_face_detection.FaceDetection(model_selection=1, min_detection_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils

v = cv2.VideoCapture(0)
while True:
    # Capture the video frame
    # by frame
    _, video = v.read()
    results = face.process(cv2.cvtColor(video, cv2.COLOR_BGR2RGB))    
    if results.detections:
        for id, detection in enumerate(results.detections):
            #print(id,detection)
            # mp_drawing.draw_detection(video, detection)
            box = detection.location_data.relative_bounding_box
            h, w, c = video.shape
            print(h,w,c)
            print(box)
            bbox = int(box.xmin*w), int(box.ymin*h),int(box.width*w), int(box.height*h)
            cv2.rectangle(video, bbox, (255,255,255), 2)
    
    
    
    # Display the resulting frame
    cv2.imshow("vedio",video)
    # the 'p' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('p'):
        break
  
# After the loop release the cap object
v.release()
# Destroy all the windows
cv2.destroyAllWindows()
