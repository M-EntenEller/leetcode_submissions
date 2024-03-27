// https://leetcode.com/problems/map-sum-pairs

class MapSum {

    Map<String, Integer> map; 

    public MapSum() {

        this.map = new HashMap<>();
        
    }
    
    public void insert(String key, int val) {
        
        map.put(key, val);

    }
    
    public int sum(String prefix) {
        
        int sum = 0;
        
        for (Map.Entry<String, Integer> e : this.map.entrySet()){

            if (comeparePrefix(e.getKey(), prefix)){
                sum += e.getValue();
            }

        }

        return sum;

    }

    private boolean comeparePrefix(String a, String prefix){

        if(prefix.length() > a.length()){return false;}
        
        int i=0;

        while (i < a.length() && i < prefix.length()){

            if (a.charAt(i) != prefix.charAt(i)){
                return false;
            }
            i++;

        }

        return true;

    }
}

/**
 * Your MapSum object will be instantiated and called as such:
 * MapSum obj = new MapSum();
 * obj.insert(key,val);
 * int param_2 = obj.sum(prefix);
 */