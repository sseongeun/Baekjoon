import java.util.*;

class Solution {
    public int[] solution(int l, int r) {
        int[] answer = {};
        List<Integer> numList= new ArrayList<>();
        for(int i =l;i<=r;i++){
            if(isValid(String.valueOf(i))){
                numList.add(i);
            }
        }
        if (numList.isEmpty()){
            return new int[]{-1};
        }
        return numList.stream().mapToInt(j -> j).toArray();
    }
    
    public static boolean isValid(String str){
        for(int i =0;i<str.length();i++){
            if (str.charAt(i)!='5' && str.charAt(i)!='0'){
                return false;
            }
        }
        return true;
        
    }
}