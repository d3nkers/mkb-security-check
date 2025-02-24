# MKB Security Check Tool

## Over dit project
Veel kleine en middelgrote bedrijven (MKB) hebben onvoldoende middelen en kennis om hun websites goed te beveiligen tegen cyberdreigingen. Dit project helpt ondernemers om eenvoudig een basisbeveiligingscheck op hun website uit te voeren. De tool is ontwikkeld door d3nkers solutions en biedt een snelle manier om kritische beveiligingsfouten op te sporen en te begrijpen.

## Functionaliteiten
✅ Controleert of HTTPS correct is geconfigureerd.  
✅ Detecteert ontbrekende security headers zoals `X-Frame-Options` en `Content-Security-Policy`.  
✅ Detecteert of een Web Application Firewall (WAF) actief is.  
✅ Controleert op bekende CMS-platformen zoals WordPress, Joomla, Drupal en Magento.  
✅ Controleert of directory listing is ingeschakeld.  
✅ Genereert een rapport in JSON of HTML voor eenvoudige analyse.

## Installatie
1. **Installeer Python 3** indien nodig: [Download hier](https://www.python.org/downloads/)  
2. **Clone deze repository**:
   ```bash
   git clone https://github.com/d3nkers/mkb-security-check.git
   cd mkb-security-check
   ```
3. **Installeer de benodigde pakketten**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Voer de tool uit met een website als invoer**:
   ```bash
   python security-check.py mijnwebsite.nl
   ```

## Gebruik
Deze tool scant een opgegeven website en toont de resultaten direct in de terminal.  
Voorbeeld:
```bash
python security-check.py https://voorbeeld.nl --output html
```
Uitvoer in de terminal:
```
Scanning: https://voorbeeld.nl
HTTPS: Website gebruikt HTTPS.
Missende Security Headers: X-Frame-Options, Content-Security-Policy
WAF Detectie: Server: Apache
CMS Detectie: WordPress
Directory Listing: Geen directory listing gevonden.
✅ Rapport succesvol opgeslagen als: security_report_voorbeeld_nl.html
```
Het rapport wordt opgeslagen in het opgegeven formaat (`json` of `html`).

## Toekomstige verbeteringen
* Toevoegen van een automatische update-check voor de tool.  
* Detectie van verouderde softwareversies en zwakke configuraties.  
* Meer gedetailleerde risicoanalyse en aanbevelingen per bevinding.

## Licentie
Copyright (c) 2025 d3nkers solutions - [https://d3nkers-solutions.nl](https://d3nkers-solutions.nl)  
Dit project valt onder de MIT-licentie.

