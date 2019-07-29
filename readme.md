# Angular - Liferay Migrator

Tool realizzato in python per l'adattamento di un progetto Angular 6 
ad una portlet Liferay 7.2

# Requisiti
- Organizzazione del progetto secondo la struttura definita nel progetto esempio
- Progetto angular versione 6.x
- Prestare attenzione al nome delle directory di progetto in quanto aluni riferimenti possono risultare non validi, per correttezza la directory di progetto 
deve avere il nome definito per il progetto all'interno del package.json

# Operazioni aggiuntive
- Rimappare la struttura del router (providers, UseHash). Visualizzare progetto esempio
- Rimuovere ogni link riferito ai file .css dai file .ts di ogni componente, i riferimenti ai file css vengono creati automaticamente, partendo dal presupporto che
ogni componente disponga di un file "nome.component.css" all'interno della directory del Component
- Per abilitare il caricamento iniziale eseguire una navigazione interna al router manuale al bootstrap del modulo, nell'esempio quindi
osservare la chiamata al metodo *navigate* nell' app.component.ts 

# Struttura progetto pre-conversione
- node_modules
- src
  - app
    - component1
    - app.module.ts
    - app.routing.module.ts
- package.json
