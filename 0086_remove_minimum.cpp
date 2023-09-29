#include <vector>

std::vector<unsigned int> removeSmallest(const std::vector<unsigned int>& numbers) {
    std::vector<unsigned int> ans;  
    unsigned int min = 2147483647;
    bool first = true;
    for (unsigned int i = 0; i < numbers.size(); i++) {
        if (numbers[i] < min) {
            min = numbers[i];
        }
    }
    for (unsigned int i = 0; i < numbers.size(); i++){
        if(numbers[i] == min && first){
            first = false;
        }
        else{
            ans.push_back(numbers[i]);
        }
    }
    

    return ans;
}
