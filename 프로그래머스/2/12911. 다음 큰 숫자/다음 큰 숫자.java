import java.util.*;

class Solution {
    public int solution(int n) {
        int answer = 0;
        int temp=n;
        
        int cnt=0;
        
        String nBin = Integer.toBinaryString(n);
        for(int i =0;i<nBin.length();i++){
            if(nBin.charAt(i)=='1'){
                cnt++;
            }
        }
    
        
        while(true){
            temp+=1;
            int tCount=0;
            
            String tBin = Integer.toBinaryString(temp);
            for(int i =0;i<tBin.length();i++){
                if(tBin.charAt(i)=='1'){
                    tCount++;
                }
            }
            
            if ( cnt == tCount){
                break;
            
            }

        }
        return temp;
    }
}