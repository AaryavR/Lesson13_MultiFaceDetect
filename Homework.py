import cv2
import numpy as np
import matplotlib as plt

def apply_color_filter(image, filter_type):
    filtered_image = image.copy()
    if filter_type == "red_tint":
        filtered_image[:, :, 0] = 0  # Blue
        filtered_image[:, :, 1] = 0  # Green
    elif filter_type == "blue_tint":
        filtered_image[:, :, 1] = 0  # Green
        filtered_image[:, :, 2] = 0  # Red
    elif filter_type == "green_tint":
        filtered_image[:, :, 0] = 0  # Blue
        filtered_image[:, :, 2] = 0  # Red
    elif filter_type == "increase_red":
        filtered_image[:, :, 2] = cv2.add(filtered_image[:, :, 2], 50)
    elif filter_type == "decrease_blue":
        filtered_image[:, :, 0] = cv2.subtract(filtered_image[:, :, 0], 50)

    return filtered_image

image_path = 'image.jpg'
image = plt.imread(image_path)

if image is None:
    print("Error: Image not found!")
else:
    filter_type = "original"

    print("Press the following keys to apply filters:"
          "\n r - Red Tint"
          "\n b - Blue Tint"
          "\n g - Green Tint"
          "\n i - Increase Red Intensity"
          "\n d - Decrease Blue Intensity"
          "\n q - Quit")

    sizex = int(input("What do you want the x size to be (px): "))
    sizey = int(input("What do you want the y size to be (px): "))

    while True:
        if filter_type == "original":
            filtered_image = image.copy()
        else:
            filtered_image = apply_color_filter(image, filter_type)

        resized_image = cv2.resize(filtered_image, (sizex, sizey))
        cv2.imshow("Filtered Image", resized_image)

        cropped_image = image[100:300, 200:400]
        cropped_rgb = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB)
        plt.imshow("image", cropped_rgb)
        plt.title("Cropped Region")
        plt.show()

        key = cv2.waitKey(0) & 0xFF

        if key == ord('r'):
            filter_type = "red_tint"
        elif key == ord('b'):
            filter_type = "blue_tint"
        elif key == ord('g'):
            filter_type = "green_tint"
        elif key == ord('i'):
            filter_type = "increase_red"
        elif key == ord('d'):
            filter_type = "decrease_blue"
        elif key == ord('q'):
            print("Exiting")
            break
        else:
            print("Invalid key")

        cv2.destroyWindow("Filtered Image")

    cv2.destroyAllWindows()