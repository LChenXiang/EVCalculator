from datetime import datetime, date, time, timedelta
import holidays
import requests


class Calculator():
    # you can choose to initialise variables here, if needed.
    def __init__(self):
        self.australian_holiday = holidays.Australia()
        self.configuration = [[2, 5],
                              [3.6, 7.5],
                              [7.2, 10],
                              [11, 12.5],
                              [22, 15],
                              [36, 20],
                              [90, 30],
                              [350, 50]]
        self.EARLIEST_DATE = datetime(2008,7,1)
        self.PANEL_SIZE = 50
        self.PANEL_EFFICIENCY = 0.2

    # you may add more parameters if needed, you may modify the formula also.
    def cost_calculation(self, initial_state: float, final_state: float, capacity: int,
                         is_peak: bool, is_holiday: bool, base_price: int):
        if is_peak:
            peak_modifier = 1
        else:
            peak_modifier = 0.5

        if is_holiday:
            surcharge_factor = 1.1
        else:
            surcharge_factor = 1

        cost = ((final_state - initial_state) / 100) * capacity * (base_price / 100) * surcharge_factor * peak_modifier
        return cost

    # you may add more parameters if needed, you may also modify the formula.
    def time_calculation(self, initial_state, final_state, capacity, power):
        time = (final_state - initial_state) / 100 * capacity / power
        return time

    # you may create some new methods at your convenience, or modify these methods, or choose not to use them.
    def get_configuration(self, config):
        return self.configuration[config - 1]

    def is_holiday(self, start_date: date):
        is_weekday = (start_date.weekday() < 5)
        return is_weekday or start_date in self.australian_holiday

    def is_peak(self, start_time: time) -> bool:
        left_peak = time(6)
        right_peak = time(18)
        return left_peak <= start_time < right_peak

    # def peak_period(self, start_time):
    #     pass

    def get_end_time(self, start_date: date, start_time: time, charge_time: int):
        starting_date_time = datetime.combine(start_date, start_time)
        time_to_add = timedelta(hours=charge_time)
        return starting_date_time + time_to_add

    def get_weather_data(self, input_date: date, postcode: str):
        """
        Returns all the weather data for the given date and postcode
        :param input_date: Date of the weather data
        :param postcode: Postcode/location of the weather data
        :return: Weather data, in requests data type
        """
        locationURL = "http://118.138.246.158/api/v1/location?postcode="
        requestLocationURL = locationURL + postcode
        resLocation = requests.get(url=requestLocationURL)
        if resLocation.status_code != 200:
            raise ValueError("Invalid postcode")
        if len(resLocation.json()) == 0:
            raise ValueError("Invalid postcode")
        locationID = resLocation.json()[0].get("id")
        if input_date.month < 10:
            month = "0" + str(input_date.month)
        else:
            month = str(input_date.month)
        if input_date.day < 10:
            day = "0" + str(input_date.day)
        else:
            day = str(input_date.day)
        dateRequest = "%s-%s-%s" % (input_date.year, month, day)
        weatherURL = "http://118.138.246.158/api/v1/weather?location=%s&date=%s" % (locationID, dateRequest)
        resWeather = requests.get(url=weatherURL)
        if resWeather.status_code != 200:
            raise ValueError("Could not get weather data")
        return resWeather

    # to be acquired through API
    def get_sun_hour(self, input_date: date, postcode: str) -> float:
        """
        Returns the sun hour data for solar energy calculation of this date and postcode
        :param input_date: Date of the data
        :param postcode: Postcode/location of the data
        :return: Sun hour data for the given date and postcode
        """
        resWeather = self.get_weather_data(input_date, postcode)
        return resWeather.json().get("sunHours")

    def get_sunrise_sunset(self, input_date: date, postcode: str):
        """
        Returns the sunrise and sunset time data type in a tuple, given date and postcode
        :param input_date: Date to get the data
        :param postcode: Location/Postcode of the data
        :return: Sunrise and sunset, in time type, in a tuple.
        """
        resWeather = self.get_weather_data(input_date, postcode)
        sunrise_arr = resWeather.json().get("sunrise").split(":")
        sunrise = time(hour=int(sunrise_arr[0]), minute=int(sunrise_arr[1]), second=int(sunrise_arr[2]))
        sunset_arr = resWeather.json().get("sunset").split(":")
        sunset = time(hour=int(sunset_arr[0]), minute=int(sunset_arr[1]), second=int(sunset_arr[2]))
        return (sunrise, sunset)

    # to be acquired through API
    # Calculate it yourself for each day
    # get the sunrise and sunset, min max the start and the end, then just get the
    # difference and convert it to hours or something.
    def get_solar_energy_duration(self, start_time: time, end_time: time, input_date: date, postcode: str):
        # THIS FUNCTION SHOULD ONLY BE USED FOR REQ 2!
        # Tell me if u want me to change this to better suit need (NYK)
        sunrise_sunset = self.get_sunrise_sunset(input_date, postcode)
        start_time_actual = max(start_time, sunrise_sunset[0])
        end_time_actual = min(end_time, sunrise_sunset[1])
        start_time_delta = timedelta(hours=int(start_time_actual.hour),
                                     minutes=int(start_time_actual.minute),
                                     seconds=int(start_time_actual.second))
        end_time_delta = timedelta(hours=int(end_time_actual.hour),
                                   minutes=int(end_time_actual.minute),
                                   seconds=int(end_time_actual.second))
        duration = (end_time_delta - start_time_delta).total_seconds() / 60 / 60
        return duration

    # to be acquired through API
    def get_day_light_length(self, input_date: date, postcode: str) -> float:
        """
        Returns the daylight length hours of the given date and postcode
        :param input_date: Date to get the data
        :param postcode: Location/Postcode of the data
        :return: Daylight length hours of the given date and postcode
        """
        sunrise, sunset = self.get_sunrise_sunset(input_date, postcode)
        sunrise_delta = timedelta(hours=sunrise.hour, minutes=sunrise.minute, seconds=sunrise.second)
        sunset_delta = timedelta(hours=sunset.hour, minutes=sunset.minute, seconds=sunset.second)

        daylight_length = (sunset_delta - sunrise_delta).total_seconds() / 60 / 60
        return daylight_length

    # to be acquired through API
    # def get_solar_insolation(self, solar_insolation):
    #     pass

    # to be acquired through API

    def get_cloud_cover(self, input_date: date, postcode: str) -> list:
        """
        Gets the list of cloud cover values for the given date and postcode.
        :param input_date: Date to find cloud cover values
        :param postcode: Postcode of the location
        :return: List of cloud cover values for hour 0 to hour 23
        """
        resWeather = self.get_weather_data(input_date, postcode)
        resWeatherCloudCoverList = resWeather.json().get("hourlyWeatherHistory")
        res_cloud_clover = []
        for each in resWeatherCloudCoverList:
            hourly_cloud = each.get("cloudCoverPct")
            res_cloud_clover.append(hourly_cloud)
        return res_cloud_clover

    def calculate_solar_energy_past_to_currentday_minus_two(self, start_time_date: datetime,
                                                            end_time_date: datetime, postcode: str):
        # TODO: implement req 2
        # RETURN 0 FOR THE DATE IF IT IS LESS THAN 1 JULY 2008!
        current_date = start_time_date.date()
        next_date = timedelta(days=1)
        total_energy = 0
        while current_date <= end_time_date.date():
            # if the date is before 01/07/2008, we do not count in the solar energy for that day, so we can exclude it
            # by excluding these days it is the same as adding 0 multiple times
            if current_date >= self.EARLIEST_DATE:

                sun_hour = self.get_sun_hour(current_date, postcode) # retrieve solar insolation of this date (sun hour)

                daylight_length = self.get_day_light_length(current_date, postcode) # retrieve daylight length of this date

                # if this date is not starting date, means a day passed, so start at earliest time of the day
                if current_date != start_time_date.date():
                    start = time.min
                else:
                    start = start_time_date.time()   # starting date, so just take the starting time

                # if this date is not end date, means we have to continue another day, so end at latest time of the day
                if current_date != end_time_date.date():
                    end = time.max
                else:
                    end = end_time_date.time()       # current date is end date, just use the end time of the end date

                # calculate the solar energy duration using the decided start and end time
                duration = self.get_solar_energy_duration(start, end, current_date, postcode)

                # finally calculate solar energy generated for the day and add into total sum
                total_energy += sun_hour * duration / daylight_length * self.PANEL_SIZE * self.PANEL_EFFICIENCY

            # proceed to the next date until reaching end date
            current_date += next_date

        return total_energy

    def calculate_solar_energy_future(self, start_time_date: datetime, end_time_date: datetime,
                               postcode: str):
        # TODO: implement req 3
        pass

    def calculate_solar_energy(self, start_time_date: datetime, end_time_date: datetime,
                               postcode: str):
        minus_two_day = timedelta(days=2)
        current_date = datetime.now().date()
        if start_time_date.date() > (current_date-minus_two_day):
            return self.calculate_solar_energy_future(start_time_date, end_time_date, postcode)
        else:
            return self.calculate_solar_energy_past_to_currentday_minus_two(start_time_date,
                                                                     end_time_date,
                                                                     postcode)

    def get_charging_time_str(self, charge_hours: float):
        hours = int(charge_hours)
        decimal_minutes = (charge_hours % 1) * 60
        minutes = int(decimal_minutes)
        seconds = int((decimal_minutes % 1) * 60)

        return_str = ""
        if hours > 0:
            if hours == 1:
                return_str += str(hours) + " hour "
            else:
                return_str += str(hours) + " hours "
        if minutes > 0:
            if minutes == 1:
                return_str += str(minutes) + " minutes "
            else:
                return_str += str(minutes) + " minutes "
        if seconds > 0:
            if seconds == 1:
                return_str += str(seconds) + " seconds "
            else:
                return_str += str(seconds) + " seconds "
        return return_str.strip()

    def total_cost_calculation(self, start_date: date, start_time: time, end_time: datetime,
                               start_state: int, base_price: int, power: int, capacity: int):
        total_holiday_peak = 0
        total_holiday_nonPeak = 0
        total_nonHoliday_peak = 0
        total_nonHoliday_nonPeak = 0

        current_date_time = datetime.combine(start_date, start_time)

        reachedEnd = False
        while (not reachedEnd):
            holiday_surcharge = self.is_holiday(current_date_time.date())
            peak = self.is_peak(current_date_time.time())
            added_time = timedelta(hours=1)
            new_datetime = min(end_time, (current_date_time + added_time).replace(minute=0, second=0, microsecond=0))
            difference_time_minutes = (new_datetime - current_date_time).total_seconds() / 60

            if holiday_surcharge:
                if peak:
                    total_holiday_peak += difference_time_minutes
                else:
                    total_holiday_nonPeak += difference_time_minutes
            else:
                if peak:
                    total_nonHoliday_peak += difference_time_minutes
                else:
                    total_nonHoliday_nonPeak += difference_time_minutes

            if new_datetime == end_time:
                reachedEnd = True
            current_date_time = new_datetime

        # Calculate Final state of charge for each category
        holiday_peak_fsoc = (((total_holiday_peak / 60) * power / capacity) + (start_state / 100)) * 100
        holiday_nonpeak_fsoc = (((total_holiday_nonPeak / 60) * power / capacity) + (start_state / 100)) * 100
        nonholiday_peak_fsoc = (((total_nonHoliday_peak / 60) * power / capacity) + (start_state / 100)) * 100
        nonholiday_nonpeak_fsoc = (((total_nonHoliday_nonPeak / 60) * power / capacity)
                                   + (start_state / 100)) * 100

        cost_holiday_peak = self.cost_calculation(start_state, holiday_peak_fsoc, capacity,
                                                  True, True, base_price)
        cost_holiday_nonpeak = self.cost_calculation(start_state, holiday_nonpeak_fsoc, capacity,
                                                     False, True, base_price)
        cost_nonholiday_peak = self.cost_calculation(start_state, nonholiday_peak_fsoc, capacity,
                                                     True, False, base_price)
        cost_nonholiday_nonpeak = self.cost_calculation(start_state, nonholiday_nonpeak_fsoc,
                                                        capacity, False, False, base_price)

        return round((cost_holiday_peak + cost_holiday_nonpeak + cost_nonholiday_peak + cost_nonholiday_nonpeak), 2)
