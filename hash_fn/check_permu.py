
class permutation:
    def check_permu(self, str1: str, str2:str)-> bool:
        if len(str1) != len(str2):
            return False
        hash_map = {}
        for char in str1:
            hash_map[char] = hash_map.get(char, 0) + 1
        print(hash_map)
        for char in str2:
            hash_map[char] = hash_map.get(char, 0) - 1
            if hash_map[char] < 0:
                return False
        return True
    
    def urlify(self,str1: str, n:int):
        i = 0
        for char in str1:
            if i ==n:
                break
            if char == ' ':
                print("%20", end="")
                i+=1
                continue
            print(char, end="")
            i+=1    
    def urlify_optimal(self, char_array: list[str], true_length: int) -> str:
    # count spaces in the true part of the string
        #print(char_array)
        space_count = 0
        for i in range(true_length):
            if char_array[i] == ' ':
                space_count += 1
        
        # new index to place characters (end of final string)
        new_index = true_length + space_count * 2 - 1
        # work backwards
        for i in range(true_length - 1, -1, -1):
            if char_array[i] == ' ':
                char_array[new_index - 2:new_index + 1] = ['%', '2', '0']
                new_index -= 3
            else:
                char_array[new_index] = char_array[i]
                new_index -= 1
        
        return ''.join(char_array)

p = permutation()
#print(p.check_permu("abcb", "bcaa"))
#p.urlify("Mr John Smith    ", 13)
print(len(p.urlify_optimal(list("Mr John Smith 2      "), 15)))