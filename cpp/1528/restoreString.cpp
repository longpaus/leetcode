#include<iostream>
#include<vector>
#include<string>
using namespace std;

class Solution {
public:
    string restoreString(string s, vector<int>& indices) {
        vector<char>ans;
        for(int index:indices){
            ans.push_back(s[index]);
        }
        string l(ans.begin(), ans.end());
        return l;
    }
    
};

int main(){
   Solution test = Solution();

  
    vector<int> vect{0,1,2};
   cout << test.restoreString("abc",vect) << "\n";
}