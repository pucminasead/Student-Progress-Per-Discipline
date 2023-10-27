from canvasapi import Canvas
from decouple import config


CANVAS = Canvas(config("API_URL"), config("API_KEY"))
