import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pathlib import Path

base_path = Path("aDBS_UPDRS.csv")

df = pd.read_csv(base_path)

metrics = ['total_updrs_iii_score', 'updrs_iii_bradykinesia', 'updrs_iii_tremor', 'updrs_iii_rigidity']
metric_labels = ['Total MDS-UPDRS III Score','Bradykinesia MDS-UPDRS III','Tremor MDS-UPDRS III','Rigidity MDS-UPDRS III']

unique_patients = df['patientid'].unique()
palette = sns.color_palette('pastel', len(unique_patients))
color_dict = {patient: palette[i] for i, patient in enumerate(unique_patients)}

fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(12, 10))
axs = axs.flatten()

offset = 0.2

condition_labels = {cond: idx for idx, cond in enumerate(df['condition'].unique())}

for i, metric in enumerate(metrics):
    sns.stripplot(
        data=df,
        x='condition', y=metric, hue='patientid',
        jitter=.075, ax=axs[i], palette=color_dict, dodge=False, size=10, alpha=0.5
    )

    for condition in df['condition'].unique():
        mean_value = df[df['condition'] == condition][metric].mean()
        std_value = df[df['condition'] == condition][metric].std()

        condition_numeric = condition_labels[condition]

        axs[i].vlines(x=condition_numeric + offset, ymin=mean_value - std_value, ymax=mean_value + std_value,
                      color='black', linewidth=2, alpha=0.5)

        axs[i].hlines(y=mean_value, xmin=condition_numeric - 0.015 + offset,
                      xmax=condition_numeric + 0.015 + offset,
                      color='black', linewidth=2, alpha=0.5)

    axs[i].set_xlabel('Condition')
    axs[i].set_ylabel(metric_labels[i])

    if i == 0:
        axs[i].legend(title='Participant ID', loc='upper right',fontsize=8)
        plt.setp(axs[i].get_legend().get_title(), fontsize='8')
    else:
        axs[i].legend().remove()

    axs[i].set_xticks(list(condition_labels.values()))
    axs[i].set_xticklabels(list(condition_labels.keys()))

    if i == 0:
        axs[i].set_ylim(0, 85)
        axs[i].set_yticks([0,10,20,30,40,50,60,70,80])
    elif i == 1:
         axs[i].set_ylim(-1, 40)
         axs[i].set_yticks([0, 10, 20, 30, 40])
    elif i == 2:
         axs[i].set_ylim(-1, 20)
         axs[i].set_yticks([0, 5, 10, 15, 20])
    elif i == 3:
        axs[i].set_ylim(-1,15)
        axs[i].set_yticks([0, 5, 10, 15])

sns.despine(top = True, right = True)

plt.tight_layout()

# save figure
plt.savefig('aDBS_UPDRS.png', dpi=300)
plt.savefig('aDBS_UPDRS.svg')
plt.savefig('/Users/aDBS_UPDRS.pdf')

plt.show()

