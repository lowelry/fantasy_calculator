# получение данных api
from espn_api.basketball import League  # инпортируем класс лиги
league = League(league_id=1013716421, year=2023)    # выполняем вход в конкретную лигу

# интерфейс
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("ЛББП")

mainframe = ttk.Frame(root, padding="10 21")    # создаем сетку
mainframe.grid(column=0, row=0, sticky=(S, S, S, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

ttk.Label(mainframe, text="Выберите команду:").grid(column=0, row=0, sticky=W)  #первый столбец
ttk.Label(mainframe, text="Актуальный состав:").grid(column=0, row=1, sticky=W)
ttk.Label(mainframe, text="Скамейка:").grid(column=0, row=14, sticky=W)

team_number = 0
team_name_list = league.teams[team_number]
players_names_list = team_name_list.roster
players_names_str = (",".join(map(str,players_names_list)))
players_names_str = players_names_str.replace("Player(", "")
players_names_str = players_names_str.replace(")", "")
players_names_list = list(players_names_str.split(","))
name_number = 0
while name_number < 16:
    if name_number < 10:
        ttk.Label(mainframe, text=players_names_list[name_number]).grid(column=0, row=name_number + 3, sticky=W)
    elif name_number > 10:
        ttk.Label(mainframe, text=players_names_list[name_number - 1]).grid(column=0, row=name_number + 4, sticky=W)
    name_number += 1

team_name_list = league.teams   #второй столбец
team_name_str = (" ".join(map(str,team_name_list)))
team_name_str = team_name_str.replace("Team(", "")
team_name_str = team_name_str.replace(")", ".")
team_name_list = list(team_name_str.split(". "))
team_name_box = ttk.Combobox(mainframe, values=team_name_list)
team_name_box.grid(column=1, row=0, sticky=(S, S))
#team_name_box.bind('<<ComboboxSelected>>', 0)  #обработчик событий выпадающего листа

team = league.teams[0]
player = team.roster[0]
ttk.Label(mainframe, text="AVR").grid(column=2, row=2, sticky=S)    #третий столбец
ttk.Label(mainframe, text=player.avg_points).grid(column=2, row=3, sticky=S)
ttk.Label(mainframe, text="Pl2").grid(column=2, row=4, sticky=S)
ttk.Label(mainframe, text="Pl3").grid(column=2, row=5, sticky=S)
ttk.Label(mainframe, text="Pl4").grid(column=2, row=6, sticky=S)
ttk.Label(mainframe, text="Pl5").grid(column=2, row=7, sticky=S)
ttk.Label(mainframe, text="Pl6").grid(column=2, row=8, sticky=S)
ttk.Label(mainframe, text="Pl7").grid(column=2, row=9, sticky=S)
ttk.Label(mainframe, text="Pl8").grid(column=2, row=10, sticky=S)
ttk.Label(mainframe, text="Pl9").grid(column=2, row=11, sticky=S)
ttk.Label(mainframe, text="Pl10").grid(column=2, row=12, sticky=S)
ttk.Label(mainframe, text="").grid(column=2, row=14, sticky=S)
ttk.Label(mainframe, text="Pl11").grid(column=2, row=15, sticky=S)
ttk.Label(mainframe, text="Pl12").grid(column=2, row=16, sticky=S)
ttk.Label(mainframe, text="Pl13").grid(column=2, row=17, sticky=S)
ttk.Label(mainframe, text="Pl14").grid(column=2, row=18, sticky=S)
ttk.Label(mainframe, text="Pl15").grid(column=2, row=19, sticky=S)

ttk.Label(mainframe, text="Количество игр:").grid(column=3, row=2, sticky=S)    #четвертый столбец

ttk.Label(mainframe, text="2").grid(column=4, row=2, sticky=S)  #пятый столбец
two_games_1 = StringVar()
check_two_games_1 = ttk.Checkbutton(mainframe, text="0/1", command=0, variable=two_games_1, onvalue='1', offvalue='0')
check_two_games_1.grid(column=4, row=3, sticky=S)

ttk.Label(mainframe, text="3").grid(column=5, row=2, sticky=S)  #шестой столбец

ttk.Label(mainframe, text="4").grid(column=6, row=2, sticky=S)  #седьмой столбец

ttk.Label(mainframe, text="5").grid(column=7, row=2, sticky=S)  #восьмой столбец

ttk.Label(mainframe, text="Week AVR").grid(column=8, row=2, sticky=S)   #девятый столбец
ttk.Label(mainframe, text="Pl1").grid(column=8, row=3, sticky=S)
ttk.Label(mainframe, text="Pl2").grid(column=8, row=4, sticky=S)
ttk.Label(mainframe, text="Pl3").grid(column=8, row=5, sticky=S)
ttk.Label(mainframe, text="Pl4").grid(column=8, row=6, sticky=S)
ttk.Label(mainframe, text="Pl5").grid(column=8, row=7, sticky=S)
ttk.Label(mainframe, text="Pl6").grid(column=8, row=8, sticky=S)
ttk.Label(mainframe, text="Pl7").grid(column=8, row=9, sticky=S)
ttk.Label(mainframe, text="Pl8").grid(column=8, row=10, sticky=S)
ttk.Label(mainframe, text="Pl9").grid(column=8, row=11, sticky=S)
ttk.Label(mainframe, text="Pl10").grid(column=8, row=12, sticky=S)
ttk.Label(mainframe, text="").grid(column=8, row=14, sticky=S)
ttk.Label(mainframe, text="Pl11").grid(column=8, row=15, sticky=S)
ttk.Label(mainframe, text="Pl12").grid(column=8, row=16, sticky=S)
ttk.Label(mainframe, text="Pl13").grid(column=8, row=17, sticky=S)
ttk.Label(mainframe, text="Pl14").grid(column=8, row=18, sticky=S)
ttk.Label(mainframe, text="Pl15").grid(column=8, row=19, sticky=S)

ttk.Label(mainframe, text="Total week team AVR:").grid(column=9, row=2, sticky=S)   #десятый столбец

ttk.Label(mainframe, text="total").grid(column=10, row=2, sticky=S) #одиннадцатый столбец
ttk.Button(mainframe, text="Обновить", command=0).grid(column=10, row=21, sticky=S)


for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

team_name_box.focus()
root.bind("<Return>", 0)

root.mainloop()
