import telepot


def main():
    bot = telepot.Bot('TOKEN')
    print(bot.getMe())


if __name__ == '__main__':
    main()
