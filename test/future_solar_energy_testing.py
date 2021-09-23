from unittest.mock import Mock, patch
from requests.exceptions import Timeout
from app.calculator import *
import unittest


class TestFutureSolar(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    @patch('app.calculator.Calculator.get_weather_data')
    def test_1(self,mocked_get):
        """
            solar_testing
            condition: This path is when the start time and end time is not within daylight length, thus it will return directly as there will be no solar energy generated
        """
        mocked_response = Mock()
        data = {"date":"2021-02-22","sunrise":"05:44:00","sunset":"19:06:00","moonrise":"15:43:00","moonset":"00:01:00","moonPhase":"Waxing Gibbous","moonIlluminationPct":73,"minTempC":9,"maxTempC":21,"avgTempC":17,"sunHours":5.3,"uvIndex":5,"location":{"id":"22d72902-b72f-4ca0-a522-4dbfb77a7b78","postcode":"7250","name":"BLACKSTONE HEIGHTS","state":"TAS","latitude":"-41.46","longitude":"147.0820001","distanceToNearestWeatherStationMetres":5607.391317385195,"nearestWeatherStation":{"name":"LAUNCESTON (TI TREE BEND)","state":"TAS","latitude":"-41.4194","longitude":"147.1219"}},"hourlyWeatherHistory":[{"hour":0,"tempC":13,"weatherDesc":"Partly cloudy","cloudCoverPct":1,"uvIndex":1,"windspeedKph":2,"windDirectionDeg":232,"windDirectionCompass":"SW","precipitationMm":0,"humidityPct":89,"visibilityKm":10,"pressureMb":1007},{"hour":1,"tempC":12,"weatherDesc":"Partly cloudy","cloudCoverPct":3,"uvIndex":1,"windspeedKph":2,"windDirectionDeg":258,"windDirectionCompass":"WSW","precipitationMm":0,"humidityPct":91,"visibilityKm":8,"pressureMb":1007},{"hour":2,"tempC":11,"weatherDesc":"Clear","cloudCoverPct":6,"uvIndex":1,"windspeedKph":3,"windDirectionDeg":284,"windDirectionCompass":"WNW","precipitationMm":0,"humidityPct":93,"visibilityKm":6,"pressureMb":1006},{"hour":3,"tempC":9,"weatherDesc":"Clear","cloudCoverPct":9,"uvIndex":1,"windspeedKph":3,"windDirectionDeg":310,"windDirectionCompass":"NW","precipitationMm":0,"humidityPct":95,"visibilityKm":5,"pressureMb":1006},{"hour":4,"tempC":10,"weatherDesc":"Clear","cloudCoverPct":7,"uvIndex":1,"windspeedKph":4,"windDirectionDeg":314,"windDirectionCompass":"NW","precipitationMm":0,"humidityPct":93,"visibilityKm":6,"pressureMb":1006},{"hour":5,"tempC":10,"weatherDesc":"Mist","cloudCoverPct":6,"uvIndex":1,"windspeedKph":4,"windDirectionDeg":319,"windDirectionCompass":"NW","precipitationMm":0,"humidityPct":90,"visibilityKm":6,"pressureMb":1006},{"hour":6,"tempC":10,"weatherDesc":"Mist","cloudCoverPct":4,"uvIndex":3,"windspeedKph":4,"windDirectionDeg":324,"windDirectionCompass":"NW","precipitationMm":0,"humidityPct":88,"visibilityKm":7,"pressureMb":1007},{"hour":7,"tempC":12,"weatherDesc":"Mist","cloudCoverPct":3,"uvIndex":3,"windspeedKph":6,"windDirectionDeg":313,"windDirectionCompass":"NW","precipitationMm":0,"humidityPct":78,"visibilityKm":8,"pressureMb":1007},{"hour":8,"tempC":14,"weatherDesc":"Sunny","cloudCoverPct":1,"uvIndex":4,"windspeedKph":7,"windDirectionDeg":303,"windDirectionCompass":"WNW","precipitationMm":0,"humidityPct":68,"visibilityKm":9,"pressureMb":1007},{"hour":9,"tempC":16,"weatherDesc":"Sunny","cloudCoverPct":0,"uvIndex":5,"windspeedKph":8,"windDirectionDeg":292,"windDirectionCompass":"WNW","precipitationMm":0,"humidityPct":58,"visibilityKm":10,"pressureMb":1007},{"hour":10,"tempC":18,"weatherDesc":"Sunny","cloudCoverPct":6,"uvIndex":5,"windspeedKph":10,"windDirectionDeg":286,"windDirectionCompass":"WNW","precipitationMm":0,"humidityPct":52,"visibilityKm":10,"pressureMb":1007},{"hour":11,"tempC":19,"weatherDesc":"Sunny","cloudCoverPct":12,"uvIndex":5,"windspeedKph":11,"windDirectionDeg":281,"windDirectionCompass":"W","precipitationMm":0,"humidityPct":45,"visibilityKm":10,"pressureMb":1007},{"hour":12,"tempC":21,"weatherDesc":"Sunny","cloudCoverPct":17,"uvIndex":6,"windspeedKph":13,"windDirectionDeg":275,"windDirectionCompass":"W","precipitationMm":0,"humidityPct":39,"visibilityKm":10,"pressureMb":1007},{"hour":13,"tempC":20,"weatherDesc":"Sunny","cloudCoverPct":19,"uvIndex":6,"windspeedKph":14,"windDirectionDeg":270,"windDirectionCompass":"W","precipitationMm":0,"humidityPct":38,"visibilityKm":10,"pressureMb":1007},{"hour":14,"tempC":20,"weatherDesc":"Partly cloudy","cloudCoverPct":20,"uvIndex":5,"windspeedKph":15,"windDirectionDeg":264,"windDirectionCompass":"W","precipitationMm":0,"humidityPct":38,"visibilityKm":10,"pressureMb":1007},{"hour":15,"tempC":20,"weatherDesc":"Partly cloudy","cloudCoverPct":22,"uvIndex":5,"windspeedKph":16,"windDirectionDeg":259,"windDirectionCompass":"WSW","precipitationMm":0,"humidityPct":37,"visibilityKm":10,"pressureMb":1007},{"hour":16,"tempC":18,"weatherDesc":"Partly cloudy","cloudCoverPct":20,"uvIndex":5,"windspeedKph":15,"windDirectionDeg":255,"windDirectionCompass":"WSW","precipitationMm":0,"humidityPct":39,"visibilityKm":10,"pressureMb":1008},{"hour":17,"tempC":17,"weatherDesc":"Partly cloudy","cloudCoverPct":18,"uvIndex":5,"windspeedKph":14,"windDirectionDeg":251,"windDirectionCompass":"WSW","precipitationMm":0,"humidityPct":42,"visibilityKm":10,"pressureMb":1008},{"hour":18,"tempC":16,"weatherDesc":"Partly cloudy","cloudCoverPct":16,"uvIndex":1,"windspeedKph":13,"windDirectionDeg":247,"windDirectionCompass":"WSW","precipitationMm":0,"humidityPct":44,"visibilityKm":10,"pressureMb":1009},{"hour":19,"tempC":15,"weatherDesc":"Partly cloudy","cloudCoverPct":14,"uvIndex":1,"windspeedKph":11,"windDirectionDeg":237,"windDirectionCompass":"WSW","precipitationMm":0,"humidityPct":50,"visibilityKm":10,"pressureMb":1010},{"hour":20,"tempC":13,"weatherDesc":"Partly cloudy","cloudCoverPct":11,"uvIndex":1,"windspeedKph":9,"windDirectionDeg":227,"windDirectionCompass":"SW","precipitationMm":0,"humidityPct":55,"visibilityKm":10,"pressureMb":1011},{"hour":21,"tempC":12,"weatherDesc":"Partly cloudy","cloudCoverPct":9,"uvIndex":1,"windspeedKph":7,"windDirectionDeg":217,"windDirectionCompass":"SW","precipitationMm":0,"humidityPct":60,"visibilityKm":10,"pressureMb":1012},{"hour":22,"tempC":11,"weatherDesc":"Partly cloudy","cloudCoverPct":7,"uvIndex":1,"windspeedKph":6,"windDirectionDeg":212,"windDirectionCompass":"SSW","precipitationMm":0,"humidityPct":64,"visibilityKm":10,"pressureMb":1012},{"hour":23,"tempC":9,"weatherDesc":"Partly cloudy","cloudCoverPct":5,"uvIndex":1,"windspeedKph":4,"windDirectionDeg":207,"windDirectionCompass":"SSW","precipitationMm":0,"humidityPct":68,"visibilityKm":10,"pressureMb":1012}]}
        mocked_response.json.return_value = data
        mocked_get.return_value = mocked_response

        start_time = datetime(2021, 2, 22, 1, 30)
        end_time = datetime(2021, 2, 22, 2, 15)
        postcode = "7250"
        solar_energy_generated = self.calculator.calculate_solar_energy_future(
            start_time, end_time, postcode)
        expected_result = 0
        self.assertAlmostEqual(solar_energy_generated, expected_result, msg=("Expected %s, got %s instead"
                                                                                         % (expected_result, solar_energy_generated)))
    
    @patch('app.calculator.Calculator.get_weather_data')
    def test_2(self,mocked_get):
        """
            solar_testing
            condition: This path is when the start time hour is the same as sunrise hour but the start time minute is smaller than the sunrise minute,
            it will update the value of start time. Then, path 8-9-10 will not be possible as path 8-9-10 indicates the start time to end time is a whole hour, 
            which won’t happen as if the start time minute is smaller than sunrise minute it won’t be a whole hour.
        """
        mocked_response = Mock()
        data = {"date":"2021-02-22","sunrise":"05:44:00","sunset":"19:06:00","moonrise":"15:43:00","moonset":"00:01:00","moonPhase":"Waxing Gibbous","moonIlluminationPct":73,"minTempC":9,"maxTempC":21,"avgTempC":17,"sunHours":5.3,"uvIndex":5,"location":{"id":"22d72902-b72f-4ca0-a522-4dbfb77a7b78","postcode":"7250","name":"BLACKSTONE HEIGHTS","state":"TAS","latitude":"-41.46","longitude":"147.0820001","distanceToNearestWeatherStationMetres":5607.391317385195,"nearestWeatherStation":{"name":"LAUNCESTON (TI TREE BEND)","state":"TAS","latitude":"-41.4194","longitude":"147.1219"}},"hourlyWeatherHistory":[{"hour":0,"tempC":13,"weatherDesc":"Partly cloudy","cloudCoverPct":1,"uvIndex":1,"windspeedKph":2,"windDirectionDeg":232,"windDirectionCompass":"SW","precipitationMm":0,"humidityPct":89,"visibilityKm":10,"pressureMb":1007},{"hour":1,"tempC":12,"weatherDesc":"Partly cloudy","cloudCoverPct":3,"uvIndex":1,"windspeedKph":2,"windDirectionDeg":258,"windDirectionCompass":"WSW","precipitationMm":0,"humidityPct":91,"visibilityKm":8,"pressureMb":1007},{"hour":2,"tempC":11,"weatherDesc":"Clear","cloudCoverPct":6,"uvIndex":1,"windspeedKph":3,"windDirectionDeg":284,"windDirectionCompass":"WNW","precipitationMm":0,"humidityPct":93,"visibilityKm":6,"pressureMb":1006},{"hour":3,"tempC":9,"weatherDesc":"Clear","cloudCoverPct":9,"uvIndex":1,"windspeedKph":3,"windDirectionDeg":310,"windDirectionCompass":"NW","precipitationMm":0,"humidityPct":95,"visibilityKm":5,"pressureMb":1006},{"hour":4,"tempC":10,"weatherDesc":"Clear","cloudCoverPct":7,"uvIndex":1,"windspeedKph":4,"windDirectionDeg":314,"windDirectionCompass":"NW","precipitationMm":0,"humidityPct":93,"visibilityKm":6,"pressureMb":1006},{"hour":5,"tempC":10,"weatherDesc":"Mist","cloudCoverPct":6,"uvIndex":1,"windspeedKph":4,"windDirectionDeg":319,"windDirectionCompass":"NW","precipitationMm":0,"humidityPct":90,"visibilityKm":6,"pressureMb":1006},{"hour":6,"tempC":10,"weatherDesc":"Mist","cloudCoverPct":4,"uvIndex":3,"windspeedKph":4,"windDirectionDeg":324,"windDirectionCompass":"NW","precipitationMm":0,"humidityPct":88,"visibilityKm":7,"pressureMb":1007},{"hour":7,"tempC":12,"weatherDesc":"Mist","cloudCoverPct":3,"uvIndex":3,"windspeedKph":6,"windDirectionDeg":313,"windDirectionCompass":"NW","precipitationMm":0,"humidityPct":78,"visibilityKm":8,"pressureMb":1007},{"hour":8,"tempC":14,"weatherDesc":"Sunny","cloudCoverPct":1,"uvIndex":4,"windspeedKph":7,"windDirectionDeg":303,"windDirectionCompass":"WNW","precipitationMm":0,"humidityPct":68,"visibilityKm":9,"pressureMb":1007},{"hour":9,"tempC":16,"weatherDesc":"Sunny","cloudCoverPct":0,"uvIndex":5,"windspeedKph":8,"windDirectionDeg":292,"windDirectionCompass":"WNW","precipitationMm":0,"humidityPct":58,"visibilityKm":10,"pressureMb":1007},{"hour":10,"tempC":18,"weatherDesc":"Sunny","cloudCoverPct":6,"uvIndex":5,"windspeedKph":10,"windDirectionDeg":286,"windDirectionCompass":"WNW","precipitationMm":0,"humidityPct":52,"visibilityKm":10,"pressureMb":1007},{"hour":11,"tempC":19,"weatherDesc":"Sunny","cloudCoverPct":12,"uvIndex":5,"windspeedKph":11,"windDirectionDeg":281,"windDirectionCompass":"W","precipitationMm":0,"humidityPct":45,"visibilityKm":10,"pressureMb":1007},{"hour":12,"tempC":21,"weatherDesc":"Sunny","cloudCoverPct":17,"uvIndex":6,"windspeedKph":13,"windDirectionDeg":275,"windDirectionCompass":"W","precipitationMm":0,"humidityPct":39,"visibilityKm":10,"pressureMb":1007},{"hour":13,"tempC":20,"weatherDesc":"Sunny","cloudCoverPct":19,"uvIndex":6,"windspeedKph":14,"windDirectionDeg":270,"windDirectionCompass":"W","precipitationMm":0,"humidityPct":38,"visibilityKm":10,"pressureMb":1007},{"hour":14,"tempC":20,"weatherDesc":"Partly cloudy","cloudCoverPct":20,"uvIndex":5,"windspeedKph":15,"windDirectionDeg":264,"windDirectionCompass":"W","precipitationMm":0,"humidityPct":38,"visibilityKm":10,"pressureMb":1007},{"hour":15,"tempC":20,"weatherDesc":"Partly cloudy","cloudCoverPct":22,"uvIndex":5,"windspeedKph":16,"windDirectionDeg":259,"windDirectionCompass":"WSW","precipitationMm":0,"humidityPct":37,"visibilityKm":10,"pressureMb":1007},{"hour":16,"tempC":18,"weatherDesc":"Partly cloudy","cloudCoverPct":20,"uvIndex":5,"windspeedKph":15,"windDirectionDeg":255,"windDirectionCompass":"WSW","precipitationMm":0,"humidityPct":39,"visibilityKm":10,"pressureMb":1008},{"hour":17,"tempC":17,"weatherDesc":"Partly cloudy","cloudCoverPct":18,"uvIndex":5,"windspeedKph":14,"windDirectionDeg":251,"windDirectionCompass":"WSW","precipitationMm":0,"humidityPct":42,"visibilityKm":10,"pressureMb":1008},{"hour":18,"tempC":16,"weatherDesc":"Partly cloudy","cloudCoverPct":16,"uvIndex":1,"windspeedKph":13,"windDirectionDeg":247,"windDirectionCompass":"WSW","precipitationMm":0,"humidityPct":44,"visibilityKm":10,"pressureMb":1009},{"hour":19,"tempC":15,"weatherDesc":"Partly cloudy","cloudCoverPct":14,"uvIndex":1,"windspeedKph":11,"windDirectionDeg":237,"windDirectionCompass":"WSW","precipitationMm":0,"humidityPct":50,"visibilityKm":10,"pressureMb":1010},{"hour":20,"tempC":13,"weatherDesc":"Partly cloudy","cloudCoverPct":11,"uvIndex":1,"windspeedKph":9,"windDirectionDeg":227,"windDirectionCompass":"SW","precipitationMm":0,"humidityPct":55,"visibilityKm":10,"pressureMb":1011},{"hour":21,"tempC":12,"weatherDesc":"Partly cloudy","cloudCoverPct":9,"uvIndex":1,"windspeedKph":7,"windDirectionDeg":217,"windDirectionCompass":"SW","precipitationMm":0,"humidityPct":60,"visibilityKm":10,"pressureMb":1012},{"hour":22,"tempC":11,"weatherDesc":"Partly cloudy","cloudCoverPct":7,"uvIndex":1,"windspeedKph":6,"windDirectionDeg":212,"windDirectionCompass":"SSW","precipitationMm":0,"humidityPct":64,"visibilityKm":10,"pressureMb":1012},{"hour":23,"tempC":9,"weatherDesc":"Partly cloudy","cloudCoverPct":5,"uvIndex":1,"windspeedKph":4,"windDirectionDeg":207,"windDirectionCompass":"SSW","precipitationMm":0,"humidityPct":68,"visibilityKm":10,"pressureMb":1012}]}
        mocked_response.json.return_value = data
        mocked_get.return_value = mocked_response

        start_time = datetime(2021, 2, 22, 5, 00)
        end_time = datetime(2021, 2, 22, 6, 00)
        postcode = "7250"
        solar_energy_generated = self.calculator.calculate_solar_energy_future(
            start_time, end_time, postcode)
        expected_result = 0.99
        self.assertAlmostEqual(solar_energy_generated, expected_result, delta=0.01, msg=("Expected %s, got %s instead"
                                                                                         % (expected_result, solar_energy_generated)))
    
    @patch('app.calculator.Calculator.get_weather_data')
    def test_3(self,mocked_get):
        """
            solar_testing
            condition: This path is when the end time hour is the same as sunset hour but the end time minute is larger than the sunset minute, 
            it will update the value of end time. Then, path 8-9-10 will not be possible as path 8-9-10 indicates the start time to end time is a whole hour, 
            which won’t happen as if the end time minute is smaller than sunset minute it won’t be a whole hour.
        """
        data_2021 = {"date":"2021-02-22","sunrise":"05:44:00","sunset":"19:06:00","moonrise":"15:43:00","moonset":"00:01:00","moonPhase":"Waxing Gibbous","moonIlluminationPct":73,"minTempC":9,"maxTempC":21,"avgTempC":17,"sunHours":5.3,"uvIndex":5,"location":{"id":"22d72902-b72f-4ca0-a522-4dbfb77a7b78","postcode":"7250","name":"BLACKSTONE HEIGHTS","state":"TAS","latitude":"-41.46","longitude":"147.0820001","distanceToNearestWeatherStationMetres":5607.391317385195,"nearestWeatherStation":{"name":"LAUNCESTON (TI TREE BEND)","state":"TAS","latitude":"-41.4194","longitude":"147.1219"}},"hourlyWeatherHistory":[{"hour":0,"tempC":13,"weatherDesc":"Partly cloudy","cloudCoverPct":1,"uvIndex":1,"windspeedKph":2,"windDirectionDeg":232,"windDirectionCompass":"SW","precipitationMm":0,"humidityPct":89,"visibilityKm":10,"pressureMb":1007},{"hour":1,"tempC":12,"weatherDesc":"Partly cloudy","cloudCoverPct":3,"uvIndex":1,"windspeedKph":2,"windDirectionDeg":258,"windDirectionCompass":"WSW","precipitationMm":0,"humidityPct":91,"visibilityKm":8,"pressureMb":1007},{"hour":2,"tempC":11,"weatherDesc":"Clear","cloudCoverPct":6,"uvIndex":1,"windspeedKph":3,"windDirectionDeg":284,"windDirectionCompass":"WNW","precipitationMm":0,"humidityPct":93,"visibilityKm":6,"pressureMb":1006},{"hour":3,"tempC":9,"weatherDesc":"Clear","cloudCoverPct":9,"uvIndex":1,"windspeedKph":3,"windDirectionDeg":310,"windDirectionCompass":"NW","precipitationMm":0,"humidityPct":95,"visibilityKm":5,"pressureMb":1006},{"hour":4,"tempC":10,"weatherDesc":"Clear","cloudCoverPct":7,"uvIndex":1,"windspeedKph":4,"windDirectionDeg":314,"windDirectionCompass":"NW","precipitationMm":0,"humidityPct":93,"visibilityKm":6,"pressureMb":1006},{"hour":5,"tempC":10,"weatherDesc":"Mist","cloudCoverPct":6,"uvIndex":1,"windspeedKph":4,"windDirectionDeg":319,"windDirectionCompass":"NW","precipitationMm":0,"humidityPct":90,"visibilityKm":6,"pressureMb":1006},{"hour":6,"tempC":10,"weatherDesc":"Mist","cloudCoverPct":4,"uvIndex":3,"windspeedKph":4,"windDirectionDeg":324,"windDirectionCompass":"NW","precipitationMm":0,"humidityPct":88,"visibilityKm":7,"pressureMb":1007},{"hour":7,"tempC":12,"weatherDesc":"Mist","cloudCoverPct":3,"uvIndex":3,"windspeedKph":6,"windDirectionDeg":313,"windDirectionCompass":"NW","precipitationMm":0,"humidityPct":78,"visibilityKm":8,"pressureMb":1007},{"hour":8,"tempC":14,"weatherDesc":"Sunny","cloudCoverPct":1,"uvIndex":4,"windspeedKph":7,"windDirectionDeg":303,"windDirectionCompass":"WNW","precipitationMm":0,"humidityPct":68,"visibilityKm":9,"pressureMb":1007},{"hour":9,"tempC":16,"weatherDesc":"Sunny","cloudCoverPct":0,"uvIndex":5,"windspeedKph":8,"windDirectionDeg":292,"windDirectionCompass":"WNW","precipitationMm":0,"humidityPct":58,"visibilityKm":10,"pressureMb":1007},{"hour":10,"tempC":18,"weatherDesc":"Sunny","cloudCoverPct":6,"uvIndex":5,"windspeedKph":10,"windDirectionDeg":286,"windDirectionCompass":"WNW","precipitationMm":0,"humidityPct":52,"visibilityKm":10,"pressureMb":1007},{"hour":11,"tempC":19,"weatherDesc":"Sunny","cloudCoverPct":12,"uvIndex":5,"windspeedKph":11,"windDirectionDeg":281,"windDirectionCompass":"W","precipitationMm":0,"humidityPct":45,"visibilityKm":10,"pressureMb":1007},{"hour":12,"tempC":21,"weatherDesc":"Sunny","cloudCoverPct":17,"uvIndex":6,"windspeedKph":13,"windDirectionDeg":275,"windDirectionCompass":"W","precipitationMm":0,"humidityPct":39,"visibilityKm":10,"pressureMb":1007},{"hour":13,"tempC":20,"weatherDesc":"Sunny","cloudCoverPct":19,"uvIndex":6,"windspeedKph":14,"windDirectionDeg":270,"windDirectionCompass":"W","precipitationMm":0,"humidityPct":38,"visibilityKm":10,"pressureMb":1007},{"hour":14,"tempC":20,"weatherDesc":"Partly cloudy","cloudCoverPct":20,"uvIndex":5,"windspeedKph":15,"windDirectionDeg":264,"windDirectionCompass":"W","precipitationMm":0,"humidityPct":38,"visibilityKm":10,"pressureMb":1007},{"hour":15,"tempC":20,"weatherDesc":"Partly cloudy","cloudCoverPct":22,"uvIndex":5,"windspeedKph":16,"windDirectionDeg":259,"windDirectionCompass":"WSW","precipitationMm":0,"humidityPct":37,"visibilityKm":10,"pressureMb":1007},{"hour":16,"tempC":18,"weatherDesc":"Partly cloudy","cloudCoverPct":20,"uvIndex":5,"windspeedKph":15,"windDirectionDeg":255,"windDirectionCompass":"WSW","precipitationMm":0,"humidityPct":39,"visibilityKm":10,"pressureMb":1008},{"hour":17,"tempC":17,"weatherDesc":"Partly cloudy","cloudCoverPct":18,"uvIndex":5,"windspeedKph":14,"windDirectionDeg":251,"windDirectionCompass":"WSW","precipitationMm":0,"humidityPct":42,"visibilityKm":10,"pressureMb":1008},{"hour":18,"tempC":16,"weatherDesc":"Partly cloudy","cloudCoverPct":16,"uvIndex":1,"windspeedKph":13,"windDirectionDeg":247,"windDirectionCompass":"WSW","precipitationMm":0,"humidityPct":44,"visibilityKm":10,"pressureMb":1009},{"hour":19,"tempC":15,"weatherDesc":"Partly cloudy","cloudCoverPct":14,"uvIndex":1,"windspeedKph":11,"windDirectionDeg":237,"windDirectionCompass":"WSW","precipitationMm":0,"humidityPct":50,"visibilityKm":10,"pressureMb":1010},{"hour":20,"tempC":13,"weatherDesc":"Partly cloudy","cloudCoverPct":11,"uvIndex":1,"windspeedKph":9,"windDirectionDeg":227,"windDirectionCompass":"SW","precipitationMm":0,"humidityPct":55,"visibilityKm":10,"pressureMb":1011},{"hour":21,"tempC":12,"weatherDesc":"Partly cloudy","cloudCoverPct":9,"uvIndex":1,"windspeedKph":7,"windDirectionDeg":217,"windDirectionCompass":"SW","precipitationMm":0,"humidityPct":60,"visibilityKm":10,"pressureMb":1012},{"hour":22,"tempC":11,"weatherDesc":"Partly cloudy","cloudCoverPct":7,"uvIndex":1,"windspeedKph":6,"windDirectionDeg":212,"windDirectionCompass":"SSW","precipitationMm":0,"humidityPct":64,"visibilityKm":10,"pressureMb":1012},{"hour":23,"tempC":9,"weatherDesc":"Partly cloudy","cloudCoverPct":5,"uvIndex":1,"windspeedKph":4,"windDirectionDeg":207,"windDirectionCompass":"SSW","precipitationMm":0,"humidityPct":68,"visibilityKm":10,"pressureMb":1012}]}
        data_2020 = {"date":"2020-02-22","sunrise":"05:43:00","sunset":"19:07:00","moonrise":"03:51:00","moonset":"18:42:00","moonPhase":"New Moon","moonIlluminationPct":0,"minTempC":8,"maxTempC":20,"avgTempC":17,"sunHours":6.8,"uvIndex":5,"location":{"id":"22d72902-b72f-4ca0-a522-4dbfb77a7b78","postcode":"7250","name":"BLACKSTONE HEIGHTS","state":"TAS","latitude":"-41.46","longitude":"147.0820001","distanceToNearestWeatherStationMetres":5607.391317385195,"nearestWeatherStation":{"name":"LAUNCESTON (TI TREE BEND)","state":"TAS","latitude":"-41.4194","longitude":"147.1219"}},"hourlyWeatherHistory":[{"hour":0,"tempC":9,"weatherDesc":"Partly cloudy","cloudCoverPct":17,"uvIndex":1,"windspeedKph":4,"windDirectionDeg":134,"windDirectionCompass":"SE","precipitationMm":0,"humidityPct":78,"visibilityKm":10,"pressureMb":1023},{"hour":1,"tempC":9,"weatherDesc":"Partly cloudy","cloudCoverPct":19,"uvIndex":1,"windspeedKph":4,"windDirectionDeg":137,"windDirectionCompass":"SE","precipitationMm":0,"humidityPct":80,"visibilityKm":10,"pressureMb":1023},{"hour":2,"tempC":8,"weatherDesc":"Partly cloudy","cloudCoverPct":21,"uvIndex":1,"windspeedKph":3,"windDirectionDeg":140,"windDirectionCompass":"SE","precipitationMm":0,"humidityPct":83,"visibilityKm":10,"pressureMb":1023},{"hour":3,"tempC":8,"weatherDesc":"Partly cloudy","cloudCoverPct":23,"uvIndex":1,"windspeedKph":3,"windDirectionDeg":142,"windDirectionCompass":"SE","precipitationMm":0,"humidityPct":85,"visibilityKm":10,"pressureMb":1023},{"hour":4,"tempC":8,"weatherDesc":"Partly cloudy","cloudCoverPct":24,"uvIndex":1,"windspeedKph":3,"windDirectionDeg":143,"windDirectionCompass":"SE","precipitationMm":0,"humidityPct":84,"visibilityKm":10,"pressureMb":1023},{"hour":5,"tempC":9,"weatherDesc":"Partly cloudy","cloudCoverPct":25,"uvIndex":1,"windspeedKph":2,"windDirectionDeg":143,"windDirectionCompass":"SE","precipitationMm":0,"humidityPct":82,"visibilityKm":10,"pressureMb":1024},{"hour":6,"tempC":9,"weatherDesc":"Partly cloudy","cloudCoverPct":26,"uvIndex":3,"windspeedKph":2,"windDirectionDeg":144,"windDirectionCompass":"SE","precipitationMm":0,"humidityPct":81,"visibilityKm":10,"pressureMb":1024},{"hour":7,"tempC":11,"weatherDesc":"Partly cloudy","cloudCoverPct":25,"uvIndex":4,"windspeedKph":4,"windDirectionDeg":184,"windDirectionCompass":"S","precipitationMm":0,"humidityPct":75,"visibilityKm":10,"pressureMb":1024},{"hour":8,"tempC":13,"weatherDesc":"Partly cloudy","cloudCoverPct":23,"uvIndex":4,"windspeedKph":5,"windDirectionDeg":225,"windDirectionCompass":"SW","precipitationMm":0,"humidityPct":68,"visibilityKm":10,"pressureMb":1024},{"hour":9,"tempC":15,"weatherDesc":"Partly cloudy","cloudCoverPct":21,"uvIndex":5,"windspeedKph":6,"windDirectionDeg":266,"windDirectionCompass":"W","precipitationMm":0,"humidityPct":62,"visibilityKm":10,"pressureMb":1024},{"hour":10,"tempC":17,"weatherDesc":"Partly cloudy","cloudCoverPct":21,"uvIndex":5,"windspeedKph":8,"windDirectionDeg":286,"windDirectionCompass":"WNW","precipitationMm":0,"humidityPct":58,"visibilityKm":10,"pressureMb":1024},{"hour":11,"tempC":18,"weatherDesc":"Partly cloudy","cloudCoverPct":21,"uvIndex":5,"windspeedKph":10,"windDirectionDeg":307,"windDirectionCompass":"NW","precipitationMm":0,"humidityPct":53,"visibilityKm":10,"pressureMb":1024},{"hour":12,"tempC":20,"weatherDesc":"Partly cloudy","cloudCoverPct":21,"uvIndex":5,"windspeedKph":11,"windDirectionDeg":327,"windDirectionCompass":"NNW","precipitationMm":0,"humidityPct":49,"visibilityKm":10,"pressureMb":1023},{"hour":13,"tempC":20,"weatherDesc":"Partly cloudy","cloudCoverPct":17,"uvIndex":5,"windspeedKph":12,"windDirectionDeg":328,"windDirectionCompass":"NNW","precipitationMm":0,"humidityPct":48,"visibilityKm":10,"pressureMb":1023},{"hour":14,"tempC":20,"weatherDesc":"Partly cloudy","cloudCoverPct":12,"uvIndex":5,"windspeedKph":13,"windDirectionDeg":329,"windDirectionCompass":"NNW","precipitationMm":0,"humidityPct":48,"visibilityKm":10,"pressureMb":1022},{"hour":15,"tempC":20,"weatherDesc":"Partly cloudy","cloudCoverPct":7,"uvIndex":6,"windspeedKph":14,"windDirectionDeg":330,"windDirectionCompass":"NNW","precipitationMm":0,"humidityPct":47,"visibilityKm":10,"pressureMb":1022},{"hour":16,"tempC":19,"weatherDesc":"Partly cloudy","cloudCoverPct":5,"uvIndex":5,"windspeedKph":13,"windDirectionDeg":332,"windDirectionCompass":"NNW","precipitationMm":0,"humidityPct":53,"visibilityKm":10,"pressureMb":1022},{"hour":17,"tempC":19,"weatherDesc":"Sunny","cloudCoverPct":2,"uvIndex":5,"windspeedKph":12,"windDirectionDeg":334,"windDirectionCompass":"NNW","precipitationMm":0,"humidityPct":58,"visibilityKm":10,"pressureMb":1022},{"hour":18,"tempC":18,"weatherDesc":"Clear","cloudCoverPct":0,"uvIndex":1,"windspeedKph":11,"windDirectionDeg":336,"windDirectionCompass":"NNW","precipitationMm":0,"humidityPct":64,"visibilityKm":10,"pressureMb":1022},{"hour":19,"tempC":18,"weatherDesc":"Clear","cloudCoverPct":0,"uvIndex":1,"windspeedKph":9,"windDirectionDeg":341,"windDirectionCompass":"NNW","precipitationMm":0,"humidityPct":71,"visibilityKm":10,"pressureMb":1022},{"hour":20,"tempC":17,"weatherDesc":"Clear","cloudCoverPct":0,"uvIndex":1,"windspeedKph":7,"windDirectionDeg":345,"windDirectionCompass":"NNW","precipitationMm":0,"humidityPct":78,"visibilityKm":10,"pressureMb":1022},{"hour":21,"tempC":16,"weatherDesc":"Clear","cloudCoverPct":0,"uvIndex":1,"windspeedKph":5,"windDirectionDeg":350,"windDirectionCompass":"N","precipitationMm":0,"humidityPct":85,"visibilityKm":10,"pressureMb":1023},{"hour":22,"tempC":14,"weatherDesc":"Clear","cloudCoverPct":15,"uvIndex":1,"windspeedKph":4,"windDirectionDeg":235,"windDirectionCompass":"SW","precipitationMm":0,"humidityPct":88,"visibilityKm":8,"pressureMb":1023},{"hour":23,"tempC":13,"weatherDesc":"Partly cloudy","cloudCoverPct":31,"uvIndex":1,"windspeedKph":3,"windDirectionDeg":120,"windDirectionCompass":"ESE","precipitationMm":0,"humidityPct":90,"visibilityKm":6,"pressureMb":1023}]}
        data_2019 = {"date":"2019-02-22","sunrise":"05:43:00","sunset":"19:07:00","moonrise":"20:57:00","moonset":"08:22:00","moonPhase":"Waning Gibbous","moonIlluminationPct":73,"minTempC":10,"maxTempC":24,"avgTempC":20,"sunHours":6.6,"uvIndex":5,"location":{"id":"22d72902-b72f-4ca0-a522-4dbfb77a7b78","postcode":"7250","name":"BLACKSTONE HEIGHTS","state":"TAS","latitude":"-41.46","longitude":"147.0820001","distanceToNearestWeatherStationMetres":5607.391317385195,"nearestWeatherStation":{"name":"LAUNCESTON (TI TREE BEND)","state":"TAS","latitude":"-41.4194","longitude":"147.1219"}},"hourlyWeatherHistory":[{"hour":0,"tempC":10,"weatherDesc":"Clear","cloudCoverPct":3,"uvIndex":1,"windspeedKph":2,"windDirectionDeg":76,"windDirectionCompass":"ENE","precipitationMm":0,"humidityPct":83,"visibilityKm":10,"pressureMb":1021},{"hour":1,"tempC":10,"weatherDesc":"Clear","cloudCoverPct":4,"uvIndex":1,"windspeedKph":2,"windDirectionDeg":75,"windDirectionCompass":"ENE","precipitationMm":0,"humidityPct":85,"visibilityKm":10,"pressureMb":1021},{"hour":2,"tempC":10,"weatherDesc":"Clear","cloudCoverPct":5,"uvIndex":1,"windspeedKph":3,"windDirectionDeg":73,"windDirectionCompass":"ENE","precipitationMm":0,"humidityPct":87,"visibilityKm":10,"pressureMb":1021},{"hour":3,"tempC":10,"weatherDesc":"Clear","cloudCoverPct":6,"uvIndex":1,"windspeedKph":3,"windDirectionDeg":71,"windDirectionCompass":"ENE","precipitationMm":0,"humidityPct":88,"visibilityKm":10,"pressureMb":1021},{"hour":4,"tempC":11,"weatherDesc":"Clear","cloudCoverPct":9,"uvIndex":1,"windspeedKph":3,"windDirectionDeg":70,"windDirectionCompass":"ENE","precipitationMm":0,"humidityPct":86,"visibilityKm":10,"pressureMb":1021},{"hour":5,"tempC":12,"weatherDesc":"Clear","cloudCoverPct":11,"uvIndex":1,"windspeedKph":3,"windDirectionDeg":69,"windDirectionCompass":"ENE","precipitationMm":0,"humidityPct":83,"visibilityKm":10,"pressureMb":1022},{"hour":6,"tempC":12,"weatherDesc":"Sunny","cloudCoverPct":14,"uvIndex":4,"windspeedKph":3,"windDirectionDeg":69,"windDirectionCompass":"ENE","precipitationMm":0,"humidityPct":80,"visibilityKm":10,"pressureMb":1022},{"hour":7,"tempC":15,"weatherDesc":"Sunny","cloudCoverPct":14,"uvIndex":5,"windspeedKph":3,"windDirectionDeg":58,"windDirectionCompass":"ENE","precipitationMm":0,"humidityPct":71,"visibilityKm":10,"pressureMb":1022},{"hour":8,"tempC":18,"weatherDesc":"Sunny","cloudCoverPct":14,"uvIndex":5,"windspeedKph":3,"windDirectionDeg":47,"windDirectionCompass":"NE","precipitationMm":0,"humidityPct":61,"visibilityKm":10,"pressureMb":1022},{"hour":9,"tempC":21,"weatherDesc":"Sunny","cloudCoverPct":13,"uvIndex":6,"windspeedKph":4,"windDirectionDeg":37,"windDirectionCompass":"NE","precipitationMm":0,"humidityPct":51,"visibilityKm":10,"pressureMb":1022},{"hour":10,"tempC":22,"weatherDesc":"Sunny","cloudCoverPct":15,"uvIndex":6,"windspeedKph":4,"windDirectionDeg":99,"windDirectionCompass":"E","precipitationMm":0,"humidityPct":48,"visibilityKm":10,"pressureMb":1022},{"hour":11,"tempC":23,"weatherDesc":"Sunny","cloudCoverPct":17,"uvIndex":6,"windspeedKph":5,"windDirectionDeg":162,"windDirectionCompass":"SSE","precipitationMm":0,"humidityPct":44,"visibilityKm":10,"pressureMb":1022},{"hour":12,"tempC":24,"weatherDesc":"Sunny","cloudCoverPct":18,"uvIndex":6,"windspeedKph":5,"windDirectionDeg":224,"windDirectionCompass":"SW","precipitationMm":0,"humidityPct":41,"visibilityKm":10,"pressureMb":1021},{"hour":13,"tempC":24,"weatherDesc":"Sunny","cloudCoverPct":23,"uvIndex":6,"windspeedKph":6,"windDirectionDeg":262,"windDirectionCompass":"W","precipitationMm":0,"humidityPct":42,"visibilityKm":10,"pressureMb":1021},{"hour":14,"tempC":24,"weatherDesc":"Partly cloudy","cloudCoverPct":27,"uvIndex":6,"windspeedKph":6,"windDirectionDeg":300,"windDirectionCompass":"WNW","precipitationMm":0,"humidityPct":43,"visibilityKm":10,"pressureMb":1021},{"hour":15,"tempC":24,"weatherDesc":"Partly cloudy","cloudCoverPct":32,"uvIndex":6,"windspeedKph":6,"windDirectionDeg":339,"windDirectionCompass":"NNW","precipitationMm":0,"humidityPct":44,"visibilityKm":10,"pressureMb":1021},{"hour":16,"tempC":22,"weatherDesc":"Partly cloudy","cloudCoverPct":32,"uvIndex":6,"windspeedKph":6,"windDirectionDeg":273,"windDirectionCompass":"W","precipitationMm":0,"humidityPct":50,"visibilityKm":10,"pressureMb":1021},{"hour":17,"tempC":20,"weatherDesc":"Partly cloudy","cloudCoverPct":32,"uvIndex":5,"windspeedKph":6,"windDirectionDeg":207,"windDirectionCompass":"SSW","precipitationMm":0,"humidityPct":56,"visibilityKm":10,"pressureMb":1022},{"hour":18,"tempC":18,"weatherDesc":"Partly cloudy","cloudCoverPct":32,"uvIndex":1,"windspeedKph":6,"windDirectionDeg":142,"windDirectionCompass":"SE","precipitationMm":0,"humidityPct":62,"visibilityKm":10,"pressureMb":1023},{"hour":19,"tempC":17,"weatherDesc":"Partly cloudy","cloudCoverPct":28,"uvIndex":1,"windspeedKph":6,"windDirectionDeg":125,"windDirectionCompass":"SE","precipitationMm":0,"humidityPct":67,"visibilityKm":10,"pressureMb":1023},{"hour":20,"tempC":15,"weatherDesc":"Clear","cloudCoverPct":25,"uvIndex":1,"windspeedKph":6,"windDirectionDeg":108,"windDirectionCompass":"ESE","precipitationMm":0,"humidityPct":72,"visibilityKm":10,"pressureMb":1023},{"hour":21,"tempC":14,"weatherDesc":"Clear","cloudCoverPct":21,"uvIndex":1,"windspeedKph":6,"windDirectionDeg":91,"windDirectionCompass":"E","precipitationMm":0,"humidityPct":77,"visibilityKm":10,"pressureMb":1024},{"hour":22,"tempC":13,"weatherDesc":"Clear","cloudCoverPct":15,"uvIndex":1,"windspeedKph":6,"windDirectionDeg":101,"windDirectionCompass":"ESE","precipitationMm":0,"humidityPct":78,"visibilityKm":10,"pressureMb":1024},{"hour":23,"tempC":13,"weatherDesc":"Clear","cloudCoverPct":9,"uvIndex":1,"windspeedKph":6,"windDirectionDeg":112,"windDirectionCompass":"ESE","precipitationMm":0,"humidityPct":80,"visibilityKm":10,"pressureMb":1024}]}
        start_time = datetime(2021, 2, 22, 19, 00)
        end_time = datetime(2021, 2, 22, 20, 00)
        postcode = "7250"

        mocked_response_1 = Mock()
        mocked_response_1.json.return_value = data_2021
        mocked_response_1.status_code = 200
        
        mocked_response_2 = Mock()
        mocked_response_2.json.return_value = data_2020
        mocked_response_2.status_code = 200

        mocked_response_3 = Mock()
        mocked_response_3.json.return_value = data_2019
        mocked_response_3.status_code = 200

        mocked_get.side_effect = [ConnectionError, Timeout, mocked_response_1,mocked_response_2,mocked_response_3]
        with self.assertRaises(ConnectionError):
            res = self.calculator.calculate_solar_energy_future(start_time, end_time, postcode)
            self.assertEqual(res, None)
        with self.assertRaises(Timeout):
            res = self.calculator.calculate_solar_energy_future(start_time, end_time, postcode)
            self.assertEqual(res, None)
        
        solar_energy_generated = self.calculator.calculate_solar_energy_future(
            start_time, end_time, postcode)
        expected_result = 0.34
        self.assertAlmostEqual(solar_energy_generated, expected_result, delta=0.01, msg=("Expected %s, got %s instead"
                                                                                         % (expected_result, solar_energy_generated)))
    def test_4(self):
        """
            solar_testing
            condition: This path is when the start time and end time has a whole hour gap which is 60 minutes. The value of du will be updated to 1.
        """
        start_time = datetime(2021, 2, 22, 17, 00)
        end_time = datetime(2021, 2, 22, 18, 00)
        postcode = "7250"
        solar_energy_generated = self.calculator.calculate_solar_energy_future(
            start_time, end_time, postcode)
        expected_result = 3.25
        self.assertAlmostEqual(solar_energy_generated, expected_result, delta=0.01, msg=("Expected %s, got %s instead"
                                                                                         % (expected_result, solar_energy_generated)))
    def test_5(self):
        """
            cost_calculation for example given in the assignment spec
        """
        config = 3
        start_time = time(17,30)
        start_date = date(2022, 2, 22)
        battery_capacity = 50
        initial_charge = 20
        power = self.calculator.get_configuration(config)[0]
        base_cost = self.calculator.get_configuration(config)[1]
        end_time = datetime(2022,2,22,18,15)   
        final_cost = self.calculator.total_cost_calculation(start_date=start_date, start_time=start_time,
                                                                start_state=initial_charge, end_time=end_time,
                                                                base_price=base_cost, power=power,
                                                                capacity=battery_capacity, postcode="7250",solar_energy=True)
        expected_output = 0.22
        self.assertAlmostEqual(final_cost, expected_output, delta=0.01, msg=("Expected %s, got %s instead"
                                                                                         % (expected_output, final_cost)))

    def test_6(self):
        """
            cost_calculation for example given in the assignment spec, with the solar_energy = False
            which by defauly will not happen if the date extends to future, this testing main aim is to cover the branch
            The boolean for solar_energy is to give much more flexibility to the calculation for future extension
        """
        config = 3
        start_time = time(17,30)
        start_date = date(2022, 2, 22)
        battery_capacity = 50
        initial_charge = 20
        power = self.calculator.get_configuration(config)[0]
        base_cost = self.calculator.get_configuration(config)[1]
        end_time = datetime(2022,2,22,18,15)   
        final_cost = self.calculator.total_cost_calculation(start_date=start_date, start_time=start_time,
                                                                start_state=initial_charge, end_time=end_time,
                                                                base_price=base_cost, power=power,
                                                                capacity=battery_capacity, postcode="7250")
        expected_output = 0.48
        self.assertAlmostEqual(final_cost, expected_output, delta=0.01, msg=("Expected %s, got %s instead"
                                                                                         % (expected_output, final_cost)))
    
    def test_7(self):
        """
            cost_calculation for same year which is 12-12-2021 to get reference date for 2020 instead of 2021, value will be difference when the date of testing exceed 12-12-2021
            This is manual calculaiton for the expected output:
            2020: si = 8.7, dl = 15.15, 
            5-6: cc = 2, du = 0.5
            6-7: cc = 1, du = 0.25

            2019: si = 8.1, dl = 15.13, 
            5-6: cc = 34, du = 0.5
            6-7: cc = 49, du = 0.25

            2018: si = 8.7, dl = 15.13, 
            5-6: cc = 6, du = 0.5 
            6-7: cc = 3, du = 0.25

                    |       2020         |        2019        |        2018        |
                    |solar | net  | cost | solar| net  | cost | solar| net  | cost | 
            5-6 pm  |2.8139|0.7861|0.0786|1.7667|1.8333|0.2017|2.7026|0.8974|0.0987|
            6-7 pm  |1.4213|0.3787|0.0189|0.6826|1.1174|0.0615|1.3944|0.4056|0.0223|
            total cost = ( 0.0786+0.0189+0.2017+0.0615+0.0987+0.0223 )/3
            total cost = 0.16
        """
        config = 3
        start_time = time(17,30)
        start_date = date(2021, 12, 12)
        battery_capacity = 50
        initial_charge = 20
        power = self.calculator.get_configuration(config)[0]
        base_cost = self.calculator.get_configuration(config)[1]
        end_time = datetime(2021,12,12,18,15)  
        final_cost = self.calculator.total_cost_calculation(start_date=start_date, start_time=start_time,
                                                                start_state=initial_charge, end_time=end_time,
                                                                base_price=base_cost, power=power,
                                                                capacity=battery_capacity, postcode="7250",solar_energy=True)
        expected_output = 0.16
        self.assertAlmostEqual(final_cost, expected_output, delta=0.01, msg=("Expected %s, got %s instead"
                                                                                         % (expected_output, final_cost)))

    # you may create test suite if needed
    # Test case needed for form
    """
    .http://118.138.246.158/api/v1/weather?location=22d72902-b72f-4ca0-a522-4dbfb77a7b78&date=2021-02-22
.http://118.138.246.158/api/v1/weather?location=22d72902-b72f-4ca0-a522-4dbfb77a7b78&date=2021-02-22
.http://118.138.246.158/api/v1/weather?location=22d72902-b72f-4ca0-a522-4dbfb77a7b78&date=2021-02-22
http://118.138.246.158/api/v1/weather?location=22d72902-b72f-4ca0-a522-4dbfb77a7b78&date=2020-02-22
http://118.138.246.158/api/v1/weather?location=22d72902-b72f-4ca0-a522-4dbfb77a7b78&date=2019-02-22
..http://118.138.246.158/api/v1/weather?location=22d72902-b72f-4ca0-a522-4dbfb77a7b78&date=2020-12-12
http://118.138.246.158/api/v1/weather?location=22d72902-b72f-4ca0-a522-4dbfb77a7b78&date=2019-12-12
http://118.138.246.158/api/v1/weather?location=22d72902-b72f-4ca0-a522-4dbfb77a7b78&date=2018-12-12
.
    """
if __name__ == "__main__":
    unittest.main()
