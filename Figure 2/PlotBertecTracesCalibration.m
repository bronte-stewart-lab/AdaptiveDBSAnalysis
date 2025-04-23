lw = 1;
fs = 8;

f1=figure

ax1=subplot(711)
load('OFF_Bertec.mat')

plot(timesip,sip_l_fz./bodyweight.*100)
hold on
plot(timesip,sip_r_fz./bodyweight.*100)
xlim([time_sip_samp(1,3)./1000 time_sip_samp(1,3)./1000+30])
xticks([time_sip_samp(1,3)./1000, time_sip_samp(1,3)./1000+5, time_sip_samp(1,3)./1000+10,time_sip_samp(1,3)./1000+15,time_sip_samp(1,3)./1000+20,time_sip_samp(1,3)./1000+25,time_sip_samp(1,3)./1000+30])
xticklabels({'0','5','10','15','20','25','30'})
box off
H=gca;
H.LineWidth=lw;
H.FontSize=fs;
H.FontName = 'Helvetica';


ax2=subplot(712)
load('TwentyFive_Bertec.mat')

plot(timesip,sip_l_fz./bodyweight.*100)
hold on
plot(timesip,sip_r_fz./bodyweight.*100)
xlim([time_sip_samp(1,3)./1000 time_sip_samp(1,3)./1000+30])
xticks([time_sip_samp(1,3)./1000, time_sip_samp(1,3)./1000+5, time_sip_samp(1,3)./1000+10,time_sip_samp(1,3)./1000+15,time_sip_samp(1,3)./1000+20,time_sip_samp(1,3)./1000+25,time_sip_samp(1,3)./1000+30])
xticklabels({'0','5','10','15','20','25','30'})

box off
H=gca;
H.LineWidth=lw;
H.FontSize=fs;
H.FontName = 'Helvetica';

ax3=subplot(713)
load('Fifty_Bertec.mat')

plot(timesip,sip_l_fz./bodyweight.*100)
hold on
plot(timesip,sip_r_fz./bodyweight.*100)

xline(time_sip_samp(1,3)./1000+allrealfreezes(1,1)./1000,'LineWidth',2)
xline(time_sip_samp(1,3)./1000+allrealfreezes(1,2)./1000,'LineWidth',2)

xlim([time_sip_samp(1,3)./1000 time_sip_samp(1,3)./1000+30])
xticks([time_sip_samp(1,3)./1000, time_sip_samp(1,3)./1000+5, time_sip_samp(1,3)./1000+10,time_sip_samp(1,3)./1000+15,time_sip_samp(1,3)./1000+20,time_sip_samp(1,3)./1000+25,time_sip_samp(1,3)./1000+30])
xticklabels({'0','5','10','15','20','25','30'})

box off
H=gca;
H.LineWidth=lw;
H.FontSize=fs;
H.FontName = 'Helvetica';




ax4=subplot(714)
load('SeventyFive_Bertec.mat')

plot(timesip,sip_l_fz./bodyweight.*100)
hold on
plot(timesip,sip_r_fz./bodyweight.*100)

xline(time_sip_samp(1,3)./1000+allrealfreezes(1,1)./1000,'LineWidth',2)
xline(time_sip_samp(1,3)./1000+allrealfreezes(1,2)./1000,'LineWidth',2)

xline(time_sip_samp(1,3)./1000+allrealfreezes(2,1)./1000,'LineWidth',2)
xline(time_sip_samp(1,3)./1000+allrealfreezes(2,2)./1000,'LineWidth',2)

xlim([time_sip_samp(1,3)./1000 time_sip_samp(1,3)./1000+30])
xticks([time_sip_samp(1,3)./1000, time_sip_samp(1,3)./1000+5, time_sip_samp(1,3)./1000+10,time_sip_samp(1,3)./1000+15,time_sip_samp(1,3)./1000+20,time_sip_samp(1,3)./1000+25,time_sip_samp(1,3)./1000+30])
xticklabels({'0','5','10','15','20','25','30'})

