class Solution {
    static int answer=0;
    
    public static void dfs(int node,int[]numbers,int target,int sum){
       
        if(node==numbers.length){
            if (sum==target){
                answer++;
            }
            return;
        }
        dfs(node+1,numbers,target,sum+numbers[node]);
        dfs(node+1,numbers,target,sum-numbers[node]);
    }
    
    
    public int solution(int[] numbers, int target) {
        dfs(0,numbers,target,0);
        return answer;
    
    }
}