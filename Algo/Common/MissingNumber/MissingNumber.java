class MissingNumber{  

    public static void main(String args[]){ 
        int[] arr = new int[] {1,3,4,5,6};
        System.out.println(missingNumber(arr));
    }  

    public static int missingNumber(int[] arr) {
        int arraySum = 0;
        int expectedSum = 0;
        for (int i = 1; i <= arr.length; i++) {
            expectedSum += i;
            arraySum += arr[i - 1];
        }
        return expectedSum - arraySum;
    } 
} 
