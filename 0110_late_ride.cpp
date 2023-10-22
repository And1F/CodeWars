#include <iostream>

int lateRide(int n) {
    int hours = n / 60;
    int minutes = n % 60;

    int digitSum = 0;
    while (hours > 0) {
        digitSum += hours % 10;
        hours /= 10;
    }
    while (minutes > 0) {
        digitSum += minutes % 10;
        minutes /= 10;
    }

    return digitSum;
}