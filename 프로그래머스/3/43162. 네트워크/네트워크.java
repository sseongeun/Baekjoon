class Solution {
    
    public static void dfs(int node,int[][] computers,boolean[] visited){

        visited[node]=true;
        
        for(int i=0;i<computers.length;i++){
            if(!visited[i] && computers[node][i]==1){
                dfs(i,computers,visited);
            }
        }
        
        
    }
    
    public int solution(int n, int[][] computers) {
        int answer = 0;
        int cNum = computers.length; //컴퓨터 개수
        boolean[] visited = new boolean[cNum];
        
        for (int i=0;i<cNum;i++){
            if (!visited[i]){
                answer++;
                dfs(i,computers,visited);   
            }
        }
        return answer;
    }
}