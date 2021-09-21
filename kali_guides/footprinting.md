#### Auslesen des Registrant

+ whois meine-domain.de
    
    
+ dig @8.8.8.8 www.meine-domain.de AAA
    + liefert die IP-Adresse
    
+ whois + IP-Adresse liefert viel mehr Infos

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

### 
