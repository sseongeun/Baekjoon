class Solution {
    public int solution(String ineq, String eq, int n, int m) {
        int answer = 0;
        String compare = ineq+eq;
        if (compare.equals(">=")){
            if (n>=m){answer=1;}
        }
        else if (compare.equals("<=")){
            if (n<=m){answer=1;}
        }
        else if (compare.equals(">!")){
            if (n>m){answer=1;}
        }
        else {
            if (n<m){answer=1;}
        }
        
        return answer;
    }
}