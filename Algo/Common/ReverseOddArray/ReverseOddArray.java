public class ReverseOddArray {
    public static void main(String[] args){
        int[] arr = {1,4,6,8,4,3,2,9};

        int i = 0;
        int j = arr.length - 1;

        int temp = 0;
        while(i < j){
            if(arr[i] % 2 == 1 && arr[j] % 2 == 1){
                temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
                i++;
                j--;
            }else if(arr[i] % 2 == 0){
                i++;
            }else if(arr[j] % 2 == 0){
                j--;
            }else{
                i++;
                j--;
            }
        }
    }   
}