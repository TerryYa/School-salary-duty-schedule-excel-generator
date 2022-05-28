import pandas as pd
import datetime as dt
import calendar as cal

atrributes = ['*聘任人員身分證字號', '*工作日期(yyyy/mm/dd)', '*工作時間(時)(起)', '*工作時間(分)(起)',
              '*工作時間(時)(迄)', '*工作時間(分)(迄)', '當日共計(小時)(自動計算)', '工作內容', '備註']


def get_data():
    data = pd.read_csv('schedular_config.csv', encoding='utf-8')
    col_names = data.columns
    return (list(data[name]) for name in col_names)


def str_to_list(str):
    return list(str.split(','))


def get_dates(weeks, first_week, max_day):
    dates = []

    for week in weeks:
        week = int(week) - 1
        date = first_week+6 - \
            (first_week-week) if week < first_week else 1+week-first_week

        while True:
            if date > max_day:
                break
            dates.append(date)
            date += 7

    dates.sort()
    return dates


def processing_time(n_weeks, times):
    n_times = len(times)
    if n_weeks < n_times:
        print(f'工作天個數 < 時間個數')
        exit()

    diff = n_weeks - n_times
    # match the number between weekday and time
    for _ in range(diff):
        times.append(times[-1])

    hours, minutes = [], []
    for t in times:
        h, m = t.split(':')
        hours.append(h)
        minutes.append(m)

    return hours, minutes


def auto_generate(ids, list_weeks, list_start, list_end, contents):
    df = pd.DataFrame(columns=(atrributes))

    today = dt.datetime.today()
    year, month_target = today.year, today.month
    first_week, max_day = cal.monthrange(year, month_target)

    for i in range(len(ids)):
        weeks, t1, t2 = str_to_list(list_weeks[i]), str_to_list(
            list_start[i]), str_to_list(list_end[i])

        dates = get_dates(weeks, first_week, max_day)
        n_weeks, n_dates = len(weeks), len(dates)
        start_h, start_m = processing_time(n_weeks, t1)
        end_h, end_m = processing_time(n_weeks, t2)

        n_times = len(start_h)

        for i_d in range(n_dates):
            idx = i_d % n_times
            h1, m1, h2, m2 = int(start_h[idx]), int(
                start_m[idx]), int(end_h[idx]), int(end_m[idx])

            df = df.append({'*聘任人員身分證字號': ids[i],
                            '*工作日期(yyyy/mm/dd)': f'{year}/{month_target:02d}/{dates[i_d]:02d}',
                            '*工作時間(時)(起)': f'{h1:02d}',
                            '*工作時間(分)(起)': f'{m1:02d}',
                            '*工作時間(時)(迄)': f'{h2:02d}',
                            '*工作時間(分)(迄)': f'{m2:02d}',
                            '當日共計(小時)(自動計算)': int((h2-h1)+(m2-m1)/60),
                            '工作內容': contents[i]}, ignore_index=True)

        df = df.append({'*聘任人員身分證字號': None,
                        '*工作日期(yyyy/mm/dd)': None,
                        '*工作時間(時)(起)': None,
                        '*工作時間(分)(起)': None,
                        '*工作時間(時)(迄)': None,
                        '*工作時間(分)(迄)': None,
                        '當日共計(小時)(自動計算)': None,
                        '工作內容': None}, ignore_index=True)

    df.to_excel(f'{year}_{month_target}月出勤表.xlsx', index=False)


def main():
    ids, weeks, start_times, end_times, contents = get_data()
    auto_generate(ids, weeks, start_times, end_times, contents)


if __name__ == "__main__":
    main()
