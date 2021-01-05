class Fibonacci{  
    public static void main(String args[]){ 
        System.out.println(fibonacci(3));
    }  

    public static int fibonacci(int number) {
        if (number == 0){
            return 0;
        } else if (number == 1 || number == 2) {
            return 1;
        } else {
            return fibonacci(number-1) + fibonacci(number-2);
        }
    }
}  