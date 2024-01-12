#include <string>
#include <algorithm>

std::string password_gen() {
    const std::string lower = "abcdefghijklmnopqrstuvwxyz";
    const std::string upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    const std::string numbers = "0123456789";

    const std::string chars = lower + upper + numbers;

    std::string password;

    unsigned int len = std::rand() % 15 + 6;

    password += lower[std::rand() % lower.size()];
    password += upper[std::rand() % upper.size()];
    password += numbers[std::rand() % numbers.size()];

    while (password.size() < len) {
        char c = chars[std::rand() % chars.size()];
        if (std::count(password.begin(), password.end(), c) < 1) {
            password += c;
        }
    }
    std::random_shuffle(password.begin(), password.end());

    return password;
}