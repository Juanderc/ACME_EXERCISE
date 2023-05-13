# Programa para la empresa ACME

ACME ofrece a sus empleados la flexibilidad de trabajar las horas que deseen. Pagarán por las horas trabajadas
según el día de la semana y la hora del día, según la siguiente tabla:

```
Lunes - viernes
00:01 - 09:00 25 USD
09:01 - 18:00 15 USD
18:01 - 00:00 20 USD

Sábado y Domingo
00:01 - 09:00 30 USD
09:01 - 18:00 20 USD
18:01 - 00:00 25 USD
```

## Usage

1. Al ejecutar el archivo python, recibiremos un mensaje en donde se nos pedira el nombre del archivo que contiene la informacion
    de los dias y horario trabajado por los empleados

2. Al introducir el nombre del archivo a leer, luego recibiremos otro mensaje, en donde deberemos introducir el nombre del archivo
   que deseamos utilizar para guardar el resultado de la operacion o el monto a pagar a dicho empleado.

3. Dichos archivos seran guardados en un folder llamado (docs), por lo que si se desea crear un archivo nuevo para ser leido, aqui 
    es donde debe ser almacenado.

4. Se cuenta ademas con un archivo llamado tester, el cual al ser ejecutado correra una prueba para validar que el codigo se esta
    ejecutando y respondiendo como deberia.

```
python3 ACME.py

Please enter the file_name to read content: [file_name with the emplyees work time information] example [employees_work_time.txt]

Please enter the file_name to write the result: [file_name to write result] example [employees_compensation.txt]
```

## Logic

Aqui estoy usando varias cosas, lo primero es un diccionario que contiene los dias, hora y pago por hora, para luego recorrer dicho diccionario
utilizando un bucle (for) y por tanto identificar en el monto a pagar a dicho empleado.

Dentro del codigo existe un metodo llamado "evaluate_compensation" el cual realiza toda la operacion, utilizando una serie de logicas como:


```
    if end_hour_in_time_format.split(":")[0] == datetime.strptime("00", "%H").strftime("%H"):
        end_hour_in_time_format = f'24:{end_hour_in_time_format.split(":")[1]}'
```
```
    if start_hour_in_time_format <= start_hour_in_time_format_from_input <= end_hour_in_time_format
```

```
    if end_hour_in_time_format_from_input <= end_hour_in_time_format:
```

```
    if start_hour_in_time_format <= start_hour_in_time_format_from_input and end_hour_in_time_format <= end_hour_in_time_format_from_input:
```

```
    if start_hour_in_time_format >= start_hour_in_time_format_from_input and start_hour_in_time_format <= end_hour_in_time_format_from_input:
```

Estas condiciones evaluan casos como que si el horario viene con 00:00, ademas de que si el horario cuanta con un rango extenso, como por ejemplo
TU07:00-23:00, lo cual me indica que el empleado trabajo varias jornadas, por lo cual en es necesario determinar el monto a pagar por la jornada 
de (00:01-09:00), (09:01-18:00) y de (18:01-00:00) (25), (15) (20) por hora respectivamente.

En resumen lo que hace dicho metodo es evaluar a cual rango de horario corresponde el horario trabajado por el empleado.


#Author

```
                                                Juander Contreras.
```