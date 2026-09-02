class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        int minLength = word1.length() < word2.length() ? word1.length() : word2.length();
        string ans = "";
        int i = 0;
        for (i = 0; i < minLength; i++) { 
            ans += word1[i];
            ans += word2[i];
        }
        
        while (word1.length() > i) { 
            ans += word1[i];
            i++;
        } 
        while (word2.length() > i) { 
            ans += word2[i];
            i++;
        }

        return ans;
    }
};