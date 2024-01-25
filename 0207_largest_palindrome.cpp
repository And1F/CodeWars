int expand(const std::string& s, int left, int right) {
    while (left >= 0 && right < s.length() && s[left] == s[right]) {
        left--;
        right++;
    }
    return right - left - 1;
}

int longest_palindrome(const std::string &s) {
    int mx = 0;

    for (int i = 0; i < s.length(); i++) {
        mx = std::max(mx, expand(s, i, i));
        mx = std::max(mx, expand(s, i, i + 1));
    }

    return mx;
}

