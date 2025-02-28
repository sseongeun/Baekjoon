import java.util.*;

class Solution {
    
    public int solution(String begin, String target, String[] words) {
         
        Queue<String> queue= new LinkedList<>();
        Map<String,Integer> map = new HashMap<>(); // 방문 여부를 저장하는 map
        queue.add(begin);
        map.put(begin,0);
        int depth=0;
            
            
        while(!queue.isEmpty()){
            String curr = queue.poll();
            depth = map.get(curr);
            
            if (curr.equals(target)){
                return depth;
            }
            
            for(String word:words){
                if (isOneDiff(word,curr)&& !(map.containsKey(word))){
                    map.put(word,depth+1);
                    queue.add(word);
                }
            }   
            
        }
        return 0;
    }
    
    
    public static boolean isOneDiff(String s1,String s2){
        int diff=0;
        for(int i=0;i<s1.length();i++){
            if (s1.charAt(i)!=s2.charAt(i)){
                diff++;
            }
        }
        if (diff==1){
            return true;
        }
        return false;
    }

    
}