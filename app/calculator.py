from datetime import datetime, date, time, timedelta
import holidays
import requests
import dateutil.relativedelta


class Calculator():
    # you can choose to initialise variables here, if needed.
    def __init__(self):
        self.configuration = [[2, 5],
                              [3.6, 7.5],
                              [7.2, 10],
                              [11, 12.5],
                              [22, 15],
                              [36, 20],
                              [90, 30],
                              [350, 50]]
        self.selection = None  # this is for location ID selection

    # you may add more parameters if needed, you may modify the formula also.
    def cost_calculation(self, initial_state: float, final_state: float, capacity: float,
                         is_peak: bool, is_holiday: bool, base_price: float) -> float:
        if is_peak:
            peak_modifier = 1
        else:
            peak_modifier = 0.5

        if is_holiday:
            surcharge_factor = 1.1
        else:
            surcharge_factor = 1

        cost = ((final_state - initial_state) / 100) * capacity * \
            (base_price / 100) * surcharge_factor * peak_modifier
        return cost

    # you may add more parameters if needed, you may also modify the formula.
    def time_calculation(self, initial_state: float, final_state: float, capacity: float, power: float) -> float:
        time = (final_state - initial_state) / 100 * capacity / power
        return time

    # you may create some new methods at your convenience, or modify these methods, or choose not to use them.
    def get_configuration(self, config):
        return self.configuration[config - 1]

    def is_holiday(self, start_date: date, state: str) -> bool:
        is_weekday = (start_date.weekday() < 5)
        state_holiday = holidays.Australia(prov=state)
        # or start_date in self.school_holidays[state]
        return is_weekday or start_date in state_holiday

    def is_peak(self, start_time: time) -> bool:
        left_peak = time(6)
        right_peak = time(18)
        return left_peak <= start_time < right_peak

    def get_end_time(self, start_date: date, start_time: time, charge_time: float):
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
        # selection was made here
        if not self.selection:
            for i in range(len(resLocation.json())):
                print(resLocation.json()[i].get("name"), i)
            self.selection = int(input("select_id: "))
        locationID = resLocation.json()[self.selection].get("id")
        # locationID = resLocation.json()[0].get("id")
        if input_date.month < 10:
            month = "0" + str(input_date.month)
        else:
            month = str(input_date.month)
        if input_date.day < 10:
            day = "0" + str(input_date.day)
        else:
            day = str(input_date.day)
        dateRequest = "%s-%s-%s" % (input_date.year, month, day)
        weatherURL = "http://118.138.246.158/api/v1/weather?location=%s&date=%s" % (
            locationID, dateRequest)
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
        sunrise = time(hour=int(sunrise_arr[0]), minute=int(
            sunrise_arr[1]), second=int(sunrise_arr[2]))
        sunset_arr = resWeather.json().get("sunset").split(":")
        sunset = time(hour=int(sunset_arr[0]), minute=int(
            sunset_arr[1]), second=int(sunset_arr[2]))
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
        duration = (end_time_delta -
                    start_time_delta).total_seconds() / 60 / 60
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
        sunrise_delta = timedelta(
            hours=sunrise.hour, minutes=sunrise.minute, seconds=sunrise.second)
        sunset_delta = timedelta(
            hours=sunset.hour, minutes=sunset.minute, seconds=sunset.second)

        daylight_length = (sunset_delta - sunrise_delta).total_seconds() / 3600
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
        pass

    def calculate_solar_energy_future(self, start_time_date: datetime, end_time_date: datetime,
                                      postcode: str):
        """
            This function is to calculate the solar energy generated between start_time_date and end_time_date in the future

            solar insolation,   si
            duration,           du
            daylight length,    dl
            cloud cover,        cc

            CONCEPT
            1) find reference data, means if given 20/05/2023, get reference data 20/05/2021
            2) get sunrise and sunset time,dl check if charging hour was at daylight, get solar insolation, si
            3) calculate the solar energy generated during daylight (a for loop based on day duration)
                - calculate the solar energy generated based on hour (another for loop)
                - get hourly cloud cover values, cc (o to 100)
                - get the duration, du (minute/60)
                - formula for this is si*1/dl * (1-cc/100) * 50 * 0.2 (in kWh)
                - sum up the total solar energy generated for the day
            4) calculate the solar energy generated for the same day in the preceding two years, repeat step 2 onward
            5) estimate the solar energy generated as the mean of the three solar energy generated
            6) sum up the total energy value for all days

            Past date: for loop each day of charging
            Future date: nested loop:
            total_power_all = 0
            FOR 3 YEARS REFERENCE DATE:
                total_power_year = 0
                for each chargingday
                    total_power_day = 0
                    retrieve solar length
                    generate solar charging hour (GET SUNRISE, SUNSET, AKA DAYLIGHT LENGTH)
                  for each solar charging hour
                      retrieve cloud cover
                      total_power_hour calc
                      total_power_day += totalpower_hour
                  total_power_year += total_power_day
              total_power_all += total_power_year
            total_power = total_power_all / 3
        """
        # calculate reference date
        day_gap = end_time_date.day - start_time_date.day
        total_solar_across_day = 0
        for day in range(day_gap, -1, -1):
            current_year = datetime.now().year
            current_date = end_time_date - timedelta(days=day)
            gap = current_date.year - current_year
            estimated_solar_mean = 0
            # same day but from three years mean
            for year in range(3):
                reference_date = current_date - \
                    dateutil.relativedelta.relativedelta(years=(gap+year))

                start_time_point = None
                end_time_point = None

                sunrise, sunset = self.get_sunrise_sunset(
                    reference_date, postcode)
                sunrise_delta = timedelta(
                    hours=sunrise.hour, minutes=sunrise.minute)
                sunset_delta = timedelta(
                    hours=sunset.hour, minutes=sunset.minute)

                if day_gap > 0:
                    if current_date.day == start_time_date.day:
                        # means start will be start_time_date, end will be sunset_time
                        # check again if the start_time_date was within daylight, if not, change start_time_date to sunrise
                        target = timedelta(
                            hours=start_time_date.hour, minutes=start_time_date.minute)
                        if sunrise_delta >= target <= sunset_delta:
                            start_time_point = target
                        else:
                            start_time_point = sunrise_delta
                        end_time_point = sunset_delta
                    elif current_date.day == end_time_date.day:
                        # means end will be end_time_date, start will be sunrise time
                        # check again if the end_time_date was within daylight, if not change end_time_date to sunset
                        target = timedelta(
                            hours=end_time_date.hour, minutes=end_time_date.minute)
                        if sunrise_delta >= target <= sunset_delta:
                            end_time_point = target
                        else:
                            end_time_point = sunset_delta
                        start_time_point = sunrise_delta
                    else:
                        # means start will be sunrise and end will be sunset
                        start_time_point = sunrise_delta
                        end_time_point = sunset_delta
                # if daygap == 0
                else:
                    start_time_point = timedelta(
                        hours=start_time_date.hour, minutes=start_time_date.minute)
                    end_time_point = timedelta(
                        hours=end_time_date.hour, minutes=end_time_date.minute)
                    # means not within daylight
                    if start_time_point > sunset_delta:
                        return 0
                dl = self.get_day_light_length(reference_date, postcode)
                si = self.get_sun_hour(reference_date, postcode)
                cloud_cover_list = self.get_cloud_cover(
                    reference_date, postcode)

                start_time_hour = (start_time_point.seconds // 3600)
                start_time_minute = (start_time_point.seconds // 60 % 60)
                end_time_hour = (end_time_point.seconds // 3600)
                end_time_minute = (end_time_point.seconds // 60 % 60)

                end = False
                total_power_daily = 0
                current_hour = start_time_hour
                while not end:
                    cc = cloud_cover_list[current_hour]
                    if current_hour == start_time_hour and current_hour == end_time_hour:
                        du = (end_time_minute - start_time_minute)/60
                    elif current_hour == start_time_hour:
                        du = (60 - start_time_minute)/60
                    elif current_hour == end_time_hour:
                        du = (end_time_minute)/60
                    else:
                        du = 1
                    hourly_generated_solar_energy = si * \
                        du / dl * (1-cc/100) * 50 * 0.2
                    total_power_daily = total_power_daily + hourly_generated_solar_energy
                    current_hour = current_hour + 1
                    if current_hour > end_time_date.hour:
                        end = True
                estimated_solar_mean = estimated_solar_mean + total_power_daily
            estimated_solar_mean = estimated_solar_mean/3
            total_solar_across_day = total_solar_across_day + estimated_solar_mean
        return total_solar_across_day

    def calculate_solar_energy(self, start_time_date: datetime, end_time_date: datetime,
                               postcode: str):
        minus_two_day = timedelta(days=2)
        current_date = datetime.now().date()
        if start_time_date.date() > (current_date - minus_two_day):
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
                return_str += str(minutes) + " minute "
            else:
                return_str += str(minutes) + " minutes "
        if seconds > 0:
            if seconds == 1:
                return_str += str(seconds) + " second "
            else:
                return_str += str(seconds) + " seconds "
        return return_str.strip()

    def get_state(self, postcode: str) -> str:
        locationURL = "http://118.138.246.158/api/v1/location?postcode="
        requestLocationURL = locationURL + postcode
        resLocation = requests.get(url=requestLocationURL)
        if resLocation.status_code != 200:
            raise ValueError("Invalid postcode")
        if len(resLocation.json()) == 0:
            raise ValueError("Invalid postcode")
        state = resLocation.json()[0].get("state")
        return state

    def total_cost_calculation(self, start_date: date, start_time: time, end_time: datetime,
                               start_state: int, base_price: float, power: float, capacity: float,
                               postcode: str, solar_energy: float = 0) -> float:
        state = self.get_state(postcode)
        total_holiday_peak = 0
        total_holiday_nonPeak = 0
        total_nonHoliday_peak = 0
        total_nonHoliday_nonPeak = 0

        current_date_time = datetime.combine(start_date, start_time)
        remaining_solar_energy = solar_energy

        reachedEnd = False
        while (not reachedEnd):
            holiday_surcharge = self.is_holiday(
                current_date_time.date(), state)
            peak = self.is_peak(current_date_time.time())
            added_time = timedelta(hours=1)
            new_datetime = min(end_time, (current_date_time +
                                          added_time).replace(minute=0, second=0, microsecond=0))
            difference_time_minutes = max(
                0, ((new_datetime - current_date_time).total_seconds() / 60))
            power_from_this_charge = (difference_time_minutes) / 60 * power
            power_after_deduct = max(
                0, power_from_this_charge - remaining_solar_energy)
            remaining_solar_energy = max(
                0, remaining_solar_energy - power_from_this_charge)
            time_remaining_charge = power_after_deduct / power * 60

            if holiday_surcharge:
                if peak:
                    total_holiday_peak += time_remaining_charge
                else:
                    total_holiday_nonPeak += time_remaining_charge
            else:
                if peak:
                    total_nonHoliday_peak += time_remaining_charge
                else:
                    total_nonHoliday_nonPeak += time_remaining_charge

            if new_datetime == end_time:
                reachedEnd = True
            current_date_time = new_datetime

        # Calculate Final state of charge for each category
        holiday_peak_fsoc = (
            ((total_holiday_peak / 60) * power / capacity) + (start_state / 100)) * 100
        holiday_nonpeak_fsoc = (
            ((total_holiday_nonPeak / 60) * power / capacity) + (start_state / 100)) * 100
        nonholiday_peak_fsoc = (
            ((total_nonHoliday_peak / 60) * power / capacity) + (start_state / 100)) * 100
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


if __name__ == "__main__":
    C = Calculator()
    config = 1
    start_time = time(17,30)
    start_date = date(2022, 2, 22)
    battery_capacity = 50
    initial_charge = 20
    final_charge = 60
    expected_cost = 0.53
    power = C.get_configuration(config)[0]
    base_cost = C.get_configuration(config)[1]
    charge_time = C.time_calculation(initial_state=initial_charge, final_state=final_charge,
                                                       capacity=battery_capacity, power=power)
    print(C.calculate_solar_energy_future(start_time, end_time, "7250"))
    end_time = C.get_end_time(start_date, start_time, charge_time)
    final_cost = C.total_cost_calculation(start_date=start_date, start_time=start_time,
                                                            start_state=initial_charge, end_time=end_time,
                                                            base_price=base_cost, power=power,
                                                            capacity=battery_capacity, postcode="7250")