class Solution {
    public int numJewelsInStones(String J, String S) {
        int count = 0;
        char[] Ss = S.toCharArray();
        char[] Js = J.toCharArray();
        for (char s : Ss) {
            for (char j : Js) {
                if (s == j)
                    count += 1;
            }
        }
        return count;
    }
}
