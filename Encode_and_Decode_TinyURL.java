/*

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

*/

import java.util.HashMap;
import java.util.Map;
import java.util.Random;

public class Codec {
    private Map<String, String> dict;
    private String domain;
    private int length;
    private Random random;

    public Codec() {
        this.dict = new HashMap<>();
        this.domain = "http://tinyurl.com/";
        this.length = 6;
        this.random = new Random();
    }

    private String generateEncryption() {
        String characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
        StringBuilder encryption = new StringBuilder();

        for (int i = 0; i < length; i++) {
            int index = random.nextInt(characters.length());
            encryption.append(characters.charAt(index));
        }

        return encryption.toString();
    }

    public String encode(String longUrl) {
        String encryptionMap = generateEncryption();

        while (dict.containsKey(encryptionMap)) {
            encryptionMap = generateEncryption();
        }

        dict.put(encryptionMap, longUrl);
        return domain + encryptionMap;
    }

    public String decode(String shortUrl) {
        String encryptionMap = shortUrl.split("/")[shortUrl.split("/").length - 1];
        return dict.get(encryptionMap);
    }

    public static void main(String[] args) {
        String url = "https://leetcode.com/problems/design-tinyurl";
        Codec codec = new Codec();
        String shortUrl = codec.encode(url);
        System.out.println(shortUrl);
        System.out.println(codec.decode(shortUrl));
    }

}
