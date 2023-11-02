import ROOT

def setResultStyle(g, col, option=None, delta=False):
    g.SetTitle("")
    g.SetMarkerStyle(8)
    g.SetMarkerSize(1.25)
    g.SetMarkerColor(1)
    g.SetLineColor(col)
    g.SetLineWidth(1)
    if option == "stat":
        g.SetLineWidth(3)
        g.SetMarkerColor(1)

    # X axis
    g.GetXaxis().SetTitle("#it{m}_{t} [GeV]")
    if delta:
        g.GetXaxis().SetTitle("#Delta#it{m}_{t} [GeV]")

    g.GetXaxis().SetTitleSize(0.02)
    g.GetXaxis().SetNdivisions(505)
    g.GetXaxis().SetTitleSize(25)
    g.GetXaxis().SetTitleFont(43)
    g.GetXaxis().SetTitleOffset(1.2)
    g.GetXaxis().SetLabelFont(43)
    g.GetXaxis().SetLabelSize(21)

    # Y axis
    g.GetYaxis().SetTitle("")
    g.GetYaxis().SetTitleSize(0.0)
    g.GetYaxis().SetLabelSize(0.0)
    g.GetYaxis().SetLabelSize(0.0)
    g.GetYaxis().SetTickLength(0.0)

def setUncertStyle(g, col, delta=False):
    setResultStyle(g, ROOT.kWhite)
    g.SetTitle("")
    g.SetFillColor(col)
    g.SetMarkerSize(0)
    g.GetXaxis().SetTitle("#it{m}_{t} uncertainty [GeV]")
    if delta:
        g.GetXaxis().SetTitle("#Delta#it{m}_{t} uncertainty [GeV]")


def addText(x, y, text, font=43, size=12, color=1):
    latex = ROOT.TLatex(3.5, 24, text)
    latex.SetNDC()
    latex.SetTextAlign(13)
    latex.SetTextFont(font)
    latex.SetTextSize(size)
    latex.SetTextColor(color)
    latex.SetX(x)
    latex.SetY(y)
    return latex

def getDummyGraph(xmin, xmax, ymin, ymax, delta = False):
    g = ROOT.TGraph(4)
    g.SetPoint(0, xmin, ymin)
    g.SetPoint(1, xmin, ymax)
    g.SetPoint(2, xmax, ymax)
    g.SetPoint(3, xmax, ymin)
    g.SetMarkerSize(0.0)
    if delta:
        setResultStyle(g, ROOT.kWhite, option=None, delta=True)
    else:
        setResultStyle(g, ROOT.kWhite)

    return g

def getDummyGraphUncert(xmin, xmax, ymin, ymax, delta = False):
    g = ROOT.TGraph(4)
    g.SetPoint(0, xmin, ymin)
    g.SetPoint(1, xmin, ymax)
    g.SetPoint(2, xmax, ymax)
    g.SetPoint(3, xmax, ymin)
    g.SetMarkerSize(0.0)
    if delta:
        setUncertStyle(g, ROOT.kWhite, delta=True)
    else:
        setUncertStyle(g, ROOT.kWhite)
    return g

def getCMS(factor=1.0):
    cmstext = ROOT.TLatex(3.5, 24, "CMS")
    cmstext.SetNDC()
    cmstext.SetTextAlign(13)
    cmstext.SetTextFont(62)
    cmstext.SetTextSize(0.08*factor)
    cmstext.SetX(0.01)
    cmstext.SetY(0.98)
    return cmstext

def getPrelim():
    prelim = ROOT.TLatex(3.5, 24, "Preliminary")
    prelim.SetNDC()
    prelim.SetTextAlign(13)
    prelim.SetTextFont(52)
    prelim.SetTextSize(0.06)
    prelim.SetX(0.01)
    prelim.SetY(0.91)
    return prelim
