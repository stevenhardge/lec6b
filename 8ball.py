import random


while True:
    s = input("Please Ask the 8ball a question: \n")
    if "?" == s[-1]:
        rndmList =["it is certain", " It is decidedly so","Without a doubt", "yes definitely", "you may rely on it", "as I see it, yes", "most likely", "outlook good", "yes", "signs point to yes", "reply hazy try again", "ask again later", "better not tell you now", "cannot predict now", "concentrate and ask again", "don't count on it", "my reply is no", "my sources say no", "outlook not so good"]
        random.shuffle(rndmList)
        print(rndmList[0])
        break

    else:
        pass
