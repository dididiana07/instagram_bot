import os
from instagram_bot import InstagramBot

def main():
    my_user = os.environ["MY_PHONE_NUMBER"]
    my_password = os.environ["PASSWORD"]
    chromedriver_path = os.environ["CHROMEDRIVER_PATH"]
    bot = InstagramBot(chromedriver_path=chromedriver_path,
                       ig_user=my_user,
                       ig_password=my_password,
                       get_followers_from="selenagomez")
    bot.login_instagram()


if __name__ == "__main__":
    main()