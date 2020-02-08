'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    count = 0
    
    # TBC
    def count_helper(word):
        
        if len(word) <= 1:
            return 0
    
        if word[0] == 't' and word[1] == 'h':
            nonlocal count
            count = count + 1
            return count_helper(word[1:])

        else:
            return count_helper(word[1:])

    count_helper(word)

    return count