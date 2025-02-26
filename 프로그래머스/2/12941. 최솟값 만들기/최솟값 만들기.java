import java.util.*;

class Solution
{
    public int solution(int []A, int []B)
    {
        int answer = 0;

        Arrays.sort(A); // 오름차순 정렬
        Arrays.sort(B); // 내림차순 정렬
        int len = A.length;

        for (int i =0;i<len;i++){
            answer+=A[i]*B[len-i-1];
        }
    
        
        return answer;
    }
}