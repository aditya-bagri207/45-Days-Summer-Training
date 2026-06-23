import pandas as pd

data = {
    "Product": ["Laptop", "Mobile", "Headphones", "Chair", "Table",
                "Sofa", "Shirt", "Jeans", "Jacket", "Watch"],
    
    "Category": ["Electronics", "Electronics", "Electronics",
                 "Furniture", "Furniture", "Furniture",
                 "Clothing", "Clothing", "Clothing", "Accessories"],
    
    "Sales": [55000, 30000, 5000, 7000, 12000,
              25000, 2000, 3500, 4500, 8000],
    
    "Region": ["North", "South", "East", "West", "North",
               "South", "East", "West", "North", "South"]
}

df = pd.DataFrame(data)

df.to_csv("sales_csv", index = False)

df = pd.read_csv("sales_csv")
print("Original Data:")
print(df)


print("\nCategory Wise Total Sales:")
category_sales = df.groupby("Category").agg( Total_Sales=("Sales", "sum"))
print(category_sales)



print("Top three product by sales: ")
sort = df.sort_values( by="Sales", ascending=False)
top3= sort.head(3)
print(top3)