box off
H=gca;
H.LineWidth=lw;
H.FontSize=fs;
H.FontName = 'Helvetica';

ax5=subplot(715)
load('EightyFive_Bertec.mat')

plot(timesip,sip_l_fz./bodyweight.*100)
hold on
plot(timesip,sip_r_fz./bodyweight.*100)

xline(time_sip_samp(1,3)./1000+allrealfreezes(1,1)./1000,'LineWidth',2)
xline(time_sip_samp(1,3)./1000+allrealfreezes(1,2)./1000,'LineWidth',2)

xline(time_sip_samp(1,3)./1000+allrealfreezes(2,1)./1000,'LineWidth',2)
xline(time_sip_samp(1,3)./1000+allrealfreezes(2,2)./1000,'LineWidth',2)

xlim([time_sip_samp(1,3)./1000 time_sip_samp(1,3)./1000+30])
xticks([time_sip_samp(1,3)./1000, time_sip_samp(1,3)./1000+5, time_sip_samp(1,3)./1000+10,time_sip_samp(1,3)./1000+15,time_sip_samp(1,3)./1000+20,time_sip_samp(1,3)./1000+25,time_sip_samp(1,3)./1000+30])
xticklabels({'0','5','10','15','20','25','30'})

box off
H=gca;
H.LineWidth=lw;
H.FontSize=fs;
H.FontName = 'Helvetica';

ax6=subplot(716)
load('Hundred_Bertec.mat')

plot(timesip,sip_l_fz./bodyweight.*100)
hold on
plot(timesip,sip_r_fz./bodyweight.*100)

xline(time_sip_samp(1,3)./1000+allrealfreezes(1,1)./1000,'LineWidth',2)
xline(time_sip_samp(1,3)./1000+allrealfreezes(1,2)./1000,'LineWidth',2)

xlim([time_sip_samp(1,3)./1000 time_sip_samp(1,3)./1000+30])
xticks([time_sip_samp(1,3)./1000, time_sip_samp(1,3)./1000+5, time_sip_samp(1,3)./1000+10,time_sip_samp(1,3)./1000+15,time_sip_samp(1,3)./1000+20,time_sip_samp(1,3)./1000+25,time_sip_samp(1,3)./1000+30])
xticklabels({'0','5','10','15','20','25','30'})

box off
H=gca;
H.LineWidth=lw;
H.FontSize=fs;
H.FontName = 'Helvetica';

ax7=subplot(717)
load('HundredTen_Bertec.mat')

plot(timesip,sip_l_fz./bodyweight.*100)
hold on
plot(timesip,sip_r_fz./bodyweight.*100)
xlim([time_sip_samp(1,3)./1000 time_sip_samp(1,3)./1000+30])
xticks([time_sip_samp(1,3)./1000, time_sip_samp(1,3)./1000+5, time_sip_samp(1,3)./1000+10,time_sip_samp(1,3)./1000+15,time_sip_samp(1,3)./1000+20,time_sip_samp(1,3)./1000+25,time_sip_samp(1,3)./1000+30])
xticklabels({'0','5','10','15','20','25','30'})

box off
H=gca;
H.LineWidth=lw;
H.FontSize=fs;
H.FontName = 'Helvetica';


%% Plot therapeutic window

freezes = [100 100 73.5 11 5.7 2.6 0];
perc = [0 25 50 75 85 100 110];

f1=figure

scatter(perc,freezes,35,'k','filled')
hold on
plot(perc,freezes,'LineWidth',1.5,'Color','k')

xlim([-5 115])
xticks([0 25 50 75 85 100 110])

xlabel('% of Clinical Stim Amp')
ylabel('% Time Freezing')
box off
H=gca;
H.LineWidth=1.5;
H.FontSize=12;
H.FontName = 'Helvetica';