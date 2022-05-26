// [2,3,6,7]
// 7
// -> [[2,2,3],[7]]
class Solution {
    protected void backtrack(int remain,
                             LinkedList<Integer> comb,
                             int start, int[] candidates,
                             List<List<Integer>> results) {
        if (remain == 0) {
            // make a deep copy of the current combination
            results.add(new ArrayList<Integer>(comb));
            return;
        }
        else if (remain < 0) {
            return;
        }
        for (int i = start; i < candidates.length; i++) {
            // add the number into the combination
            comb.add(candidates[i]);
            this.backtrack(remain-candidates[i], comb, i, candidates, results);
            // back track, remove the number from the combination
            comb.removeLast();
        }
    }




    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        // empty list of list
        List<List<Integer>> results = new ArrayList<List<Integer>>();
        LinkedList<Integer> comb = new LinkedList<Integer>();

        this.backtrack(target, comb, 0, candidates, results);
        return results;

    }
}