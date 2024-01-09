#include <string>
#include <vector>

std::string removeDuplicateWords(const std::string& str) {
    std::vector<std::string> v;
  
    unsigned int s = 0;
    for (unsigned int i = 0; i < str.size(); i++) {
        if (str.at(i) == ' ') {
            v.push_back(str.substr(s, i - s));
            s = i + 1;  // Move s to the beginning of the next word
        }
    }
    v.push_back(str.substr(s, str.size() - s));
  
    std::vector<std::string> uniqueWords;
    for (const auto& word : v) {
        if (std::find(uniqueWords.begin(), uniqueWords.end(), word) == uniqueWords.end()) {
            uniqueWords.push_back(word);
        }
    }
    std::string result;
    for (const auto& word : uniqueWords) {
        result += word + " ";
    }

    result.pop_back();

    return result;
}