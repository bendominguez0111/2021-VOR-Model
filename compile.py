import pandas as pd

positions = ['rb', 'wr', 'qb', 'te']

dfs = []

for position in positions:
    df = pd.read_csv(f'data/{position}.csv')
    df.drop(df.index[0], inplace=True)
    df['POS'] = position.upper()
    if position == 'rb':
        df = df.rename({
            'ATT': 'RUSH_ATT',
            'YDS': 'RUSH_YD',
            'TDS': 'RUSH_TD',
            'YDS.1': 'REC_YD',
            'TDS.1': 'REC_TD', 
        }, axis=1)
    elif position == 'qb':
        df = df.rename({
            'ATT': 'PASS_ATT',
            'YDS': 'PASS_YD',
            'TDS': 'PASS_TD',
            'ATT.1': 'RUSH_ATT',
            'YDS.1': 'RUSH_YD',
            'TDS.1': 'RUSH_TD'
        }, axis=1)
    elif position == 'wr':
        df = df.rename({
            'ATT': 'RUSH_ATT',
            'YDS': 'REC_YD',
            'TDS': 'REC_TD',
            'YDS.1': 'RUSH_YD',
            'TDS.1': 'RUSH_TD'
        }, axis=1)
    elif position == 'te':
        df = df.rename({
            'YDS': 'REC_YD',
            'TDS': 'REC_TD',
        }, axis=1)
    df = df.drop('FPTS', axis=1)
    dfs.append(df)

df = pd.concat(dfs)
df = df.fillna(0)

df = df.loc[:, df.columns[0:2].tolist()+['POS']+df.columns[2:].tolist()]
df = df.loc[:,~df.columns.duplicated()]

df.to_csv('data/all_compiled.csv')