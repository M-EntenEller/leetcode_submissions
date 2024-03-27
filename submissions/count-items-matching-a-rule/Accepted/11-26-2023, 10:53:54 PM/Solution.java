// https://leetcode.com/problems/count-items-matching-a-rule

class Solution {
    public int countMatches(List<List<String>> items, String ruleKey, String ruleValue) {

        int count = 0;

        for (var item: items)
        {
            switch (ruleKey)
            {
                case "type":
                    count += ruleValue.equals(item.get(0)) ? 1 : 0;
                    break;
                case "color":
                    count += ruleValue.equals(item.get(1)) ? 1 : 0;
                    break;
                case "name":
                    count += ruleValue.equals(item.get(2)) ? 1 : 0;
            }
        }

        return count; 
        
    }
}