class Solution {
public:

    string encode(vector<string>& strs) {
        string encoded_str = "";
        for(auto& str : strs){
            encoded_str += str; encoded_str += "\n";
        }
        cout << encoded_str;
        return encoded_str;
    }

    vector<string> decode(string s) {
        vector<string> result = {};
        string curr = "";
        for(auto ch : s){
            if(ch != '\n') curr += ch;
            else {
              result.push_back(curr);
              curr = "";  
            } 
        }
        return result;
    }
};
