// https://leetcode.com/problems/map-sum-pairs

class Inode {

    Inode[] branches;
    int val;

    public Inode(){
        this.branches = new Inode[26];
        this.val = 0;
    }

}

class MapSum {

    Map<String, Integer> lastSeen;
    Inode root; 

    public MapSum() {
        
        this.lastSeen = new HashMap<String, Integer>();
        this.root = new Inode();

    }
    
    public void insert(String key, int val) {

        Inode tmp = this.root;

        for (int i=0; i<key.length(); i++){

            if (tmp.branches[key.charAt(i) - 'a'] == null){
                tmp.branches[key.charAt(i) - 'a'] = new Inode();
            };

            tmp = tmp.branches[key.charAt(i) - 'a'];
            tmp.val += val - lastSeen.getOrDefault(key, 0);

        }        

        this.lastSeen.put(key, val);

    }
    
    public int sum(String prefix) {
    
        Inode tmp = this.root; 

        for (int i=0; i< prefix.length(); i++){

            tmp = tmp.branches[prefix.charAt(i) - 'a'];
            if (tmp == null){
                return 0;
            }

        }

        return tmp.val;

    }

}

/**
 * Your MapSum object will be instantiated and called as such:
 * MapSum obj = new MapSum();
 * obj.insert(key,val);
 * int param_2 = obj.sum(prefix);
 */