import ROOT
import math
from measurement import measurement
from graphs import *


ROOT.gROOT.SetBatch(ROOT.kTRUE)


measurements = []

m_7TeV = measurement("7 TeV (5.0 fb^{-1}) ideogram")
m_7TeV.setResult(173.49, 1.07)
m_7TeV.setUncertainties(stat=0.43,
                        exp=math.sqrt(0.06**2+0.61**2+0.28**2+0.02**2+0.06**2
                                      +0.23**2+0.12**2+0.07**2+0.13**2),
                        mod=math.sqrt(0.07**2+0.24**2+0.18**2+0.15**2+0.54**2),
                        theo=0)
m_7TeV.setReference("JHEP 12 (2012) 105")

m_8TeV = measurement("8 TeV (19.7 fb^{-1}) ideogram")
m_8TeV.setResult(172.35, 0.51)
m_8TeV.setUncertainties(stat=0.16,
                        exp=math.sqrt(0.04**2+0.01**2+0.12**2+0.10**2+0.04**2
                                      +0.01**2+0.04**2+0.03**2+0.06**2+0.04**2+0.03**2),
                        mod=math.sqrt(0.34**2+0.16**2+0.04**2+0.09**2+0.07**2+0.12**2+
                                      0.02**2+0.11**2+0.09**2+0.01**2),
                        theo=math.sqrt(0.07**2+0.07**2+0.08**2+0.11**2+0.09**2))
m_8TeV.setReference("Phys. Rev. D 93 (2016) 072004")

m_13TeV_2016 = measurement("13 TeV (35.9 fb^{-1}) ideogram")
m_13TeV_2016.setResult(172.25, 0.63)
m_13TeV_2016.setUncertainties(stat=0.08,
                              exp=math.sqrt(0.05**2+0.18**2+0.04**2+0.03**2+0.05**2+0.02**2),
                              mod=math.sqrt(0.39**2+0.12**2+0.02**2+0.01**2+0.05**2+
                                            0.22**2+0.07**2+0.13**2+0.01**2+0.07**2+
                                            0.07**2+0.31**2),
                              theo=math.sqrt(0.11**2+0.07**2+0.05**2+0.07**2+0.07**2+0.08**2))
m_13TeV_2016.setReference("Eur. Phys. J. C 78 (2018) 891")

m_13TeV_prof2d = measurement("13 TeV (36.3 fb^{-1}) 2D")
m_13TeV_prof2d.setResult(172.00, 0.52)
m_13TeV_prof2d.setUncertainties(stat=0.05, exp=0.34, mod=0.51, theo=0)
m_13TeV_prof2d.setReference("Eur. Phys. J. C 83 (2023) 963")


m_13TeV_prof = measurement("13 TeV (36.3 fb^{-1}) profiled")
m_13TeV_prof.setResult(171.77, 0.37)
m_13TeV_prof.setUncertainties(stat=0.04, exp=0.22, mod=0.36, theo=0)
m_13TeV_prof.setReference("Eur. Phys. J. C 83 (2023) 963")

measurements.append(m_13TeV_prof)
#measurements.append(m_13TeV_prof2d)
measurements.append(m_13TeV_2016)
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
ymax = 1+2*len(measurements)
dummy_results = getDummyGraph(171, 174.5, -1, ymax)
dummy_results.SetMarkerSize(0.)
dummy_results.SetMarkerColor(ROOT.kWhite)
dummy_results.Draw("AP")
g_results_tot.Draw("P SAME")
g_results_stat.Draw("P SAME")

texts = []
lowest_y = 0.312
textsep = (1-lowest_y)/(len(measurements) + 0.9)
refsep = 0.04

for i, m in enumerate(measurements):
    texts.append(addText(x=0.01, y=lowest_y+i*textsep,               text = m.title(), font=43, size=18))
    texts.append(addText(x=0.01, y=lowest_y+i*textsep-1.11*refsep,   text = "#it{m}_{t} = "+str(m.mtop())+" #pm "+str(m.uncertTotal())+" GeV", font=43, size=14))
    texts.append(addText(x=0.01, y=lowest_y+i*textsep-2*refsep,      text = m.reference(), font=43, size=14))

texts.append(getCMS(1.5))
# texts.append(getPrelim())
for t in texts:
    t.Draw()



################################################################################
# Create a Marker for the legend and label stat. and tot. uncertainty bars
leg_marker_x = 171.5
leg_marker_y = ymax-0.3
leg_marker_statUncert = 0.5
leg_marker_totUncert = 0.5


legend_marker_tot = ROOT.TGraphErrors(1)
legend_marker_stat = ROOT.TGraphErrors(1)
legend_marker_tot.SetPoint(0, leg_marker_x, leg_marker_y-0.9)
legend_marker_tot.SetPointError(0, leg_marker_totUncert, 0.0)
legend_marker_stat.SetPoint(0, leg_marker_x, leg_marker_y)
legend_marker_stat.SetPointError(0, leg_marker_statUncert, 0.0)
setResultStyle(legend_marker_tot, color_tot)
setResultStyle(legend_marker_stat, color_stat, option="stat")
legend_marker_tot.Draw("P SAME")
legend_marker_stat.Draw("P SAME")

y_legend_marker_text = 0.91
y_legend_marker_text2 = 0.843
allTexts = []
allTexts.append(addText(0.665, y_legend_marker_text, "Stat. uncertainty", font=43, size=18, color=1))
allTexts.append(addText(0.665, y_legend_marker_text2, "Total uncertainty", font=43, size=18, color=1))

for t in allTexts:
    t.Draw()

ROOT.gPad.RedrawAxis()

################################################################################

pad2.cd()
dummy_uncerts = getDummyGraphUncert(0, 0.75, -1, ymax)
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

c.SaveAs("DirectResults.pdf")
