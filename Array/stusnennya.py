from zavd3 import GrayscaleImage


class Photo:
    DCT = {str(i) + '-': i for i in range(256)}
    LST3 = []
    VALUE_NUM = 255
    NUM_NOW = ''

    def __init__(self, row, coln):
        self.array_2d = GrayscaleImage(row, coln)
        self.array_1d = []
        for i in range(row):
            for j in range(coln):
                self.array_1d.append(self.array_2d.__getitem__(i, j))

    def encode(self):
        for i in self.array_1d:
            check_num = Photo.NUM_NOW + i + "-"
            print(check_num)
            if check_num in Photo.DCT:
                Photo.NUM_NOW = check_num
            else:
                Photo.LST3.append(Photo.DCT[Photo.NUM_NOW])
                Photo.DCT[check_num] = Photo.VALUE_NUM + 1
                Photo.VALUE_NUM += 1
                Photo.NUM_NOW = i + "-"
        Photo.LST3.append(Photo.DCT[str(self.array_1d[-1]) + "-"])

    @staticmethod
    def decode(lst, dct):
        my_lst = []
        for i in lst:
            for j in dct:
                if i == dct[j]:
                    my_lst.append(j.split("-"))
        my_lst_int = []
        for i in my_lst:
            for j in i:
                if bool(j) is True:
                    my_lst_int.append(int(j))
        return my_lst_int
