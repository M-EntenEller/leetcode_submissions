// https://leetcode.com/problems/remove-sub-folders-from-the-filesystem

class Solution {

  private boolean isIn(String s1, String s2){

    if (s1 == null){
      return false;
    }
    
    if (s1.length() > s2.length()){
      return false;
    }

    if (s1.equals(s2.substring(0, s1.length())) && s2.charAt(s1.length()) == '/'){
      return true;
    }

    return false;

  }

  public List<String> removeSubfolders(String[] folder) {

    List<String> res = new ArrayList<>();
    String tmp = null;

    Arrays.sort(folder);

    for (String s: folder)
    {
      if (!isIn(tmp, s)){
        tmp = s;
        res.add(s);
      }
    }

    return res;
  }
}