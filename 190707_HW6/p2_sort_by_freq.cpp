#include <iostream>
#include <vector>
#include <unordered_map>
#include <numeric>
#include <limits>

using namespace std;

vector < int > sortFrequency(vector < int > arr) {
    unordered_map<int,int> Map;
    unordered_map<int,int> order;
    for (unsigned i = 0; i < arr.size(); i++) {
        if (Map.find(arr[i]) != Map.end()) {
            Map[arr[i]] += 1;
        }
        else {
            Map.insert({arr[i], 1});
            order.insert({arr[i], i});
        }
    }
    unordered_map<int,int> count;
    vector<int> temp = {};
    vector< vector<int> > bucket(arr.size()+1, temp);
    for (unordered_map<int,int>::iterator it = Map.begin(); it != Map.end(); ++it ) {
        int c = it -> second;
        int k = it -> first;
        // printf("num=%d, count=%d\n", k, c);
        temp = bucket[c];

        int pos = 0;
        int cur_pos = order[k];
        for (unsigned i = 0; i < temp.size(); ++i) {
            if (order[temp[i]] > cur_pos) {
                pos = i;
                break;
            }
        }

        for (int i = 0; i < c; ++i) {
            temp.insert(temp.begin() + pos, k);
        }
        bucket[c] = temp;
    }
    vector<int> results;
    for (unsigned i = arr.size(); i > 0; --i) {
        if(!bucket[i].empty())
            results.insert(results.end(), bucket[i].begin(), bucket[i].end());
    }
    return results;
}


int main() {
    vector < int > res;

    vector<int> _arr = {2, 2, 2, 8, 8, 5, 5, 5, 6, 6 ,6 ,6};

    res = sortFrequency(_arr);
    for(int res_i=0; res_i < res.size(); res_i++) {
    	cout << res[res_i] << endl;;
    }

    return 0;
}
