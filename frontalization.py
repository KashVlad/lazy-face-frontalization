import numpy as np
import os
import glob
import cv2
import insightface
from insightface.app import FaceAnalysis
from insightface.data import get_image as ins_get_image
from pathlib import Path


INPUT_PATH=Path('./input/*')
OUTPUT_PATH=Path('./output')
OUTPUT_SIZE=(300,400)
DUMMY_PATH = Path("./dummies/G_dummy.png")
dummy=cv2.imread(str(DUMMY_PATH))


input_imgs=glob.glob(str(INPUT_PATH))


app = FaceAnalysis(name='buffalo_l')
app.prepare(ctx_id=0, det_size=(640, 640))


swapper = insightface.model_zoo.get_model('inswapper_128', download=False, download_zip=False)


for img_path in input_imgs:
    dummy_img = cv2.imread(str(DUMMY_PATH))
    input_img = cv2.imread(img_path)

    dummy_face = app.get(dummy_img)[0]
    input_face = app.get(input_img)[0]

    output_img = dummy_img.copy()
    output_img = swapper.get(output_img, dummy_face, input_face)
    
    output_img=cv2.cvtColor(output_img, cv2.COLOR_BGR2RGB
    output_face = app.get(output_img)
    bbox = output_face[0]['bbox']
    bbox = [int(b) for b in bbox]
    cropped_output_face = output_img[bbox[1]:bbox[3], bbox[0]:bbox[2], ::-1]
    cropped_resized_output_face = resized = cv2.resize(cropped_output_face, OUTPUT_SIZE, interpolation=cv2.INTER_AREA)

    cv2.imwrite(str(OUTPUT_PATH / Path(img_path).stem) + '_cropped_face.png', cropped_resized_output_face)

    ###if you don't need to crop the image you can use the next line###
    # cv2.imwrite(str(OUTPUT_PATH / Path(img_path).stem) + '_output.png',output_img)
