class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return 0
        list_num=list(str(abs(num)))
        if num < 0 :
            list_num.sort(reverse=True)
            return -int(''.join(list_num))
        else:
            new_list=sorted(list_num)
            if new_list[0]=='0':
                for i in range(1,len(new_list)):
                    if new_list[i] != '0':
                        new_list[0],new_list[i]=new_list[i],new_list[0]
                        return int(''.join(new_list))
            else:
                return int(''.join(new_list))
