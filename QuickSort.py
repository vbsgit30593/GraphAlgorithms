'''
    In Quick Sort we want to ensure that the items to the left of the a chosen pivot are lesser than the pivot
    and the items to the right are greater than the pivot

    * Choose pivot
    * left - obtain less array
    * right - obtain more array
    * return QS(left) + pivot + QS(right)

'''

class Sort:
    def QuickSort(self, ar):
        #base case
        if len(ar) < 2:
            return ar

        pivot = ar[0]
        left = [ele for ele in ar[1:] if ele <= pivot]
        right = [ele for ele in ar[1:] if ele > pivot]
        #recursive case
        return self.QuickSort(left) + [pivot] + self.QuickSort(right)

def main():
    obj = Sort()
    ar = [2,4,5,1,3,7,10,11,8,8,8]
    print (f'Array before Sort : {ar}')
    ar = obj.QuickSort(ar)
    print (f'Array after sort : {ar}')

if __name__ == "__main__":
    main()