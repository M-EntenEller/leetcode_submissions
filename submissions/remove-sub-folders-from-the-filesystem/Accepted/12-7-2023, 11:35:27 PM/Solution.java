// https://leetcode.com/problems/remove-sub-folders-from-the-filesystem

class Solution {

  private boolean isIn(String s1, String s2){
    
    if (s1 == null || s2 == null){
      return false;
    }

    if (s1.length() > s2.length()){
      return false;
    }

    String[] sp1 = s1.split("/");
    String[] sp2 = s2.split("/");

    if (sp1.length > sp2.length){
      return false;
    }

    for (int i=0; i<sp1.length; i++)
    {
      if (! sp1[i].equals(sp2[i])){
        return false;
      }
    }

    return true;

  }

  private boolean isIn2(String s1, String s2){

    if (s1 == null){
      return false;
    }
    
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
    String tmp = null;
    List<String> res = new ArrayList<>();

    for (String s: folder)
    {
      if (! isIn2(tmp, s)){
        tmp = s;
        res.add(tmp);
      }
    }

    return res;
  }
}