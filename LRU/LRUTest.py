# import unittest
from lru_cache import LRUCache

# class LRUTest(unittest.TestCase):
#     def setUp(self):
#         self.setcache = LRUCache(4)

#     def test_put(self):
#         result = self.setcache.put(10,20)
        
#         self.assertEqual(result,None)

#     def test_get_cache(self):
#         result = self.setcache.get(10)
#         self.assertEqual(result,20)
#     # def test_getCache(self):

#     def test_get_caches(self):
#         result = self.setcache.get_cache()
#         self.assertEqual(result,(10,20))

def main():
    checks = LRUCache(4)

    checks.put(1,10)
    checks.put(2,11)
    checks.put(3,12)
    assert checks.get_cache() == [10,11,12]
    assert checks.get(1) == 10
    assert checks.get(11) == -1




if __name__ == "__main__":
    def main():       
        print("passed")
            


