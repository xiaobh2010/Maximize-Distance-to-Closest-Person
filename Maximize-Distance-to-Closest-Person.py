class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        m=0
        seats=[str(i) for i in seats]
        s=''.join(seats).split('1')
        print(s)
        # print(s)
        L=[]
        for i in s:
            if i!='':
                L.append(i)
        for i in L: 
            m=max(m,len(s[0]),len(s[-1]),(len(i)+1)//2)
        return m
