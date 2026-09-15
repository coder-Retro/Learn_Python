data = ["cat", "elephant", 12, "dog", "python", 5, "ai"]
ans = list(filter(lambda x: type(x)==str and len(x)>4,data))
print(f"String with len greater than 4: {ans}")