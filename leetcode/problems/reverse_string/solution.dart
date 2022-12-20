class Solution {
  void reverseString(List<String> s) {
    for(int i = 0; i < (s.length / 2).toInt(); i++) {
        String temp = s[i];
        s[i] = s[s.length - i - 1];
        s[s.length - i - 1] = temp; 
    }
  }
}