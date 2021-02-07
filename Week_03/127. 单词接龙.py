class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        n = len(wordList)
        wordlen = len(beginWord)
        word_set = set(wordList)
        if n==0 or endWord not in wordList:
            return 0
        
        if beginWord in word_set:
            word_set.remove(beginWord)
        queue = [beginWord]
        visited = set(beginWord)
        step = 1
        
        while queue:
            current_size = len(queue)
            for i in range(current_size):
                word = queue[0]
                queue = queue[1:]
                word_list = list(word)
                for j in range(wordlen):
                    orgin_word = word_list[j]
                    for k in range(26):
                        word_list[j] = chr(ord('a') + k)
                        nextword = ''.join(word_list)
                        if nextword in word_set:
                            if nextword==endWord:
                                return step+1
                            if nextword not in visited:
                                queue.append(nextword)
                                visited.add(nextword)
                    word_list[j]=orgin_word
            step+=1
        
        return 0
