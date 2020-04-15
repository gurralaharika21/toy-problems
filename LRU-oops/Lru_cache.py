import collections 
# import OrderedDict
class LRUCache:
    # dict = {}
    def __init__(self,capacity :int):
        self.capacity = capacity
        self.cache = collections.OrderedDict()

    def put(self,key:int,value:int):
        try:
            self.cache.pop(key)
        except KeyError:
            if len(self.cache) >= self.capacity:
                self.cache.popitem(last=False)
                # //first in first out
        self.cache[key] = value   
    



    def get(self,key:int): 
        try:
            value = self.cache.pop(key)   
            self.cache[key] = value
            val = value
            # print(value)
            return value
        except KeyError:
            # print(-1)
            return -1


   
    def get_cache(self):
        return self.cache
        # print(self.cache)     


# if __name__ == "__main__":
#     dict = LRUCache(4)
#     dict.put(1,10)
#     dict.put(2,11)
#     dict.put(3,12)
#     dict.put(3,13)
#     dict.put(4,13)
#     dict.get_cache()




    # dict.get(7)

    #   self.key = key
    #   self.value = value

# cach = LRUCache(4)
# dict.put(1,10)
# dict.put(2,3)  
# # print(dict)
# # cach = LRUcache(4)
# cache.get(1)


    #   capacity = 10
    #   put(1,10)
    #   put(2,90)
    #   get(2)


           