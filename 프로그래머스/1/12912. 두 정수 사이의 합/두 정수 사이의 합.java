class Solution {
    public long solution(int a, int b) {
        long answer = 0;
        int temp;
        if (a>b){
            temp=b;
            b=a;
            a=temp;
        }
        
        for(int i=a;i<=b;i++){
            answer+=i;
        }
  
        return answer;
    }
}