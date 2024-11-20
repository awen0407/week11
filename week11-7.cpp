// week11-7.cpp 學習計畫basic第9題
// leetcode 1502. Can Make Arithmetic Progression From Sequence
class Solution {
public:
    bool canMakeArithmeticProgression(vector<int>& arr) {
        sort(arr.begin(), arr.end());
        int N =arr.size();
        for(int i=0;i<N-2;i++ ){
            if(arr[i]-arr[i+1] != arr[i+1]-arr[i+2])return false;
        }
        return true;
    }
};