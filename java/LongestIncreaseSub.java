class Solution {
    public int lengthOfLIS(int[] nums) {
        // initialize array dp with nums.length
        int[] dp = new int[nums.length];
        Arrays.fill(dp, 1);
        // interate pivot index, and element before the pivot
        for (int i = 1; i < nums.length; i++) {
            for (int j = 0; j < i; j++) {
                if( nums[i] > nums[j]) {
                    dp[i] = Math.max(dp[i], dp[j]+1);
                }
            }
        }
        // find max in dp[i]
        int longest = 0;
        for (int c: dp) {
            longest = Math.max(longest, c);
        }
        return longest;
    }
}

// O(nlog(n))
class Solution {
    public int lengthOfLIS(int[] nums) {
        ArrayList<Integer> sub = new ArrayList<>();
        sub.add(nums[0]);
        
        for (int i = 1; i < nums.length; i++) {
            int num = nums[i];
            if (num > sub.get(sub.size() - 1)) {
                sub.add(num);
            } else {
                int j = binarySearch(sub, num); // bisect return index left (number in sub that less than or equal to num num)
                sub.set(j, num);
            }
        }
        
        return sub.size();
    }
    
    private int binarySearch(ArrayList<Integer> sub, int num) {
        int left = 0;
        int right = sub.size() - 1;
        int mid = (left + right) / 2;
        
        while (left < right) {
            mid = (left + right) / 2;
            if (sub.get(mid) == num) {
                return mid;
            }
            
            if (sub.get(mid) < num) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        
        return left;
    }
}