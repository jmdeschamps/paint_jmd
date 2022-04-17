from tkinter import *

class Vue():
    def __init__(self,parent):
        self.parent=parent
        self.modele=self.parent.modele
        self.root=Tk()
        self.cadres={"cadre_paint":None,
                     "cadre_palette":None}
        self.creer_cadres()

    def creer_cadres(self):
        self.creer_cadre_paint()
        self.creer_cadre_outil()

    def creer_cadre_paint(self):
        self.cadre_paint=Frame(self.root)
        self.canevas=Canvas(self.cadre_paint,width=600,height=600)
        self.canevas.bind("<Button-1>",self.debuter_selection)
        self.canevas.bind("<ButtonRelease>",self.terminer_selection)
        self.canevas.pack()
        self.cadre_paint.pack()

    def creer_cadre_outil(self):
        self.cadre_outil=Frame(self.root)
        self.btnEffacer=Button(self.root,text="Effacer",command=self.effacer_tout)
        self.btnEffacer.pack(side=LEFT)
        self.btnDessiner=Button(self.root,text="Effacer",command=self.dessiner_tout)
        self.btnDessiner.pack(side=LEFT)
        self.cadre_outil.pack()
    def dessiner_tout(self):
        for i in self.modele.formes.keys():
            if i=="Rectangle":
                for j in self.modele.formes["Rectangle"]:
                    self.canevas.create_rectangle(j.debut, j.fin)

    def effacer_tout(self):
        self.canevas.delete(ALL)

    def debuter_selection(self, evt):
        self.debut_rectangle = [evt.x, evt.y]

    def terminer_selection(self,evt):
        self.fin_rectangle=[evt.x,evt.y]
        self.canevas.create_rectangle(self.debut_rectangle,self.fin_rectangle)
        self.parent.creer_forme(forme="Rectangle",debut=self.debut_rectangle,fin=self.fin_rectangle )


class Modele():
    def __init__(self,parent):
        self.parent=parent
        self.createur_formes={"Rectangle":self.creer_rectangle,
                     "Oval":self.creer_oval}
        self.formes={"Rectangle":[],
                     "Oval":[]}

    def creer_forme(self,forme,origine,fin):
        obj=self.createur_formes[forme](origine,fin)
        self.formes[forme].append(obj)

    def creer_rectangle(self,origine,fin):
        obj=Rectangle(self,origine,fin)
        return obj

    def creer_oval(self,origine,fin):
        pass

class Forme():
    def __init__(self,parent,debut,fin):
        self.parent=parent
        self.debut=debut
        self.fin=fin



class Rectangle(Forme):
    def __init__(self,parent,debut,fin):
        Forme.__init__(self,parent,debut,fin)

class Controleur():
    def __init__(self):
        self.modele=Modele(self)
        self.vue=Vue(self)
        self.vue.root.mainloop()

    def creer_forme(self,forme,debut,fin):
        self.modele.creer_forme(forme,debut,fin)

if __name__ == '__main__':
    c=Controleur()
    print("L'application se termine")