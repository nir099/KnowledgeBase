public class ReverseArray{
    public static void main(String[] args){

        int[] arr = {1,4,6,8,4,3,2,9};

        /*
            i and j are the pointers and i is pointing to the start of the array and j is pointing the end of the array
        */
        int i = 0;
        int j = arr.length - 1;

        // swap elemets of the array using two pointer mechanism
        int temp = 0;
        while(i < j){
            temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
            i++;
            j--;
        }
    }
}