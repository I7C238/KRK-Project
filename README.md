Gitpod müködés:

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#snapshot/f044db47-05aa-4ae0-9801-302aea4e3f73)


# Funkciónális Specifikáció

## Áttekintés
Az alkalmazásunk lényege hogy a tic-tac-toe kedvelők számára legyen egy hely ahol megméretetthetik tudásukat a játékban.
Ez a rendszer ingyenes lesz, ezért bárki bárhonnan le tudja majd tölteni számítógépére vagy esetleg interneten keresztül beregisztrál és máris hozzájut a legfrissebb újdonságokhoz és az alkalmazásunk nyújtotta előnyökkel.
Játékosok mecs keresés alapján tudnak egymás ellenjátszani vagy mesterséges intellengecia ellen mérethetik meg erejüket.

## Jelenlegi helyzet
Szeretnénk nyújtani egy egyszerűen használható, könnyen hozzáférhető lehetőséget amatőr felhasználók számára is. Amatőr és profi bajnokságok is lennének hetente. Ezeket élő időben lehet megnézni. Gyakorlásra is lesznek lehetőségek. A XXI. században a gyors játékmenetű játékok előnyt élveznek minden téren játékos és készitő terén.

## Jelenlegi üzleti folyamatok modellje

A  mai világban ahol már majdnem mindenhol van internet könnyű elérhetést jelent ez bármilyen online tartalomhoz igy gondoltuk hogy ezzel a könnyen és gyorsan érthető játékhoz készitünk egy online felületet ahol együtt tudnak játszani a felhasználók. Mai világban elterjedt az egymás ellen "küzdés" igy ez egy nagyon jó helyzet. Illetve a gyors játékmenete miatt a felhasználók legtöbbje ezt preferálja. Tartalmat gyorsan és könnyedén lehet fejleszteni bármikor. A játékosok hamar megtalálhatják erősebb ellenfeleiket akik ellen fejlödhetnek és a kompetetiv szféra hamar kialakul.


## Igényelt üzleti folyamatok modellje
Azért hogy egyszerűbbé tegyük a felhasználók dolgát, létrehoztunk egy játékot ami a mai kornak és igényeknek könnyedén és jól hely tud állni a mai játékok szinpadán. A játékosoknak a minimalista de lényegretörő dizájnban és reszponziv kialakitásban könnyedén megtalálják mit szeretnének. A gyors játékmenet miatt nem kell órákat tölteni az alkalmazásban igy többször tud visszatérni ha ideje, kedve adódik. A kompetetiv vagy szórakozásra vágyó felhasználók is jól tudnak szórakozni.



## Használati esetek
**User**: A User eléri saját profilját, és azok profiljának publikus részét, illetve mások publikus profilját. Továbbá képes belépni a publikus chatre illetve játékmódokba. A User(ek)nek hozzá kell férniük saját profiljukhoz, amin módosítani kell tudniuk saját személyes adataikat (Név, Ország, e-mail), és meg kell tudni jelölniük azokat privátnak vagy publikusnak. Meg kell tudniuk változtatni jelszavukat biztonsági okokból.

## Követelménylista

|   Modul   | ID |  Név   |  Verzió  |
|-----------|----|--------|----------|
|Jogosultság| K1 | Bejelentkezés|1.0|
|Jogosultság|K2|Regisztráció|1.0|
|Modifikáció|K3|Felhasználó módosítása|1.0|
|Modifikáció|K4|Jelszó módosítása|1.0|
|Modifikáció|K5|Elfelejtett felhasználónév/jelszó|1.0|
|Feladattípus|K6|Játék, Chat|1.0|
|Statisztika|K7|Toplista|1.0|
|Felület|K8|Üzenetek|1.0|
|Felület|K9|Profil|1.0|

### Kifejtés    
#### ID
- K1  A felhasználó a "Bejelentkezés" gombbal be tud jelentkezni a megadott felhasználónév és jelszó párossal. Ha bármelyik mező hiányzik, vagy hibásan van kitöltve, az aktuális mező fölött piros betűkkel tudatja velünk.

- K2  A "Regisztráció gombra kattintva a felhasználó megadhatja az oldal használatához szükséges adatokat: "felhasználó" mezőbe egy egyedi felhasználónevet; "email" mezőbe a saját érvényes email címét; "jelszó" mezőbe egy egyedi kulcsszót, amit harmadik személynek semmiféleképpen nem adhatunk ki.
Ha bármelyik mező hiányzik, vagy hibásan van kitöltve, az aktuális mező fölött piros betűkkel tudatja velünk.

