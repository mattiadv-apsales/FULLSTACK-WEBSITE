==========================================
 TODO WEB APP - Flask Version
==========================================

🔹 Descrizione
------------------------------------------
Questa è una web app full-stack sviluppata con Python (Flask) per la gestione delle attività (to-do list).
Gli utenti possono registrarsi, accedere, aggiungere, spuntare o eliminare le attività.
I dati vengono salvati in un file JSON locale (`db.json`) che funge da piccolo database.

Il progetto include:
- Sistema di autenticazione con sessione Flask
- Hashing delle password con bcrypt
- Pagina errore personalizzata (error.html)
- Interfaccia responsive in HTML, CSS e JavaScript
- Struttura completa tipica di un progetto full-stack


🔹 Struttura del progetto
------------------------------------------
📁 project/
│
├── app.py                  → Server Flask principale
├── lib.py                  → Logica per utenti e to-do (funzioni CRUD e autenticazione)
├── db.json                 → File JSON che funge da database
│
├── templates/
│   ├── index.html          → Pagina login e registrazione
│   ├── sbem.html           → Pagina principale della to-do list
│   └── error.html          → Pagina errore 404 personalizzata
│
├── static/
│   ├── style/
│   │   ├── style.css       → Stile principale per login/registrazione
│   │   ├── sbem.css        → Stile per la pagina della to-do list
│   │   └── error.css       → Stile per la pagina errore
│   │
│   └── script/
│       ├── script.js       → Script per la gestione del login/registrazione
│       ├── sbem.js         → Script per la gestione delle attività nella to-do list
│       └── error.js        → Script per la pagina di errore
│
└── .env                    → File con variabili d’ambiente (SECRET_KEY)


🔹 Avvio in locale
------------------------------------------
1️⃣ Installa i moduli richiesti:
    pip install flask python-dotenv bcrypt

2️⃣ Crea un file `.env` nella root del progetto con dentro:
    SECRET_KEY=qualcosa_di_unico_e_lungo

3️⃣ Crea un file `db.json` con questo contenuto iniziale:
    []

4️⃣ Avvia il server:
    python app.py

5️⃣ Apri il browser su:
    http://127.0.0.1:5000


🔹 Sicurezza
------------------------------------------
- Le password sono criptate con bcrypt
- Le sessioni Flask sono protette da una SECRET_KEY
- Le route riservate richiedono login
- Gestione errori personalizzata (404)
- Nessuna password salvata in chiaro


🔹 Autore
------------------------------------------
👤 Sviluppato da: Mattia De Vincentis  
💼 Full-Stack Web Developer  
📆 Anno: 2025