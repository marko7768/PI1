# Proyecto MLOps: Desarrollo de un Sistema de Recomendación para Steam

¡Bienvenido al repositorio del proyecto MLOps de Steam! En este proyecto de Henry, se asumió el rol de un MLOps Engineer para llevar a cabo la implementación de un sistema de recomendación de videojuegos en la plataforma Steam.

# Descripción del Problema y Rol a Desarrollar

## Contexto
La tarea es crear un sistema de recomendación de videojuegos para usuarios en la plataforma Steam. Donde enfrentas desafíos debido a la falta de madurez en los datos, que requiere intervención en el área de Data Engineering.

## Rol a Desarrollar
Comenzaras tu trabajo como Data Scientist en Steam, abordando la falta de madurez en los datos y creando un sistema de recomendación eficiente desde cero. Se debe realizar transformaciones, ingeniería de características y desarrollar una API utilizando FastAPI para exponer los datos de la empresa.

# Propuesta de Trabajo

## Transformaciones
Los datos originales estan comprimidos en la carpeta datos_originales. Los datos fueron descomprimidos con las herramientas incluidas en Linux y guardados en la carpeta datos. En el notebook ETL se transforman los datos a parquet por cuestiones de comodidad.

# Desarrollo API
Proporciona datos de la empresa a través de FastAPI con los siguientes endpoints:

* developer(desarrollador: str): Cantidad de items y porcentaje de contenido Free por año según la empresa desarrolladora.

* userdata(User_id: str): Dinero gastado por el usuario, porcentaje de recomendación y cantidad de items.

* UserForGenre(genero: str): Usuario con más horas jugadas para el género dado y acumulación de horas jugadas por año.

* best_developer_year(año: int): Top 3 de desarrolladores con juegos MÁS recomendados por usuarios para el año dado.

* developer_reviews_analysis(desarrolladora: str): Análisis de sentimiento de reseñas por desarrolladora.
