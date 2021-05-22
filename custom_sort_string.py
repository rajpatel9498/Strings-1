class Solution:
    def customSortString(self, order: str, str: str) -> str:
        
        
        t_dict={}
        res=[]
        s=""
        for i in range(len(str)):
            
            if str[i] not in t_dict:
                t_dict[str[i]] = 1
            
            else:
                t_dict[str[i]] = t_dict[str[i]] + 1
                
        for i in range(len(order)):
            
            if order[i] in t_dict:
                count=t_dict[order[i]]
                while(count>0):
                    res.append(order[i])
                    count-=1
                del t_dict[order[i]]
                
        for key in t_dict:
            count = t_dict[key]
            while count>0:
                res.append(key)
                count-=1
                
        return s.join(res)
