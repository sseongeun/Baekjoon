class Solution {
    boolean solution(String s) {
        boolean answer = true;
        int cntP=0;
        int cntY=0;
        char[] arr = s.toCharArray();
        for(char c:arr){
            if (c=='p' || c=='P'){
                cntP+=1;
            }
            else if(c=='y'|| c=='Y'){
                cntY+=1;
            }
            else{;}
        }
        
        if (cntP!=cntY){
            return false;
        }
        return answer;
    }
}