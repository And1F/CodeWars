long long mygcd(long long a, long long b) {
  while (b != 0) {
    long long temp = b;
    b = a % b;
    a = temp;
  }
  return a;
}