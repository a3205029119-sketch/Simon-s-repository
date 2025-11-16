import streamlit as st
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

def Male_BMI(weight_kg, height_m):
    bmi =  weight_kg / (height_m ** 2)
    if 17.9 <= bmi <= 23.9:
        score_BMI = 100
        status = "正常"
    elif 24.0 <= bmi <= 27.9:
        score_BMI = 80
        status = "超重"
    elif bmi <= 17.8:
        score_BMI = 80
        status = "偏瘦"
    elif bmi >= 28.0:
        score_BMI = 60
        status = "肥胖"
    else:
        score_BMI = 80
        status = "偏瘦 (边缘)"

    return score_BMI, status, bmi
def Female_BMI(weight_kg, height_m):
    bmi =  weight_kg / (height_m ** 2)
    if 17.2 <= bmi <= 23.9:
        score_BMI = 100
        status = "正常"
    elif 24.0 <= bmi <= 27.9:
        score_BMI = 80
        status = "超重"
    elif bmi <= 17.1:
        score_BMI = 80
        status = "偏瘦"
    elif bmi >= 28.0:
        score_BMI = 60
        status = "肥胖"
    else:
        score_BMI = 80
        status = "偏瘦 (边缘)"

    return score_BMI, status, bmi
##———————————————男生——————————————————##
##大一大二男生50米跑
SCORE_50M_MALE_G1_G2 = [
    (6.7, 100), (6.9, 95), (7.1, 90), (7.3, 85), (7.5, 80),
    (7.7, 78), (7.9, 76), (8.1, 74), (8.3, 72), (8.5, 70),
    (8.7, 68), (8.9, 66), (9.1, 64), (9.2, 62), (9.3, 60),
    (9.5, 50), (9.7, 40), (9.9, 30), (10.1, 20), (10.3, 10)
]
##大三大四男生50米跑
SCORE_50M_MALE_G3_G4 = [
    (6.6, 100), (6.7, 95), (6.8, 90), (6.9, 85), (7.0, 80),
    (7.2, 78), (7.4, 76), (7.6, 74), (7.8, 72), (8.0, 70),
    (8.2, 68), (8.4, 66), (8.6, 64), (8.8, 62), (9.0, 60),
    (9.2, 50), (9.4, 40), (9.6, 30), (9.8, 20), (10.0, 10)
]


##大一大二男生坐位体前屈
SCORE_SITREACH_MALE_G1_G2 = [
    (24.9, 100), (23.1, 95), (21.3, 90), (19.5, 85), (17.7, 80),
    (16.3, 78), (14.9, 76), (13.5, 74), (12.1, 72), (10.7, 70),
    (9.3, 68), (7.9, 66), (6.5, 64), (5.1, 62), (3.7, 60),
    (2.7, 50), (1.7, 40), (0.7, 30), (-0.3, 20), (-1.3, 10)
]
##大三大四男生坐位体前屈
SCORE_SITREACH_MALE_G3_G4 = [
    (25.1, 100), (23.3, 95), (21.5, 90), (19.9, 85), (18.2, 80),
    (16.8, 78), (15.4, 76), (14.0, 74), (12.6, 72), (11.2, 70),
    (9.8, 68), (8.4, 66), (7.0, 64), (5.6, 62), (4.2, 60),
    (3.2, 50), (2.2, 40), (1.2, 30), (0.2, 20), (-0.8, 10)
]


##大一大二男生1000米跑
SCORE_1000M_MALE_G1_G2 = [
    (197, 100), (202, 95), (207, 90), (214, 85), (222, 80),
    (227, 78), (232, 76), (237, 74), (242, 72), (247, 70),
    (252, 68), (257, 66), (262, 64), (267, 62), (272, 60),
    (292, 50), (312, 40), (332, 30), (352, 20), (372, 10)
]
##大三大四男生1000米跑
SCORE_1000M_MALE_G3_G4 = [
    (195, 100), (200, 95), (205, 90), (212, 85), (220, 80),
    (225, 78), (230, 76), (235, 74), (240, 72), (245, 70),
    (250, 68), (255, 66), (260, 64), (265, 62), (270, 60),
    (290, 50), (310, 40), (330, 30), (350, 20), (370, 10)
]


