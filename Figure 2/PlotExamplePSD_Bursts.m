%%
load(NeuralWorkspace.mat)

%%
color_OFF = [12/255 44/255 132/255];
color_25 = [34/255 94/255 168/255];
color_50 = [29/255 145/255 192/255];
color_75 = [65/255 182/255 196/255];
color_85 = [127/255 205/255 187/255];
color_100 = [199/255 233/255 180/255];
color_110 = [255/255 255/255 204/255];

Fw_OFF = PSD_OFF_ch1(:,1);
Pw_OFF = PSD_OFF_ch1(:,2);
conf_lim_OFF= PSD_OFF_ch1(:,5:6);

Fw_25 = PSD_Titration2_ch1(:,1,3);
Pw_25 = PSD_Titration2_ch1(:,2,3);
conf_lim_25= PSD_Titration2_ch1(:,5:6,3);

Fw_50 = PSD_Titration2_ch1(:,1,1);
Pw_50 = PSD_Titration2_ch1(:,2,1);
conf_lim_50= PSD_Titration2_ch1(:,5:6,1);

Fw_75 = PSD_Titration1_ch1(:,1,1);
Pw_75 = PSD_Titration1_ch1(:,2,1);
conf_lim_75= PSD_Titration1_ch1(:,5:6,1);

Fw_85 = PSD_Titration1_ch1(:,1,2);
Pw_85 = PSD_Titration1_ch1(:,2,2);
conf_lim_85= PSD_Titration1_ch1(:,5:6,2);

Fw_100 = PSD_Titration1_ch1(:,1,3);
Pw_100 = PSD_Titration1_ch1(:,2,3);
conf_lim_100= PSD_Titration1_ch1(:,5:6,3);

Fw_110 = PSD_Titration2_ch1(:,1,2);
Pw_110 = PSD_Titration2_ch1(:,2,2);
conf_lim_110= PSD_Titration2_ch1(:,5:6,2);


%%

figure
hold on;
plot(Fw_OFF, 10*log10(Pw_OFF),'Color',color_OFF);
boundedline(Fw_OFF, 10*log10(Pw_OFF),[10*log10(Pw_OFF)-10*log10(conf_lim_OFF(:,1))  -10*log10(Pw_OFF)+10*log10(conf_lim_OFF(:,2))],'cmap',color_OFF,'alpha');
% 25%
plot(Fw_25, 10*log10(Pw_25),'Color',color_25);
boundedline(Fw_25, 10*log10(Pw_25),[10*log10(Pw_25)-10*log10(conf_lim_25(:,1))  -10*log10(Pw_25)+10*log10(conf_lim_25(:,2))],'cmap',color_25,'alpha');
% 50%
plot(Fw_50, 10*log10(Pw_50),'Color',color_50);
boundedline(Fw_50, 10*log10(Pw_50),[10*log10(Pw_50)-10*log10(conf_lim_50(:,1))  -10*log10(Pw_50)+10*log10(conf_lim_50(:,2))],'cmap',color_50,'alpha');
% 75%
plot(Fw_75, 10*log10(Pw_75),'Color',color_75);
boundedline(Fw_75, 10*log10(Pw_75),[10*log10(Pw_75)-10*log10(conf_lim_75(:,1))  -10*log10(Pw_75)+10*log10(conf_lim_75(:,2))],'cmap',color_75,'alpha');
% 85%
plot(Fw_85, 10*log10(Pw_85),'Color',color_85);
boundedline(Fw_85, 10*log10(Pw_85),[10*log10(Pw_85)-10*log10(conf_lim_85(:,1))  -10*log10(Pw_85)+10*log10(conf_lim_85(:,2))],'cmap',color_85,'alpha');
% 100%
plot(Fw_100, 10*log10(Pw_100),'Color',color_100);
boundedline(Fw_100, 10*log10(Pw_100),[10*log10(Pw_100)-10*log10(conf_lim_100(:,1))  -10*log10(Pw_100)+10*log10(conf_lim_100(:,2))],'cmap',color_100,'alpha');
% 110%
plot(Fw_110, 10*log10(Pw_110),'Color',color_110);
boundedline(Fw_110, 10*log10(Pw_110),[10*log10(Pw_110)-10*log10(conf_lim_110(:,1))  -10*log10(Pw_110)+10*log10(conf_lim_110(:,2))],'cmap',color_110,'alpha');

ylabel('Power (dB/Hz)')
xlabel('Frequency (Hz)')
xlim([0 60])

