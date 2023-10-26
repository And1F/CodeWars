#include <iostream>
#include <string>

std::string to24HourTime(int hour, int minute, const std::string& period) {
    if (period == "am" && hour == 12) {
        hour = 0; 
    } else if (period == "pm" && hour != 12) {
        hour += 12;
    }
    char result[5];
    sprintf(result, "%02d%02d", hour, minute);
    return std::string(result);
}