float find_uniq(const std::vector<float> &v){
  if(v[0]!=v[1]&&v[0]!=v[2]){
    return v[0];
  }
  for(int i = 1;i <= v.size();i++){
    if(v[0] != v[i]){
      return v[i];
    }
  }
}