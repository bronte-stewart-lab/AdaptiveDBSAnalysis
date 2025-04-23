import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from matplotlib.gridspec import GridSpec
import numpy as np
from pathlib import Path

time2_ced = pd.read_csv(Path("time2_ced.csv"))
ycurrent = pd.read_csv(Path("ycurrent.csv"))
apdm_data = pd.read_csv(Path("apdm_data.csv"))
leftSide = pd.read_csv(Path("leftSide.csv"))

right_start = 5.378409982999999e+02
right_end = 6.488410051000000e+02

leftSide['stride_time_CV_arrhythmicity'] = 100 * leftSide['stride_time_CV_arrhythmicity']
leftSide = leftSide.iloc[5:]
apdm_data["left_ankle_gyro_z"] = -np.degrees(apdm_data["left_ankle_gyro_z"])
apdm_data["right_ankle_gyro_z"] = np.degrees(apdm_data["right_ankle_gyro_z"])

frames = [time2_ced, ycurrent]
amp = pd.concat(frames)
amp.columns = ['time2_ced', 'ycurrent1', 'ycurrent2']

base_path = Path("aDBS_TBC.csv")
df = pd.read_csv(base_path)

fig = plt.figure(figsize=(15, 10))

gs = GridSpec(5, 8, figure=fig)

ax1 = fig.add_subplot(gs[0, 2:8])
ax2 = fig.add_subplot(gs[1, 2:8])
ax3 = fig.add_subplot(gs[2, 2:8])

sns.lineplot(ax=ax1, x="time2_ced", y="ycurrent1", data=amp, errorbar=None, color="#fbb4ae", alpha=1, linewidth=3)
sns.lineplot(ax=ax1, x="time2_ced", y="ycurrent2", data=amp, errorbar=None, color="#b3cde3", alpha=1, linewidth=3)
sns.set_palette("pastel")
ax1.set_xlabel('')
ax1.set_ylabel('Stim Amp (mA)')
ax1.set_xlim(right_start - 5, right_end + 5)
ax1.set_ylim(0, 3)
ax1.set_xticklabels([])
ax1.set_yticks([0,1,2,3])
ax1.set_yticklabels([0,1.0,2.0,3.0])

sns.lineplot(ax=ax2, x="time_ced", y="left_ankle_gyro_z", data=apdm_data, errorbar=None, color="#ccebc5", alpha=1, linewidth=2)
sns.lineplot(ax=ax2, x="time_ced", y="right_ankle_gyro_z", data=apdm_data, errorbar=None, color="#decbe4", alpha=1, linewidth=2)
ax2.set_xlabel('')
ax2.set_ylabel('Angular Velo (deg/s)')
ax2.set_xlim(right_start - 5, right_end + 5)
ax2.set_ylim(-200, 200)
ax2.set_xticklabels([])
ax2.set_yticks([-200,-100,0,100,200])

sns.scatterplot(
    data=leftSide,
    x='peak_times',
    y='stride_time_CV_arrhythmicity',
    ax=ax3,
    hue='model_freeze_labels',
    palette={0: 'black', 1: 'red'},
    size=5,
    alpha=0.5
)

ax3.legend().remove()
ax3.set_xlabel('Time (s)')
ax3.set_ylabel('Arrhythmicity')
ax3.set_xlim(right_start - 5, right_end + 5)
ax3.set_ylim(0, 75)

ax3.set_xticks([right_start-5,right_start+15,right_start+35,right_start+55,right_start+75,right_start+95])
ax3.set_xticklabels([0,20,40,60,80,100])

fig.align_ylabels((ax1,ax2,ax3))

ax4 = fig.add_subplot(gs[3:5, 0:4])
ax5 = fig.add_subplot(gs[3:5, 4:8])

metrics = ['mean_freezing', 'mean_shankav']
metric_labels = ['% Time Freezing','Mean Peak Shank Ang Velo (deg/s)']

unique_patients = df['patient_num'].unique()
palette = sns.color_palette('pastel', len(unique_patients))
color_dict = {patient: palette[i] for i, patient in enumerate(unique_patients)}

condition_labels = {cond: idx for idx, cond in enumerate(df['condition'].unique())}

for i, ax in enumerate([ax4, ax5]):
    sns.stripplot(
        data=df,
        x='condition', y=metrics[i], hue='patient_num',
        jitter=.075, ax=ax, palette=color_dict, dodge=False, size=10, alpha=0.5
    )

    for condition in df['condition'].unique():
        mean_value = df[df['condition'] == condition][metrics[i]].mean()
        std_value = df[df['condition'] == condition][metrics[i]].std()

        condition_numeric = condition_labels[condition]

        ax.vlines(x=condition_numeric + 0.2, ymin=mean_value - std_value, ymax=mean_value + std_value,
                   color='black', linewidth=2, alpha=0.5)

        ax.hlines(y=mean_value, xmin=condition_numeric - 0.015 + 0.2,
                   xmax=condition_numeric + 0.015 + 0.2,
                   color='black', linewidth=2, alpha=0.5)

    ax.set_xlabel('Condition')
    ax.set_ylabel(metric_labels[i])
    ax.legend().remove()
    ax.set_xticks(list(condition_labels.values()))
    ax.set_xticklabels(list(condition_labels.keys()))

    if i == 0:
        ax.set_ylim(-1, 105)
        ax.set_yticks([0,20,40,60,80,100])
    elif i == 1:
        ax.set_ylim(-1, 350)
        ax.set_yticks([0, 100, 200, 300])

sns.despine(top=True, right=True)


plt.tight_layout()
plt.savefig('aDBS_TBC.png', dpi=300)
plt.savefig('aDBS_TBC.svg')
plt.savefig('aDBS_TBC.pdf')

plt.show()
