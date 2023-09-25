import pandas as pd
import numpy as np

df = pd.read_csv("0825_top.csv")
df_mid = pd.read_csv("0825_mid.csv")
df_jug = pd.read_csv("0825_jug.csv")
df_adc = pd.read_csv("0825_adc.csv")
df_spt = pd.read_csv("0825_spt.csv")

print(f"TOP 데이터 수 : {len(df)}")
print(f"MID 데이터 수 : {len(df_mid)}")
print(f"JUG 데이터 수 : {len(df_jug)}")
print(f"ADC 데이터 수 : {len(df_adc)}")
print(f"SPT 데이터 수 : {len(df_spt)}")

df_list = []
df_id_list = []

for j in range(0,6,2):
    sub_df_list = []
    sub_df_id_list = []
    blue_data_frame = pd.DataFrame(
        [
            # [ TOP , MID , jUG, ADC, SPT ]
            [df.iloc[j]['kda'], df_mid.iloc[j]['kda'], df_jug.iloc[j]['kda'], df_adc.iloc[j]['kda'], df_spt.iloc[j]['kda']],
            [df.iloc[j]['dpd'], df_mid.iloc[j]['dpd'], df_jug.iloc[j]['dpd'], df_adc.iloc[j]['dpd'], df_spt.iloc[j]['dpd']],
            [df.iloc[j]['dpm'], df_mid.iloc[j]['dpm'], df_jug.iloc[j]['dpm'], df_adc.iloc[j]['dpm'], df_spt.iloc[j]['dpm']],
            [df.iloc[j]['dpg'], df_mid.iloc[j]['dpg'], df_jug.iloc[j]['dpg'], df_adc.iloc[j]['dpg'], df_spt.iloc[j]['dpg']],
            [df.iloc[j]['dtpm'],df_mid.iloc[j]['dtpm'],df_jug.iloc[j]['dtpm'], df_adc.iloc[j]['dtpm'], df_spt.iloc[j]['dtpm']],
            [df.iloc[j]['win'], df_mid.iloc[j]['win'], df_jug.iloc[j]['win'], df_adc.iloc[j]['win'], df_spt.iloc[j]['win']]
        ],
        columns=['TOP','MID','JUG','ADC','SPT'],
        index=['kda', 'dpd', 'dpm', 'dpg', 'dtpm','win']
    )
    sub_df_list.append(blue_data_frame)
    sub_df_id_list.append(df.iloc[j]['tid'])
    red_data_frame = pd.DataFrame(
        [
            # [ TOP , MID , jUG, ADC, SPT ]
            [df.iloc[j+1]['kda'], df_mid.iloc[j+1]['kda'], df_jug.iloc[j+1]['kda'], df_adc.iloc[j+1]['kda'], df_spt.iloc[j+1]['kda']],
            [df.iloc[j+1]['dpd'], df_mid.iloc[j+1]['dpd'], df_jug.iloc[j+1]['dpd'], df_adc.iloc[j+1]['dpd'], df_spt.iloc[j+1]['dpd']],
            [df.iloc[j+1]['dpm'], df_mid.iloc[j+1]['dpm'], df_jug.iloc[j+1]['dpm'], df_adc.iloc[j+1]['dpm'], df_spt.iloc[j+1]['dpm']],
            [df.iloc[j+1]['dpg'], df_mid.iloc[j+1]['dpg'], df_jug.iloc[j+1]['dpg'], df_adc.iloc[j+1]['dpg'], df_spt.iloc[j+1]['dpg']],
            [df.iloc[j+1]['dtpm'],df_mid.iloc[j+1]['dtpm'],df_jug.iloc[j+1]['dtpm'], df_adc.iloc[j+1]['dtpm'], df_spt.iloc[j+1]['dtpm']],
            [df.iloc[j+1]['win'], df_mid.iloc[j+1]['win'], df_jug.iloc[j+1]['win'], df_adc.iloc[j+1]['win'], df_spt.iloc[j+1]['win']]
        ],
        columns=['TOP','MID','JUG','ADC','SPT'],
        index=['kda', 'dpd', 'dpm', 'dpg', 'dtpm','win']
    )
    sub_df_list.append(red_data_frame)
    sub_df_id_list.append(df.iloc[j+1]['tid'])
    sub_df_feature = pd.concat(sub_df_list,
                               keys=sub_df_id_list, names=['team', 'feature'])
    df_list.append(sub_df_feature)
    df_id_list.append(df.iloc[j]['id'] // 10)
    blue_id = df.iloc[j]['id'] // 10
    red_id = df.iloc[j+1]['id'] // 10
    if(blue_id != red_id):
        print("아이디가 안맞아요")
    print(j)

df_feature = pd.concat(df_list, keys=df_id_list,
                       names=['id'])
df_feature.to_pickle("0825all_data.pkl")
print(df_feature)