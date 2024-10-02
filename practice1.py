def main():
    arr=[1,2,76,342,32,1,3,687,12,12,43,65,863,22]
    print("origonal array; " , arr) 

    arr=sort_array(arr)
    print("Soorted Array:", arr)



def sort_array(arr):
    length= len(arr)
    j=0

    while j < length-1:
        if(arr[j]>arr[j+1]):
            temp=arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=temp
            j= -1
        j+=1
    return arr

if __name__ == '__main__':
    main()
