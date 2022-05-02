#include <iostream>
#include <string>
#include <vector>
#include <numeric>
using namespace std;

int leap(int R, int L){
    int ans = 0;
    for (int i = L; i <= R; i++){
        if (i % 4 == 0)
            ans ++;
    }
    return ans;
}

int data_parse(int day, int month, int year, int L){
    int ans = day - 1;
    vector<int> days{31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    for (int i = 0; i < month - 1; i++) {
        if ((i == 1) && (year % 4 == 0))
            ans += 1;
        ans += days[i];
    }
    for (int i = L; i < year; i++){
        if (i % 4 == 0)
            ans += 1;
        ans += 365;
    }
    return ans;
}

int main() {
    int n = 0, R = 0, L = 0, num = 0, count = 0;
    string tmp;
    cin >> n >> L >> R;
    int siz = (R-L - leap(R, L) + 1) * 365 + leap(R, L) * 366;
    vector<bool> data(siz, false);
    for (int i = 0; i < n; ++i){
        cin >> tmp;
        num = data_parse(stoi(tmp.substr(0, 2)), stoi(tmp.substr(3, 2)), stoi(tmp.substr(6, 4)), L);
        if (!data[num]) {
            data[num] = true;
            count++;
        }
    }
    int r1 = siz - count;
    int l1 = 0, ans = 0;
    if (r1 <= 1){
        cout << r1;
        return 0;
    }
    int m = 0;
    while (r1 - l1 > 1){
        m = (r1 + l1) / 2;
        int i = 0;
        while (i < siz - m + 1){
            if (accumulate(data.begin() + i, data.begin() + i + m, 0) == 0){
                ans = m;
                break;
            } else {
                while (data[i] != 1)
                    i++;
            }
            i++;
        }
        if (ans == m){
            l1 = m;
        }
        else {
            r1 = m;
        }
    }
    cout << ans;
}
