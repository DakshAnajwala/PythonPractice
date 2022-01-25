fn_skins = input("Pls enter fortnite skins(comma separated): ")
fn_list = fn_skins.split(",")
print(fn_list)

for a in fn_list:
    print(a.strip())