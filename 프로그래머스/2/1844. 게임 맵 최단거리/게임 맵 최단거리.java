import java.util.*;

class Solution {
    public static void bfs(int x,int y,int[][]maps){
        int[] dx ={0,0,-1,1};
        int[] dy ={-1,1,0,0};
        Queue<int[]>queue= new LinkedList<>();
        queue.add(new int[]{x,y});
        int height = maps.length;
        int length = maps[0].length;
        
        while(!queue.isEmpty()){
            int [] curr= queue.poll();
            for(int i=0;i<4;i++){
                int nx=(curr[0]+dx[i]);
                int ny=(curr[1]+dy[i]);
                
                if (0<=nx&& nx<height && 0<=ny&& ny<length && maps[nx][ny]==1){
                    queue.add(new int[]{nx,ny});
                    maps[nx][ny]=(maps[curr[0]][curr[1]]+1);
                }
            }

        }
        
    }
    
    public int solution(int[][] maps) {

        int rows = maps.length;
        int cols = maps[0].length;

        bfs(0, 0, maps); // ✅ 단 한 번만 BFS 실행

        if (maps[rows - 1][cols - 1] <= 1) {
            return -1; // 도달할 수 없는 경우
        }
        return maps[rows - 1][cols - 1]; // ✅ 마지막 위치의 값 반환

    }
}