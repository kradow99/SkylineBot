import random
import matplotlib.pyplot as plt


class Skyline:

    def __init__(self, id=None, bs=[]):
        self.id = id
        self.buildings = bs
        self.area = Skyline.getArea(bs)
        self.height = Skyline.getHeight(bs)

    def simple(xmin, height, xmax):
        if (xmin >= xmax or height < 0):
            return []
        return [[xmin, height], [xmax, 0]]

    def deepcopy(l):
        result = []
        for x in l:
            result.append(x.copy())
        return result

    def random(n, h, w, xmin, xmax):
        bs = []
        if (n <= 0 or h < 0 or xmin >= xmax or xmax-xmin < w):
            return []
        for i in range(n):
            h_rand = random.randint(0, h)
            w_rand = random.randint(1, w)
            xmin_rand = random.randint(xmin, xmax-w_rand)
            xmax_rand = xmin_rand + w_rand
            new = [[xmin_rand, h_rand], [xmax_rand, 0]]
            Skyline.addBuilding(bs, new)
            if i == n/2:
                Skyline.clean(bs)
        Skyline.clean(bs)
        return bs

    def clean(bs):
        i = 0
        while i < len(bs)-2:
            if bs[i][0] == bs[i+1][0]:
                bs.pop(i)
            elif bs[i][1] == bs[i+1][1]:
                bs.pop(i+1)
            else:
                i += 1

    def addBuilding(bs, b1):
        xmin = b1[0][0]
        xmax = b1[1][0]
        h = b1[0][1]
        l = len(bs)
        i = 0
        last_y = 0
        while i < l and bs[i][0] < xmin:
            last_y = bs[i][1]
            i += 1
        if i < l:
            if bs[i][0] == xmin and bs[i][1] < h:
                last_y = bs[i][1]
                bs[i][1] = h
                i += 1

            elif xmin < bs[i][0] and last_y < h:
                bs.insert(i, [xmin, h])
                i += 1
                l += 1
        else:
            bs.insert(i, [xmin, h])
            i += 1
            l += 1
        while i < l and bs[i][0] < xmax:
            last_y = bs[i][1]
            if bs[i][1] < h and bs[i-1][1] != h:
                bs[i][1] = h
            elif bs[i][1] < h:
                bs.pop(i)
                i -= 1
                l -= 1
            i += 1

        if i == l:
            bs.insert(i, [xmax, 0])
        elif bs[i][0] != xmax and last_y < h:
            bs.insert(i, [xmax, last_y])

    def union(bs1, bs2):
        if bs1 == []:
            return bs2
        if bs2 == []:
            return bs1
        result = []
        i = 0
        j = 0
        last_y1 = 0
        last_y2 = 0
        l1 = len(bs1)
        l2 = len(bs2)
        if bs1[0][0] < bs2[0][0] and bs1[0][1] == 0:
            result.append([bs1[0][0], 0])
            i += 1
        elif bs2[0][0] < bs1[0][0] and bs2[0][1] == 0:
            result.append([bs2[0][0], 0])
            j += 1
        elif bs1[0][0] == bs2[0][0] and bs1[0][1] == 0:
            result.append([bs1[0][0], 0])
            i += 1
            j += 1
        while i < l1 and j < l2:
            x1 = bs1[i][0]
            y1 = bs1[i][1]
            x2 = bs2[j][0]
            y2 = bs2[j][1]
            if x1 < x2:
                if y1 > last_y2:
                    result.append([x1, y1])
                elif last_y2 < last_y1:
                    result.append([x1, last_y2])
                i += 1
                last_y1 = y1
            elif x2 < x1:
                if y2 > last_y1:
                    result.append([x2, y2])
                elif last_y1 < last_y2:
                    result.append([x2, last_y1])
                j += 1
                last_y2 = y2
            else:  # x1 == x2
                if y1 >= y2:
                    result.append([x1, y1])
                else:
                    result.append([x1, y2])
                i += 1
                j += 1
                last_y1 = y1
                last_y2 = y2

        while i < l1:
            result.append(bs1[i])
            i += 1
        while j < l2:
            result.append(bs2[j])
            j += 1
        Skyline.clean(result)
        return result

    def replic(bs, n):
        dist_ini = bs[-1][0] - bs[0][0]
        dist = 0
        result = []
        for i in range(0, n):
            result += list(map(lambda b: [b[0]+dist, b[1]], bs))
            dist += dist_ini
        Skyline.clean(result)
        return result

    def despl(bs, n):
        result = bs
        for b in result:
            b[0] += n
        return result

    def mirror(bs):
        xmin = bs[0][0]
        xmax = bs[-1][0]
        result = []
        l = len(bs)
        for i in range(1, l+1):
            new_x = xmin + xmax - bs[-i][0]
            if i != l:
                new_y = bs[-i-1][1]
            else:
                new_y = 0
            result.append([new_x, new_y])
        return result

    def intersection(bs1, bs2):
        result = []
        i = 0
        j = 0
        last_y1 = 0
        last_y2 = 0
        l1 = len(bs1)
        l2 = len(bs2)
        while i < l1 and j < l2:
            x1 = bs1[i][0]
            y1 = bs1[i][1]
            x2 = bs2[j][0]
            y2 = bs2[j][1]
            if x1 < x2:
                if y1 < last_y2:
                    result.append([x1, y1])
                elif last_y2 > last_y1:
                    result.append([x1, last_y2])
                i += 1
                last_y1 = y1
            elif x2 < x1:
                if y2 < last_y1:
                    result.append([x2, y2])
                elif last_y1 > last_y2:
                    result.append([x2, last_y1])
                j += 1
                last_y2 = y2
            else:  # x1 == x2
                if y1 < y2:
                    result.append([x1, y1])
                else:
                    result.append([x1, y2])
                i += 1
                j += 1
                last_y1 = y1
                last_y2 = y2

        Skyline.clean(result)
        return result

    def getPlot(bs):
        if bs == []:
            plt.fill_between([0, 0], [0, 1])
            return plt
        xs = []
        ys = []
        xs.append(bs[0][0])
        ys.append(bs[0][1])
        last_x = bs[0][0]
        last_y = bs[0][1]
        for i in range(len(bs)-1):
            xs.append(bs[i][0])
            ys.append(bs[i][1])
            xs.append(bs[i+1][0])
            ys.append(bs[i][1])
        plt.fill_between(xs, ys)
        return plt

    def getArea(bs):
        a = 0
        for i in range(len(bs)-1):
            h = bs[i][1]
            b = bs[i+1][0] - bs[i][0]
            a += b*h
        return a

    def getHeight(bs):
        h = 0
        for b in bs:
            if b[1] > h:
                h = b[1]
        return h
