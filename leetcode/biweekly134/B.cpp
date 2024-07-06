// Maximum Points After Enemy Battles
class Solution {
public:
    long long maximumPoints(vector<int>& adversaryPowers, int initialEnergy) {
        int numEnemies = adversaryPowers.size();
        long long totalPoints = 0;
        sort(adversaryPowers.begin(), adversaryPowers.end());
        int start = 0, end = numEnemies - 1;
        while (start <= end) {
            if (adversaryPowers[start] > initialEnergy) {
                if (totalPoints == 0) {
                    return 0;
                }
                while (initialEnergy < adversaryPowers[start]) {
                    initialEnergy += adversaryPowers[end];
                    end--;
                }
            } else {
                int increment = initialEnergy / adversaryPowers[start];
                initialEnergy %= adversaryPowers[start];
                totalPoints += increment;
            }
        }
        return totalPoints;
    }
};