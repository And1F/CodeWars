def calculate_cost_per_person(array: list[int], rental: int) -> dict[int, int]:
    ans = {}
    rent = 0
    for day in range(1, max(array)+1):
        rent += int(rental +0.5)
        if day in array:
            paid_rent = rent/len(array) 
            rent -= paid_rent * array.count(day) 
            ans[day] = int(paid_rent + 0.5)
            array = [x for x in array if x != day]
    print(ans)
    print(20 + 3*37 + 3*62 + 95 + 2*295)
person = [12, 20, 4, 20, 10, 10, 10, 7, 7, 7]
house_price = 50
calculate_cost_per_person(person,house_price)