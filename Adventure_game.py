import time
import random


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(4)


def valid_input(prompt, options):
    while True:
        response = input(prompt).lower()
        for option in options:
            if option in response:
                return response
        print_pause("enter a valid input")


def end():
    response = valid_input("would you like to play again? (yes/no)\n", "yes "
                           "no")
    if "yes" in response:
        game()
    elif "no" in response:
        print_pause("good bye, see you on another day Mr detective")
        exit()


def game():
    evidence = []

    def site():
        print_pause("now you can take a closer look and analyze")
        while True:
            response = valid_input("1-check the car. 2-check the dead body. "
                                   "3-ask the workers around. 4-End "
                                   "investigation\n", "1,2,3,4")
            if "1" in response:
                print_pause("you see the front hull of the car as it was "
                            "damaged by some sort of axe or a tool does't seem"
                            " that another car has crashed into it also the "
                            "front windows are completely broken in addition "
                            "to the driver side window ")
                print_pause("evidence added (not killed by car accident)")
                evidence.append("not killed by car accident")
            elif "2" in response:
                print_pause("you see that there are some marks on his neck, "
                            "seems like he was suffocated not as it thought to"
                            " be a car accident. There were very some little "
                            "cuts in the neck and small fragments of wood")
                print_pause("evidence added (doesn't seem familiar to what the"
                            " serial killer usually does)")
                evidence.append("not the serial killer")
                print_pause("you also find a gun in the victim's pocket so you"
                            " take it")
                evidence.append("gun")
            elif "3" in response:
                workers = ["niels", "lucas", "lucas", "teeth"]
                worker = random.choice(workers)
                print_pause("you come across some workers so you randomly ask "
                            "some of them")
                if "niels" in worker:
                    print_pause("hello sir, I have just returned to my work "
                                "after I got called by my manger. I was "
                                "surpriesed since he told us few days ago that"
                                " our business will stop since the minister "
                                "decided to end all cutting wood activies in "
                                "that area for better envirnment")
                    evidence.append("surprise return")
                elif "lucas" in worker:
                    print_pause("don't waste your time here you will not "
                                "probably find anything, I saw the accident")
                    if "not killed by car accident" in evidence:
                        response = valid_input("1-suspect the worker. 2-leave "
                                               "him alone(1 or 2)\n", "1 2")
                        if "1" in response:
                            print_pause("He puts his hand in his pocket and "
                                        "tries to pull a gun ")
                            if "gun" in evidence:
                                print_pause("you quickly pull the gun you "
                                            "found and shoot him first")
                                if "not the serial killer" in evidence:
                                    print_pause("you send the dead body to the"
                                                " DNA lab and the blood on the"
                                                " wood fragments was identical"
                                                " to the worker's blood")
                                    print_pause("you seem to have found the "
                                                "actual killer but the serial "
                                                "killer mystery remains a "
                                                "secret, good job anyways Mr "
                                                "detective.")
                                    if "talked to william":
                                        if "surprise return" in evidence:
                                            print_pause("Though, you have very"
                                                        " great certainity "
                                                        "that william planned "
                                                        "all that to keep his "
                                                        "business going but "
                                                        "there are no enough "
                                                        "evidence against him")
                                            print_pause("you got the 2nd "
                                                        "ending")
                                            end()
                                else:
                                    print_pause("you were very surprised that "
                                                "he did that, seems like he "
                                                "might have known the serial "
                                                "killer or cooperated with him"
                                                ". Unfortunately you don't "
                                                "have the required evidence to"
                                                " prove anything, but at least"
                                                " you have helped with some "
                                                "evidence")
                                    if "talked to william":
                                        if "surprsie return" in evidence:
                                            print_pause("Though, you have very"
                                                        " great certainity "
                                                        "that william planned "
                                                        "all that to keep his "
                                                        "business going but "
                                                        "there are no enough "
                                                        "evidence against him")
                                            print_pause("you got the 3rd "
                                                        "ending")
                                            end()
                            else:
                                print_pause("he shoots you and you bleed "
                                            "to death")
                                print_pause("you got the 1st ending")
                                end()
                else:
                    print_pause("Hello sir, I don't really have an idea about "
                                "anything, You can try asking my mates around")
            else:
                break
        if "kill order" in evidence:
            print_pause("when you almost finshed your investigation you find "
                        "some worker covering his face approaching you, he "
                        "seemed suspucious. You see a pistol on his pocket "
                        "with a silencer")
            if "gun" in evidence:
                response = valid_input("1-shoot him in the leg. 2-question him"
                                       " loudly 3-try to leave quietly\n",
                                       "1,2,3")
                if "1" in response:
                    print_pause("the suspect gets injured and you start "
                                "questioning him")
                    print_pause('the suspect kept saying "do not kill me '
                                'please, I will confess with everything"')
                    print_pause("you ask him who sent you and why did you want"
                                " to kill me")
                    print_pause("he replies: Mr William sent me to kil you "
                                "because you suspected him that he killed the "
                                "minister. He threatned to kill my family if"
                                " I didn't kill you, please let me live and "
                                "help")
                    response = valid_input("1-kill him. 2-let him live\n",
                                           "1,2")
                    if "1" in response:
                        print_pause("he is dead now, your assistant saw you "
                                    "killing him and he left you for showing "
                                    "no mercy, this may affect your career in "
                                    "the future")
                        print_pause("you now realize who is behind all this, "
                                    "it is Mr william, he sent someone to kill"
                                    " the prime minstser as he did with you")
                        print_pause("you reported your evidence as soon as "
                                    "possible and Mr william had a verdict of "
                                    "guilty at the courtroom")
                        print_pause("seems like you succefully solved this "
                                    "mystery but the serial killer mystery "
                                    "remains unclear, good job anyways Mr "
                                    "detective")
                        print_pause("you got the 4th ending")
                        end()
                    elif "2" in response:
                        print_pause("you are a real hero aren't you? you send "
                                    "him to the hospital and he will be moved "
                                    "to the police station after he get cured."
                                    " You also send his family to live in a "
                                    "safe house under the police surveillance")
                        print_pause("you now realize who is behind all this, "
                                    "it is Mr william, he sent someone to kill"
                                    " the prime minstser as he did with you")
                        print_pause("you reported your evidence as soon as "
                                    "possible and Mr william had a verdict of "
                                    "guilty at the courtroom")
                        print_pause("seems like you succefully solved this "
                                    "mystery but the serial killer mystery "
                                    "remains unclear, good job anyways Mr "
                                    "detective")
                        print_pause("you got the 4th ending")
                        end()
                else:
                    print_pause("he grabs his gun and he shoots you wihout "
                                "hesitation, you are dead")
                    print_pause("you got the 5th ending")
                    end()
            else:
                response = valid_input("1-question him loudly 2-try to leave "
                                       "quietly\n", "1,2")
                if "1" or "2" in response:
                    print_pause("he grabs his gun and he shoots you wihout "
                                "hesitation, you are dead")
                    print_pause("you got the 5th ending")
                    end()
        else:
            print_pause("seems like the mystery will continue, there is no "
                        "enough evidence or witnesses to claim there is a "
                        "serial killer")
            print_pause("Thanks for your help anyways")
            end()

