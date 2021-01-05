public class PairOfSums {
    public static void main(String[] args){
        int[] arr = {1,1,2,3,4,5,6,7,8,8,9,10};
        int sum = 15;

        int i = 0;
        int j = arr.length - 1;

        int total = 0;

        while(i < j){
            total = arr[i] + arr[j];

            if(total == sum){
                System.out.println(arr[i] + " , " + arr[j]);
                i++;
                j--;
            }else if(total < sum){
                i++;
            }else{
                j--;
            }
        }
    }
}