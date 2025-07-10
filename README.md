# MKB Security Check Tool

## Over dit project
Veel kleine en middelgrote bedrijven (MKB) hebben beperkte middelen en kennis om hun websites goed te beveiligen tegen cyberdreigingen. Hackers maken hier gebruik van, waardoor kwetsbare websites vaak een doelwit worden. Dit project is ontwikkeld om MKB'ers een eenvoudige en toegankelijke manier te bieden om hun website snel op een aantal kritische beveiligingspunten te controleren.

De tool is geen vervanging voor een uitgebreide vulnerability scan of pentest, maar helpt ondernemers een eerste stap te zetten naar een betere beveiliging van hun online aanwezigheid.

## Functionaliteiten
- ✅ Controleert of HTTPS correct is geconfigureerd.
- ✅ Checkt op ontbrekende security headers zoals `Content-Security-Policy`.
- ✅ Detecteert of een Web Application Firewall (WAF) actief is.
- ✅ Herkent bekende CMS’en zoals WordPress, Joomla, Magento en Drupal.
- ✅ Controleert of directory listing per ongeluk is ingeschakeld.
- ✅ Genereert een HTML of JSON-rapport voor snelle analyse.

## Installatie
1. **Zorg dat Python 3 is geïnstalleerd**: [Download hier](https://www.python.org/downloads/)
2. **Clone de repository**:
   ```bash
   git clone https://github.com/d3nkers/mkb-security-check.git
   cd mkb-security-check
   ```
3. **Installeer de benodigde afhankelijkheden**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Start de tool met een URL als invoer**:
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
Missende security headers: X-Frame-Options, Content-Security-Policy
WAF detectie: Server: Apache
CMS detectie: WordPress
Directory listing: Geen directory listing gevonden.
✅ Rapport succesvol opgeslagen als: security_report_voorbeeld_nl.html
```
Het rapport wordt opgeslagen in het opgegeven formaat (`json` of `html`).

## Toekomstige verbeteringen
Toevoegen van een automatische update-check voor de tool.  
Detectie van verouderde softwareversies en zwakke configuraties.  
Meer gedetailleerde risicoanalyse en aanbevelingen per bevinding.  
Mogelijkheid om meerdere websites tegelijk te scannen.


## Licentie
Copyright (c) 2025 D3nkers Solutions - [https://d3nkers-solutions.nl](https://d3nkers-solutions.nl)  
Dit project valt onder de MIT-licentie.

