// https://leetcode.com/problems/remove-sub-folders-from-the-filesystem

class Solution {

  private boolean isIn(String s1, String s2){

    if (s1.length() > s2.length()){
      return false;
    }

    String[] sp1 = s1.split("/");
    String[] sp2 = s2.split("/");

    for (int i =0; i<sp1.length; i++)
    {
      if (! sp1[i].equals(sp2[i])){
        return false;
      }
    }

    return true;

  }

  public List<String> removeSubfolders(String[] folder) {

    Set<String> minSet = new HashSet<>();
    String tmp;

    for (int i=0; i<folder.length; i++)
    {
      tmp = folder[i];

      for (int j=0; j<folder.length; j++)
      {
        if (i==j){
          continue;
        }
        if (isIn(folder[j], tmp)){
          tmp = folder[j];
          continue;
        }
      }
      
      minSet.add(tmp);
    } 

    return minSet.stream().collect(Collectors.toList());
  }
}