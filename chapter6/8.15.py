"""from printing_model import printing_model as pm"""
import printing_model as pm

current_designs = [1,2,3,4,5]
unprinted_designs = [5,6,7,8,9]
pm.printing_model(unprinted_designs, current_designs)
for item in current_designs:
    print(item)

