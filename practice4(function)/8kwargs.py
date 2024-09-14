
"""
-> keyvalue-args (kwargs)
key-value ma multiple argument ne leva
"""

def kwars_print(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{value}")
        
kwars_print(name="achyut")
kwars_print(name="achyut", surname="dhaduk")
kwars_print(name="achyut", surname="dhaduk", field="IT") 