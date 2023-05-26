import cv2
import numpy as np

def cross_dissolve_morphing(source_image, destination_image, morphing_factor):
    src = cv2.imread(source_image)
    dst = cv2.imread(destination_image)

    src = cv2.resize(src, (dst.shape[1], dst.shape[0]))

    src = np.float32(src)
    dst = np.float32(dst)

    morphed_image = np.uint8((1 - morphing_factor) * src + morphing_factor * dst)

    return morphed_image

source_image_path = 'dog.jpg'
destination_image_path = 'human.jpg'

morphing_factor = 0.4

morphed_image = cross_dissolve_morphing(source_image_path, destination_image_path, morphing_factor)

cv2.imwrite("morphed_image_04.png", morphed_image)