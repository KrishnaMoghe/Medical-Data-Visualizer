import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv("medical_examination.csv")

# 2
df['overweight'] = None

# 3
# Normalize Cholesterol
df['cholesterol'] = np.where(df['cholesterol'] == 1, 0, df['cholesterol']) 
df['cholesterol'] = np.where(df['cholesterol'] > 1, 1, df['cholesterol'])
# Normalize gluc
df['gluc'] = np.where(df['gluc'] == 1, 0, df['gluc'])
df['gluc'] = np.where(df['gluc'] > 1, 1, df['gluc'])

# 4
def draw_cat_plot():
    # 5. Create a DataFrame for the cat plot using pd.melt
    df_cat = pd.melt(df, id_vars='cardio', value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])
    
    # 6. Group and reformat the data in df_cat to split it by cardio
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='count')
    
    # 7. Convert the data into long format and create a chart that shows the value counts
    fig = sns.catplot(data=df_cat, x='variable', y='count', hue='value', col='cardio', kind='bar')
    
    # 8. Get the figure for the output and store it in the fig variable
    plt.subplots_adjust(top=0.8)  # Adjust the top to fit the title
    fig.fig.suptitle('Categorical Plot of Medical Examination Data')

    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) & 
                 (df['height'] >= df['height'].quantile(0.025)) & 
                 (df['height'] <= df['height'].quantile(0.975)) & 
                 (df['weight'] >= df['weight'].quantile(0.025)) & 
                 (df['weight'] <= df['weight'].quantile(0.975))]

    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(np.ones_like(corr, dtype=bool))



    # 14
    fig, ax = plt.subplots(figsize=(16, 9))

    # 15
    sns.heatmap(corr, mask=mask, annot=True, fmt=".1f", cmap='coolwarm', square=True)
    plt.title('Correlation Heatmap of Medical Examination Data')

    # 16
    fig.savefig('heatmap.png')
    return fig