##大一大二男生肺活量
SCORE_LUNGCAP_MALE_G1_G2 = [
    (5040, 100), (4920, 95), (4800, 90), (4650, 85), (4500, 80),
    (4300, 78), (4100, 76), (3900, 74), (3700, 72), (3550, 70),
    (3400, 68), (3300, 66), (3200, 64), (3100, 62), (3000, 60),
    (2900, 50), (2800, 40), (2600, 30), (2450, 20), (2300, 10)
]
##大三大四男生肺活量
SCORE_LUNGCAP_MALE_G3_G4 = [
    (5140, 100), (5020, 95), (4900, 90), (4650, 85), (4400, 80),
    (4280, 78), (4160, 76), (4040, 74), (3920, 72), (3800, 70),
    (3680, 68), (3560, 66), (3440, 64), (3320, 62), (3200, 60),
    (3030, 50), (2860, 40), (2690, 30), (2520, 20), (2350, 10)
]


##大一大二男生引体向上
SCORE_PULLUP_MALE_G1_G2 = [
    (19, 100), (18, 95), (17, 90), (16, 85), (15, 80),
    (14, 76), (13, 72), (12, 68), (11, 64), (10, 60),
    (9, 50), (8, 40), (7, 30), (6, 20), (5, 10)
]
##大三大四男生引体向上
SCORE_PULLUP_MALE_G3_G4 = [
    (20, 100), (19, 95), (18, 90), (17, 85), (16, 80),
    (15, 76), (14, 72), (13, 68), (12, 64), (11, 60),
    (10, 50), (9, 40), (8, 30), (7, 20), (6, 10)
]


##大一大二男生立定跳远
SCORE_LONGJUMP_MALE_G1_G2 = [
    (273, 100), (268, 95), (263, 90), (258, 85), (253, 80),
    (248, 78), (243, 76), (238, 74), (233, 72), (228, 70),
    (223, 68), (218, 66), (213, 64), (208, 62), (203, 60),
    (198, 50), (193, 40), (188, 30), (183, 20), (178, 10)
]
##大三大四男生立定跳远
SCORE_LONGJUMP_MALE_G3_G4 = [
    (275, 100), (270, 95), (265, 90), (258, 85), (250, 80),
    (246, 78), (242, 76), (238, 74), (234, 72), (230, 70),
    (226, 68), (222, 66), (218, 64), (214, 62), (210, 60),
    (205, 50), (200, 40), (195, 30), (190, 20), (185, 10)
]
##————————————————男生—————————————————##


##———————————————女生——————————————————##
##女生立定跳远
SCORE_LONGJUMP_FEMALE_G1_G2 = [
    (207, 100), (201, 95), (195, 90), (188, 85), (181, 80),
    (178, 78), (175, 76), (172, 74), (169, 72), (166, 70),
    (163, 68), (160, 66), (157, 64), (154, 62), (151, 60),
    (146, 50), (141, 40), (136, 30), (131, 20), (126, 10)
]
SCORE_LONGJUMP_FEMALE_G3_G4 = [
    (208, 100), (202, 95), (196, 90), (189, 85), (182, 80),
    (179, 78), (176, 76), (173, 74), (170, 72), (167, 70),
    (164, 68), (161, 66), (158, 64), (155, 62), (152, 60),
    (147, 50), (142, 40), (137, 30), (132, 20), (127, 10)
]

