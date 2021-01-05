class SecondMax{  

    public static void main(String args[]){ 
        int[] arr = new int[] {19,4,17,16,17,30,13,8,30};
        minMax(arr);
    }  

    public static void minMax(int[] numbers) {
        int secondMax = numbers[0];
        int max = numbers[0];
        for (int value: numbers) {
            if (value > max) {
                secondMax = max;
                max = value;
            }
        }
        System.out.println("Max is " + max);
        System.out.println("Second Max is " + secondMax);
    }
} 