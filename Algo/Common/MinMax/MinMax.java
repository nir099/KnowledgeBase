class MinMax{  

    public static void main(String args[]){ 
        int[] arr = new int[] {3,7,2,8,3};
        minMax(arr);
    }  

    public static void minMax(int[] arr) {
        int min = arr[0];
        int max = arr[0];
        for(int value: arr) {
            if (value > max) {
                max = value;
            }
            if (value < min) {
                min = value;
            }
        }

        System.out.println("Min is " + min);
        System.out.println("Max is " + max);
    } 
} 