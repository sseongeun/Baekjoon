class Solution {
    boolean solution(String s) {
        boolean answer = true;
        int countP=0;
        int countY=0;
        
        

        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == 'p' || s.charAt(i) == 'P') {
                countP++;
            } else if (s.charAt(i) == 'y' || s.charAt(i) == 'Y') {
                countY++;
            }
        }

        if (countP==countY){
            return true;
        }
        else{
            return false;
        }

 
    }
}