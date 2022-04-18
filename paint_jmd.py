from tkinter import *
# importing the choosecolor package
from tkinter import colorchooser

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
        self.canevas=Canvas(self.cadre_paint,width=600,height=600,bg="white")
        self.canevas.bind("<Button-1>",self.debuter_selection)
        self.canevas.bind("<ButtonRelease>",self.terminer_selection)
        self.canevas.pack()
        self.cadre_paint.pack()

    def creer_cadre_outil(self):
        self.cadre_outil=Frame(self.root)
        #
        self.cadre_formes=Frame(self.cadre_outil)
        self.v = StringVar()
        formes = {"Rectangle": "Rectangle",
                  "Oval": "Oval"}
        for (text, value) in formes.items():
            Radiobutton(self.cadre_formes, text=text, variable=self.v,
                        value=value, indicator=0,
                        background="light blue").pack(side=LEFT)
        self.v.set("Rectangle")
        self.cadre_formes.pack(side=LEFT)
        #
        self.cadre_options=Frame(self.cadre_outil)
        self.btnCouleur=Button(self.cadre_options,text="Couleur",command=self.choisir_couleur)
        self.btnCouleur.pack(side=LEFT)
        self.monspin=Spinbox(self.cadre_options,width=6,from_=1,to=50)
        self.monspin.pack(side=LEFT)

        #
        self.cadre_commandes=Frame(self.cadre_outil)
        self.btnEffacer=Button(self.cadre_commandes,text="Effacer",command=self.effacer_tout)
        self.btnEffacer.pack(side=LEFT)
        self.btnDessiner=Button(self.cadre_commandes,text="Dessiner",command=self.dessiner_tout)
        self.btnDessiner.pack(side=LEFT)

        self.cadre_options.pack(side=LEFT)
        self.cadre_commandes.pack(side=RIGHT)
        self.cadre_outil.pack(expand=1,fill=X)

    def choisir_couleur(self):
        color_code = colorchooser.askcolor(title="Choisir couleur")
        print(color_code)
        self.btnCouleur.config(bg=color_code[1])

    def dessiner_tout(self):
        for i,forme in self.modele.formes.items():
            for j in forme:
                self.dessiner_forme(i,j)

    def dessiner_forme(self,cle,j):
            if cle=="Rectangle":
                self.canevas.create_rectangle(j.debut, j.fin,outline=j.couleur,width=j.largeur,activedash=((7,1,1,1)))
            elif cle=="Oval":
                self.canevas.create_oval(j.debut, j.fin,outline=j.couleur,width=j.largeur,activedash=((7,1,1,1)))

    def effacer_tout(self):
        self.canevas.delete(ALL)

    def debuter_selection(self, evt):
        self.debut_rectangle = [evt.x, evt.y]

    def terminer_selection(self,evt):
        self.fin_rectangle=[evt.x,evt.y]
        val=self.v.get()
        f=self.parent.creer_forme(forme=val,debut=self.debut_rectangle,fin=self.fin_rectangle,
                                couleur=self.btnCouleur.cget("bg"),largeur=self.monspin.get())
        self.dessiner_forme(val,f)

class Modele():
    def __init__(self,parent):
        self.parent=parent
        self.createur_formes={"Rectangle":self.creer_rectangle,
                     "Oval":self.creer_oval}
        self.formes={"Rectangle":[],
                     "Oval":[]}

    def creer_forme(self,forme,origine,fin,couleur,largeur):
        obj=self.createur_formes[forme](origine,fin,couleur,largeur)
        self.formes[forme].append(obj)
        return obj

    def creer_rectangle(self,origine,fin,couleur,largeur):
        obj=Rectangle(self,origine,fin,couleur,largeur)
        return obj

    def creer_oval(self,origine,fin,couleur,largeur):
        obj=Oval(self,origine,fin,couleur,largeur)
        return obj

class Forme():
    def __init__(self,parent,debut,fin,couleur,largeur):
        self.parent=parent
        self.debut=debut
        self.fin=fin
        self.couleur=couleur
        self.largeur=largeur

class Rectangle(Forme):
    def __init__(self,parent,debut,fin,couleur,largeur):
        Forme.__init__(self,parent,debut,fin,couleur,largeur)

class Oval(Forme):
    def __init__(self, parent, debut, fin,couleur,largeur):
        Forme.__init__(self, parent, debut, fin,couleur,largeur)

class Controleur():
    def __init__(self):
        self.modele=Modele(self)
        self.vue=Vue(self)
        self.vue.root.mainloop()

    def creer_forme(self,forme,debut,fin,couleur,largeur):
        f=self.modele.creer_forme(forme,debut,fin,couleur,largeur)
        return f

if __name__ == '__main__':
    c=Controleur()
    print("L'application se termine")