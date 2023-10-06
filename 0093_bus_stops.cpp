#include <vector>

int number(std::vector<std::pair<int, int>> busStops) {
    int totalPeople = 0;
    for (const auto& stop : busStops) {
        totalPeople += stop.first;  
        totalPeople -= stop.second; 
    }
    return totalPeople >= 0 ? totalPeople : 0; 
}
