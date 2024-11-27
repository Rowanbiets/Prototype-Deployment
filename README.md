# **My Custom GitHub Action**

[![Actions Status](https://github.com/your-username/your-repo/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/your-username/your-repo/actions)

## **Beschrijving**
Deze repository bevat een GitHub Action die automatisch een specifieke taak uitvoert, zoals het groeten van een gebruiker of een andere procesautomatisering. Het project is opgezet om eenvoudig te integreren in CI/CD-workflows.

---

## **Inhoud**
- [Beschrijving](#beschrijving)
- [Inhoud](#inhoud)
- [Kenmerken](#kenmerken)
- [Installatie](#installatie)
- [Gebruik](#gebruik)
- [Workflowvoorbeeld](#workflowvoorbeeld)
- [Ontwikkeling](#ontwikkeling)
- [Contributie](#contributie)
- [Licentie](#licentie)

---

## **Kenmerken**
- Automatische uitvoering binnen GitHub Actions.
- Eenvoudige invoerparameters om je proces aan te passen.
- Ondersteunt versiebeheer en automatische updates.

---

## **Installatie**

Volg deze stappen om de actie te installeren en te gebruiken in je project:

### 1. Voeg de actie toe aan je workflow
In je `.github/workflows` map, maak een nieuwe workflow (bijvoorbeeld `ci-cd.yml`) en voeg de volgende configuratie toe:

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
          name: Rowan
