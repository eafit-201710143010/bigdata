# bigdata

## Lab word count

### Instrucciones de ejecución:

*python mr.py otros/dataempleados.csv*

### Solución a:
Se tiene un conjunto de datos, que representan el salario anual de los empleados formales en Colombia por sector económico, según la DIAN.

Se realizó un programa en Map/Reduce, con hadoop en Python o Java, que permite calcular:

El salario promedio por Sector Económico (SE)
El salario promedio por Empleado
Número de SE por Empleado que ha tenido a lo largo de la estadística

### Resultados:

"Salario promedio empleado: 1115"       62333
"Salario promedio empleado: 3233"       35500
"Salario promedio empleado: 3237"       40000
"Salario promedio secEcon: 1212"        77000
"Salario promedio secEcon: 1234"        37500
"Salario promedio secEcon: 1412"        76000
"Salario promedio secEcon: 3432"        34000
"Salario promedio secEcon: 5434"        36000
"SecEcon por empleado: 1115"    3
"SecEcon por empleado: 3233"    2
"SecEcon por empleado: 3237"    1

## Lab covid

se realizó un archivo de notebook jupyter con las siguientes características

- carga de datos csv en spark desde un bucket S3.
- borrar y crear algunas columnas
- realizar filtrados de datos por alguna información que le parezca interesante
- realizar alguna agrupación y consulta de datos categorica, por ejemplo número de casos por región o por sexo/genero.
- finalmente grave los resultados en un bucket público en S3
- realice toda la documentación en el mismo notebook, y cuando ya lo tenga listo adjuntelo a su github para su entrega final.
