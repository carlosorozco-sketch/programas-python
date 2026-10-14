from tkinter import *
from tkinter import ttk

root = Tk()

countrycodes = ('ar', 'au', 'be', 'br', 'ca', 'cn', 'dk', 'fl', 'fr',
                'gr', 'in', 'it', 'jp', 'mx', 'nl', 'no', 'es', 'se', 'ch')
countrynames = ('Argentina', 'Australia', 'Belgium', 'Brazil',
                'Canada', 'China', 'Denmark', 'Finland', 'France', 'Greece',
                'India', 'Italy', 'Japan', 'Mexico', 'Netherlands', 'Norway',
                'Spain', 'Sweden', 'Switzerland')

cnames = StringVar(value=countrynames)

populations = {'ar': 41000000, 'au': 22179211, 'be': 10584534,
               'br': 185971537, 'ca': 33148682, 'cn': 1323128240, 'dk': 5457415,
               'fl': 5302000, 'fr': 64102140, 'gr': 11147000, 'in': 1181040000,
               'it': 59086382, 'jp': 127718000, 'mx': 106535000, 'nl': 16402414,
               'no': 4738085, 'es': 45116894, 'se': 9174802, 'ch': 7508800}

gifts = {'card': 'Greeting card', 'flowers': 'Flowers', 'chocolates': 'Chocolates'}

gift = StringVar()
sentmsg = StringVar()
statusmsg = StringVar()

def showPopulation(*args):
    idxs = lbox.curselection()
    if len(idxs) == 1:
        idx = int(idxs[0])
        code = countrycodes[idx]
        name = countrynames[idx]
        popn = populations[code]
        statusmsg.set(f"The population of {name} ({code}) is {popn:,}")
    sentmsg.set('')

def sendGift(*args):
    idxs = lbox.curselection()
    if len(idxs) == 1:
        idx = int(idxs[0])
        lbox.see(idx)
        name = countrynames[idx]
        sentmsg.set(f"Sent {gift.get()} to leader of {name}")

# --- Construcción de la interfaz ---
c = ttk.Frame(root, padding=(5, 5, 12, 0))
c.grid(column=0, row=0, sticky=(N, W, E, S))
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

# Lista de países
lbox = Listbox(c, listvariable=cnames, height=10)
lbox.grid(column=0, row=0, rowspan=6, sticky=(N, S, E, W))

# Barra de desplazamiento
scroll = ttk.Scrollbar(c, orient=VERTICAL, command=lbox.yview)
scroll.grid(column=1, row=0, rowspan=6, sticky=(N, S))
lbox.configure(yscrollcommand=scroll.set)

# Etiquetas y mensajes
ttk.Label(c, text="Select a country:").grid(column=2, row=0, sticky=W)
statuslbl = ttk.Label(c, textvariable=statusmsg)
statuslbl.grid(column=2, row=1, sticky=(N, W))
sentlbl = ttk.Label(c, textvariable=sentmsg)
sentlbl.grid(column=2, row=5, sticky=(N, W))

# Selección de regalo
ttk.Label(c, text="Send a gift:").grid(column=2, row=2, sticky=W, pady=(10, 0))
for i, (key, text) in enumerate(gifts.items()):
    ttk.Radiobutton(c, text=text, variable=gift, value=key, command=sendGift).grid(column=2, row=3+i, sticky=W)

# Configurar expansión
c.grid_columnconfigure(0, weight=1)
c.grid_rowconfigure(0, weight=1)

# Enlazar selección de la lista
lbox.bind('<<ListboxSelect>>', showPopulation)

# Inicializar
gift.set('card')
sentmsg.set('')
statusmsg.set('Select a country from the list')

root.mainloop()