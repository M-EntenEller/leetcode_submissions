// https://leetcode.com/problems/remove-sub-folders-from-the-filesystem

class Solution {

  private boolean isIn(String s1, String s2){
    
    if (s1.length() > s2.length()){
      return false;
    }

    // substring methed end-index is exclusive.
    if (s1.equals(s2.substring(0, s1.length())) && s2.charAt(s1.length()) == '/'){
      return true;
    }

    return false;

  }

  public List<String> removeSubfolders(String[] folder) {

    Arrays.sort(folder);
    List<String> res = new ArrayList<>();
    res.add(folder[0]);
    String tmp = folder[0];

    for (int i=1; i<folder.length; i++)
    {
      if (! isIn(tmp, folder[i])){
        tmp = folder[i];
        res.add(tmp);
      }
    }

    return res;
  }
}