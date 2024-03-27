// https://leetcode.com/problems/sort-the-people

class NH implements Comparable<NH>{

    String name; 
    int height;

    public NH(String name, int height){
        this.name = name;
        this.height = height; 
    }

    @Override
    public int compareTo(NH x){
        return x.height - this.height;
    }

}

class Solution {

    public String[] sortPeople(String[] names, int[] heights) {
        
        NH[] combined = new NH[names.length];

        for (int i=0; i <names.length; i++){

            combined[i] = new NH(names[i], heights[i]);

        }

        Arrays.sort(combined);
        
        for (int i = 0; i < names.length; i++){

            names[i] = combined[i].name;

        }

        return names;

    }
}