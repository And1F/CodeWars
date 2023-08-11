import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    ans = []
    orders = orders["Customer_Id"].to_list()
    for num in range(len(customers)):
        if customers.loc[num]["id"] not in orders:
            ans.append(customers.loc[num]["name"])
    return pd.DataFrame({"Customers":ans})

customers = pd.DataFrame({"id":[1,2,3,4], "name":["Joe","Henry", "Sam", "Max"]})
order = pd.DataFrame({"Customer_Id":[3,1]})

print(find_customers(customers,order))    