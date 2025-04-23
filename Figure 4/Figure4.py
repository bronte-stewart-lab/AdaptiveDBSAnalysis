import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from matplotlib.gridspec import GridSpec
from pathlib import Path

# Load your data for the first plot
time2_ced = pd.read_csv(Path("time2_ced.csv"))
ycurrent = pd.read_csv(Path("ycurrent.csv"))
bertec_data = pd.read_csv(Path("bertec_data.csv"))
apdm_gait_parameters = pd.read_csv(Path("apdm_gait_parameters.csv"))
body_weight = 8.429434213653230e+02
move_start_ced_adjusted = 1.264262413000000e+02
move_end_ced_adjusted = 2.303882413000000e+02

bertec_data['force_left'] = 100*bertec_data['force_left']/body_weight
bertec_data['force_right'] = 100*bertec_data['force_right']/body_weight

apdm_gait_parameters['stride_time_CV_arrhythmicity'] = 100*apdm_gait_parameters['stride_time_CV_arrhythmicity']
apdm_gait_parameters = apdm_gait_parameters.iloc[5:]

frames = [time2_ced, ycurrent]
amp = pd.concat(frames)
amp.columns =['time2_ced', 'ycurrent1','ycurrent2']

base_path = Path("aDBS_SIP.csv")
df = pd.read_csv(base_path)

fig = plt.figure(figsize=(15, 10))
gs = GridSpec(4, 10, figure=fig)

ax1 = fig.add_subplot(gs[0, 2:10])
ax2 = fig.add_subplot(gs[1, 2:10])

sns.lineplot(ax=ax1, x="time2_ced", y="ycurrent1",
             data=amp,errorbar=None,color="#fbb4ae",alpha=1,linewidth=3)

sns.lineplot(ax=ax1, x="time2_ced", y="ycurrent2",
             data=amp,errorbar=None,color="#b3cde3",alpha=1,linewidth=3)
sns.set_palette("pastel")

ax1.set_xlabel('')
ax1.set_ylabel('Stim Amp (mA)')
ax1.set_xlim(move_start_ced_adjusted-5, move_end_ced_adjusted + 5)
ax1.set_ylim(0, 5.5)
ax1.set_xticklabels([])
ax1.set_yticks([0,2,4])
ax1.set_yticklabels([0,2.0,4.0])

sns.lineplot(ax=ax2, x="ced_time", y="force_left",
             data=bertec_data,errorbar=None,color="#ccebc5",alpha=1,linewidth=2)
sns.lineplot(ax=ax2, x="ced_time", y="force_right",
             data=bertec_data,errorbar=None,color="#decbe4",alpha=1,linewidth=2)
ax2.set_xlabel('')
ax2.set_ylabel('% Body Weight')
ax2.set_xlim(move_start_ced_adjusted-5, move_end_ced_adjusted + 5)
ax2.set_ylim(-1, 101)
ax2.set_xticklabels([])

ax2.set_xlabel('Time (s)')
ax2.set_xticklabels([0,20,40,60,80,100])

fig.align_ylabels((ax1,ax2))

ax4 = fig.add_subplot(gs[2:4, 0:5])
ax5 = fig.add_subplot(gs[2:4, 5:10])

metrics = ['freezes', 'mean_shank_av']
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
    ax.legend().remove()  # Remove legend from subplots
    ax.set_xticks(list(condition_labels.values()))
    ax.set_xticklabels(list(condition_labels.keys()))

    if i == 0:
        ax.set_ylim(-1, 105)
        ax.set_yticks([0,20,40,60,80,100])
    elif i == 1:
        ax.set_ylim(-1, 120)
        ax.set_yticks([0, 20, 40, 60, 80, 100, 120])

sns.despine(top=True, right=True)

plt.tight_layout()
plt.savefig('aDBS_SIP.png', dpi=300)
plt.savefig('aDBS_SIP.svg')
plt.savefig('aDBS_SIP.pdf')

plt.show()
