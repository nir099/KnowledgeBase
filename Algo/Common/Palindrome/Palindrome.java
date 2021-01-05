class Palindrome{  

    public static void main(String args[]){ 
        String word = "abcba";
        
        if (isPalindrome(word)) {
            System.out.println("Palindrom");
        } else {
            System.out.println("Not Palindrom");
        }
    }  

    public static boolean isPalindrome(String word) {
        int wordLength = word.length();
        char[] letters = word.toCharArray();
    
        for (int i = 0; i < wordLength/2; i++) {
            if (letters[i] != letters[wordLength-1-i]) {
                return false;
            }
        }
        return true;
    }
} 
