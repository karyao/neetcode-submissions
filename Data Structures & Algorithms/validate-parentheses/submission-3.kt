class Solution {
    fun isValid(s: String): Boolean {
        var deque = ArrayDeque<Char>()
        if (s.length % 2 != 0) { 
            return false
        }

        for (c in s) { 
            if ((c == '[') || (c == '{') || (c == '(')) { 
                deque.addLast(c)
            }
            else { 
                if (deque.isEmpty()) { 
                    return false 
                }
                var p: Char = deque.removeLast()
                if (!(p == '(' && c == ')') && !(p == '[' && c == ']') && !(p == '{' && c == '}')) {
                    return false 
                }
            }
        }

        return deque.isEmpty()
    }
}