- K3 A felhasználó módosítani tudja saját Felhasználónevét a saját profil beállításain belül. Ehhez szükséges a régi és az új felhasználók megadása, az új megerősítése, valamint a felhasználó jelszojának megadása. 

- K4 A felhasználó módosítani tudja saját jelszavát a saját profil beállításain belül. Ehhez szükséges a régi és az új jelszojának megadása, valamint az új megerősítése.

- K5 Ha a felhasználó elfelejtette a felhasználónevét vagy jelszavát, akkor ezzel az opcióval egy Supporthoz tud fordulni email címen keresztül.

- K6 A felhasználó regisztráció után játékba kezdhet illetve chatelhet. A nem megnézett üzenetekről értesitést is kap.

- K7 Egy lista a legjobb játékosokról és pontjairól, a lista elején a legtöbb pontot elért felhasználó található illetve szűrni lehet egyéb más adatokra(nyerési esély stb..).
 
- K8 A felhasználók egymást között tudnak küldeni üzeneteket, jogosultságuktól függően.

- K9 A felhasználónak lehetősége van a profilján található bemutatkozó szöveg módosítására.

## Fogalomszótár
	- Szűrők: Csak azokat a felhasználókat adja ki a kereső mező, ami megfelel a beállított feltételeknek.

	- Profil: A felhasználó itt testre szabhatja saját profilképét. Készíthet rövid leírást magáról hogy jobban megismerjék.

	- Értesítő sáv: A felhasználót értesíti az oldal (?) sarkában lévő ikon ha valaki más üzenetet küldött neki vagy eredményt ért el.

	- Reszponzív felület: Az oldal méretei automatikusan igazodnak az aktuális eszközön.
	
	- Kompetetiv: Vetélkedő, versenyző játékos.

## Forgatókönyv
-Megnyitja a felhasználó az alkalmazást.
-Bejelentkezik vagy regisztrál, itt megadja a megfelelő adatait.
-Bejelentkezés/regisztráció után felhasználó már játékba is kezdhet vagy chattelhet a többiekkel. Illetve megnézheti mások publikus profilját, ranglistát megtekintheti.
-Ha valaki játék közben üzenet ir a felhasználónak az esetben egy felugró ablak jelzi melyre kattintva azonnal az üzenetek között találjuk magunkat. Ahonnan vissza lehet lépni a játékba.
-Jobb alul található egy beállítások gomb, amivel a saját profilunkra ugorhatunk, és módosíthatjuk saját adatainkat.

## Funkció-Követelmény megfeleltetés
- **Jogosultság:** *-regisztráció:* a szolgáltatás használatához felhasználói fiók szükséges, ennek létrehozáshoz szükség van egy regisztrációs felülethez. *-bejelentkezés:* Ahhoz, hogy a felhasználó elérhesse fiókját és a szolgáltatás által nyújtott lehetőségeket, továbbá hogy a szerver az ő, és nem más fiókjához kötött adatokat küldje át bejelenkezés szükséges.
- **Modifikáció:** *-név:* A felhasználó saját profiljába belépve képes lesz módosítani nevét. *-jelszó:* A felhasználó profilján keresztül képes lesz elérni a jelszómódosítás képernyőt, amin az eddigi jelszava megadásával képes lesz újat beállítani magának. *-elfelejtett jelszó:* A belépési képernyő része, amin képes lesz a felhasználó külső jelszóváltoztatást kérni regisztrált e-mail címére az automata rendszertől.
- **Feladattípus:** *-demó:* A felhasználó képes lesz játszani illetve chatelni másokkal illetve a főbb adatokat(statisztikákat) a központi adatbázisban fogunk tárolni.
- **Statisztika:** *-toplista:* Külön felület, amin a felhasználók láthatják az aktuális, felhasználók által pontozott ranglétrát.
- **Felület:** *-üzenet:* Chatszobák, amiken keresztül a felhasználók képesek felvenni a kapcsolatot az általuk kiválasztott felhasználótársakkal. *-profil:* A felhasználó saját felülete, ahol képes saját adatait (pl.: műfajok, hangszerek) módosítani.
