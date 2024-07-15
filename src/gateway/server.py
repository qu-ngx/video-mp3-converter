import json
import os

import gridfs
import pika
from auth_svc import access
from flask import Flask, request
from flask_pymongo import PyMongo
from storage import util

from auth import validate

server = Flask(__name__)
server.config["MONGO_URI"] = "mongodb://host.minikube.internal:27017/videos"

mongo = PyMongo(server)

fs = gridfs.Gridfs(mongo.db)

connection = pika.BlockingConnection(pika.ConnectionParameters("rabbitmq"))
channel = connection.channel()


@server.route("/login", methods=["POST"])
def login():
    token, err = access.login(request)
