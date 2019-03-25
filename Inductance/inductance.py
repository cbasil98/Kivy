from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import math

wire_table={.025:[50,.036,34026,.0005067], .030:[49,.041,23629,.0007297], .041:[48,.051,13291,.001297],
           .051:[47,.064,8507,.002027], .061:[46,.074,5907,.002919], .071:[45,.086,4340,.003973],
           .081:[44,.097,3323,.005189], .091:[43,.109,2626,.005189], .102:[42,.119,2127,.008107],
           .112:[41,.132,1758,.009810], .122:[40,.142,1477,.011675], .132:[39,.152,1258,.013701],
           .152:[38,.175,945.2,.018242], .173:[37,.198,735.9,.02343], .193:[36,.218,589.1,.02927],
           .213:[35,.241,482.2,.03575], .234:[34.264,402,.04289], .254:[33,.287,340.3,.05067],
           .274:[32,.307,291.7,.05910], .295:[31,.33,252.9,.06818], .315:[30,.351,221.3,.07791],
           .345:[29,.384,183.97,.09372], .376:[28,.417,155.34,.111], .417:[27,.462,126.51,.1363],
           .457:[26,.505,105.2,.1642], .508:[25,.561,85.07,.2027], .559:[24,.612,70.3,.2452],
           .610:[23,.665,59.07,.2919], .711:[22,.770,43.4,.3973], .813:[21,.874,33.23,.5189],
           .914:[20,.978,26.26,.6567], 1.106:[19,1.082,21.27,.8107], 1.219:[18,1.293,14.768,1.167],
           1.422:[17,1.01,10.85,1.589], 1.626:[16,1.709,8.307,2.075], 1.829:[15,1.92,6.654,2.627],
           2.032:[14,2.129,5.317,3.243], 2.337:[13,2.441,4.020,4.289], 2.642:[12,2.756,3.146,5.78],
           2.946:[11,3.068,2.529,6.818], 3.251:[10,3.383,2.077,8.302], 3.658:[9,3.8,1.64,10.51],
           4.064:[8,40219,1.329,12.97]}
#selection_table={AcAw:{coretype,Ac,Aw,energy}}
selection_table={33.7:['L202',12.3,27.7,.13], 1227.6:['L164',23,53.3,.46], 3329:['L109',41,81.3,1.25],
                19033:['12AX',90.3,210.9,7.1], 19716:['T17',161.3,122.2,7.4], 28392:['INT41',169,168,10.6],
                31070:['17A',161.3,122.2,7.4], 47533:['12A',252.8,188,17.8], 112052:['10A',252.8,443.2,42],
                183138:['T1',278.9,656.7,68.7], 69806:['T74',30.3,227.9,26.2], 99118:['T23',364.8,271.7,37.2],
                39862:['T2',364.8,1092.5,149.5], 120000:['t30',400,300,45], 182168:['T45',492.8,369.6,68.3], 
                312173:['T15',645.2,489.9,159], 423637:['T14', 645.2,636.7,173], 460992:['T33',784,588,287],
                765346:['T3',1011.2,786.8,596], 1585913:['T16',1451.6,1092.5,691], 1843312:['T5',1451.6,1269.8,1054],
                2809562:['T6',1451.6,1935.5,720], 1920000:['INT120',1600,1200,1873], 4994777:['T43',2550.6,1935.5,4824],
                12864258:['T8',2580.6,4984.9,3645], 9720000:['INT180',3600,2700,15482], 4126911:['8A',5806.4,7096.8,10884],
                28944581:['8B',5806.4,4984.9,21699], 57865181:['8C',5806.4,9963.7,44963], 119774000:['T100',10322.6,11612.9,555],
                1479626:['4AX',566.4,2612.2,428500]}

class induct(BoxLayout):
    def closest_key(self,data,val):
        lastkey=None
        lastdif=None
        for i in data.keys():
            dif=abs(i-val)
            if lastdif != None and lastdif > dif:
                lastkey=i
                lastdif=dif
            elif lastdif == None:
                lastdif=dif
                lastkey=i
            elif lastdif < dif:
                return lastkey
        return i

    def calc(self,ip,irms,l,j,kw,bm):
        ip=float(ip)
        irms=float(irms)
        l=float(l)
        j=float(j)
        kw=float(kw)
        bm=float(bm)
        ap=l*ip*irms/(kw*bm*j)*pow(10,12)

        ap = selection_table.get(ap, selection_table[min(selection_table.keys(), key=lambda k: abs(k - ap))])
        Ac = ap[1] * pow(10, -6)
        Aw = ap[2] * pow(10, -6)
        n = l * ip / (Ac * bm)
        if n % 1 != 0:
            n = int(n) + 1
        aw = (irms / j)*pow(10,6)
        aw=self.closest_key(wire_table,aw)

        wire_size = wire_table[aw][0]
        lg = 4 * math.pi * pow(10, -7) * ip / bm
        j = irms / aw
        kw = n * aw / Aw
        l = kw * j * bm * Ac * Aw / ip / irms
        x = "Core Model:" + ap[0] + "\nWire size:" + str(wire_size) + "SWG\nNumber of turns:" + str(n)+ "\nInductance:" +str(l)+"H"
        self.display.text = str(x)

class app(App):
    def build(self):
        return induct()

app().run()
