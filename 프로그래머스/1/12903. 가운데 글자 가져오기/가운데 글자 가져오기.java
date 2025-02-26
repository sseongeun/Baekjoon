import java.util.*;

class Solution {
    public String solution(String s) {
        String answer = "";
        int len = s.length();
        
        if (len%2!=0){
            return String.valueOf(s.charAt(len/2));
        }
        else{
            return s.substring(len/2-1,len/2+1);
        }
        
   
    }
}