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

class Codec_2 {

    private dict: { [key: string]: string };
    private domain: string;
    private length: number;

    constructor() {
        this.dict = {};
        this.domain = "http://tinyurl.com/";
        this.length = 6;
    }

    private generateEncryption(): string {
        const characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
        let encryption = "";

        for (let i = 0; i < this.length; i++) {
            const index = Math.floor(Math.random() * characters.length);
            encryption += characters[index];
        }

        return encryption;
    }

    public encode(longUrl: string): string {
        let encryptionMap = this.generateEncryption();

        while (this.dict[encryptionMap]) {
            encryptionMap = this.generateEncryption();
        }

        this.dict[encryptionMap] = longUrl;
        return this.domain + encryptionMap;
    }

    public decode(shortUrl: string): string {
        const encryptionMap = shortUrl.split("/").pop()!;
        return this.dict[encryptionMap];
    }
}

const url_2 = "https://leetcode.com/problems/design-tinyurl";
const codec_2 = new Codec_2();
const shortUrl_2 = codec_2.encode(url_2);
console.log(shortUrl_2);
console.log(codec_2.decode(shortUrl_2));
