import time

class ThreeSum:

    def count(self, a):
        N = len(a)
        count = 0
        for i in range(N):
            for j in range(i + 1, N):
                for k in range(j + 1, N):
                    if a[i] + a[j] + a[k] == 0:
                        count += 1
        return count



if __name__ == '__main__':
    a = list(map(int,input().split(' '))) 
    start = time.time()
    ThreeSum.count(a)
    end = time.time()
    print(end-start)