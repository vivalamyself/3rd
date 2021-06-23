default broken_leg=False
default money=100
default my_name="death"

label gfgjjk:
    menu:
        "break ":
            $  broken_leg=True
        "not broken":
            $ broken_leg=False   
    if broken_leg==True:
        "my leg is broken"
    "..........."    
    return