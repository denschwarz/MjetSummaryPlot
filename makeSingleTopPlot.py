import ROOT
from measurement import measurement
from graphs import *

ROOT.gROOT.SetBatch(ROOT.kTRUE)


measurements = []

m_8TeV = measurement("8 TeV (19.7 fb^{-1})")
m_8TeV.setResult(172.95, 1.24)
m_8TeV.setUncertainties(stat=0.77, exp=0.83, mod=0.51, theo=None)
m_8TeV.setReference("Eur. Phys. J. C 77 (2017) 354")

m_13TeV_2016 = measurement("13 TeV (35.9 fb^{-1})")
m_13TeV_2016.setResult(172.13, 0.77)
m_13TeV_2016.setUncertainties(stat=0.32, exp=0.50, mod=0.50, theo=None)
m_13TeV_2016.setReference("JHEP 12 (2021) 161")


measurements.append(m_13TeV_2016)
measurements.append(m_8TeV)

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

setResultStyle(g_results_tot, color_tot)
setResultStyle(g_results_stat, color_stat, "stat")

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

c = ROOT.TCanvas("", "", 800, 500)
ROOT.gStyle.SetLegendBorderSize(0)
ROOT.gStyle.SetPadTickX(1)
ROOT.gStyle.SetPadTickY(1)
ROOT.gStyle.SetOptStat(0)
ROOT.gStyle.SetEndErrorSize(5)

xboundary = 0.65
seperation = 0.05
topmarg = 0.01
botmarg = 0.15
leftmarg = 0.35
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
xmin = 171.
xmax = 174.2
ymax = 4
dummy_results = getDummyGraph(xmin, xmax, -1, ymax)
dummy_results.SetMarkerSize(0.)
dummy_results.SetMarkerColor(ROOT.kWhite)
dummy_results.Draw("AP")
g_results_tot.Draw("P SAME")
g_results_stat.Draw("P SAME")

texts = []
lowest_y = 0.422
textsep = 0.275
refsep = 0.05

texts.append(addText(x=0.01, y=lowest_y+textsep,               text = m_8TeV.title(), font=43, size=18))
texts.append(addText(x=0.01, y=lowest_y+textsep-1.11*refsep,   text = "#it{m}_{t} = "+str(m_8TeV.mtop())+" #pm "+str(m_8TeV.uncertTotal())+" GeV", font=43, size=14))
texts.append(addText(x=0.01, y=lowest_y+textsep-2*refsep,      text = m_8TeV.reference(), font=43, size=14))
texts.append(addText(x=0.01, y=lowest_y,                 text = m_13TeV_2016.title(), font=43, size=18))
texts.append(addText(x=0.01, y=lowest_y-1.11*refsep,     text = "#it{m}_{t} = "+str(m_13TeV_2016.mtop())+" #pm "+str(m_13TeV_2016.uncertTotal())+" GeV", font=43, size=14))
texts.append(addText(x=0.01, y=lowest_y-2*refsep,        text = m_13TeV_2016.reference(), font=43, size=14))
texts.append(getCMS(1.5))
# texts.append(getPrelim())
for t in texts:
    t.Draw()

# leg1 = ROOT.TLegend(.5, .8, .95, .93)
# leg1.SetNColumns(1)
# leg1.AddEntry(g_results_stat, "Stat. uncertainty","pl")
# leg1.AddEntry(g_results_tot, "Total uncertainty","pl")
# leg1.SetTextSize(0.04)
# leg1.Draw()

################################################################################
# Create a Marker for the legend and label stat. and tot. uncertainty bars
leg_marker_x = 171.5
leg_marker_y = ymax-0.2
leg_marker_statUncert = 0.5
leg_marker_totUncert = 0.5

legend_marker_tot = ROOT.TGraphErrors(1)
legend_marker_stat = ROOT.TGraphErrors(1)
legend_marker_tot.SetPoint(0, leg_marker_x, leg_marker_y-0.5)
legend_marker_tot.SetPointError(0, leg_marker_totUncert, 0.0)
legend_marker_stat.SetPoint(0, leg_marker_x, leg_marker_y)
legend_marker_stat.SetPointError(0, leg_marker_statUncert, 0.0)
setResultStyle(legend_marker_tot, color_tot)
setResultStyle(legend_marker_stat, color_stat, option="stat")
legend_marker_tot.Draw("P SAME")
legend_marker_stat.Draw("P SAME")

y_legend_marker_text = 0.91
y_legend_marker_text2 = 0.847
allTexts = []
allTexts.append(addText(0.63, y_legend_marker_text, "Stat. uncertainty", font=43, size=18, color=1))
allTexts.append(addText(0.63, y_legend_marker_text2, "Total uncertainty", font=43, size=18, color=1))

for t in allTexts:
    t.Draw()

ROOT.gPad.RedrawAxis()

################################################################################

pad2.cd()
dummy_uncerts = getDummyGraphUncert(0, 1.0, -1, ymax)
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

c.SaveAs("SingleTopResults.pdf")
