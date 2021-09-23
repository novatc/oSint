#### Auslesen des Registrant

+ whois meine-domain.de
    
    
+ dig @8.8.8.8 www.meine-domain.de AAA
    + liefert die IP-Adresse
    
+ whois + IP-Adresse liefert viel mehr Infos
+ https://www.whatsmydns.net

+ python3 SubDomainizer.py -u http://www.example.com
    + liefert gefundene Subdomains zur gegebenen Domain

###Webserver und Sicherheit
+ nslookup -type=mx meine-domain.de  
    + liefert Infos über zugeordnete Server + Webserver
    
+ wafw00f -a https://meine-domain.de 
    + Gibt Informationen über die eingesetzte Firewall
  
+ python metagoofil.py -d meinedomain.com -t doc,pdf -l 200 -n 50 -o applefiles -f meinedomain.html

### Webseiten Metainformationen

+ metasploitable -> use search_email_collector -> set DOMAIN meine-domain.de -> run

+ recon-ng -> workspaces create ... -> modules load ...
  
        +hackertarget: liefert verschiedene Hostsysteme für eine Domain
        + hunter_io: liefert  Emails
+ cewl -d 2 -m 5 -w output.txt https://www.meine-domain.de 
    + liefert Passwortlisten basierend auf der Domain
  
+ python3 Ashok.py -h
    + liefert viele nützliche Informationen zu einer Domain
  
+ python metagoofil.py -d meine-domain.com -t doc,pdf -l 200 -n 50 -o output -f result.html
    + Liefert Metainfos über Nutzer, Mails und Software basierend auf den Dateien der Seite

### 

### Subdomain
+ SubDomainizer -> python3 SubDomainizer.py -u http://meine-domain.de
