import os 

# if (not os.path.exists("100 days of python")):
#     os.mkdir("100 days of python")

for i in range (0,100):
    os.rename(f"100 days of python/day{i+1}" , f"100 days of python /tutorials {i+1}")