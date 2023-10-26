class Solution {
    public int countSubstrings(String s) {
        int result = 0;
        for(int i=0;i<=s.length();i++)
        {
            int left = i;
            int right = i;
            
            while(left>=0 && right< s.length() && s.charAt(left) == s.charAt(right))
            {
                result +=1;
                left -=1;
                right +=1;
            }
            int l=i;
            int r = i+1;
            while(l>=0 && r< s.length() && s.charAt(l) == s.charAt(r))
            {
                result +=1;
                l -=1;
                r +=1;
            }
        }
        return result;
    }
}