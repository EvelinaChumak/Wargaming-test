class TupleFuc():
    
    @staticmethod
    def get_diff_index(first: tuple, second: tuple):
        if (len(first)!=len(second) or first == second):
            return 0            #null because first val in tuple
        else:                   #is ship, weapon, engine or hull
            for i in range(0, len(first)):
                if first[i]!=second[i]:
                    return i
