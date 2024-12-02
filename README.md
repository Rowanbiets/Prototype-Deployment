# **My Custom GitHub Action**

## **Beschrijving**

Deze repository bevat een GitHub Action die automatisch een specifieke taak uitvoert, zoals het groeten van een gebruiker of andere procesautomatisering. Het project is opgezet om eenvoudig te integreren in CI/CD-workflows en kan worden aangepast voor verschillende use cases, zoals het uitvoeren van build-processen, verzenden van notificaties of andere taken.

---

## **Inhoud**
- [Beschrijving](#beschrijving)
- [Kenmerken](#kenmerken)
- [Installatie](#installatie)
- [Gebruik](#gebruik)
- [Workflowvoorbeeld](#workflowvoorbeeld)
- [Ontwikkeling](#ontwikkeling)
- [Contributie](#contributie)
- [Licentie](#licentie)

---

## **Kenmerken**
- **Automatische uitvoering binnen GitHub Actions**: Integreer de actie eenvoudig in je GitHub CI/CD-pijplijn.
- **Eenvoudige invoerparameters**: Pas de actie aan door invoerparameters door te geven (bijvoorbeeld naam, bericht, enz.).
- **Ondersteunt versiebeheer**: Gebruik de actie met versiebeheer, zodat je kunt kiezen welke versie van de actie je wilt gebruiken in je workflow.
- **Makkelijk aan te passen**: De actie is eenvoudig aan te passen voor verschillende use cases zoals het uitvoeren van build-processen, notificaties sturen, of andere aangepaste taken.

---

## **Installatie**

Volg de onderstaande stappen om de actie te installeren en te gebruiken in je project.

### 1. Voeg de actie toe aan je workflow

Maak een nieuwe workflow in je project door een bestand toe te voegen in de `.github/workflows` directory. Noem het bijvoorbeeld `ci-cd.yml`. Voeg de volgende configuratie toe aan dit bestand om de actie te gebruiken:

```yaml
name: Test Action Workflow

on:
  push:
    branches:
      - main

jobs:
  test-action:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Run Custom Action
        uses: ./my-action
        with:
          name: Rowan  # Pas de naam aan zoals gewenst



name: Welcome Workflow

on:
  push:
    branches:
      - main

jobs:
  greeting:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Run Greeting Action
        uses: ./my-action
        with:
          name: Rowan




