import numpy as np
import cv2

from Dict import objects
from Dict import environments


class Map:
    def __init__(self, n: int, m: int):
        self.__n = n
        self.__m = m
        self.__pole = {'environment': np.zeros((self.__n, self.__m)),
                       'objects': np.zeros((self.__n, self.__m))-1}
        self.__size = 32

    @property
    def pole(self):
        return self.__pole

    @pole.setter
    def pole(self, pole):
        if (self.__n, self.__m) != pole.shape:
            return 0
        self.__pole = pole

    def draw(self)->np.array:
        '''
        Метод орисовки поля
        :return:
                img - картинка поля
        '''
        img = np.zeros((self.__n * self.__size, self.__m * self.__size, 3), np.uint8)
        for i in range(self.__n):
            for j in range(self.__m):
                if self.__pole['objects'][i][j] >= 0:
                    img[i * self.__size: (i+1) * self.__size,
                        j * self.__size: (j+1) * self.__size] = objects[self.__pole['objects'][i][j]].picture
                else:
                    img[i * self.__size: (i + 1) * self.__size,
                    j * self.__size: (j + 1) * self.__size] = environments[self.__pole['environment'][i][j]].picture
        return img


if __name__ == '__main__':
    map = Map(20, 35)
    cv2.imshow('World', map.draw())
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    a = map.pole
    a[0][6] = 1
    map.pole = np.array([1])
    cv2.imshow('World', map.draw())
    cv2.waitKey(0)
    cv2.destroyAllWindows()