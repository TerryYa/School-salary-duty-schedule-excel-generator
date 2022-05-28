# School-salary-duty-schedule-excel-generator(自動生成出勤表)

## Description

Auto-generate the duty schedule sheet for the school salary. It's based on the excel format of the school salary system requirement.

The python script will get the data from the `schedular_config.csv`, and generate the duty schedule excel file.

>**📌** If there is no `schedular_config.csv`, please build it by yourself, don't be lazy pals~😂

## schedular_config format
|身分證字號|工作天(星期)|開始時間(hr:min)|截止時間(hr:min)|工作內容|
|:-------:|:----------:|:-------------:|:--------------:|:-----:|
|Your ID/ARC|Workday(weekday)|Start Time|End Time|Work content|
|A123456789| 1,5,7| 9:00, 18:00|12:00,21:00|Ai tech survey|
|...|...|...|...|...|

## Columns explanation

1. 身分證字號
    - Please enter your ID/ARC, it's only accept a single data

2. 工作天(星期)

    - It means weekdays that you work in the current month, From 1(Mon) to 7(Sun), accept multi-data.

3. 開始時間(hr:min)

    - When you start your work, accept multi-data
    
    - It corresponds to each weekday, the last one will be used for the left weekdays if the number is less than the number of weekdays.

        - e.g.
            1. Each time matches each weekday
                |工作天(星期)|開始時間(hr:min)|
                |:---------:|:--------------:|
                |2,5,6|09:00,18:00,09:00|

            2. Left weekdays are at the same time
                |工作天(星期)|開始時間(hr:min)|
                |:---------:|:--------------:|
                |2,5,6|09:00,18:00|

            3. All weekdays are at the same times
                |工作天(星期)|開始時間(hr:min)|
                |:---------:|:--------------:|
                |2,5,6|09:00|

4. 截止時間(hr:min)

    - When you end your work, accept multi-data
    
    - The way to fill in the time is almost same as the start time.

5. 工作內容

    - what job do you work at, only accept a single data