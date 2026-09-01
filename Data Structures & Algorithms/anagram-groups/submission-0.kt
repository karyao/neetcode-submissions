class Solution {
    fun groupAnagrams(strs: Array<String>): List<List<String>> {
        val freq = HashMap<String, MutableList<String>>()
        for (str in strs) { 
            val sortedKey = str.toCharArray().sorted().joinToString("")
            freq.getOrPut(sortedKey) { mutableListOf() }.add(str)
        }

        return ArrayList(freq.values)
    }
}
