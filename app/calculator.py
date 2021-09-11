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

    # to be acquired through API
    def get_sun_hour(self, sun_hour):
        pass

    # to be acquired through API
    def get_solar_energy_duration(self, start_time):
        pass

    # to be acquired through API
    def get_day_light_length(self, input_date: date, postcode: str) -> float:
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
        sunrise_arr = resWeather.json().get("sunrise").split(":")
        sunrise = timedelta(hours=int(sunrise_arr[0]), minutes=int(sunrise_arr[1]), seconds=int(sunrise_arr[2]))
        sunset_arr = resWeather.json().get("sunset").split(":")
        sunset = timedelta(hours=int(sunset_arr[0]), minutes=int(sunset_arr[1]), seconds=int(sunset_arr[2]))

        daylight_length = (sunset - sunrise).total_seconds() / 60 / 60
        return daylight_length

    # to be acquired through API
    def get_solar_insolation(self, solar_insolation):
        pass

    # to be acquired through API
    def get_cloud_cover(self):
        pass

    def calculate_solar_energy(self):
        pass

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
