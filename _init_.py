
from ChatResponse import ChatResponse


class _init_:



    flag = True
    print("ROBO: My name is Robo. I will answer your queries about Chatbots. If you want to exit, type Bye!")
    while (flag == True):
        user_response = input()
        user_response = user_response.lower()
        if (user_response != 'bye'):
            if (user_response == 'thanks' or user_response == 'thank you'):
                flag = False
                print("ROBO: You are welcome..")
            else:
                if (ChatResponse.greeting(user_response) != None):
                    print("ROBO: " + ChatResponse.greeting(user_response))
                else:
                    print("ROBO: ", end="")
                    print(ChatResponse.response(user_response))
                    ChatResponse.sent_token.remove(user_response)
        else:
            flag = False
            print("ROBO: Bye! take care..")