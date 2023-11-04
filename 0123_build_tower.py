def tower_builder(n_floors):
     return [(n_floors-x)*" "+(2*x-1)*"*"+(n_floors-x)*" " for x in range(1,n_floors+1)]
