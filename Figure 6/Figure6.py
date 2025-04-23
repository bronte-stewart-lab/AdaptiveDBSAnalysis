import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from matplotlib.gridspec import GridSpec
import imageio.v3 as iio
import matplotlib.image as mpimg
from pathlib import Path

img = mpimg.imread(Path("WFE_Cartoon.png"))
im = iio.imread(Path("WFE_Cartoon.png"))
print(im.shape)

time2_synced = pd.read_csv(Path("time2_synced.csv"))
ycurrent = pd.read_csv(Path("ycurrent.csv"))
synced_apdm_time = pd.read_csv(Path("synced_apdm_time.csv"))
filteredGyroDataLeft = pd.read_csv(Path("filteredGyroDataLeft.csv"))

base_path = Path("aDBS_WFE.csv")
df = pd.read_csv(base_path)

time_start = 85.942635043700340
time_end = 1.147777336874129e+02
ced_apdm_time_sync = 4.541991800000000

fig = plt.figure(figsize=(15, 10))
gs = GridSpec(4, 6, figure=fig)

ax0 = fig.add_subplot(gs[0:2, 0:2])
imgplot = plt.imshow(img)
plt.axis('off')

ax1 = fig.add_subplot(gs[0, 2:6])
ax2 = fig.add_subplot(gs[1, 2:6])

frames = [time2_synced, ycurrent]
amp = pd.concat(frames, axis=1)
amp.columns = ['time2_synced', 'ycurrent1', 'ycurrent2']

frames = [synced_apdm_time, filteredGyroDataLeft]
apdm = pd.concat(frames, axis=1)
apdm.columns = ['synced_apdm_time', 'filteredGyroDataLeft']

sns.lineplot(ax=ax1, x="time2_synced", y="ycurrent1", data=amp, errorbar=None, color="#fbb4ae", alpha=1, linewidth=3)
sns.lineplot(ax=ax1, x="time2_synced", y="ycurrent2", data=amp, errorbar=None, color="#b3cde3", alpha=1, linewidth=3)
ax1.set_xlabel('')
ax1.set_ylabel('Stim Amp (mA)')
ax1.set_xlim(time_start + ced_apdm_time_sync - 5, time_end + ced_apdm_time_sync + 5)
ax1.set_ylim(2, 5)
ax1.set_xticklabels([])
ax1.set_yticks([2.0, 3.0, 4.0, 5.0])
ax1.set_yticklabels([2.0, 3.0, 4.0, 5.0])

sns.lineplot(ax=ax2, x="synced_apdm_time", y="filteredGyroDataLeft", data=apdm, errorbar=None, color="#ccebc5", alpha=1, linewidth=2)
ax2.set_xlabel('Time (s)')
ax2.set_ylabel('Angular Velo (deg/s)')
ax2.set_xlim(time_start + ced_apdm_time_sync - 5, time_end + ced_apdm_time_sync + 5)
ax2.set_ylim(-500, 500)
ax2.set_yticks([-500, -250,0,250, 500])
ax2.set_xticks([time_start + ced_apdm_time_sync - 5, time_start + ced_apdm_time_sync, time_start + ced_apdm_time_sync + 5, time_start + ced_apdm_time_sync + 10, time_start + ced_apdm_time_sync + 15, time_start + ced_apdm_time_sync + 20, time_start + ced_apdm_time_sync + 25, time_start + ced_apdm_time_sync + 30])
ax2.set_xticklabels([0, 5, 10, 15, 20, 25, 30, 35])

fig.align_ylabels((ax1,ax2))

ax3 = fig.add_subplot(gs[2:4, 0:3])
ax4 = fig.add_subplot(gs[2:4, 3:6])

metrics = ['LP_vrms', 'cyc_per_sec']
metric_labels = ['Vrms (deg/s)', 'Cycles Per Second (Hz)']

unique_patients = df['patient_num'].unique()
palette = sns.color_palette('pastel', len(unique_patients))
color_dict = {patient: palette[i] for i, patient in enumerate(unique_patients)}

condition_labels = {cond: idx for idx, cond in enumerate(df['condition'].unique())}

for i, ax in enumerate([ax3, ax4]):
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
                   color='black', linewidth=1, alpha=0.5)

    ax.set_xlabel('Condition')
    ax.set_ylabel(metric_labels[i])
    ax.legend().remove()
    ax.set_xticks(list(condition_labels.values()))
    ax.set_xticklabels(list(condition_labels.keys()))

    if i == 0:
        ax.set_ylim(-5, 500)
        ax.set_yticks([0, 100, 200, 300, 400, 500])
    elif i == 1:
        ax.set_ylim(-.1, 3)
        ax.set_yticks([0, 0.5, 1, 1.5, 2, 2.5, 3])

sns.despine(top=True, right=True)

plt.tight_layout()
plt.savefig('aDBS_WFE.png', dpi=300)
plt.savefig('aDBS_WFE.svg')
plt.savefig('aDBS_WFE.pdf')

plt.show()
