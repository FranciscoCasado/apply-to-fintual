# ¡Hola Fintual :wave:!
Acá explico un poco lo que hice, en tres etapas: entender, modelar y t

## Primero saber qué es un portafolio 
Un portafolio es una colecciones de acciones (stocks). Cada acción tiene un valor monetario que varía en el tiempo, por lo que el valor del portafolio, calculado como la suma de todas las acciones que contiene, también varía en el tiempo.

El retorno o rentabilidad (profit) de un portafolio se calcula como la variación del precio del portafolio entre dos fechas. Puede expresarse como la diferencia absoluta o, más comunmente, como la variación porcentual:
```
profit = (valor_fecha_2 / valor_fecha_1) - 1
```

El *retorno anualizado* corresponde extrapolar la rentabilidad de un periodo arbitrario (`N` días) a un periodo de un año, considerando una tasa compuesta fija:
```
annualized_return = (1 + profit) ^ (365/N) - 1
```

## Modelar un portafolio *simple*
Un portafolio debe tener al menos:
- Un conjunto de `Stocks`
- La cantidad de unidades de cada `Stock` que componen el portafolio
- Un nombre, ojalá uno *cool* como  los de Fintual

El archivo `src/portfolio.py` contiene la clase con los atributos: 
- `stocks`: diccionario cuya llave es el nombre del stock y su valor una instancia de dicha `stock`
- `stock_units`: diccionatio cuya llave es el nombre del stock y su valor la cantidad de unidades que se poseen de dichas acciones
- `name`: el nombre del portafolio

Por defecto, `stocks` y `stock_units` se inicializan vacíos. Para incorporar `Stocks`, debe existir un método adicional `Portfolio.add_stocks`.

El método `Portfolio.profit` hace lo siguiente:
- calcular el valor del portafolio *para cada fecha* como la suma ponderada entre cada precio de stock y las unidades que lo componen
- calcular la diferencia porcentual
- calcular el valor anualizado a partir de la diferencia porcentual

Por defecto, retorna el valor anualizado, si no (`annualized=False`) retorna la diferencia porcentual.

## Programar y testear
Implementé las clases `Stock` y `PortfolioFactory` para poder testear como corresponde.

El método `Stock.price` calcula el precio de la acción considerando una tasa compuesta fija y tomando como referencia el precio al 01 de enero de 2021.


## Referencias

Fintual API: https://fintual.cl/api-docs/index.html

