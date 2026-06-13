'''import cv2

facecascade = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
def extract_face(img):
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = facecascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(10,10))
    if len(faces) == 0:
        return None
    (x,y,w,h) = faces[0]
    return gray[y:y+w,x:x+h]
def features(img):
    orb = cv2.ORB_create()
    kp,descriptor = orb.detectAndCompute(img,None)
    return descriptor
def face_match(descriptor1,descriptor2):
    bf = cv2.BFMatcher(cv2.NORM_HAMMING,crossCheck=True)
    matches = bf.match(descriptor1,descriptor2)
    print(f"matches {matches}")




train_image = cv2.imread("IMG_20240210_131650.jpg")
test_image = cv2.imread("IMG_20240210_131650.jpg")
train_face = extract_face(train_image)
test_face = extract_face(test_image)

if train_face is not None and test_face is not None:
    train_features = features(train_face)
    test_features = features(test_face)
    if train_features is not None and test_features is not None:
        print(face_match(train_features, test_features))
        a = face_match(train_features,test_features)
        threshold = 3
        if threshold > a:
            print("face match")
        else:
            print("face not match")
    else:
        print("feature not match")
else:
    print("can't compute")'''
import cv2

facecascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

def extract_face(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = facecascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(10, 10))
    if len(faces) == 0:
        return None
    (x, y, w, h) = faces[0]
    return gray[y:y+h, x:x+w]

def features(img):
    orb = cv2.ORB_create()
    kp, descriptor = orb.detectAndCompute(img, None)
    return descriptor

def face_match(descriptor1, descriptor2):
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(descriptor1, descriptor2)
    return len(matches)

train_image = cv2.imread("0.jpg")
test_image = cv2.imread("0.jpg")

if train_image is None or test_image is None:
    print("Error loading images")
    exit(1)

train_face = extract_face(train_image)
test_face = extract_face(test_image)

print(f"Train face shape: {train_face.shape if train_face is not None else 'None'}")
print(f"Test face shape: {test_face.shape if test_face is not None else 'None'}")

if train_face is not None and test_face is not None:
    train_features = features(train_face)
    test_features = features(test_face)
    
    print(f"Train descriptors shape: {train_features.shape if train_features is not None else 'None'}")
    print(f"Test descriptors shape: {test_features.shape if test_features is not None else 'None'}")

    if train_features is not None and test_features is not None:
        num_matches = face_match(train_features, test_features)
        print(f"Number of matches: {num_matches}")
        threshold = 3
        if num_matches > threshold:
            print("Face match")
        else:
            print("Face not match")
    else:
        print("Feature extraction failed")
else:
    print("Face extraction failed")

