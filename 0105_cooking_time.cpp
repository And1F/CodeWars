unsigned int cookingTime(unsigned int eggs) {
    const int eggsPerBatch = 8; 
    const int timePerEgg = 5;  

    int batches = (eggs + eggsPerBatch - 1) / eggsPerBatch; 
    int totalTime = batches * timePerEgg; 

    return totalTime;
}