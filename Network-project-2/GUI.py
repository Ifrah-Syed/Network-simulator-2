import cv2
import numpy as np
from matplotlib import pyplot as plt


def draw(source,dest):
    img = np.zeros((1200, 2800, 3), np.uint8)
    font = cv2.FONT_HERSHEY_SIMPLEX
    img = cv2.circle(img, (1300, 100), 63, (0, 0, 255), -1)
    cv2.putText(img, "R[0]", (1100,100), font, 1, (255, 255, 0), 2, cv2.LINE_AA)
    img = cv2.circle(img, (900, 350), 63, (0, 0, 255), -1)
    cv2.putText(img, "R[1]", (700,350), font, 1, (255, 255, 0), 2, cv2.LINE_AA)
    img = cv2.circle(img, (1700, 350), 63, (0, 0, 255), -1)
    cv2.putText(img, "R[2]", (1800,350), font, 1, (255, 255, 0), 2, cv2.LINE_AA)

    img = cv2.line(img, (1300, 100), (900,350), (255, 255, 255), 2)
    img = cv2.line(img, (900,350), (1700,350), (255, 255, 255), 2)
    img = cv2.line(img, (1700,350), (1300,100), (255, 255, 255), 2)

    img = cv2.rectangle(img, (500,600), (600,700), (100, 100, 100), -1)
    img = cv2.rectangle(img, (1100,600), (1200,700), (100, 100, 100), -1)
    img = cv2.rectangle(img, (2000,600), (2100,700), (100, 100, 100), -1)

    img = cv2.line(img, (550, 600), (900,350), (255, 255, 255), 2)
    img = cv2.line(img, (1150,600), (900,350), (255, 255, 255), 2)
    img = cv2.line(img, (2050,600), (1700,350), (255, 255, 255), 2)

    img = cv2.rectangle(img, (250,800), (350,900), (0, 155, 0), -1)
    cv2.putText(img, "PC[0]", (250,980), font, 1, (0, 255, 0), 2, cv2.LINE_AA)
    cv2.putText(img, "192.168.1.1", (230, 1100), font, 1, (255, 0, 0), 2, cv2.LINE_AA)

    img = cv2.rectangle(img, (650,800), (750,900), (0, 155, 0), -1)
    cv2.putText(img, "PC[1]", (650,980), font, 1, (0, 255, 0), 2, cv2.LINE_AA)
    cv2.putText(img, "192.168.1.2", (630, 1100), font, 1, (255, 0, 0), 2, cv2.LINE_AA)

    img = cv2.rectangle(img, (950,800), (1050,900), (0, 155, 0), -1)
    cv2.putText(img, "PC[2]", (950,980), font, 1, (0, 255, 0), 2, cv2.LINE_AA)
    cv2.putText(img, "192.168.2.1", (930, 1100), font, 1, (255, 0, 0), 2, cv2.LINE_AA)

    img = cv2.rectangle(img, (1250,800), (1350,900), (0, 155, 0), -1)
    cv2.putText(img, "PC[3]", (1250,980), font, 1, (0, 255, 0), 2, cv2.LINE_AA)
    cv2.putText(img, "192.168.2.2", (1230, 1100), font, 1, (255, 0, 0), 2, cv2.LINE_AA)

    img = cv2.rectangle(img, (1850,800), (1950,900), (0, 155, 0), -1)
    cv2.putText(img, "PC[4]", (1850,980), font, 1, (0, 255, 0), 2, cv2.LINE_AA)
    cv2.putText(img, "192.168.3.1", (1830, 1100), font, 1, (255, 0, 0), 2, cv2.LINE_AA)

    img = cv2.rectangle(img, (2150,800), (2250,900), (0, 155, 0), -1)
    cv2.putText(img, "PC[5]", (2150,980), font, 1, (0, 255, 0), 2, cv2.LINE_AA)
    cv2.putText(img, "192.168.3.2", (2130, 1100), font, 1, (255, 0, 0), 2, cv2.LINE_AA)

    img = cv2.line(img, (300, 800), (550,700), (255, 255, 255), 2)
    img = cv2.line(img, (700, 800), (550,700), (255, 255, 255), 2)

    img = cv2.line(img, (1000, 800), (1150,700), (255, 255, 255), 2)
    img = cv2.line(img, (1300, 800), (1150,700), (255, 255, 255), 2)

    img = cv2.line(img, (1900, 800), (2050,700), (255, 255, 255), 2)
    img = cv2.line(img, (2200, 800), (2050,700), (255, 255, 255), 2)

    str1="Source IP:"+source
    str2="Destination IP:"+dest
    cv2.putText(img, str1,(1800, 100), font, 1, (255, 255, 0), 2, cv2.LINE_AA)
    cv2.putText(img,str2, (1800, 200), font, 1, (255, 255, 0), 2, cv2.LINE_AA)

    cv2.putText(img, "NETWORK LAYER IMPLEMENTATION", (1700,1170), font, 2, (255, 255, 0), 2, cv2.LINE_AA)
    plt.imshow(img, cmap='gray', interpolation='bicubic')


    plt.show()