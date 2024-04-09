[Výsledný Datalore dashboard na ukázku](https://datalore.jetbrains.com/report/static/oe9Oq43QW0xITpjgLX6x1v/fdqEemItzszWYbuW9SVcPK)

## 1. Vytvoření API aplikace
a) Přihlásit se na svůj učet Strava.

b) Jít na https://www.strava.com/settings/api a vytvořit aplikaci, website a authorization callback domain nastavit jako "localhost". Je nutné vybrat pro aplikaci nějaký obrázek jako ikonu.

![image](https://github.com/koldamartin/Strava_API_analysis/assets/68967537/392ba881-1844-41bb-a563-029c9db1b145)


c) Zjistit "Client ID" číslo a "Client Secret" číslo

![image](https://github.com/koldamartin/Strava_API_analysis/assets/68967537/2936f965-9ec5-4dbb-b74e-74cb1e63f950)

## 2. Spuštění skriptu main.py
Nainstalovat knihovnu python-dotenv (pip install python-dotenv)

Vytvořit .env soubor ve stejné složce jako je main.py a vepsat proměnné CLIENT_ID a CLIENT_SECRET
![image](https://github.com/koldamartin/Strava_API_analysis/assets/68967537/08c7087b-958b-40d4-8f4b-7bf793fbcd7f)


Spustit Python skript main.py

Skrpit je částečně převzatý odsud https://www.grace-dev.com/python-apis/strava-api/ Není tedy nutné používat Swagger client, který Strava API běžně vyžaduje

## 3. Získání Acces Tokenu

Kliknout na vygenerovaný link a odsouhlasit autorizaci

![image](https://github.com/koldamartin/Strava_API_analysis/assets/68967537/b3686411-3fb0-43e7-bcfa-cf4bbd8e8f5c)

Zkopírovat kód z http://localhost/ a vložit ho jako input do dotazu 'Insert the code from the url: '
![image](https://github.com/koldamartin/Strava_API_analysis/assets/68967537/82214b81-3140-4c85-ba9c-73210b058736)

## 4. Vygenerování dat

Po úspěšném spuštění skriptu se vygeneruje soubor activities.csv se všemi daty ze stravy, jeden řádek = jedna aktivita. Maximum vygenerovaných aktivit je 2000. 

## 5. Datová anaýlza

Spustit Strava API.ipynb notebook, je potřeba mít nainstalované knihovny Pandas, Matplotlib a Seaborn

Nastavit správnou cestu pro vyhledání souboru activities.csv


![image](https://github.com/koldamartin/Strava_API_analysis/assets/68967537/9e7fd300-ecdf-481d-a091-8f2e9e453f10)

Ručně přepsat hodnoty gear_id, z jakéhosi důvodu strava načte jen nic neříkající kódy a je nutné přijít na to který kód patří pro které kolo.

![image](https://github.com/koldamartin/Strava_API_analysis/assets/68967537/0b7d45ce-095c-46b5-88b7-2e101b65ef16)


Spustit notebook








