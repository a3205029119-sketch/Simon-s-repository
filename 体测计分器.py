def get_score_higher_is_better(value, score_table):

    for threshold, score in score_table:
        # 只要测量值 >= 阈值，就返回对应的分数
        if value >= threshold:
            return score
    return 0
    # 如果低于最低标准 (10分线)

def get_score_lower_is_better(value, score_table):

    for threshold, score in score_table:
        # 只要测量值 <= 阈值，就返回对应的分数
        if value <= threshold:
            return score

    # 如果低于最低标准 (10分线)
    return 0

def MALE_BMI(weight_kg, height_M):
    bmi =  weight_kg / (height_M ** 2)
    if bmi >= 28.0:
        score_BMI = 60
        status = "肥胖"
    if bmi <=17.8:
        score_BMI = 80
        status = "偏瘦"
    if 24.0<bmi<=27.9:
        score_BMI = 80
        status = "超重"
    if 17.9<=bmi<=23.9:
        score_BMI = 100
        status = "正常"
    return score_BMI, status,bmi

SCORE_50M_MALE_G1 = [
    (6.7, 100), (6.9, 95), (7.1, 90), (7.3, 85), (7.5, 80),
    (7.7, 78), (7.9, 76), (8.1, 74), (8.3, 72), (8.5, 70),
    (8.7, 68), (8.9, 66), (9.1, 64), (9.2, 62), (9.3, 60),
    (9.5, 50), (9.7, 40), (9.9, 30), (10.1, 20), (10.3, 10)
]
##50米跑
SCORE_SITREACH_MALE_G1 = [
    (24.9, 100), (23.1, 95), (21.3, 90), (19.5, 85), (17.7, 80),
    (16.8, 78), (15.9, 76), (15.0, 74), (14.1, 72), (13.2, 70),
    (12.3, 68), (11.4, 66), (10.5, 64), (9.6, 62), (8.7, 60),
    (6.8, 50), (4.9, 40), (3.7, 30), (3.1, 20), (2.5, 10)
]
##坐位体前屈
SCORE_1000M_MALE_G1 = [
    (197, 100), (207, 95), (217, 90), (227, 85), (237, 80),
    (247, 78), (257, 76), (267, 74), (277, 72), (287, 70),
    (297, 68), (307, 66), (317, 64), (327, 62), (337, 60),
    (347, 50), (357, 40), (367, 30), (377, 20), (390, 10)
]
##1000米跑
SCORE_LUNGCAP_MALE_G1 = [
    (5040, 100), (4920, 95), (4800, 90), (4650, 85), (4500, 80),
    (4300, 78), (4100, 76), (3900, 74), (3700, 72), (3550, 70),
    (3400, 68), (3300, 66), (3200, 64), (3100, 62), (3000, 60),
    (2900, 50), (2800, 40), (2600, 30), (2450, 20), (2300, 10)
]##肺活量

SCORE_PULLUP_MALE_G1 = [
    (19, 100), (18, 95), (17, 90), (16, 85), (15, 80),
    (14, 78), (13, 76), (12, 74), (11, 72), (10, 70),
    (9, 68), (8, 66), (7, 64), (6, 62), (5, 60),
    (4, 50), (3, 40), (2, 30), (1, 20), (0, 10) # 0次得10分
]##引体向上

SCORE_LONGJUMP_MALE_G1 = [
    (273, 100), (268, 95), (263, 90), (258, 85), (253, 80),
    (248, 78), (243, 76), (238, 74), (233, 72), (228, 70),
    (223, 68), (218, 66), (213, 64), (208, 62), (203, 60),
    (198, 50), (193, 40), (188, 30), (183, 20), (178, 10)
]##立定跳远

weight_kg = float(input("请输入您的体重 (kg)："))
height_cm = float(input("请输入您的身高 (cm)："))
height_M = height_cm / 100
Score_BMI,Status,BMI = MALE_BMI(weight_kg, height_M)
print(f"您的BMI得分为{Score_BMI}，状态为{Status}，BMI值为{BMI}")


Time_50M = float(input("请输入50米跑的成绩(s)："))
Score_50M = get_score_lower_is_better(Time_50M, SCORE_50M_MALE_G1)
print(f"50米跑的成绩为{Score_50M}")

Length_SITREACH = float(input("请输入坐位体前屈的成绩(cm)："))
Score_SITREACH = get_score_higher_is_better(Length_SITREACH, SCORE_SITREACH_MALE_G1)
print(f"坐位体前屈的成绩为{Score_SITREACH}")

Time_1000M = float(input("请输入1000米跑的成绩(s)："))
Score_1000M = get_score_lower_is_better(Time_1000M, SCORE_1000M_MALE_G1)
print(f"1000米跑的成绩为{Score_1000M}")

Volume_LUNGCAP = float(input("请输入肺活量的成绩(mL)："))
Score_LUNGCAP = get_score_higher_is_better(Volume_LUNGCAP, SCORE_LUNGCAP_MALE_G1)
print(f"肺活量的成绩为{Score_LUNGCAP}")

Time_PULLUP = float(input("请输入引体向上的成绩(次)："))
Score_PULLUP = get_score_higher_is_better(Time_PULLUP, SCORE_PULLUP_MALE_G1)
print(f"引体向上的成绩为{Score_PULLUP}")

Length_LONGJUMP = float(input("请输入立定跳远的成绩(cm)："))
Score_LONGJUMP = get_score_higher_is_better(Length_LONGJUMP, SCORE_LONGJUMP_MALE_G1)
print(f"立定跳远的成绩为{Score_LONGJUMP}")

##总分
Toalt_Score = Score_50M*0.2 + Score_SITREACH*0.1 + Score_1000M*0.2 + Score_LUNGCAP*0.15 + Score_PULLUP*0.1 + Score_LONGJUMP*0.1+score_BMI*0.15
print(f"总分的成绩为{Total_Score}")
