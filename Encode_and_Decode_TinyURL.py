"""
535. Encode and Decode TinyURL
Solved
Medium
Topics
Companies

    Note: This is a companion problem to the System Design problem: Design TinyURL.

TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk. Design a class to encode a URL and decode a tiny URL.

There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.

Implement the Solution class:

    Solution() Initializes the object of the system.
    String encode(String longUrl) Returns a tiny URL for the given longUrl.
    String decode(String shortUrl) Returns the original long URL for the given shortUrl. It is guaranteed that the given shortUrl was encoded by the same object.



Example 1:

Input: url = "https://leetcode.com/problems/design-tinyurl"
Output: "https://leetcode.com/problems/design-tinyurl"

Explanation:
Solution obj = new Solution();
string tiny = obj.encode(url); // returns the encoded tiny url.
string ans = obj.decode(tiny); // returns the original url after decoding it.



Constraints:

    1 <= url.length <= 104
    url is guaranteed to be a valid URL.

"""

import random
import string


class Codec:

    def __init__(self):
        self.dict = {}
        self.domain = "http://tinyurl.com/"
        self.length = 6

    def _generate_encryption(self):
        charcters = string.ascii_letters + string.digits
        return "".join(random.choice(charcters) for _ in range(self.length))

    def encode(self, longUrl: str) -> str:
        encryption_map = self._generate_encryption()

        while encryption_map in self.dict:
            encryption_map = self._generate_encryption()

        self.dict[encryption_map] = longUrl
        return self.domain + encryption_map

    def decode(self, shortUrl: str) -> str:
        encryption_map = shortUrl.split("/")[-1]
        return self.dict[encryption_map]


url = "https://leetcode.com/problems/design-tinyurl"
codec = Codec()
print(codec.encode(url))
print(codec.decode(codec.encode(url)))
