class Solution(object):
    def countString(string):
        saved=[] #已经保存过的字母
        nums=[]
        output=[]
        for i in string:
            if not i in saved:
                saved.append(i)
                nums.append(1)
            else:
                for j in range(len(saved)):
                    if i == saved[j]:
                        nums[j] += 1
        #已经保存了saved和nums的关键数据
        for k in range(len(saved)):
            output.append(saved[k])
            output.append(nums[k])
        list2 =[str(i) for i in output]
        list3 = ''.join(list2)
        return list3
        