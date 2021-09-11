from datetime import datetime, date, time, timedelta
import holidays


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
    def cost_calculation(self, initial_state: float, final_state: float, capacity:int,
                         is_peak:bool, is_holiday:bool, base_price:int):
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
    def get_day_light_length(self, start_time):
        pass

    # to be acquired through API
    def get_solar_insolation(self, solar_insolation):
        pass

    # to be acquired through API
    def get_cloud_cover(self):
        pass

    def calculate_solar_energy(self):
        pass

    def total_cost_calculation(self, start_date: date, start_time: time, end_time: datetime,
                               start_state:int, final_state:int, base_price: int, power:int, capacity: int):
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
            difference_time_minutes = (new_datetime - current_date_time).total_seconds()/60

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
        holiday_peak_fsoc = (((total_holiday_peak/60)*power/capacity) + (start_state/100)) * 100
        holiday_nonpeak_fsoc = (((total_holiday_nonPeak/60)*power/capacity) + (start_state/100)) * 100
        nonholiday_peak_fsoc = (((total_nonHoliday_peak/60)*power/capacity) + (start_state/100)) * 100
        nonholiday_nonpeak_fsoc = (((total_nonHoliday_nonPeak/60)*power/capacity)
                                   + (start_state/100)) * 100

        cost_holiday_peak = self.cost_calculation(start_state, holiday_peak_fsoc, capacity,
                                                  True, True, base_price)
        cost_holiday_nonpeak = self.cost_calculation(start_state, holiday_nonpeak_fsoc, capacity,
                                                     False, True, base_price)
        cost_nonholiday_peak = self.cost_calculation(start_state, nonholiday_peak_fsoc, capacity,
                                                     True, False, base_price)
        cost_nonholiday_nonpeak = self.cost_calculation(start_state, nonholiday_nonpeak_fsoc,
                                                        capacity, False, False, base_price)

        return round((cost_holiday_peak + cost_holiday_nonpeak + cost_nonholiday_peak + cost_nonholiday_nonpeak), 2)

