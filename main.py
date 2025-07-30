import time


def main():
    # making bot
    bot_name = "__pibby__"
    centered = bot_name.center(70)
    print(centered)

# Greeting
    print("hello i am your new asistant pibby please leme know your name!! (^0^)")
    enter_name = input("please enter your name: ")
    entered_name = enter_name.strip()

# main logic
    struct_time = time.localtime()
    rtime = struct_time.tm_hour

    match rtime:
        case rtime if rtime < 12:
            print(
                f"Good morning {entered_name}!! (^0^) \n {time.asctime(struct_time)} ")
        case rtime if rtime >= 12 and rtime <= 15:
            print(
                f"good afternoon {entered_name} !! (^0^) \n {time.asctime(struct_time)}")
        case rtime if rtime >= 17 and rtime <= 19:
            print(
                f"good evening {entered_name}!! (^0^) \n {time.asctime(struct_time)}")
        case rtime if rtime >= 17 and rtime < 22:
            print(
                f"oi..dont forget to have dinner!!(-o-) \n {time.asctime(struct_time)}")
        case rtime if rtime >= 22:
            print(
                f"Its getting late dont you wanna sleep.......(-_-) \n {time.asctime(struct_time)}")


if __name__ == "__main__":
    main()
