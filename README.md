# Ejemplo de blog con Flask

├── api
│   ├── api.py
│   ├── models.py
│   └── initialize.py
├── install.sh
├── README.md
└── webApp
    ├── static
    │   └── main.css
    ├── templates
    │   ├── create.html
    │   └── index.html
    └── webapp.py

Para instalar los requerimientos necesarios para la api y la aplicación:
	chmod +x install.sh
	./install.sh

Despues en una ventana ejecutar:
	cd api
	sudo python api.py

Y en otra:
	cd webApp
	sudo python webapp.py

Luego, en el navegador ingresas a localhost:5000