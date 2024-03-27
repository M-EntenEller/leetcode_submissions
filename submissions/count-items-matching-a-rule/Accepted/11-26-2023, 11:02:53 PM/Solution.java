// https://leetcode.com/problems/count-items-matching-a-rule

class Solution {

    public int countMatches(List<List<String>> items, String ruleKey, String ruleValue) {

        int count=0;
        int r=0;

        switch (ruleKey)
        {
            case "type":
                r = 0;
                break;
            case "color":
                r = 1;
                break;
            case "name":
                r = 2;
                break;                
        }
        
        for (var item : items)
        {
            if (item.get(r).equals(ruleValue))
            {
                count++;
            }
        }

        return count; 
    }
}