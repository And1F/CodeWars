def tower_builder(n_floors, block_size):
    return [((n_floors-((x // block_size[1])+1))*block_size[0])*" " + 
            (((2*(x // block_size[1])+1))*block_size[0])*"*" + 
            ((n_floors-((x // block_size[1])+1))*block_size[0])*" "           
            for x in range(n_floors * block_size[1])]
