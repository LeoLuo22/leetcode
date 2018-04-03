public class Solution {
    public int hammingWeight(int n) {
        int count;
        while (n > 1) {
            if (n % 2 == 1) {
                count += 1;
            }
            n = n / 2;
        }
        if (n == 1) {
            count += 1;
        }
        return count;
    }
}
