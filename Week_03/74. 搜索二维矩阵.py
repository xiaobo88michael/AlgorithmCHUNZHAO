func searchMatrix(matrix [][]int, target int) bool {

    n,m:=len(matrix[0]),len(matrix)
    if n==0 {
        return false
    }

    low , high := 0, n*m-1
    pivot:=0

    for low<=high {
        mid:= (low+high)/2
        pivot = matrix[mid/n][mid%n]
        if pivot==target {
            return true
        } else if pivot>target {
            high = mid-1
        } else {
            low = mid+1
        }


    }
    return false

}
