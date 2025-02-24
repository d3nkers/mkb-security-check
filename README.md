# MKB security check

## Over deze tool
Deze tool is ontwikkeld om MKB'ers meer zelfcontrole te geven over de basisbeveiliging van hun website. Zonder technische kennis kunnen gebruikers met een eenvoudige scan inzicht krijgen in mogelijke kwetsbaarheden en verbeterpunten.

## Functionaliteiten
- Controleert of een Web Application Firewall (WAF) actief is
- Analyseert HTTP-headers op veelvoorkomende beveiligingsfouten
- Voert fingerprinting uit om gebruikte technologieën te detecteren
- Geeft duidelijke aanbevelingen in begrijpelijke taal

## Installatie
1. Installeer Python 3 als dit nog niet is geïnstalleerd: [Download hier](https://www.python.org/downloads/)
2. Clone deze repository:
   ```bash
   git clone https://github.com/jouwgebruikersnaam/mkb-security-check.git
   cd mkb-security-check
   ```
3. Installeer de benodigde pakketten:
   ```bash
   pip install -r requirements.txt
   ```
4. Voer de tool uit met een website als invoer:
   ```bash
   python security_check.py example.com
   ```

## Gebruik
Deze tool controleert een opgegeven website en geeft de resultaten direct weer. Voorbeelden:
```bash
python security_check.py https://voorbeeld.nl
```
Uitvoer kan bijvoorbeeld zijn:
```
Domein: voorbeeld.nl
✅ WAF gevonden: Cloudflare
🔎 CMS gedetecteerd: WordPress
🔐 SSL/TLS-configuratie: OK
⚠️ Headers missen: X-Frame-Options, Content-Security-Policy
```

## Optionele Docker-installatie
Voor gebruikers die geen Python willen installeren, is een Docker-versie beschikbaar:
```bash
docker build -t mkb-security-check .
docker run mkb-security-check voorbeeld.nl
```

