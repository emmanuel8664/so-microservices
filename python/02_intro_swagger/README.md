### Introducción al lenguaje Python
Universidad ICESI  
Curso: Sistemas Operativos  
Docente: Daniel Barragán C.  
Tema: Introducción a Swagger  
Correo: daniel.barragan at correo.icesi.edu.co

### Objetivos
* Documentar servicios web por medio de swagger

### Introducción
Swagger es un framework de código abierto para el diseño, construcción, documentación y consumo de APIs RESTful.

### Instalación

En esta guía se asume que cuenta con una máquina virtual con el sistema operativos CentOS 7.x instalado. Las versiones de CentOS incluyen Python por defecto.

### Desarrollo

#### Ejemplo básico

```python
from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/consultar_estado', methods=['GET'])
def consulta_estado():
    data = request.json
    return jsonify(data=data, meta={"status": "ok"})

app.run()
```

#### Scripts con Python

Cree un archivo de nombre greeting.py

```python
import sys
print "hi " + sys.argv[1]
print "salut %s" % (sys.argv[1])
```

```
$ python greeting.py "daniel"
```

#### Leer archivo en Python



### Actividades

#### Ejecutando cualquier comando en consola
Realice un script en python que reciba como parametro una cadena de texto con un comando (el comando debe tener argumentos de entrada) y lo ejecute en la consola. Debe usar subprocess.

### Referencias
https://flask-restplus.readthedocs.io/en/stable/
http://michal.karzynski.pl/blog/2016/06/19/building-beautiful-restful-apis-using-flask-swagger-ui-flask-restplus/
https://github.com/postrational/rest_api_demo
http://petstore.swagger.io/
