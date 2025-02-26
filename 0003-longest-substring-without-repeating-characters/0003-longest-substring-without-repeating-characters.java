class Solution {
    public int lengthOfLongestSubstring(String s) {
        HashMap<Character, Integer> map = new HashMap();
        int max = 0;
        int tempMax = 0;
        int stringlen = s.length();
        for (int i = 0; i < stringlen; i++) {
            // System.out.println(tempMax);
            if (map.get(s.charAt(i)) != null) {
                if (max < tempMax) max = tempMax;
                tempMax = 0;
                i = map.get(s.charAt(i)) + 1;
                map.clear();
                // map.remove(character);
                // continue;
            }
            map.put(s.charAt(i), i);
            tempMax += 1;
        }
        if (max < tempMax) max = tempMax;
        return max;
     }
}