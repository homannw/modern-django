WBF    README.txt
---------------------

## evtl mal ansehen  zum tieferen Debuggen ...
https://mutelight.org/minimal-guide-to-debugging-php-with-xdebug-and-vim



### git  ...
git   Handling

Es liegt ein Bare Repository  unter  /srv/git   ,  dies ist das HOME vom User git

Das Repo heisst   wbf.git

Potentielle Nutzer muessen mit ihrem  ssh  Key  in   /srv/git/.ssh/authorized_keys  eingetragen
sein, und  koennen dann 

Sich ein REPO mit Arbeitsverzeichnis  CLONEN

 git  clone  git@localhost:wbf.git   <Arbeitsverzeichnis>
 
Dies wird dabei automatisch angelegt und der aktuelle HEAD   aus dem REPO uebenommen.

Nach Abschluss der Aenderungen :

After making changes, the developer saves changes locally:
$ git commit -a

Abgleich mit dem zentralen WBF  Repo erfolgt dann durch 

To update to the latest version:
$ git pull
Any merge conflicts should be resolved then committed:
$ git commit -a
To check in local changes into the central repository:
$ git push
If the main server has new changes due to activity by other developers, the push fails, and the developer
should pull the latest version, resolve any merge conflicts, then try again.


Test  mit Apache  :

su - www-data
cd WBF/test_rs       ! fuer Roland
cd WBF/test_wh       ! fuer Walter

--- Erstes anlegen  ...

165$ sudo su - www-data
$ ls
index.html  supporter  WBF
$ cd WBF
git clone  <username>@localhost:~/<Verzeichnispfadquelle>  <Verzeichnispfadtest>
...

Anschliessend notwendige Aenderungen damit es in der Testumgebung laufen kann  ..

../get_test_modifications.sh

Falls ein neuer bisher nicht genannter Pfad unterhalb WBF  benutzt wird,  
muss  /etc/apache2/conf.d/wbf    angepasst werden

--- Aenderungen in Testumgebung holen , per git    ...

doe02lx - homannw - /auto/people/doe10/homannw/pj/php - (-ksh)
165$ sudo su - www-data
$ ls
index.html  supporter  WBF
$ cd WBF/test_wh
$ git pull
Could not create directory '/var/www/.ssh'.
The authenticity of host 'localhost (127.0.0.1)' can't be established.
ECDSA key fingerprint is 8b:52:91:71:2b:52:83:3e:9e:53:3e:76:c9:ab:af:45.
Are you sure you want to continue connecting (yes/no)? yes
Failed to add the host to the list of known hosts (/var/www/.ssh/known_hosts).
homannw@localhost's password:
Permission denied, please try again.
homannw@localhost's password:
Already up-to-date.  ---  nur wenn noch nichts veraendert wurde...





 