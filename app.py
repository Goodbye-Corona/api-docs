from flask import Flask
from flask_restx import Api, Resource, reqparse

app = Flask(__name__)

api = Api(app, version='1.0', title='Corona-19-API', description="<b>굿바이코로나에서 제공하는 코로나바이러스감염증-19 API 입니다.</b> <br>코로나바이러스감염증-19 API 서비스 제공 - 코로나19 관련 API를 무제한 무료로 사용하세요! 🇰🇷 South Korea's COVID-19 API service provided - Use COVID-19 related API for free for unlimited !", doc="/")

covid19_api001 = api.namespace('COVID-19-INFECTION', description='코로나19 감염 정보(COVID-19 Infection Information)')
covid19_api002 = api.namespace('COVID-19-VACCINE', description='코로나19 백신접종 정보(COVID-19 Vaccination Information)')

@covid19_api001.route('/')
@covid19_api002.route('/')
class Test(Resource):
    def get(self):
    	return 'Hello World!'


if __name__ == '__main__':
    app.run()