# получение данных api
from espn_api.basketball import League  # инпортируем класс лиги
league = League(league_id=1013716421, year=2024)    # выполняем вход в конкретную лигу

# интерфейс
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("ЛББП")
root.state("zoomed")

# создание стиля отображения
# style = ttk.Style()
# style.configure("BW.TLabel", foreground="black", background="white")

mainframe = ttk.Frame(root, padding="11 22")    # создаем сетку
mainframe.grid(column=0, row=0, sticky=(S+S+S+S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
# mainframe.configure(style="BW.TLabel")  #применение стиля

in_game_checkbox = StringVar()
ttk.Checkbutton(mainframe, command=0, variable=in_game_checkbox, onvalue='in', offvalue='out').grid(column=0, row=3,
                                                                                                    sticky=S)
ttk.Checkbutton(mainframe, command=0, variable=in_game_checkbox, onvalue='in', offvalue='out').grid(column=0, row=4,
                                                                                                    sticky=S)
ttk.Checkbutton(mainframe, command=0, variable=in_game_checkbox, onvalue='in', offvalue='out').grid(column=0, row=5,
                                                                                                    sticky=S)
ttk.Checkbutton(mainframe, command=0, variable=in_game_checkbox, onvalue='in', offvalue='out').grid(column=0, row=6,
                                                                                                    sticky=S)
ttk.Checkbutton(mainframe, command=0, variable=in_game_checkbox, onvalue='in', offvalue='out').grid(column=0, row=7,
                                                                                                    sticky=S)
ttk.Checkbutton(mainframe, command=0, variable=in_game_checkbox, onvalue='in', offvalue='out').grid(column=0, row=8,
                                                                                                    sticky=S)
ttk.Checkbutton(mainframe, command=0, variable=in_game_checkbox, onvalue='in', offvalue='out').grid(column=0, row=9,
                                                                                                    sticky=S)
ttk.Checkbutton(mainframe, command=0, variable=in_game_checkbox, onvalue='in', offvalue='out').grid(column=0, row=10,
                                                                                                    sticky=S)
ttk.Checkbutton(mainframe, command=0, variable=in_game_checkbox, onvalue='in', offvalue='out').grid(column=0, row=11,
                                                                                                    sticky=S)
ttk.Checkbutton(mainframe, command=0, variable=in_game_checkbox, onvalue='in', offvalue='out').grid(column=0, row=12,
                                                                                                    sticky=S)
ttk.Checkbutton(mainframe, command=0, variable=in_game_checkbox, onvalue='in', offvalue='out').grid(column=0, row=13,
                                                                                                    sticky=S)
ttk.Checkbutton(mainframe, command=0, variable=in_game_checkbox, onvalue='in', offvalue='out').grid(column=0, row=14,
                                                                                                    sticky=S)
ttk.Checkbutton(mainframe, command=0, variable=in_game_checkbox, onvalue='in', offvalue='out').grid(column=0, row=15,
                                                                                                    sticky=S)
ttk.Checkbutton(mainframe, command=0, variable=in_game_checkbox, onvalue='in', offvalue='out').grid(column=0, row=16,
                                                                                                    sticky=S)
ttk.Checkbutton(mainframe, command=0, variable=in_game_checkbox, onvalue='in', offvalue='out').grid(column=0, row=17,
                                                                                                    sticky=S)
ttk.Checkbutton(mainframe, command=0, variable=in_game_checkbox, onvalue='in', offvalue='out').grid(column=0, row=18,
                                                                                                    sticky=S)
ttk.Checkbutton(mainframe, command=0, variable=in_game_checkbox, onvalue='in', offvalue='out').grid(column=0, row=19,
                                                                                                    sticky=S)
ttk.Checkbutton(mainframe, command=0, variable=in_game_checkbox, onvalue='in', offvalue='out').grid(column=0, row=20,
                                                                                                    sticky=S)

ttk.Label(mainframe, text="Выберите команду:").grid(column=1, row=0, sticky=W)  # первый столбец
ttk.Label(mainframe, text="Состав").grid(column=1, row=2, sticky=W)

team_number = 0
team_name_list = list
team = list
def writeroster():
    global team_name_list
    team_name_list = league.teams[team_number]
    players_names_list = team_name_list.roster
    players_names_str = (",".join(map(str, players_names_list)))
    players_names_str = players_names_str.replace("Player(", "")
    players_names_str = players_names_str.replace(")", "")
    players_names_list = list(players_names_str.split(","))
    global team
    team = league.teams[team_number]
    name_number = 0
    while name_number < 18:
        # очищаем имя игрока в 1 столбеце
        ttk.Label(mainframe, text="").grid(column=1, row=name_number + 3, sticky=W + E + N + S)
        # очищем AVR игрока в 3 столбце
        ttk.Label(mainframe, text="").grid(column=3, row=name_number + 3, sticky=W + E + N + S)
        # очищаем инжури статус в 2 столбце
        ttk.Label(mainframe, text="").grid(column=2, row=name_number + 3, sticky=W + E + N + S)
        # очищаем боксы и Week Avr
        resetChbxsAndRdbtns()
        name_number += 1
    name_number = 0
    while name_number < 18:
        # пишем имя игрока в 1 столбец
        ttk.Label(mainframe, text=players_names_list[name_number]).grid(column=1, row=name_number + 3,
                                                                        sticky=W + E + N + S)
        # пишем инжури статус в 2 столбец
        ttk.Label(mainframe, text=team.roster[name_number].injuryStatus.lower()).grid(column=2, row=name_number + 3,
                                                                                      sticky=N + S)
        # пишем AVR игрока в 3 столбец
        ttk.Label(mainframe, text=team.roster[name_number].avg_points).grid(column=3, row=name_number + 3,
                                                                            sticky=W + E + N + S)
        name_number += 1

def team_name_box_function(*arg):
    global team_number
    team_number = team_name_box.current()
    writeroster()

team_name_list = league.teams   # второй столбец
team_name_str = (" ".join(map(str, team_name_list)))
team_name_str = team_name_str.replace("Team(", "")
team_name_str = team_name_str.replace(")", ".")
team_name_list = list(team_name_str.split(". "))
team_name_box = ttk.Combobox(mainframe, values=team_name_list)
team_name_box.grid(column=2, row=0, sticky=(S+S))
team_name_box.bind('<<ComboboxSelected>>', team_name_box_function)  # обработчик событий выпадающего листа
ttk.Label(mainframe, text="статус").grid(column=2, row=2, sticky=S)

ttk.Label(mainframe, text="AVR").grid(column=3, row=2, sticky=S)
ttk.Label(mainframe, text="Количество игр:").grid(column=4, row=2, sticky=S)
ttk.Label(mainframe, text="2").grid(column=5, row=2, sticky=S)
ttk.Label(mainframe, text="3").grid(column=6, row=2, sticky=S)
ttk.Label(mainframe, text="4").grid(column=7, row=2, sticky=S)
ttk.Label(mainframe, text="5").grid(column=8, row=2, sticky=S)


def pl1wkAvr():
    ttk.Label(mainframe, text=round(team.roster[0].avg_points * pl1gmNumber.get(), 2)).grid(column=9, row=3,
                                                                                            sticky=N+S)

pl1gmNumber = IntVar()
ttk.Radiobutton(mainframe, variable=pl1gmNumber, value=2, command=pl1wkAvr).grid(column=5, row=3, sticky=S)
ttk.Radiobutton(mainframe, variable=pl1gmNumber, value=3, command=pl1wkAvr).grid(column=6, row=3, sticky=S)
ttk.Radiobutton(mainframe, variable=pl1gmNumber, value=4, command=pl1wkAvr).grid(column=7, row=3, sticky=S)
ttk.Radiobutton(mainframe, variable=pl1gmNumber, value=5, command=pl1wkAvr).grid(column=8, row=3, sticky=S)

def pl2wkAvr():
    ttk.Label(mainframe, text=round(team.roster[1].avg_points * pl2gmNumber.get(), 2)).grid(column=9, row=4,
                                                                                            sticky=N+S)

pl2gmNumber = IntVar()
ttk.Radiobutton(mainframe, variable=pl2gmNumber, value=2, command=pl2wkAvr).grid(column=5, row=4, sticky=S)
ttk.Radiobutton(mainframe, variable=pl2gmNumber, value=3, command=pl2wkAvr).grid(column=6, row=4, sticky=S)
ttk.Radiobutton(mainframe, variable=pl2gmNumber, value=4, command=pl2wkAvr).grid(column=7, row=4, sticky=S)
ttk.Radiobutton(mainframe, variable=pl2gmNumber, value=5, command=pl2wkAvr).grid(column=8, row=4, sticky=S)

def pl3wkAvr():
    ttk.Label(mainframe, text=round(team.roster[2].avg_points * pl3gmNumber.get(), 2)).grid(column=9, row=5,
                                                                                            sticky=N+S)

pl3gmNumber = IntVar()
ttk.Radiobutton(mainframe, variable=pl3gmNumber, value=2, command=pl3wkAvr).grid(column=5, row=5, sticky=N+S)
ttk.Radiobutton(mainframe, variable=pl3gmNumber, value=3, command=pl3wkAvr).grid(column=6, row=5, sticky=N+S)
ttk.Radiobutton(mainframe, variable=pl3gmNumber, value=4, command=pl3wkAvr).grid(column=7, row=5, sticky=N+S)
ttk.Radiobutton(mainframe, variable=pl3gmNumber, value=5, command=pl3wkAvr).grid(column=8, row=5, sticky=N+S)

def pl4wkAvr():
    ttk.Label(mainframe, text=round(team.roster[3].avg_points * pl4gmNumber.get(), 2)).grid(column=9, row=6,
                                                                                            sticky=N+S)

pl4gmNumber = IntVar()
ttk.Radiobutton(mainframe, variable=pl4gmNumber, value=2, command=pl4wkAvr).grid(column=5, row=6, sticky=N+S)
ttk.Radiobutton(mainframe, variable=pl4gmNumber, value=3, command=pl4wkAvr).grid(column=6, row=6, sticky=N+S)
ttk.Radiobutton(mainframe, variable=pl4gmNumber, value=4, command=pl4wkAvr).grid(column=7, row=6, sticky=N+S)
ttk.Radiobutton(mainframe, variable=pl4gmNumber, value=5, command=pl4wkAvr).grid(column=8, row=6, sticky=N+S)

def pl5wkAvr():
    ttk.Label(mainframe, text=round(team.roster[4].avg_points * pl5gmNumber.get(), 2)).grid(column=9, row=7,
                                                                                            sticky=N+S)

pl5gmNumber = IntVar()
ttk.Radiobutton(mainframe, variable=pl5gmNumber, value=2, command=pl5wkAvr).grid(column=5, row=7, sticky=S)
ttk.Radiobutton(mainframe, variable=pl5gmNumber, value=3, command=pl5wkAvr).grid(column=6, row=7, sticky=S)
ttk.Radiobutton(mainframe, variable=pl5gmNumber, value=4, command=pl5wkAvr).grid(column=7, row=7, sticky=S)
ttk.Radiobutton(mainframe, variable=pl5gmNumber, value=5, command=pl5wkAvr).grid(column=8, row=7, sticky=S)

def pl6wkAvr():
    ttk.Label(mainframe, text=round(team.roster[5].avg_points * pl6gmNumber.get(), 2)).grid(column=9, row=8,
                                                                                            sticky=N+S)

pl6gmNumber = IntVar()
ttk.Radiobutton(mainframe, variable=pl6gmNumber, value=2, command=pl6wkAvr).grid(column=5, row=8, sticky=S)
ttk.Radiobutton(mainframe, variable=pl6gmNumber, value=3, command=pl6wkAvr).grid(column=6, row=8, sticky=S)
ttk.Radiobutton(mainframe, variable=pl6gmNumber, value=4, command=pl6wkAvr).grid(column=7, row=8, sticky=S)
ttk.Radiobutton(mainframe, variable=pl6gmNumber, value=5, command=pl6wkAvr).grid(column=8, row=8, sticky=S)

def pl7wkAvr():
    ttk.Label(mainframe, text=round(team.roster[6].avg_points * pl7gmNumber.get(), 2)).grid(column=9, row=9,
                                                                                            sticky=N+S)

pl7gmNumber = IntVar()
ttk.Radiobutton(mainframe, variable=pl7gmNumber, value=2, command=pl7wkAvr).grid(column=5, row=9, sticky=S)
ttk.Radiobutton(mainframe, variable=pl7gmNumber, value=3, command=pl7wkAvr).grid(column=6, row=9, sticky=S)
ttk.Radiobutton(mainframe, variable=pl7gmNumber, value=4, command=pl7wkAvr).grid(column=7, row=9, sticky=S)
ttk.Radiobutton(mainframe, variable=pl7gmNumber, value=5, command=pl7wkAvr).grid(column=8, row=9, sticky=S)

def pl8wkAvr():
    ttk.Label(mainframe, text=round(team.roster[7].avg_points * pl8gmNumber.get(), 2)).grid(column=9, row=10,
                                                                                            sticky=N+S)

pl8gmNumber = IntVar()
ttk.Radiobutton(mainframe, variable=pl8gmNumber, value=2, command=pl8wkAvr).grid(column=5, row=10, sticky=S)
ttk.Radiobutton(mainframe, variable=pl8gmNumber, value=3, command=pl8wkAvr).grid(column=6, row=10, sticky=S)
ttk.Radiobutton(mainframe, variable=pl8gmNumber, value=4, command=pl8wkAvr).grid(column=7, row=10, sticky=S)
ttk.Radiobutton(mainframe, variable=pl8gmNumber, value=5, command=pl8wkAvr).grid(column=8, row=10, sticky=S)

def pl9wkAvr():
    ttk.Label(mainframe, text=round(team.roster[8].avg_points * pl9gmNumber.get(), 2)).grid(column=9, row=11,
                                                                                            sticky=N+S)

pl9gmNumber = IntVar()
ttk.Radiobutton(mainframe, variable=pl9gmNumber, value=2, command=pl9wkAvr).grid(column=5, row=11, sticky=S)
ttk.Radiobutton(mainframe, variable=pl9gmNumber, value=3, command=pl9wkAvr).grid(column=6, row=11, sticky=S)
ttk.Radiobutton(mainframe, variable=pl9gmNumber, value=4, command=pl9wkAvr).grid(column=7, row=11, sticky=S)
ttk.Radiobutton(mainframe, variable=pl9gmNumber, value=5, command=pl9wkAvr).grid(column=8, row=11, sticky=S)

def pl10wkAvr():
    ttk.Label(mainframe, text=round(team.roster[9].avg_points * pl10gmNumber.get(), 2)).grid(column=9, row=12,
                                                                                             sticky=N+S)

pl10gmNumber = IntVar()
ttk.Radiobutton(mainframe, variable=pl10gmNumber, value=2, command=pl10wkAvr).grid(column=5, row=12, sticky=S)
ttk.Radiobutton(mainframe, variable=pl10gmNumber, value=3, command=pl10wkAvr).grid(column=6, row=12, sticky=S)
ttk.Radiobutton(mainframe, variable=pl10gmNumber, value=4, command=pl10wkAvr).grid(column=7, row=12, sticky=S)
ttk.Radiobutton(mainframe, variable=pl10gmNumber, value=5, command=pl10wkAvr).grid(column=8, row=12, sticky=S)

def pl11wkAvr():
    ttk.Label(mainframe, text=round(team.roster[10].avg_points * pl11gmNumber.get(), 2)).grid(column=9, row=13,
                                                                                              sticky=N+S)

pl11gmNumber = IntVar()
ttk.Radiobutton(mainframe, variable=pl11gmNumber, value=2, command=pl11wkAvr).grid(column=5, row=13, sticky=S)
ttk.Radiobutton(mainframe, variable=pl11gmNumber, value=3, command=pl11wkAvr).grid(column=6, row=13, sticky=S)
ttk.Radiobutton(mainframe, variable=pl11gmNumber, value=4, command=pl11wkAvr).grid(column=7, row=13, sticky=S)
ttk.Radiobutton(mainframe, variable=pl11gmNumber, value=5, command=pl11wkAvr).grid(column=8, row=13, sticky=S)

def pl12wkAvr():
    ttk.Label(mainframe, text=round(team.roster[11].avg_points * pl12gmNumber.get(), 2)).grid(column=9, row=14,
                                                                                              sticky=N+S)

pl12gmNumber = IntVar()
ttk.Radiobutton(mainframe, variable=pl12gmNumber, value=2, command=pl12wkAvr).grid(column=5, row=14, sticky=S)
ttk.Radiobutton(mainframe, variable=pl12gmNumber, value=3, command=pl12wkAvr).grid(column=6, row=14, sticky=S)
ttk.Radiobutton(mainframe, variable=pl12gmNumber, value=4, command=pl12wkAvr).grid(column=7, row=14, sticky=S)
ttk.Radiobutton(mainframe, variable=pl12gmNumber, value=5, command=pl12wkAvr).grid(column=8, row=14, sticky=S)

def pl13wkAvr():
    ttk.Label(mainframe, text=round(team.roster[12].avg_points * pl13gmNumber.get(), 2)).grid(column=9, row=15,
                                                                                              sticky=N+S)

pl13gmNumber = IntVar()
ttk.Radiobutton(mainframe, variable=pl13gmNumber, value=2, command=pl13wkAvr).grid(column=5, row=15, sticky=S)
ttk.Radiobutton(mainframe, variable=pl13gmNumber, value=3, command=pl13wkAvr).grid(column=6, row=15, sticky=S)
ttk.Radiobutton(mainframe, variable=pl13gmNumber, value=4, command=pl13wkAvr).grid(column=7, row=15, sticky=S)
ttk.Radiobutton(mainframe, variable=pl13gmNumber, value=5, command=pl13wkAvr).grid(column=8, row=15, sticky=S)

def pl14wkAvr():
    ttk.Label(mainframe, text=round(team.roster[13].avg_points * pl14gmNumber.get(), 2)).grid(column=9, row=16,
                                                                                              sticky=N+S)

pl14gmNumber = IntVar()
ttk.Radiobutton(mainframe, variable=pl14gmNumber, value=2, command=pl14wkAvr).grid(column=5, row=16, sticky=S)
ttk.Radiobutton(mainframe, variable=pl14gmNumber, value=3, command=pl14wkAvr).grid(column=6, row=16, sticky=S)
ttk.Radiobutton(mainframe, variable=pl14gmNumber, value=4, command=pl14wkAvr).grid(column=7, row=16, sticky=S)
ttk.Radiobutton(mainframe, variable=pl14gmNumber, value=5, command=pl14wkAvr).grid(column=8, row=16, sticky=S)

def pl15wkAvr():
    ttk.Label(mainframe, text=round(team.roster[14].avg_points * pl15gmNumber.get(), 2)).grid(column=9, row=17,
                                                                                              sticky=N+S)

pl15gmNumber = IntVar()
ttk.Radiobutton(mainframe, variable=pl15gmNumber, value=2, command=pl15wkAvr).grid(column=5, row=17, sticky=S)
ttk.Radiobutton(mainframe, variable=pl15gmNumber, value=3, command=pl15wkAvr).grid(column=6, row=17, sticky=S)
ttk.Radiobutton(mainframe, variable=pl15gmNumber, value=4, command=pl15wkAvr).grid(column=7, row=17, sticky=S)
ttk.Radiobutton(mainframe, variable=pl15gmNumber, value=5, command=pl15wkAvr).grid(column=8, row=17, sticky=S)

def pl16wkAvr():
    ttk.Label(mainframe, text=round(team.roster[15].avg_points * pl16gmNumber.get(), 2)).grid(column=9, row=18,
                                                                                              sticky=N+S)

pl16gmNumber = IntVar()
ttk.Radiobutton(mainframe, variable=pl16gmNumber, value=2, command=pl16wkAvr).grid(column=5, row=18, sticky=S)
ttk.Radiobutton(mainframe, variable=pl16gmNumber, value=3, command=pl16wkAvr).grid(column=6, row=18, sticky=S)
ttk.Radiobutton(mainframe, variable=pl16gmNumber, value=4, command=pl16wkAvr).grid(column=7, row=18, sticky=S)
ttk.Radiobutton(mainframe, variable=pl16gmNumber, value=5, command=pl16wkAvr).grid(column=8, row=18, sticky=S)

def pl17wkAvr():
    ttk.Label(mainframe, text=round(team.roster[16].avg_points * pl17gmNumber.get(), 2)).grid(column=9, row=19,
                                                                                              sticky=N+S)

pl17gmNumber = IntVar()
ttk.Radiobutton(mainframe, variable=pl17gmNumber, value=2, command=pl17wkAvr).grid(column=5, row=19, sticky=S)
ttk.Radiobutton(mainframe, variable=pl17gmNumber, value=3, command=pl17wkAvr).grid(column=6, row=19, sticky=S)
ttk.Radiobutton(mainframe, variable=pl17gmNumber, value=4, command=pl17wkAvr).grid(column=7, row=19, sticky=S)
ttk.Radiobutton(mainframe, variable=pl17gmNumber, value=5, command=pl17wkAvr).grid(column=8, row=19, sticky=S)

def pl18wkAvr():
    ttk.Label(mainframe, text=round(team.roster[17].avg_points * pl18gmNumber.get(), 2)).grid(column=9, row=20,
                                                                                              sticky=N+S)

pl18gmNumber = IntVar()
ttk.Radiobutton(mainframe, variable=pl18gmNumber, value=2, command=pl18wkAvr).grid(column=5, row=20, sticky=S)
ttk.Radiobutton(mainframe, variable=pl18gmNumber, value=3, command=pl18wkAvr).grid(column=6, row=20, sticky=S)
ttk.Radiobutton(mainframe, variable=pl18gmNumber, value=4, command=pl18wkAvr).grid(column=7, row=20, sticky=S)
ttk.Radiobutton(mainframe, variable=pl18gmNumber, value=5, command=pl18wkAvr).grid(column=8, row=20, sticky=S)

ttk.Label(mainframe, text="Week AVR").grid(column=9, row=2, sticky=S)   # девятый столбец

ttk.Label(mainframe, text="Total week team AVR:").grid(column=10, row=2, sticky=S)   # десятый столбец

ttk.Label(mainframe, text="total").grid(column=11, row=2, sticky=S)    # одиннадцатый столбец

def resetChbxsAndRdbtns():
    in_game_checkbox.set(value="out"), pl1gmNumber.set(value=0), pl2gmNumber.set(value=0), pl3gmNumber.set(value=0)
    pl4gmNumber.set(value=0), pl5gmNumber.set(value=0), pl6gmNumber.set(value=0), pl7gmNumber.set(value=0)
    pl8gmNumber.set(value=0), pl9gmNumber.set(value=0), pl10gmNumber.set(value=0), pl11gmNumber.set(value=0)
    pl12gmNumber.set(value=0), pl13gmNumber.set(value=0), pl14gmNumber.set(value=0), pl15gmNumber.set(value=0)
    pl16gmNumber.set(value=0), pl17gmNumber.set(value=0), pl18gmNumber.set(value=0)
    name_number = 0
    while name_number < 18:
        ttk.Label(mainframe, text="").grid(column=9, row=name_number + 3, sticky=W + E + N + S)
        name_number += 1

ttk.Button(mainframe, text="Очистить", command=resetChbxsAndRdbtns).grid(column=11, row=21, sticky=S)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

team_name_box.focus()
root.bind("<Return>", 0)

root.mainloop()
