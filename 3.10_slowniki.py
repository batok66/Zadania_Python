# sposoby tworzenia slownikow dla liczb rzysmkich

#1
rzymskie1 = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}

#2
rzymskie2 = dict(I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, M = 1000)

#3
wartosc = [1, 5, 10, 50, 100, 500, 1000]
litera = ["I", "V", "X", "L", "C", "D", "M"]
rzysmkie3 = dict(zip(litera, wartosc))

#4
rzymskie4 = {}
rzymskie4['I'] = 1 ; rzymskie4['V'] = 5 ; rzymskie4['X'] = 10 ; rzymskie4['L'] = 50 ; rzymskie4['C'] = 100
rzymskie4['D'] = 500 ;rzymskie4['M'] = 1000



