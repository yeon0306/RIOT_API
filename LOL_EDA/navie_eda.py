import pandas as pd

df_top = pd.read_csv("0825_top.csv")
df_mid = pd.read_csv("0825_mid.csv")
df_jug = pd.read_csv("0825_jug.csv")
df_spt = pd.read_csv("0825_spt.csv")
df_adc = pd.read_csv("0825_adc.csv")

print(df_top.head())

select_top = df_top[['kda', 'dpd', 'dpm', 'dpg', 'dtpm', 'id']].iloc[0]
select_mid = df_top[['kda', 'dpd', 'dpm', 'dpg', 'dtpm', 'id']].iloc[0]
select_jug = df_jug[['kda', 'dpd', 'dpm', 'dpg', 'dtpm', 'id']].iloc[0]
select_spt = df_top[['kda', 'dpd', 'dpm', 'dpg', 'dtpm', 'id']].iloc[0]
select_adc = df_jug[['kda', 'dpd', 'dpm', 'dpg', 'dtpm', 'id']].iloc[0]
df = pd.DataFrame({'T': select_top, 'M': select_mid, 'J': select_jug, 'S': select_spt, 'A': select_adc})

print(df)