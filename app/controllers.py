from flask import jsonify, request
from app import app, validators
from app.services import WeatherService, UserService
from app.models import UserAuth
import os
from dotenv import load_dotenv
load_dotenv()


@app.route('/weather')
def get_weather():
    if request.args.get('apikey') == os.getenv("API_KEY"):
        city = request.args.get('city')
        units = request.args.get('units')
        return jsonify({"weather": WeatherService.get_weather_by_city(city, units)})


@app.route('/login', methods=['POST'])
def login():
    email = request.json.get('email')
    password = request.json.get('password')
    login = UserService.login_user(UserAuth(email, password))
    if (login["logged"]):
        return jsonify({"status": login["status"], "token": os.getenv("API_KEY")}), 200
    return jsonify({"status": login["status"]}), 403