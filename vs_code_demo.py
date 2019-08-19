# import requests


def greeting(who_to_greet):
    """Returns friendly greeting"""
    greeting = "Hello {}".format(who_to_greet)
    print(greeting)


greeting('Jason')