##女生仰卧起坐
SCORE_SITUP_FEMALE_G1_G2 = [
    (56, 100), (54, 95), (52, 90), (49, 85), (46, 80),
    (44, 78), (42, 76), (40, 74), (38, 72), (36, 70),
    (34, 68), (32, 66), (30, 64), (28, 62), (26, 60),
    (24, 50), (22, 40), (20, 30), (18, 20), (16, 10)
]
SCORE_SITUP_FEMALE_G3_G4 = [
    (57, 100), (55, 95), (53, 90), (50, 85), (47, 80),
    (45, 78), (43, 76), (41, 74), (39, 72), (37, 70),
    (35, 68), (33, 66), (31, 64), (29, 62), (27, 60),
    (25, 50), (23, 40), (21, 30), (19, 20), (17, 10)
]

##女生800米跑
SCORE_800M_FEMALE_G1_G2 = [
    (198, 100), (204, 95), (210, 90), (217, 85), (224, 80),
    (229, 78), (234, 76), (239, 74), (244, 72), (249, 70),
    (254, 68), (259, 66), (264, 64), (269, 62), (274, 60),
    (284, 50), (294, 40), (304, 30), (314, 20), (324, 10)
]
SCORE_800M_FEMALE_G3_G4 = [
    (196, 100), (202, 95), (208, 90), (215, 85), (222, 80),
    (227, 78), (232, 76), (237, 74), (242, 72), (247, 70),
    (252, 68), (257, 66), (262, 64), (267, 62), (272, 60),
    (282, 50), (292, 40), (302, 30), (312, 20), (322, 10)
]

##女生坐位体前屈
SCORE_SITREACH_FEMALE_G1_G2 = [
    (25.8, 100), (24.0, 95), (22.2, 90), (20.6, 85), (19.0, 80),
    (17.7, 78), (16.4, 76), (15.1, 74), (13.8, 72), (12.5, 70),
    (11.2, 68), (9.9, 66), (8.6, 64), (7.3, 62), (6.0, 60),
    (5.2, 50), (4.4, 40), (3.6, 30), (2.8, 20), (2.0, 10)
]
SCORE_SITREACH_FEMALE_G3_G4 = [
    (26.3, 100), (24.4, 95), (22.4, 90), (21.0, 85), (19.5, 80),
    (18.2, 78), (16.9, 76), (15.6, 74), (14.3, 72), (13.0, 70),
    (11.7, 68), (10.4, 66), (9.1, 64), (7.8, 62), (6.5, 60),
    (5.7, 50), (4.9, 40), (4.1, 30), (3.3, 20), (2.5, 10)
]

##女生50米跑
SCORE_50M_FEMALE_G1_G2 = [
    (7.5, 100), (7.6, 95), (7.7, 90), (7.9, 85), (8.0, 80),
    (8.3, 78), (8.5, 76), (8.7, 74), (8.9, 72), (9.1, 70),
    (9.3, 68), (9.5, 66), (9.7, 64), (9.9, 62), (10.1, 60),
    (10.3, 50), (10.5, 40), (10.7, 30), (10.9, 20), (11.1, 10)
]
SCORE_50M_FEMALE_G3_G4 = [
    (7.4, 100), (7.5, 95), (7.6, 90), (7.8, 85), (7.9, 80),
    (8.2, 78), (8.4, 76), (8.6, 74), (8.8, 72), (9.0, 70),
    (9.2, 68), (9.4, 66), (9.6, 64), (9.8, 62), (10.0, 60),
    (10.2, 50), (10.4, 40), (10.6, 30), (10.8, 20), (11.0, 10)
]

##女生肺活量
SCORE_LUNGCAP_FEMALE_G1_G2 = [
    (3400, 100), (3350, 95), (3300, 90), (3150, 85), (3000, 80),
    (2900, 78), (2800, 76), (2700, 74), (2600, 72), (2500, 70),
    (2400, 68), (2300, 66), (2200, 64), (2100, 62), (2000, 60),
    (1960, 50), (1920, 40), (1880, 30), (1840, 20), (1800, 10)
]
SCORE_LUNGCAP_FEMALE_G3_G4 = [
    (3450, 100), (3400, 95), (3350, 90), (3200, 85), (3050, 80),
    (2950, 78), (2850, 76), (2750, 74), (2650, 72), (2550, 70),
    (2450, 68), (2350, 66), (2250, 64), (2150, 62), (2050, 60),
    (2010, 50), (1970, 40), (1930, 30), (1890, 20), (1850, 10)
]
##———————————————女生——————————————————##