box off
H=gca;
H.LineWidth=2.5; 
H.FontSize=18;
H.FontName = 'Helvetica';

%%
num_bins = 100;
LW = 1;
bin_width = 0.2;
bd_thresh = 0.771;

figure
hold on
ax1 = subplot(421);
histogram(OFF_pksThresh_ch1(:,7), num_bins,'BinWidth',bin_width,'FaceColor',color_OFF)
xline(bd_thresh,'--','Color','k','LineWidth',LW)
ylim([0 10])
box off

subax = axes('Position',[0.3 0.86 0.15 0.05])
histogram(subax,OFF_pksThresh_ch1(:,7),'BinWidth',0.2,'FaceColor',color_OFF)
xlim([5 10])


% 25%
ax2 = subplot(423)
histogram(run2(3).Titration_pksThresh_ch1(:,7),'BinWidth',bin_width,'FaceColor',color_25) 
xline(bd_thresh,'--','Color','k','LineWidth',LW)
ylim([0 5])
box off

subax = axes('Position',[0.3 0.64 0.15 0.05])
histogram(subax,run2(3).Titration_pksThresh_ch1(:,7),'BinWidth',0.2,'FaceColor',color_25)
xlim([5 10])


% 50%
ax3 = subplot(425)
histogram(run2(1).Titration_pksThresh_ch1(:,7),'BinWidth',bin_width,'FaceColor',color_50) 
xline(bd_thresh,'--','Color','k','LineWidth',LW)
ylim([0 5])
box off

subax = axes('Position',[0.3 0.42 0.15 0.05])
histogram(subax,run2(1).Titration_pksThresh_ch1(:,7),'BinWidth',0.2,'FaceColor',color_50)
xlim([5 10])

% 75%
ax4 = subplot(427)
histogram(run(1).Titration_pksThresh_ch1(:,7),'BinWidth',bin_width,'FaceColor',color_75)
xline(bd_thresh,'--','Color','k','LineWidth',LW)
ylim([0 20])
box off

% 85%
ax5 = subplot(422)
histogram(run(2).Titration_pksThresh_ch1(:,7),'BinWidth',bin_width,'FaceColor',color_85) 
xline(bd_thresh,'--','Color','k','LineWidth',LW)
ylim([0 25])
box off

% 100%
ax6 = subplot(424)
histogram(run(3).Titration_pksThresh_ch1(:,7),'BinWidth',bin_width,'FaceColor',color_100)
xline(bd_thresh,'--','Color','k','LineWidth',LW)
ylim([0 50])
box off

% 110%
ax7 = subplot(426)
histogram(run2(2).Titration_pksThresh_ch1(:,7),'BinWidth',bin_width,'FaceColor',color_110) 
xline(bd_thresh,'--','Color','k','LineWidth',LW)
ylim([0 60])
box off

linkaxes([ax1 ax2 ax3 ax4 ax5 ax6 ax7],'x')
xlim([0 5])


ax8 = subplot(428)

mean_OFF = mean(OFF_pksThresh_ch1(:,7));
std_OFF = std(OFF_pksThresh_ch1(:,7));
mean_25 = mean(run2(3).Titration_pksThresh_ch1(:,7));
std_25 = std(run2(3).Titration_pksThresh_ch1(:,7));
mean_50 = mean(run2(1).Titration_pksThresh_ch1(:,7));
std_50 = std(run2(1).Titration_pksThresh_ch1(:,7));
mean_75 = mean(run(1).Titration_pksThresh_ch1(:,7));
std_75 = std(run(1).Titration_pksThresh_ch1(:,7));
mean_85 = mean(run(2).Titration_pksThresh_ch1(:,7));
std_85 = std(run(2).Titration_pksThresh_ch1(:,7));
mean_100 = mean(run(3).Titration_pksThresh_ch1(:,7));
std_100 = std(run(3).Titration_pksThresh_ch1(:,7));
mean_110 = mean(run2(2).Titration_pksThresh_ch1(:,7));
std_110 = std(run2(2).Titration_pksThresh_ch1(:,7));

errorbar([1 2 3 4 5 6 7],[mean_OFF mean_25 mean_50 mean_75 mean_85 mean_100 mean_110],[std_OFF std_25 std_50 std_75 std_85 std_100 std_110],'Color','k') % ,'LineWidth',1.5
ylim([-1 7])

box off
xticks([1 2 3 4 5 6 7])
xticklabels({'0','25','50','75','85','100','110'})


