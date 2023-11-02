import ROOT
from measurement import measurement
from graphs import *

ROOT.gROOT.SetBatch(ROOT.kTRUE)


measurements = []
m_7TeV = measurement("7 TeV (5 fb^{-1})")
m_7TeV.setResult(-0.44, 0.53)
m_7TeV.setUncertainties(stat=0.46, exp=0.17, mod=0.16, theo=None)
m_7TeV.setReference("JHEP 06 (2012) 109")

m_8TeV = measurement("8 TeV (19.7 fb^{-1})")
m_8TeV.setResult(-0.15, 0.21)
m_8TeV.setUncertainties(stat=0.19, exp=0.11, mod=0.11, theo=None)
m_8TeV.setReference("Phys. Lett. B 770 (2017) 50")

m_13TeV = measurement("13 TeV (35.9 fb^{-1})")
m_13TeV.setResult(0.83, 1.79)
m_13TeV.setUncertainties(stat=0.69, exp=1.31, mod=1.09, theo=None)
m_13TeV.setReference("JHEP 12 (2021) 161")

measurements.append(m_13TeV)
measurements.append(m_8TeV)
measurements.append(m_7TeV)

################################################################################
## Contruct results graphs
g_results_tot = ROOT.TGraphErrors(len(measurements))
g_results_stat = ROOT.TGraphErrors(len(measurements))

for i, m in enumerate(measurements):
    g_results_tot.SetPoint(i, m.mtop(), i*2)
    g_results_tot.SetPointError(i, m.uncertTotal(), 0.0)
    g_results_stat.SetPoint(i, m.mtop(), i*2)
    g_results_stat.SetPointError(i, m.uncertStat(), 0.0)

color_tot = 15
color_stat = ROOT.TColor.GetColor("#2b2b2b")

setResultStyle(g_results_tot, color_tot, option=None, delta=True)
setResultStyle(g_results_stat, color_stat, option="stat", delta=True )

col_prediction = ROOT.kMagenta+3
style_prediction = 6
width_prediction = 2

################################################################################
## Contruct ucnert graphs

g_uncerts_stat = ROOT.TGraphErrors(len(measurements))
g_uncerts_exp = ROOT.TGraphErrors(len(measurements))
g_uncerts_model = ROOT.TGraphErrors(len(measurements))

for i, m in enumerate(measurements):
    ywidth = 0.3
    sep = 0.05
    g_uncerts_stat.SetPoint(i, m.uncertStat()/2, i*2+sep+ywidth)
    g_uncerts_stat.SetPointError(i, m.uncertStat()/2, ywidth/2)

    g_uncerts_exp.SetPoint(i, m.uncertExp()/2, i*2)
    g_uncerts_exp.SetPointError(i, m.uncertExp()/2, ywidth/2)

    g_uncerts_model.SetPoint(i, m.uncertModel()/2, i*2-sep-ywidth)
    g_uncerts_model.SetPointError(i, m.uncertModel()/2, ywidth/2)


setUncertStyle(g_uncerts_stat, 16)
setUncertStyle(g_uncerts_exp, ROOT.kAzure+7)
setUncertStyle(g_uncerts_model, ROOT.kRed+2)

################################################################################
## Contruct ucnert graphs

c = ROOT.TCanvas("", "", 800, 600)
ROOT.gStyle.SetLegendBorderSize(0)
ROOT.gStyle.SetPadTickX(1)
ROOT.gStyle.SetPadTickY(1)
ROOT.gStyle.SetOptStat(0)
ROOT.gStyle.SetEndErrorSize(5)

xboundary = 0.65
seperation = 0.05
topmarg = 0.01
botmarg = 0.12
leftmarg = 0.43
rightmarg = 0.03
pad1 = ROOT.TPad("pad1", "pad1", 0.0, 0.0, xboundary, 1.0)
pad1.SetTopMargin(topmarg)
pad1.SetLeftMargin(leftmarg)
pad1.SetRightMargin(seperation/2)
pad1.SetBottomMargin(botmarg)
pad1.Draw()
pad2 = ROOT.TPad("pad2", "pad2", xboundary, 0.0, 1.0, 1.0)
pad2.SetTopMargin(topmarg)
pad2.SetLeftMargin(seperation/2)
pad2.SetRightMargin(rightmarg)
pad2.SetBottomMargin(botmarg)
pad2.Draw()

pad1.cd()
# dummy_results = getDummyGraph(160, 182, -1, 7)
dummy_results = getDummyGraph(-2.5, 2.75, -1, 7, delta=True)
dummy_results.SetMarkerSize(0.)
dummy_results.SetMarkerColor(ROOT.kWhite)
dummy_results.Draw("AP")
prediction = ROOT.TLine(0., -1., 0., 4.6)
prediction.SetLineColor(col_prediction)
prediction.SetLineStyle(style_prediction)
prediction.SetLineWidth(width_prediction)
prediction.Draw("SAME")
g_results_tot.Draw("P SAME")
g_results_stat.Draw("P SAME")

