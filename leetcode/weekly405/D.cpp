// 3213. Construct String with Minimum Cost

class TrieNode {
public:
    unordered_map<char, TrieNode*> children;
    vector<pair<int, int>> word_ends;
};

class Trie {
public:
    TrieNode* root;

    Trie() {
        root = new TrieNode();
    }

    void insert(string word, int index, int cost) {
        TrieNode* node = root;
        for (char c : word) {
            if (!node->children.count(c)) {
                node->children[c] = new TrieNode();
            }
            node = node->children[c];
        }
        node->word_ends.push_back({index, cost});
    }
};

class Solution {
public:
    int  minimumCost(string target, vector<string>& words, vector<int>& costs) {
        int n = target.size();
        vector<int> dp(n + 1, INT_MAX);
        dp[0] = 0;

        Trie trie;
        for (int i = 0; i < words.size(); ++i) {
            trie.insert(words[i], i, costs[i]);
        }

        for (int i = 0; i < n; ++i) {
            if (dp[i] == INT_MAX) {
                continue;
            }

            TrieNode* node = trie.root;
            for (int j = i; j < n; ++j) {
                if (!node->children.count(target[j])) {
                    break;
                }
                node = node->children[target[j]];
                for (auto& p : node->word_ends) {
                    int word_len = words[p.first].size();
                    if (i + word_len <= n) {
                        dp[i + word_len] = min(dp[i + word_len], dp[i] + p.second);
                    }
                }
            }
        }

        return dp[n] == INT_MAX? -1 : dp[n];
    }
};