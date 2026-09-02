#include <cctype>
#include <iostream>

class Solution {
public:
    bool isPalindrome(string s) {
        int left = 0;
        int right = s.length()-1;

        while (left < right) { 
            while ((left < right) && (!std::isalnum(s[left]))) { 
                left++;
            }

            while ((left < right) && (!std::isalnum(s[right]))) { 
                right--;
            }

            char left_char = std::tolower(s[left]);
            char right_char = std::tolower(s[right]);

            // if left index is bigger than right index, or index is not matching.
            if (left >= right) { 
                return true;
            }

            std::cout << left_char << std::endl;
            std::cout << right_char << std::endl;

            if (left_char != right_char) { 
                return false;
            }

            left++;
            right--;
        }

        return true;
    }
};
