std::pair<std::size_t, std::size_t> two_sum(const std::vector<int>& numbers, int target) {
  for(int ans1 = 0;ans1 < numbers.size();ans1++){
    for(int ans2 = 0;ans2 < numbers.size();ans2++){
      if(ans1==ans2) continue;
      else if(numbers[ans1] + numbers[ans2] == target) return {ans1, ans2};
    }
  }
}