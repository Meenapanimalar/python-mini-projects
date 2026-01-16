def add(*args):
    return args

print(list(add(5,6)))
def commit( status, with_love = "love" ):

    if status == True:
        print(f"Committed with {with_love}")

commit(True)