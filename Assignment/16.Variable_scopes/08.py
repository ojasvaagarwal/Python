# name = "Asha"
# def show():
#     print(name)
#     name = "Ravi"
# show()

# Why this raises an error (UnboundLocalError):
# Because name = "Ravi" is inside show(), Python treats name as a local variable for the entire function.
# When print(name) runs before name is assigned locally, Python sees a local variable with no value yet and raises UnboundLocalError.
