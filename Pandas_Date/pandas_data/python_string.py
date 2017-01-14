# conding:utf-8
val = "a,   b,    a"
list_val = [v.strip() for v in val.split(",")]
set_val = (set(v.strip()) for v in val.split(","))
set_val = set.union(*set_val)
print list_val
print set_val