##———————————————UI部分——————————————————##
st.markdown("<h1 style='text-align: center;'>体测计分器</h1>", unsafe_allow_html=True)
st.header("基本信息")
grade_choice = st.radio("请选择你的年级：",('大一/大二', '大三/大四'),index=0,horizontal=True)
gender_choice = st.radio("请选择你的性别：",("男", "女"),index=0,horizontal=True)
weight = st.number_input("体重(kg)",value = 50.00,min_value = 0.00,format = "%.2f")
height = st.number_input("身高(cm)",value = 175.0 ,min_value = 0.00,format = "%.2f")
st.header("必测项目")
if gender_choice == "男":
    col1, col2 = st.columns(2)
    with col1:
        Time_50M = st.number_input("50米跑 (s)", value= 0.0,format="%.1f")
        Time_1000M = st.number_input("1000米跑 (s)", value=0, format="%d")
        Volume_LUNGCAP = st.number_input("肺活量 (ml)", value=0, format="%d")
    with col2:
        Length_SITREACH = st.number_input("坐位体前屈 (cm)", value=0.0, format="%.1f")
        Time_PULLUP = st.number_input("引体向上 (次)", value=0, format="%d")
        Length_LONGJUMP = st.number_input("立定跳远 (cm)", value=0.0, format="%.0f")
elif gender_choice == "女":
    col1, col2 = st.columns(2)
    with col1:
        Time_50M = st.number_input("50米跑 (s)", value= 0.0,format="%.1f")
        Time_800M = st.number_input("800米跑 (s)", value=0.0, format="%.1f")
        Volume_LUNGCAP = st.number_input("肺活量 (ml)", value=0, format="%d")
    with col2:
        Length_SITREACH = st.number_input("坐位体前屈 (cm)", value=0.0, format="%.1f")
        Time_SITUP = st.number_input("仰卧起坐 (次)", value=0, format="%d")
        Length_LONGJUMP = st.number_input("立定跳远 (cm)", value=0.0, format="%.0f")

