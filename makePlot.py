import ROOT
from measurement import measurement
from graphs import *

ROOT.gROOT.SetBatch(ROOT.kTRUE)


measurements = []

m_8TeV = measurement("8 TeV (19.7 fb^{-1})")
m_8TeV.setResult(170.8, 9.0)
m_8TeV.setUncertainties(stat=6.0, exp=2.8, mod=4.6, theo=4.0)
m_8TeV.setReference("Eur. Phys. J. C 77 (2017) 467")

m_13TeV_2016 = measurement("13 TeV (35.9 fb^{-1})")
m_13TeV_2016.setResult(172.6, 2.5)
m_13TeV_2016.setUncertainties(stat=0.4, exp=1.6, mod=1.5, theo=1.0)
m_13TeV_2016.setReference("Phys. Rev. Lett. 124 (2020) 202001")

m_13TeV_RunII = measurement("13 TeV (138 fb^{-1})")
m_13TeV_RunII.setResult(173.06, 0.84)
m_13TeV_RunII.setUncertainties(stat=0.24, exp=0.61, mod=0.47, theo=0.23)
m_13TeV_RunII.setReference("Accepted by EPJC")

measurements.append(m_13TeV_RunII)
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

setResultStyle(g_results_tot, 15)
setResultStyle(g_results_stat, ROOT.kBlack)

################################################################################
## Contruct ucnert graphs

g_uncerts_stat = ROOT.TGraphErrors(len(measurements))
g_uncerts_exp = ROOT.TGraphErrors(len(measurements))
g_uncerts_model = ROOT.TGraphErrors(len(measurements))
g_uncerts_theory = ROOT.TGraphErrors(len(measurements))

for i, m in enumerate(measurements):
    ywidth = 0.3
    sep = 0.05
    g_uncerts_stat.SetPoint(i, m.uncertStat()/2, i*2+sep/2+ywidth+sep+ywidth/2)
    g_uncerts_stat.SetPointError(i, m.uncertStat()/2, ywidth/2)

    g_uncerts_exp.SetPoint(i, m.uncertExp()/2, i*2+sep/2+ywidth/2)
    g_uncerts_exp.SetPointError(i, m.uncertExp()/2, ywidth/2)

    g_uncerts_model.SetPoint(i, m.uncertModel()/2, i*2-sep/2-ywidth/2)
    g_uncerts_model.SetPointError(i, m.uncertModel()/2, ywidth/2)

    g_uncerts_theory.SetPoint(i, m.uncertTheory()/2, i*2-sep/2-ywidth-sep-ywidth/2)
    g_uncerts_theory.SetPointError(i, m.uncertTheory()/2, ywidth/2)

setUncertStyle(g_uncerts_stat, 15)
setUncertStyle(g_uncerts_exp, ROOT.kAzure+7)
setUncertStyle(g_uncerts_model, ROOT.kRed+2)
setUncertStyle(g_uncerts_theory, ROOT.kOrange-3)

################################################################################
## Contruct ucnert graphs

c = ROOT.TCanvas("", "", 800, 600)
ROOT.gStyle.SetLegendBorderSize(0)
ROOT.gStyle.SetPadTickX(1)
ROOT.gStyle.SetPadTickY(1)
ROOT.gStyle.SetOptStat(0)
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
dummy_results = getDummyGraph(160, 182, -1, 7)
dummy_results.Draw("AP")
g_results_tot.Draw("P SAME")
g_results_stat.Draw("P SAME")

texts = []
lowest_y = 0.312
textsep = 0.182
refsep = 0.04

texts.append(addText(x=0.01, y=lowest_y+2*textsep,               text = m_8TeV.title(), font=43, size=18))
texts.append(addText(x=0.01, y=lowest_y+2*textsep-1.11*refsep,   text = "#it{m}_{t} = "+str(m_8TeV.mtop())+" #pm "+str(m_8TeV.uncertTotal())+" GeV", font=43, size=14))
texts.append(addText(x=0.01, y=lowest_y+2*textsep-2*refsep,      text = m_8TeV.reference(), font=43, size=14))
texts.append(addText(x=0.01, y=lowest_y+textsep,                 text = m_13TeV_2016.title(), font=43, size=18))
texts.append(addText(x=0.01, y=lowest_y+textsep-1.11*refsep,     text = "#it{m}_{t} = "+str(m_13TeV_2016.mtop())+" #pm "+str(m_13TeV_2016.uncertTotal())+" GeV", font=43, size=14))
texts.append(addText(x=0.01, y=lowest_y+textsep-2*refsep,        text = m_13TeV_2016.reference(), font=43, size=14))
texts.append(addText(x=0.01, y=lowest_y,                         text = m_13TeV_RunII.title(), font=43, size=18))
texts.append(addText(x=0.01, y=lowest_y-1.11*refsep,             text = "#it{m}_{t} = "+str(m_13TeV_RunII.mtop())+" #pm "+str(m_13TeV_RunII.uncertTotal())+" GeV", font=43, size=14))
texts.append(addText(x=0.01, y=lowest_y-2*refsep,                text = m_13TeV_RunII.reference(), font=43, size=14))
texts.append(getCMS())
texts.append(getPrelim())
for t in texts:
    t.Draw()

leg1 = ROOT.TLegend(.5, .8, .95, .93)
leg1.SetNColumns(1)
leg1.AddEntry(g_results_stat, "Stat. uncertainty","pl")
leg1.AddEntry(g_results_tot, "Total uncertainty","pl")
leg1.SetTextSize(0.04)
leg1.Draw()
ROOT.gPad.RedrawAxis()


pad2.cd()
dummy_uncerts = getDummyGraphUncert(0, 6.5, -1, 7)
dummy_uncerts.Draw("AP")
g_uncerts_stat.Draw("E2 SAME")
g_uncerts_exp.Draw("E2 SAME")
g_uncerts_model.Draw("E2 SAME")
g_uncerts_theory.Draw("E2 SAME")

leg2 = ROOT.TLegend(.02, .8, 1, .93)
leg2.SetNColumns(2)
leg2.AddEntry(g_uncerts_stat, "Statistical","f")
leg2.AddEntry(g_uncerts_exp, "Experimental","f")
leg2.AddEntry(g_uncerts_model, "Model","f")
leg2.AddEntry(g_uncerts_theory, "Theory","f")
leg2.SetTextSize(0.06)
leg2.Draw()

ROOT.gPad.RedrawAxis()

c.SaveAs("MjetResults.pdf")