# the beginning of the game
    print_pause("Hello! Nice to meet you again Mr detective.")
    print_pause("There have been some cases that we couldn't solve so we need "
                "your assistance to investigate")
    print_pause("so simply we believe there is a serial killer who murders "
                "important ploticians without leaving traces")
    print_pause("We need you to figure out who this suspect might be and "
                "help us catch him")
    response = valid_input("Would you like to investigate in this case?\n",
                           "yes/no")
    if "yes" in response:
        print_pause("great sir, let's get started")
        print_pause("let me tell you the story in detail")
        print_pause("1 month ago the prime minister has been killed in his"
                    " car before he fully parks it beside his house")
        print_pause("it is believed that the prime minster had a normal "
                    "car accident but we don't think so since 2 more "
                    "politicians died by the same way last month. No one "
                    "knows about that serial killer except our local "
                    "intelligence though. We believe the killer usually "
                    "kill his victims by car crashing")
        print_pause("anyways enough talking let's go to the incident "
                    "field")
        print_pause("1 hour later")
        print_pause("we have arrived sir, let's take a closer look, I will"
                    " give you a note to gather as much evidence as you "
                    "can")
        print_pause("first thing you have noticed that the car isn't in "
                    "great condition, and both the front and right side "
                    "windows are broken")
        print_pause("then shortly you notice that there are some feet "
                    "traces leading to a small house")
        response = valid_input("follow the traces or not(yes/no)\n",
                               "yes no")
        if "yes" in response:
            print_pause("you reach the house, knock on the door but seems "
                        "like no one was answering")
            response = valid_input("1-break into the house. 2-watch the "
                                   "house from distant and wait for anyone"
                                   " to appear(1 or 2)\n", "1 2")
            if "1" in response:
                print_pause("you have broken into the house but found no "
                            "one, then you shortly you hear someone "
                            "entering the house")
                print_pause("the man was handling a gun, then he shot you"
                            " thinking you are a theif, the man tended to"
                            " be just the minister's friend")
                print_pause("Maybe next time, try be a little bit more "
                            "polite?")
                print_pause("you got the 6th ending")
                end()
            elif "2" in response:
                print_pause("after few minutes, you see a gentleman "
                            "entering the house so you knock the door to "
                            "investigate with him")
                print_pause("you knock on the door and he opens, ask him "
                            "some his questions")
                while True:
                    response = valid_input("1-who are you and your "
                                           "relation to the minister. "
                                           "2-ask him about the traces. "
                                           "3-ask him if you know anything"
                                           " about what happened 4-End the"
                                           "conversation \n", "1,2,3,4")
                    if "1" in response:
                        print_pause("I am William Forster, the minsier's "
                                    "closest friend, and I have my own "
                                    "business of cutting woods here")
                    elif "2" in response:
                        print_pause("Oh, they are from yesterday when the "
                                    "incident happened, I heard some crash"
                                    " sound then went quickly to see what "
                                    "happened")
                    elif "3" in response:
                        print_pause("well I don't know if the minster died"
                                    "by a car accident or was murdered but"
                                    "I have heard about the serial killer "
                                    "who kills and hide it as if it was "
                                    "normal accident")
                        evidence.append("knows the serial killer")
                    else:
                        evidence.append("talked to william")
                        break
                response = valid_input("1-leave Mr william. 2-suspect Mr "
                                       "william of knowing anything about "
                                       "the killer\n", "1,2")
                if "1" in response:
                    print_pause("you are back to the investigation site")
                    site()
                elif "2" in response:
                    print_pause("he got disappointed and didn't seem "
                                "pleased since you didn't have any evidnce"
                                "on him to suspect him that way")
                    evidence.append("kill order")
                    print_pause("you returned back to the investigation "
                                "site")
                    site()

            if "no" in response:
                site()
    else:
        end()


game()