texts = []
lowest_y = 0.325
textsep = 0.182
refsep = 0.04

texts.append(addText(x=0.01, y=lowest_y+2*textsep,               text = m_7TeV.title(), font=43, size=18))
texts.append(addText(x=0.01, y=lowest_y+2*textsep-1.11*refsep,   text = "#it{m}_{t} = "+str(m_7TeV.mtop())+" #pm "+str(m_7TeV.uncertTotal())+" GeV", font=43, size=14))
texts.append(addText(x=0.01, y=lowest_y+2*textsep-2*refsep,      text = m_7TeV.reference(), font=43, size=14))
texts.append(addText(x=0.01, y=lowest_y+textsep,                 text = m_8TeV.title(), font=43, size=18))
texts.append(addText(x=0.01, y=lowest_y+textsep-1.11*refsep,     text = "#it{m}_{t} = "+str(m_8TeV.mtop())+" #pm "+str(m_8TeV.uncertTotal())+" GeV", font=43, size=14))
texts.append(addText(x=0.01, y=lowest_y+textsep-2*refsep,        text = m_8TeV.reference(), font=43, size=14))
texts.append(addText(x=0.01, y=lowest_y,                         text = m_13TeV.title(), font=43, size=18))
texts.append(addText(x=0.01, y=lowest_y-1.11*refsep,             text = "#it{m}_{t} = "+str(m_13TeV.mtop())+" #pm "+str(m_13TeV.uncertTotal())+" GeV", font=43, size=14))
texts.append(addText(x=0.01, y=lowest_y-2*refsep,                text = m_13TeV.reference(), font=43, size=14))
texts.append(getCMS(1.5))
# texts.append(getPrelim())
for t in texts:
    t.Draw()



################################################################################
# Create a Marker for the legend and label stat. and tot. uncertainty bars
leg_marker_x = -2.
leg_marker_y = 7
leg_marker_statUncert = 0.8
leg_marker_totUncert = 0.8
leg_sep = 0.7


legend_marker_tot = ROOT.TGraphErrors(1)
legend_marker_stat = ROOT.TGraphErrors(1)
legend_marker_tot.SetPoint(0, leg_marker_x, leg_marker_y-leg_sep)
legend_marker_tot.SetPointError(0, leg_marker_totUncert, 0.0)
legend_marker_stat.SetPoint(0, leg_marker_x, leg_marker_y)
legend_marker_stat.SetPointError(0, leg_marker_statUncert, 0.0)
legend_line = ROOT.TLine(leg_marker_x-leg_marker_totUncert, leg_marker_y-(2*leg_sep), leg_marker_x+leg_marker_totUncert, leg_marker_y-(2*leg_sep))
legend_line.SetLineColor(col_prediction)
legend_line.SetLineStyle(style_prediction)
legend_line.SetLineWidth(width_prediction)

legend_line.Draw("SAME")
setResultStyle(legend_marker_tot, color_tot)
setResultStyle(legend_marker_stat, color_stat, option="stat")
legend_marker_tot.Draw("P SAME")
legend_marker_stat.Draw("P SAME")

y_legend_marker_text = 0.93
y_legend_marker_text2 = 0.867
y_legend_marker_text3 = 0.804

allTexts = []
allTexts.append(addText(0.665, y_legend_marker_text, "Stat. uncertainty", font=43, size=18, color=1))
allTexts.append(addText(0.665, y_legend_marker_text2, "Total uncertainty", font=43, size=18, color=1))
allTexts.append(addText(0.665, y_legend_marker_text3, "SM prediction", font=43, size=18, color=1))

for t in allTexts:
    t.Draw()

ROOT.gPad.RedrawAxis()

################################################################################

pad2.cd()
dummy_uncerts = getDummyGraphUncert(0, 2, -1, 7, delta=True)
dummy_uncerts.Draw("AP")
g_uncerts_stat.Draw("E2 SAME")
g_uncerts_exp.Draw("E2 SAME")
g_uncerts_model.Draw("E2 SAME")

leg2 = ROOT.TLegend(.02, .8, 1, .93)
leg2.SetNColumns(2)
leg2.AddEntry(g_uncerts_stat, "Statistical","f")
leg2.AddEntry(g_uncerts_exp, "Experimental","f")
leg2.AddEntry(g_uncerts_model, "Model","f")
leg2.SetTextSize(0.06)
leg2.Draw()

ROOT.gPad.RedrawAxis()

c.SaveAs("SingleTopDeltaMtopResults.pdf")
