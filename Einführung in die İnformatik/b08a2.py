
#bo8a2
def zusammenfuehren(w1, w2):
    new_Wb = {}
    # zuerst W1
    for key in w1:

        if key in w2:

            new_Wb[key] = (w1[key],w2[key])
        else:
            new_Wb[key] = w1[key]

    # danach nur die in W2
    for key in w2:
         if key not in new_Wb:
             new_Wb[key] = w2[key]
    return new_Wb


print(zusammenfuehren({"apfel": 12, "birne": 7}, {"apfel": "KI.B", "kirsche": "KI.A"}))
