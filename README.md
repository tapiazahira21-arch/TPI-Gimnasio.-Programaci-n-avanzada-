# TPI-Gimnasio.-Programacion-avanzada-

# Sistema de Gestión de Gimnasio

## Descripción del Proyecto

Este proyecto consiste en el desarrollo de un sistema de gestión para un gimnasio utilizando Programación Orientada a Objetos (POO) en Python. Su objetivo es administrar clientes, profesores y pagos mediante una estructura organizada y escalable basada en clases y relaciones entre objetos.

El sistema permite registrar clientes y profesores, gestionar pagos asociados a los clientes y consultar la información almacenada a través de un menú interactivo por consola.

## Objetivos

* Aplicar los principios de la Programación Orientada a Objetos.
* Modelar una situación real mediante clases y objetos.
* Implementar relaciones entre clases como asociación y agregación.
* Utilizar patrones de diseño para mejorar la organización del sistema.
* Gestionar información de un gimnasio de manera simple y eficiente.

## Funcionalidades

### Gestión de Clientes

* Registrar nuevos clientes.
* Almacenar nombre, apellido, DNI y número de socio.
* Consultar la información de los clientes registrados.

### Gestión de Profesores

* Registrar profesores.
* Almacenar nombre, apellido, DNI y turno de trabajo.
* Consultar la información de los profesores registrados.

### Gestión de Pagos

* Registrar pagos asociados a un cliente.
* Buscar clientes por DNI antes de registrar el pago.
* Almacenar monto, fecha, método de pago y estado.
* Consultar el historial de pagos registrados.

## Conceptos de POO Aplicados

### Encapsulamiento

Los atributos de las clases se encuentran protegidos mediante el uso de atributos internos, permitiendo una mejor organización de los datos.

### Herencia

Las clases Cliente, Profesor y Administrador heredan de la clase Persona, reutilizando atributos y comportamientos comunes.

### Polimorfismo

Las clases derivadas redefinen el método `mostrar_datos()`, proporcionando información específica según el tipo de objeto.

### Abstracción

Las operaciones de registro y consulta ocultan los detalles internos de implementación, facilitando el uso del sistema.

## Relaciones entre Clases

### Asociación

La clase Pago mantiene una relación con la clase Cliente, ya que cada pago pertenece a un cliente específico.

### Agregación

La clase Gimnasio almacena y administra colecciones de clientes, profesores y pagos.

## Patrón de Diseño Utilizado

### Singleton

La clase Gimnasio implementa el patrón Singleton para garantizar que exista una única instancia encargada de gestionar toda la información del sistema.

## Estructura General del Sistema

* Persona

  * Cliente
  * Profesor
  * Administrador
* Pago
* Gimnasio

## Instrucciones de ejecución

### Requisitos
- Python 3.x instalado.

### Pasos

1. Descargar o clonar el repositorio.
2. Abrir una terminal en la carpeta del proyecto.
3. Ejecutar el siguiente comando:

```bash
python gimnasio.py

3. Utilizar el menú interactivo para registrar clientes, profesores y pagos.

## Autores

* Amarilla Hérnan
* Franco Ariel
* Navarro Tiara
* Tapia Zahira
