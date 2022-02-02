fn_friends = input("Enter fortnite friends ")
fn_friends = fn_friends.split(",")
fn_list = []

for f in fn_friends:
    f = f.upper()
    fn_list.append(f)



fn_friends.sort(reverse=False)
fn_list.sort(reverse=False)
print(fn_friends)
print(fn_list)

