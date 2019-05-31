import cv2, requests, sys


# Gets an image from the webcam
def returnWC_Pic():
    cam = cv2.VideoCapture(0)
    try:
        ok, image = cam.read()
        if ok != True:
            raise ValueError("Problem using the webcam")
        ok, data = cv2.imencode('.jpg', image)
        if ok != True:
            raise ValueError("Problem getting image data")
        if sys.version_info[0] < 3:
            # Python 2 approach to handling bytes
            return data.encode("base64")
        else:
            # Python 3 approach to handling bytes
            import base64
            return base64.b64encode(data).decode()
    finally:
        cam.release()


# This function will pass your image to the machine learning model
# and return the top result with the highest confidence
def classify():
    key = "3abe5c70-82e0-11e9-a2fc-136bef59fee38888745f-73df-4073-9d47-daddb02fc4cc"
    url = "https://machinelearningforkids.co.uk/api/scratch/" + key + "/classify"

    response = requests.post(url, json={"data": returnWC_Pic()})

    if response.ok:
        responseData = response.json()
        topMatch = responseData[0]
        return topMatch
    else:
        response.raise_for_status()
