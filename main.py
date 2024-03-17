import cv2

from Pole.map import Map
from Dict import objects


if __name__ == '__main__':
    map = Map(24, 39)
    pole = map.pole

    pole['environment'][0][0] = 1
    pole['environment'][2][2] = 1
    pole['environment'][23][38] = 1

    cv2.imshow('World', map.draw())
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite('World.png', map.draw())