# **Flask Web Application with CI/CD Pipeline**

## **Beschrijving**

Dit project bevat een Flask-webtoepassing die wordt gebruikt voor het groeten van een gebruiker en het uitvoeren van eenvoudige rekenkundige bewerkingen, zoals optellen. Het is geïntegreerd met een CI/CD-pijplijn via GitHub Actions om automatisch tests uit te voeren en de applicatie te implementeren wanneer er wijzigingen in de `main` branch worden gepusht. Deze oplossing bevat ook een custom GitHub Action om specifieke taken zoals het uitvoeren van tests te automatiseren.

---

## **Inhoud**
- [Beschrijving](#beschrijving)
- [Kenmerken](#kenmerken)
- [Installatie](#installatie)
- [Gebruik](#gebruik)
- [CI/CD Pipeline](#cicd-pipeline)
- [Ontwikkeling](#ontwikkeling)
- [Contributie](#contributie)
- [Licentie](#licentie)

---

## **Kenmerken**
- **Flask Webapplicatie**: Een eenvoudige webapp die een gezondheidsoverzicht en optelling van twee getallen biedt via een REST API.
- **Automatische uitvoering van tests**: Geïntegreerd met een GitHub Actions CI/CD-pijplijn om tests automatisch uit te voeren bij elke push naar de `main` branch.
- **Deployment naar GitHub Pages**: De applicatie kan automatisch worden gedeployed naar GitHub Pages of een andere server na succesvolle tests.
- **Eenvoudige configuratie**: Het is eenvoudig aan te passen voor andere projecten die gebruik maken van Flask en GitHub Actions.

---

## **Installatie**

Volg deze stappen om de applicatie lokaal te draaien en om de CI/CD-pijplijn in te stellen.

### 1. Clone de repository
Clone het project naar je lokale machine:

```bash
git clone https://github.com/yourusername/Prototype-Deployment.git
cd Prototype-Deployment
```

### 2. Maak een virtuele omgeving
Het is aanbevolen om een virtuele omgeving te gebruiken om de afhankelijkheden van het project te installeren. Dit zorgt ervoor dat de benodigde versies van de pakketten geïsoleerd blijven van andere projecten op je machine.

```bash
python -m venv venv
source venv/bin/activate  # Voor Linux/Mac
venv\Scripts\activate  # Voor Windows
```

### 3. Installeer de afhankelijkheden

Installeer de benodigde Python-pakketten met behulp van pip. De afhankelijkheden worden gedefinieerd in het bestand requirements.txt:
```bash
pip install -r requirements.txt
```

### 4. Start de Flask-applicatie lokaal

Start de Flask-webapplicatie door het volgende commando uit te voeren:
```bash
flask run
```
### CI/CD Pipeline

Dit project maakt gebruik van GitHub Actions om geautomatiseerde tests uit te voeren en de applicatie te deployen naar een server of GitHub Pages zodra er wijzigingen in de main branch worden gepusht.

Workflowbestand
De CI/CD-pijplijn wordt gedefinieerd in de GitHub Actions workflowbestanden die zich bevinden in de .github/workflows/ map. Het bestand ci-cd.yml bevat de configuratie voor zowel het uitvoeren van tests als het deployen van de applicatie.

```bash
name: Test and Deploy

on:
  push:
    branches:
      - main

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v3
      with:
        python-version: '3.12'

    - name: Install dependencies
      run: |
        python -m venv venv
        . venv/bin/activate
        pip install -r requirements.txt
        pip install flask

    - name: Run tests
      run: |
        . venv/bin/activate
        venv/bin/pytest

  deploy:
    needs: test
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./build

```
### Ontwikkeling

Dit project is flexibel en kan verder worden uitgebreid naar eigen wens. Enkele mogelijke uitbreidingen zijn:

- Extra API endpoints: Voeg meer API-endpoints toe voor andere rekenkundige bewerkingen of functionaliteiten.
- Authenticatie en Autorisatie: Voeg gebruikersauthenticatie toe om de applicatie veiliger te maken.
- Logging en Foutafhandeling: Verbeter de logging en voeg meer gedetailleerde foutafhandelingsmechanismen toe voor een robuustere applicatie.
- Containerization met Docker: Containeriseer de applicatie met Docker voor eenvoudiger deployen naar verschillende omgevingen.

### Contributie

Contributies aan dit project zijn welkom! Als je wilt bijdragen, volg dan de onderstaande stappen:

1.Fork de repository naar je eigen GitHub-account.
2.Maak een nieuwe branch voor de feature of bugfix waaraan je wilt werken.
3.Maak je wijzigingen en commit ze.
4.Open een pull request naar de main branch van dit repository voor review.
5.Zorg ervoor dat je tests uitvoert en documentatie bijwerkt voordat je een pull request maakt.

### Licentie

Dit project is gelicentieerd onder de MIT License - zie het LICENSE bestand voor details.
