hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

                                    # 12:17 y 59 minutos de duracion

mins += dura                        # total de minutos
                                    # i.e. 17 min + 59 min de duracion = 76 min totales

hour += mins // 60                  # encuentra un numero de horas escondido en los minutos y actualiza la hora
                                    # i.e. 76 min totales // 60 min / hora = 1
                                    #      12 horas + 1 hora = 13 horas

mins %= 60                          # corrige los minutos para que entren en el rango de (0..59)
                                    # i.e. 76 min totales % 60 = 16 minutos

hour %= 24                          # corrige las horas para que entren en el rango de (0..23)
                                    # i.e. 13 horas % 24 = 13 horas

print(hour, ":", mins, sep="")      # output: 13:16