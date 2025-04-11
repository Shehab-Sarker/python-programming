#include <iostream>

using namespace std;

#define ll long long

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    int T;
    cin >> T;

    int digit_sums[10] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}; // Precompute digit sums

    while (T--) {
        ll n;
        cin >> n;

        // Calculate base number (multiple of 9)
        ll base = (n / 9) * 9;

        // Add sum of digits from 1 to base
        ll sum = 0;
        for (int i = 1; i <= base; ++i) {
            sum += digit_sums[i % 10];
        }

        // Add sum of digits from base + 1 to n
        for (int i = base + 1; i <= n; ++i) {
            sum += (i % 10);
        }

        cout << sum << endl;
    }

    return 0;
}
