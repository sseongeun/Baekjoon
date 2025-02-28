import java.util.*;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer=new int[commands.length];
        for (int i=0;i<commands.length;i++){
            int[] command = commands[i];
            int[] curr = Arrays.copyOfRange(array,command[0]-1,command[1]);
         
            Arrays.sort(curr);
            
            answer[i]=curr[command[2]-1];
            
        }
        return answer; 
    }
}