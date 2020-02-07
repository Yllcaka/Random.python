def pyetsori(pyetja,pergjigjet,sakt):
    print(pyetja)
    for k,v in pergjigjet.items():
        print(f"{k}) {v}")
    while True:
        put = input("Pergjigjia e juaj eshte: ").lower().strip()
        if put == sakt or put == pergjigjiet[sakt]:
            print("Pergjigjia e jote eshte e sakt")
            return 1
        elif put in pergjigjiet or put in pergjigjiet.values():
            print("Pergjigjia e pasakt")
            return 0
        else:
            print("Pergjigjia nuk ekziston \n")
            print(pyetja)
            for k , v in pergjigjet.items():
                print(f"{k}) {v}")

pyetja1 = "Sa eshte masa relative molekulare e amoniakut?"
pergjigjiet1 = {"a":"","b":"","c":"","d":"","e":""}
pyetja2 = "Cili eshte shteti me me se shumti banore?"
pergjigjiet2 = {"a":"","b":"","c":"","d":"","e":""}
pyetja3 = "Nga cili shtet rrjedh fjala Kimi?"
pergjigjiet3 = {"a":"","b":"","c":"","d":"","e":""}
pyetja4 = "Ne cilin vit udhetoi Magelani rreth botes?"
pergjigjiet4 = {"a":"","b":"","c":"","d":"","e":""}
pyetja5 = "Qfare domethenie ka fjala Iskender?"
pergjigjiet5 = {"a":"","b":"","c":"","d":"","e":""}
pyetja6 = "Kush e vrau Esat Pashe Toptanin?"
pergjigjiet6 = {"a":"","b":"","c":"","d":"","e":""}
pyetja7 = "Shkruhet ndryshe lexohet ndryshe?"
pergjigjiet7 = {"a":"","b":"","c":"","d":"","e":""}
pyetja8 = "Sa bejne 2+2*2?"
pergjigjiet8 = {"a":"","b":"","c":"","d":"","e":""}
pyetja9 = "Sa perqind % natrium ka trupi?"
pergjigjiet9 = {"a":"","b":"","c":"","d":"","e":""}
pyetja10 = "Qka eshte Tautonomia?"
pergjigjiet10 = {"a":"","b":"","c":"","d":"","e":""}

pyetjet = [pyetja1,pyetja2,pyetja3,pyetja4,pyetja5,pyetja6,pyetja7,pyetja8,pyetja9,pyetja10]
stuff = [pergjigjiet1,pergjigjiet2,pergjigjiet3,pergjigjiet4,pergjigjiet5,pergjigjiet6,pergjigjiet7,pergjigjiet8,pergjigjiet9,pergjigjiet10]
# print(pergjigjiet["d"])
piket = 0
for i in stuff:
    piket += pyetsori(i)
    print(f"Piket e tuaja jane {piket}")

print(f"Piket totale jane {piket}")