if st.button("计算总分"):

    height_M = height / 100
    if grade_choice == "大一/大二":
        Score_Table_50M = SCORE_50M_MALE_G1_G2
        Score_Table_SITREACH = SCORE_SITREACH_MALE_G1_G2
        Score_Table_1000M = SCORE_1000M_MALE_G1_G2
        Score_Table_LUNGCAP = SCORE_LUNGCAP_MALE_G1_G2
        Score_Table_PULLUP = SCORE_PULLUP_MALE_G1_G2
        Score_Table_LONGJUMP = SCORE_LONGJUMP_MALE_G1_G2

        Female_Score_Table_50M = SCORE_50M_FEMALE_G1_G2
        Female_Score_Table_800M = SCORE_800M_FEMALE_G1_G2
        Female_Score_Table_SITREACH = SCORE_SITREACH_FEMALE_G1_G2
        Female_Score_Table_LUNGCAP = SCORE_LUNGCAP_FEMALE_G1_G2
        Female_Score_Table_STRENGTH = SCORE_SITUP_FEMALE_G1_G2
        Female_Score_Table_LONGJUMP = SCORE_LONGJUMP_FEMALE_G1_G2
    else :
        Score_Table_50M = SCORE_50M_MALE_G3_G4
        Score_Table_SITREACH = SCORE_SITREACH_MALE_G3_G4
        Score_Table_1000M = SCORE_1000M_MALE_G3_G4
        Score_Table_LUNGCAP = SCORE_LUNGCAP_MALE_G3_G4
        Score_Table_PULLUP = SCORE_PULLUP_MALE_G3_G4
        Score_Table_LONGJUMP = SCORE_LONGJUMP_MALE_G3_G4

        Female_Score_Table_50M = SCORE_50M_FEMALE_G3_G4
        Female_Score_Table_800M = SCORE_800M_FEMALE_G3_G4
        Female_Score_Table_SITREACH = SCORE_SITREACH_FEMALE_G3_G4
        Female_Score_Table_LUNGCAP = SCORE_LUNGCAP_FEMALE_G3_G4
        Female_Score_Table_STRENGTH = SCORE_SITUP_FEMALE_G3_G4
        Female_Score_Table_LONGJUMP = SCORE_LONGJUMP_FEMALE_G3_G4

    #各项得分
    if gender_choice == "男":
        Score_BMI, Status, BMI = Male_BMI(weight, height_M)
        Score_50M = get_score_lower_is_better(Time_50M, Score_Table_50M)
        Score_SITREACH = get_score_higher_is_better(Length_SITREACH, Score_Table_SITREACH)
        Score_LONG = get_score_lower_is_better(Time_1000M, Score_Table_1000M)
        Score_LUNGCAP = get_score_higher_is_better(Volume_LUNGCAP, Score_Table_LUNGCAP)
        Score_STRENGTH = get_score_higher_is_better(Time_PULLUP, Score_Table_PULLUP)
        Score_LONGJUMP = get_score_higher_is_better(Length_LONGJUMP, Score_Table_LONGJUMP)



    elif gender_choice == "女":
        Score_BMI, Status, BMI = Female_BMI(weight, height_M)
        Score_50M = get_score_lower_is_better(Time_50M, Female_Score_Table_50M)
        Score_SITREACH = get_score_higher_is_better(Length_SITREACH, Female_Score_Table_SITREACH)
        Score_LONG = get_score_lower_is_better(Time_800M, Female_Score_Table_800M)
        Score_LUNGCAP = get_score_higher_is_better(Volume_LUNGCAP, Female_Score_Table_LUNGCAP)
        Score_STRENGTH = get_score_higher_is_better(Time_SITUP, Female_Score_Table_STRENGTH)
        Score_LONGJUMP = get_score_higher_is_better(Length_LONGJUMP, Female_Score_Table_LONGJUMP)




    total_score = (Score_50M * 0.2) + (Score_SITREACH * 0.1) + \
                  (Score_LONG * 0.2) + (Score_LUNGCAP * 0.15) + \
                  (Score_STRENGTH * 0.1) + (Score_LONGJUMP * 0.1) + \
                  (Score_BMI * 0.15)
    # 5. 显示结果
    st.header("--- 计算结果 ---")
    st.subheader(f"你的总分是: {total_score:.2f}")
    st.metric(label="BMI", value=f"{BMI:.2f} ({Status})", delta=f"{Score_BMI} 分")
    # 用列来展示各项得分
    col_res1, col_res2, col_res3 = st.columns(3)
    with col_res1:
        st.metric(label="50米跑", value=f"{Time_50M}s", delta=f"{Score_50M} 分")
        if gender_choice == "男":
            st.metric(label="1000米跑", value=f"{Time_1000M}s", delta=f"{Score_LONG} 分")
        else:
            st.metric(label="800米跑", value=f"{Time_800M}s", delta=f"{Score_LONG} 分")
    with col_res2:
        st.metric(label="坐位体前屈", value=f"{Length_SITREACH}cm", delta=f"{Score_SITREACH} 分")
        if gender_choice == "男":
            st.metric(label="引体向上", value=f"{Time_PULLUP}次", delta=f"{Score_STRENGTH} 分")
        else:
            st.metric(label="仰卧起坐", value=f"{Time_SITUP}次", delta=f"{Score_STRENGTH} 分")
    with col_res3:
        st.metric(label="肺活量", value=f"{Volume_LUNGCAP}ml", delta=f"{Score_LUNGCAP} 分")
        st.metric(label="立定跳远", value=f"{Length_LONGJUMP}cm", delta=f"{Score_LONGJUMP} 分")



