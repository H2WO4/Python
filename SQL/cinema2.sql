SQLite format 3   @    	   B                                                           	 -�   �    D� ���                                                                                            �]''�ytabledistributionsdistributionsCREATE TABLE distributions (idfilm integer NOT NULL REFERENCES films(id), idacteur integer NOT NULL REFERENCES acteurs(id), rang integer default NULL,  PRIMARY KEY (idfilm,idacteur))9M' indexsqlite_autoindex_distributions_1distributions   ��utablefilmsfilmsCREATE TABLE films (id integer NOT NULL, titre varchar(70) default NULL, annee decimal(4,0) default NULL,score float default NULL, nbvotant integer default NULL, idrealisateur integer default NULL REFERENCES realisateurs(id), PRIMARY KEY  (id))�%%�MtablerealisateursrealisateursCREATE TABLE realisateurs (id integer NOT NULL, nom varchar(35) default NULL, PRIMARY KEY  (id))u�AtableacteursacteursCREATE TABLE acteurs (id integer NOT NULL, nom varchar(35) default NULL, PRIMARY KEY    C   �    �������������������                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               �   �^   �q   �   �q   �+   �:   �   �/   �j   �   �x   �    �   �X   
�o   	�   �c   �1   �    ��                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       �   �g   �    $������                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         #�R   "�   !�F    �D   {   $   �    B��������������                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        ?�*   =�a   ;�   :�N   7�   5�:   3�o   1�$   /�Y   .�   +�C   )�w   &�+   %\    @c��S�%E�4�p��                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 2
 ��!   0
 ���   8
����   4�vT   ,	FyP�   '
L=   A
�0��             9
���   *	)" �   ( �w   6	
 �f   -	y��       	        >
 	��   <
y
@�   2 s �������ziYF-�������n\K9*�������q_R@0
 � � � � � � � s       �1 'Ralph Fiennes�* !John Wayne�' -Donald Pleasence�% +Charlton Heston�$ %Gregory Peck�  'Max von Sydow� 'Billy Crystal� #Joan Cusack� +Charles Chaplin� #Bill Paxton #Jack Warden} 'Dennis Hopper{ Frank Ozv 'James Stewarts 'Peter Sellersj #Jack Lemmond #Liam Neesonc 1Christopher Walken^ %Diane Keaton[ )Morgan FreemanZ )Roman PolanskiY /Samuel L. JacksonU 'Marlon BrandoL %Kevin SpaceyK !Cary GrantI 'Harvey Keitel? %Meryl Streep; 'Terry Gilliam6 -Sigourney Weaver2 /Matthew Broderick, 'Robert Duvall+ )Jack Nicholson* #Paul Newman) /Denzel Washington' +Anthony Hopkins$ )Robert Redford" 'John Travolta  #John Cusack 5Francis Ford Coppola )Dustin Hoffman #Tim Robbins %Danny DeVito %Gene Hackman %Bruce Willis Al Pacino Tom Hanks 'Harrison Ford )Robert De Niro )Clint Eastwood #Woody Allen   0 i ������|jZJ7"�������ygXI6$�������p^K9! � � � � � � z i �c #Ving Rhames�b +Charles Durning�` /Christopher Guest�\ +Giovanni Ribisi�Y #Henry Fonda�V %Claire Danes�T -Shirley MacLaine�P 5J&#252;rgen Prochnow�M 'Minnie Driver�K 1Laurence Fishburne�I %Ben Kingsley�D 'Russell Crowe�> %Tom Sizemore�8 #John Huston�4 'Gabriel Byrne�3 #Bonnie Hunt�2 %Martin Sheen�0 -Malcolm McDowell�. -Benicio Del Toro�- #Peter Boyle�* 1Billy Bob Thornton�' 1Harry Dean Stanton� %Cameron Diaz� 'Steve McQueen� Joe Pesci� Brad Pitt�} %Orson Welles�| +Lance Henriksen�z !James Caan�y )Annette Bening�w 'Albert Brooks�v !Dan Hedaya�t )Michael Madsen�s #Uma Thurman�o Ian Holm�k 5Richard Attenborough�b +William H. Macy�a 'Anne Bancroft�^ !Cary Elwes�Y !J.T. Walsh�W %Jodie Foster�U +Humphrey Bogart�S +Gwyneth Paltrow�C #John Cleese�: 'Steve Buscemi�7 )William Holden�6 %Faye Dunaway�5 !Matt Damon   . n ������zhWD-	������u^K3 �������taL5 � � � � � � � n          � 1Stephen Tobolowsky� 3Christopher Plummer� 'Martin Landau� #Brion James�  )Matthew Modine�} %Simon Callow�{ !Bob Gunton�w )John Malkovich�v #Talia Shire�p /Catherine Deneuve�o /Frances McDormand�n +Cloris Leachman�m 'Michael Biehn�i )Don Taylor [I]�e -Edward Burns [I]�b %R. Lee Ermey�a #Oliver Reed�_ +George C. Scott�\ )George Kennedy�Z %Natalie Wood�X %James Coburn�O %Sissy Spacek�N 'Carrie Fisher�L 1Giancarlo Esposito�E 'Martin Balsam�A /Vincent D'Onofrio�< /Quentin Tarantino�; 9Philip Seymour Hoffman�: +Joaquin Phoenix�9 -Chazz Palminteri�7 'Jeffrey Jones�6 John Hurt�5 )M. Emmet Walsh�4 !Carol Kane�/ )James Cromwell�- /Katharine Hepburn�+ 'Edward Norton�! #David Morse� %Kirk Douglas�	 %Yun-Fat Chow�u 'Lloyd Bridges�r -Laurence Olivier�p -Rosanna Arquette�h %George Lucas�e #Bruno Kirby�d %Tom Skerritt   0 l ������tbQ@/ �������p\C/�������yjP>) � � � � � � � } l    �o #Rod Steiger�m Eric Idle�k #Scott Glenn�i Udo Kier�g Rip Torn�` )Embeth Davidtz�_ 3Toshir&#244; Mifune�[ 3William Daniels [I]�X -Chris Cooper [I]�U )Eileen Brennan�R +Ernest Borgnine�O %Warren Oates�L 5Helena Bonham Carter�I Brian Cox�G +Murray Hamilton�F !Chris Penn�> #Eric Stoltz�: +Keith David [I]�6 #Terry Jones�5 #John Milius�0 +Takashi Shimura�/ #John Ritter�, Tim Allen�* )Melinda Dillon�( )Chris Sarandon� 3Veronica Cartwright�z )Graham Chapman�u )George Dzundza�r !Gene Kelly�q %Peter Sallis�R -Beverly D'Angelo�O %Daryl Hannah�K )Mike Starr [I]�B 'Toni Collette�0 /Philip Baker Hall�. )Shelley Duvall�+ Teri Garr�* #Hume Cronyn�( #Mark Hamill�& #Ben Gazzara�% %Gina Gershon�" -James Earl Jones� )Lindsay Crouse� -Elizabeth Taylor� %Robin Wright� 'Lauren Bacall� %Kevin Pollak� +Denholm Elliott   0 i �������m_K8'�������s^L8 �������q^M<+ � � � � � � } i �X )William Sadler�U %Groucho Marx�I #Thora Birch�D /F. Murray Abraham�C )Allen Garfield�3 'Elliott Gould�2 -Gillian Anderson�/ 'Anthony Quinn�- )Robert Mitchum�* !Kim Hunter�) #John Cazale�% #Karen Allen�" #John Savage� 'Alec Guinness� )Marilyn Monroe� #Joe Grifasi� +Strother Martin� ;Gunnar Bj&#246;rnstrand�} %James Garner�| 'Teresa Wright�{ Tom Hulce�w Ed O'Ross�q +Peter Gallagher�^ 1Pete Postlethwaite�Q )Amanda Plummer�M %Robert Stack�G +Bernard Lee [I]�E )John Carradine�A %Colleen Camp�? )Edward Furlong�< #Bette Davis�; )Ingrid Bergman�4 +Roberto Benigni�/ -Luis Bu&#241;uel�+ -Ir&#232;ne Jacob�% )Richard Burton�" #James Mason� 'Michael Palin� )Jean-Marc Barr� Tim Roth� 'Joseph Cotten� !Ray Liotta� +Rade Serbedzija� %Fairuza Balk�{ +Louise Fletcher�z !Debi Mazar�u #Ray Walston�p 'Dennis Farina   / w ������oVD3!�������wgQ?.�������q]H4# � � � � � � w                 � -Tony Roberts [I]�
 +Henry Jones [I]� )Andre Braugher�| Ward Bond�r %Yaphet Kotto�i %George Segal�g 1Graham Greene [II]�d %Piper Laurie�b !Vin Diesel�a #Tony Burton�` )Connie Nielsen�[ +Stephen Baldwin�Z )Jeffrey DeMunn�W 'James Hampton�R )Michael Gambon�Q )Cliff De Young�P %Kasi Lemmons�O 'Ralph Bellamy�N 'E.G. Marshall�F 'Wallace Shawn�E !Peter Falk�A )Everett McGill�? 'Jason Lee [I]�7 #Anna Paquin�2 %Clancy Brown�. -Frederic Forrest�+ !Ted Danson�# /Patricia Clarkson�  #Robert Shaw� -Charles Laughton� #Annie Potts� %Diane Venora� )Kelsey Grammer�
 #Don Rickles�| )Bibi Andersson�y !Sean Young�h %Claude Rains�T #Clark Gable�L %Rutger Hauer�5 3Thomas Mitchell [I]�  )George Sanders� )Fred MacMurray� %Paul Sorvino� #Grace Kelly�  1Pen&#233;lope Cruz�m 1Edward James Olmos�Z -Caroline Goodall   0 p ������xfUD0	�������t_K1 �������wgXC0 � � � � � � � p        �  )Walter Brennan�w )Farley Granger�v 'Warren Clarke�t %Vivien Leigh�e #Jean Arthur�X 1John Williams [II]�S %Ruth Warrick�P )Maureen O'Hara�D #Sihung Lung�@ 'Michelle Yeoh�? 'Sofia Coppola�; +Charles Bronson�8 Myrna Loy�5 !Danny Kaye�2 #Roy Dotrice�- +Sterling Hayden�* !James Hong�) %Jack Hawkins�# 'Julie Walters�" #Karl Malden� -Rosalind Russell� 'Trevor Howard� )Marco Leonardi� #Keir Dullea� 5Elizabeth Wilson [I]� )Katharine Ross� +Olivia Williams�~ )Otto Preminger�z )Mary Kay Place�t #Tony Darrow�n /Claudia Cardinale�a %Wallace Ford�` %Billy Crudup�Z Ed Binns�I 'Jason Robards�G 'Lee Van Cleef�B )Jack MacGowran�@ )Joanna Cassidy�> #James Cosmo�8 #Porter Hall�5 %Kenneth Mars�1 #Paul Bartel�+ )Cathy Moriarty�* )Leo G. Carroll�" -Patrick McGoohan�! )Peter Stormare� %Bruce McGill� 'Michael Jeter   / f ������xbN:(�������m[F2������n]H0 � � � � � � � w f�x #Victor Argo�u Joel Grey�n #Keenan Wynn�l 1Anatoli Solonitsyn�f Lew Ayres�b !Colm Feore�V %Slim Pickens�T %Wayne Knight�O )Pupella Maggio�N %Harry Morgan�H 1Christine Ebersole�? 1Billy Dee Williams�> +Ben Johnson [I]�= #Stacy Keach�8 /Michael Bates [I]�5 #Janet Leigh�3 7Michael Clarke Duncan�- +Cybill Shepherd�( )Darren McGavin�" +Tatsuya Nakadai� 1Edward G. Robinson� -John Rhys-Davies� +Elsa Lanchester�| )James Whitmore�w +Anthony Daniels�u %Barry Pepper�s +Judith Anderson�h 'Paul Giamatti�W +Albert Hall [I]�S Lena Olin�O +Lorraine Bracco�7 %Sam Rockwell�2 !Jeff Corey�. 'G.D. Spradlin�+ %Ronald Lacey�( 'Anthony Heald�& %Derek Jacobi�" )Frankie Faison� )Allison Janney� -Peter Graves [I]� 'Kenneth Tsang� %Glynis Johns� 1Richard Farnsworth�
 +Angela Lansbury�	 #Lee J. Cobb� #Akira Terao� )William Powell   . l ������xdR;'������zjV@.
������~bI4	 � � � � � � � l        � 1Erich von Stroheim� /Kamatari Fujiwara
� Arletty�r 'Henry Bergman�n 3Fernanda Montenegro�\ 'Henry Travers�Y #Errol Flynn�S #Anne Baxter�P -Barry Fitzgerald�L +Miki Manojlovic�E +Robert J. Wilke�A 3Jessie Royce Landis�9 9Jean-Pierre L&#233;aud�8 -Erland Josephson�. )Djimon Hounsou�) /Nicoletta Braschi�! %Ethan Suplee� 'Jeremy Davies� 'Minoru Chiaki� 'Sean McGinley� #Paul Reiser�y 'Adam Goldberg�u %Barry Dennen�r -Cecil B. DeMille�m )Leslie Carlson�g !Ted Levine�Y !Abe Vigoda�L Suzy Amis�H Mel Smith�D /Billy Gilbert [I]�7 )John Hillerman�5 /Robert Webber [I]�+ /Patrick Magee [I]�' %Adam Baldwin�# )Laurie Metcalf�  )William Windom� /Frank Vincent [I]� %David Proval� )Richard Harris� %Mark Rolston� 'Zeljko Ivanek�
 %Zach Grenier�	 /Jenette Goldstein� +Stefan Gierasch�  !Jack Kehoe�} +Mildred Natwick   , y ������rbO6%�������jW9%������}jXC* � � � � � � y                         �j ?Victor Sj&#246;str&#246;m�f )Nikolai Grinko�I -Vincent Gardenia�? #Sam Bottoms�6 3Olivia de Havilland�4 'Boris Karloff�+ +Debbie Reynolds�! -James Donald [I]� 3James Robinson [II]�p +Dorian Harewood�l %Judy Garland�\ 'Jack Kruschen�Y +Jack Carson [I]�M !Bj&#246;rk� 'Jennifer Lien� !Chico Marx� 'Joan Fontaine� 1Cindy Williams [I]�	 'Claire Trevor�\ !Jean Gabin�F %Cecilia Roth�> )Carole Lombard�5 =Alexandra Dahlstr&#246;m�3 'Fredric March�1 /Haley Joel Osment�" #Gustav Botz� /Gabriele Ferzetti� )Fred Clark [I]� )Basil Rathbone� 1Kristina Adolphson�} !Harpo Marx�{ 'Frank Overton�o 3Gr&#233;goire Colin�c #Gary Cooper�_ 3&#201;lodie Bouchez�] 'Gladys Cooper�K !Lee Remick�A %Alastair Sim�8 +Gaspard Manesse�4 'Gene Lockhart�% -Bajram Severdzan�# -Antonella Attili�! #Eli Wallach� /Hermione Baddeley   . s ������r]L:"������|dO<'������m]J4 � � � � � � � s               �/ )Siobhan Fallon�* 'Clifton James�% /David Andrews [I]� -Leopoldo Trieste� -John Fiedler [I]�	 #Mena Suvari� #Sheb Wooley� !Diane Ladd�~ John Finn�} -Catherine Keener�{ -Leonard Rossiter�y 'Alfred Molina�x !Bo Hopkins�w %Ewen Bremner�h !Buck Henry�c -Philip Stone [I]�_ )Jay O. Sanders�Y %Brock Peters�T !Amy Wright�N -Scatman Crothers�K )Richard Bright�C Ian Wolfe�B 'Jason Flemyng�A +Kenny Baker [I]�8 'Walter Gotell� +Shelley Winters� 1Raymond Massey [I]� +Pierre Batcheff�| )Luigi Pistilli�p /Y&#244;ji Matsuda�h #Peter Lorre�U -Magali No&#235;l�< /Robert Morley [I]�( %Tyrone Power�$ -Montgomery Clift�# 1Maureen O'Sullivan�p %Mieko Harada�f #Tony Curtis�Z +Tsutomu Tatsumi�Y #Tom Helmore�X 3Michael Constantine�K !Vera Miles�@ +Michael Hordern�, #Marion Mack� -Paul Freeman [I]�y 1Robert Strauss [I]   , p ������nXF6#�������n^H4������nI2 � � � � � � � p                � !Jean Hagen� +Carol Cleveland� +Hattie McDaniel�~ -Srdjan Todorovic�v %Raymond Burr�m #Nigel Bruce�j /Peter Mayhew [II]�g 'Finlay Currie�e #Perry Lopez�] )Theodore Bikel�Y /James Gleason [I]"�U KStanislas Carr&#233; de Malberg"�Q KFernando Fern&#225;n G&#243;mez�M %Scott Bakula�E Sig Ruman�B /Stephen Young [I]�A -Paulette Goddard�< -Richard Basehart�7 +Howard St. John�6 %Ralph Meeker�4 -Charley Grapewin�3 )Ralph Carlsson�0 -Hoagy Carmichael�/ !Jim Varney�' %Paul Henreid�& /Hugh Griffith [I]�# %Hugh Marlowe� )Patric Knowles� -Lucas Black [II]�~ 3Spencer Treat Clark�y !Alan North�s #Dylan Bruno�f -Gary Lewis [III]�_ 'Henry Daniell�W !L.Q. Jones�L %Harold Gould�J -Peter Greene [I]�I )Harve Presnell�> /John Ratzenberger�= -Arthur O'Connell�< )Janet Margolin�; Meat Loaf�7 %Evelyn Keyes�6 9Philippe Morier-Genoud   / p ������vbM8%�������q`I4"�������mZF. � � � � � � � p          �: %Henry Victor�7 %Les Tremayne�3 )Mandy Patinkin�- )Dimitra Arliss�, /Robert Beatty [I]�* 1David Hemmings [I]� !Dub Taylor�y 'Paul Calderon�n #Alida Valli�j Eve Arden�d 1Tommy Flanagan [I]�a )Sophie Marceau�^ 'Reg E. Cathey�[ %Peter Brocco�Y !Edie Adams�U 3Michael Higgins [I]�K 'Lynne Thigpen�E Rudy Bond�> #John Qualen�3 !Joe Turkel�1 'Dwight Yoakam�, !Kirk Baltz�* )Dorothy Malone�( %Roscoe Karns�& +Margaret Dumont�" /Maria de Medeiros� #Rita Moreno� 'Louis Calhern� 'Lee Strasberg� #Kate Hudson�~ +Donald O'Connor�p -Michael Angarano�k )Tracy Reed [I]�e -Barry Nelson [I]�b 'Arliss Howard�P +Andy Devine [I]�I 'Sam Jaffe [I]�D +Ruth White [II]�= +Anthony Higgins�< )Josephine Hull�5 +David Schofield�/ -Marlene Dietrich�, )Peter Bull [I]�+ !Dana Elcar�% -Randy Brooks [I]�" 'Peter Cushing�! %Moroni Olsen   / w ������gQ6!
�������weN=( ������~hT=( � � � � � � � w                 �+ %Sandy Dennis� #Coleen Gray� %Connie Booth� 'Daniel Zacapa� )Scott Schwartz� %Conrad Veidt� %Vinnie Jones� Tim Holt�~ 'Brent Briscoe�s !John Clive�m +Richard Davalos�a /Fortunio Bonanova�U )Marisa Paredes�T -Michael Berryman�R %James Sloyan�P 'Edward Brophy�> 'Minna Gombell�7 %John Ridgely�1 'Thelma Ritter�, %Jens Albinus�& 'Mischa Barton� +Elisha Cook Jr.� 'John Shrapnel� +Victor Jory [I]� #Norman Fell� /Sean Sullivan [I]� %Cara Seymour�{ %David Prowse�y !Orson Bean�q #Sam Robards�a +Macdonald Carey�] !Don Keefer�P +Chester Conklin�G +Ernest Thesiger�> #Leib Lensky�5 /Larry Brandenburg�# +Ray Collins [I]� 7Daisuke Kat&#244; [I]� -Lewis Martin [I]�w 1Wilfrid Hyde-White�l #Robert Ryan�i +George Macready�` #George Raft�M )Horst Buchholz�J )Estelle Harris�G Curt Bois�C 'Jihmi Kennedy   , n ������o]H7'������wdE6 ������}hP<* � � � � � � � n              �q /William Sylvester�o -Albert R&#233;my�j +Akemi Yamaguchi�i %Akihiro Miwa�g 'Akim Tamiroff�d Alan Hale�c -Y&#251;ko Tanaka�^ /Yoshiko Shinohara�\ 3B&#246;rje Ahlstedt�V %Avery Brooks�R )Valerie Hobson�N 1Barbara Bel Geddes�K +Ayano Shiraishi�I 3Andrew Kevin Walker�? #Arnold Lucy�: +Armando Brancia�- %Bengt Ekerot�% -Barbara Stanwyck� )Barton MacLane�} 'Virginia Mayo�r +Victor McLaglen�i -Antonia San Juan�\ Anne Reid�T ?Vin&#237;cius de Oliveira�7 'Sally Yeh [I]�6 1Salvador Dal&#237;�$ 1Daniel Richter [I]�  7Seizabur&#244; Kawazu� #Sean Lawlor� +Rosemary Murphy� #Daisuke Ryu� +Sessue Hayakawa� 3Sergio Bini Bustric� !Ruth Roman�~ #Ruth Hussey�t +Seiji Miyaguchi�p %Dana Andrews�Q 'Danny Lee [I]�L /Sandy Nelson [II]�J #Colin Clive�F #Danny Lloyd�C -Colleen Dewhurst�> 5Collin Wilcox Paxton�: +Samuel Le Bihan   / t ������~gQ>+������ydRA( ������w^P>,
 � � � � � � � t              � %Joan Shawlee� !Jo Prestia�  %Jo Van Fleet�y 'Jinpachi Nezu�r 'Bruce Bennett�H #Carrie Henn�7 /Candela Pe&#241;a�. )Tom Murray [I]� Bert Lahr� 'Tiny Sandford� %Beulah Bondi� %Branka Katic�b Chu Kong�L 3Stefan H&#246;rberg�A )Simone Mareuil�? 'Cliff Edwards�8 -Ciccio Ingrassia�3 -Slim Summerville�1 'Clarence Kolb�/ )Claire Maurier�, Soia Lira�( -Cecil Parker [I]�% %Celeste Holm�
 3Cathy O'Donnell [I]�  #Charles Kay�x %Stephen Boyd�t +Charles Ruggles�s /Charles Smith [V]�o !Chen Chang�d #Wes Bentley�c /Alexander Granach�U -Aldo Silvani [I]�P -William Redfield�E %William Hope�; #Allan Jones�6 )Walter Catlett�2 'Walter Huston�$ 'Wendell Corey�# -Wayne Morris [I]�" /Aldo Giuffr&#232;� )Adolphe Menjou� 'Yuriko Ishida� +Agnes Moorehead� %Yoshio Inaba� !Zhang Ziyi�	 !Zeppo Marx�z )Wolfgang Heinz   - s ������zhS>,	�������lUA+������rYC- � � � � � � s                 �q -Madeleine LeBeau�k 'John Wray [I]�f 9Mar&#237;lia P&#234;ra�] +Kevin P. Farley�X !Mack Swain�U %Kumeko Urabe�R +Ky&#244;ko Seki�? )Kitty Carlisle�< +Klaus Wennemann�; -Machiko Ky&#244;�7 -Kristian Almgren�6 3Kristin Rudr&#252;d�. %Jean Heather�- %Jean Heywood�, 5Natacha R&#233;gnier�% #Nando Orfei�$ #Nancy Olson�# 3Jean-Louis Barrault�" 9Jean-Louis Trintignant� 'Nat Pendleton� #Ned Bellamy� -Natalie Canerday� )Jeffrey Hunter�s /Jean-Pierre Lorit�d +Myron McCormick�V %Nobuo Kaneko�Q !Nils Poppe�O %Othon Bastos�E -Nikolai Sergeyev�6 9Nicholas Colasanto [I]�4 %Jane Darwell� !Jamie Bell� %Jamie Draven� #John Farley� %John Gottowt� +John Howard [I]� +Melville Cooper� %Mervyn Johns�  -Millard Mitchell�l %John Ireland�a )John Terry [I]�L !John Megna�6 )Jim Farley [I]�1 -Mathias Rust [I]� !Joanne Dru   + v ������s^K9&������ydL5 ������s^H1	 � � � � � � v                        �^ +Georges Flamant�R %Georgia Hale�F !Ray Bolger�@ 1Raphael Fejt&#246;�4 7Richard S. Castellano�1 )Felix Bressart�! +Eugene Pallette� +Eva Marie Saint� 'Evelyn Varden� /Richmond Arquette� -Francis De Wolff�
 +Florijan Ajdini� -Frank Morgan [I]�z AFr&#233;d&#233;rique Feder�w -Francine Racette�g +Kaoru Kobayashi�^ 'Karl Etlinger�Q )Julien Carette�K )Jullan Kindahl�9 #Katy Jurado�5 +Marcella Rovere�+ /Kathleen Harrison�( 1Maria Casar&#232;s� +Zooey Deschanel� +Jonathan Sagall� )Joseph Calleia� 1Martin Semmelrogge� /Masayuki Mori [I]�] )Martha Vickers�N 1Lawrence A. Bonney�L 1Lawrence T. Wrentz�H #Lou Antonio�* 'Louis Wolheim� %Lillian Gish� 'Lionel Atwill� +Ljubica Adzovic� %Leo Gullotta� 3Leonard Harris [II]� 'Leslie Howard�
 7Leopoldine Konstantin�  Kim Novak�y %Madison Lanc�u 'Makoto Kobori   , p ������nZC4������z_L4	�����}jVA* � � � � � � � p                � !Jack Oakie�  )Jackie Gleason�z /Patricia Collinge�w %Ivan Lapikov�r )Jack Haley [I]�o #J.D. Cannon�n !Jack Benny�k #Jack Creley�j Jack Elam�h 1Patricia Hitchcock�X /Rebecka Liljeberg�R +Harry Carey Jr.�I )Harvey Lembeck�F 'Haya Harareet�E +Pernilla August�D +Pernilla Allwin�B /Peter Billingsley�4 1Paul H&#246;rbiger�2 -Hubertus Bengsch�* ;Herbert Gr&#246;nemeyer�) )Paul Simon [I]�$ /Harriet Andersson� 1Elizabeth Berridge� 'Robert Drivas� 7Edward Everett Horton� -Eijir&#244; Tono�} +Eleanor Coppola�r )Eric Weinstein�q 1Erica Carlson [II]�V )Enzo Cannavale�H 'Edward Arnold�A +Donnie Wahlberg�; !Dita Parlo�( /Robert Walker [I]�% Ed Begley�" /Dorothy Comingore� )Edmond O'Brien� %Douglas Rain� 'Dorris Bowdon� /Reginald Gardiner�u 'Gary Lockwood�t %Gary Merrill�o 5Richard Anderson [I]�n /Richard Allen [I]   - � �������pZC.�������n\H3!�������s^H5 � � � � � �                                                             �8 )Ken Curtis [I]�0 +Manning Redwood�. %Regis Toomey�$ #H.B. Warner� Paul Fix�{ 'Joyce Jameson�j %Frank Sivero�g /Andr&#233; Morell�f 'Henry Brandon�e -Darrell Zwerling�R +Godfrey Quigley�P %Una O'Connor�E +Octavia Spencer�5 !Eddra Gale�3 /Benito Stefanelli�( 'Edward Bunker�' %George Furth� +James Keane [I]� #Jack Purvis� +Norbert Weisser� %Shane Rimmer� +Jude Ciccolella� )Jack Walsh [I]�
 %Frank Adonis� -William Hootkins�_ )Priscilla Lane�V )Pierre Fresnay�U !Guy Kibbee�S 'Glen Cavender�R )Gloria Swanson�N 'Pierre Renoir�M %Guy Decomble�I #Philip Ober�D +Pierre Brasseur�< +Giustino Durano�5 /Giuliana Lojodice�4 -Giulietta Masina�3 +Patrick Mercado�& !Irma Raush�% #Isa Danieli�$ 'Patrick Fugit�! 'Ingrid Thulin� %Ian Petrella� #Pat O'Brien�	 #Pat Henning   / u ������~lXG6"��������lZH;&������x^H- � � � � � � u               �g )Lars von Trier�C -Bob Clark  (III)�< Nick Park�y 9Fran&#231;ois Truffaut�< /Quentin Tarantino�, 'Stanley Donen�$ )Ingmar Bergman� 'David Fincher� %Milos Forman� 7Franklin J. Schaffner� -Federico Fellini� 5Krzysztof Kieslowski�
 5Pedro Almod&#243;var� #Frank Capra� 'Cameron Crowe�~ %Edward Zwick�h %George Lucas�8 #John Huston�* 1Billy Bob Thornton� John Ford� )Jonathan Demme� +George Roy Hill
� Ang Lee� %Sergio Leone�} %Orson Welles�P )Akira Kurosawa�L John Woo�F 'James Cameron�E %Howard Hawks� +Charles Chaplin� /Wolfgang Petersen� #David Lyncho Joel Coenn %Ridley ScottZ )Roman PolanskiR +Stanley KubrickP %Sidney LumetO %Billy WilderN +Martin Scorsese; 'Terry Gilliam/ %Mike Nichols% !Rob Reiner 5Francis Ford Coppola !Mel Gibson -Steven Spielberg -Alfred Hitchcock #Woody Allen   / p �������jVB,�������xgU;%�������nU@( � � � � � � � p          � 'W.S. Van Dyke�  'Walter Salles�n !Sam Mendes�d Sam Wood�) %John Sturges� 3Brian Desmond Hurst�a 'Isao Takahata�' )Clyde Bruckman�t #Jean Renoir� #Guy Ritchie�^ 1Giuseppe Tornatore�Z +Lewis Milestone�P 3Grigori Aleksandrov� #Erick Zonca�{ #Ash Brannon�s #F.W. Murnau�o Fax Bahr�^ )Ernst Lubitsch�^ 'Werner Herzog�M #Spike Jonze�~ )Otto Preminger� -Charles Laughton� )Victor Fleming�p -Darren Aronofsky�W 5Joseph L. Mankiewicz�R %Michael Mann�I #James Whale�8 !David Lean�0 'Sam Peckinpah� )Hayao Miyazaki� )Frank Darabont� 7Stuart Rosenberg  (I)�k !Carol Reed�` #Leo McCarey�F 1M. Night Shyamalan�4 +Roberto Benigni�/ -Luis Bu&#241;uel�# )Michael Curtiz� )Emir Kusturica� -Andrei Tarkovsky� !Elia Kazan� )Irvin Kershner� %Bryan Singer�t %George Cukor�l 'William Wyler�k #Louis Malle�i )Fred Zinnemann   	M ������s^M                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   � #Yimou Zhang�s +Lukas Moodysson�` )Stephen Daldry� %Melvin Frank�g )Tony Kaye  (I)�U )Michael Cimino�- 'Robert Rossen� +Robert Mulligan� /Marcel Carn&#233;    B ���K ����[>����cF% � � � � k B        '$ 3Princess Bride, The�@ ffffffQ�%# Alien�@ ffffffRn'" 3Clockwork Orange, A�@ ffffffR�R! !Fight Club�@!      S��  Gladiator�@ ������U�n4 KOne Flew Over the Cuckoo's Nest�@!ffffffYT� !Casablanca�@!������Z�� Aliens�@ ffffff]� �) 72001: A Space Odyssey�@ ������_�R Fargo�@ ffffffa�o Se7en�@ 333333bF�% -Sixth Sense, The�@!      k��. ?Silence of the Lambs, The�@!      s�  %Blade Runner�@ ������t�n )Godfather, The�	y�+ ;Raiders of the Lost Ark�@!333333|$
 +American Beauty�@!������#	�	 !Braveheart�@ ������ �f( 3Saving Private Ryan�@!       �A% -Schindler's List�@!������ ��) 3Usual Suspects, The�@!ffffff ��D iStar Wars: Episode V - The Empire Strikes Back�@!333333 ��" %Pulp Fiction�@!333333 ���( ?Shawshank Redemption, The�	 �� Star Wars�@!������ �?h    E ��]=���y[:���nE$ � � � � h E             !{ 'Graduate, The�@ 333333%V/*y 7To Kill a Mockingbird�@!      %�
 t #Toy Story 2�@!      '$�'i 1Gone with the Wind�@ 333333)�a Vertigo�@!      +�&^ 1North by Northwest�@!333333-DW #Rear Window�@!ffffff0�'R 1American History X�@ ������2�
g*J 7Vita &#232; bella, La�@!3333334[4$I +Green Mile, The�@ ������4a&H /Wizard of Oz, The�@ ������4�)F 5Being John Malkovich�@ ������5��%E /Full Metal Jacket�@ 3333336'RA #Taxi Driver�@ ������7
N@ Amadeus�@ ffffff8� ? %Shining, The�@ 3333339=R+= ;Godfather: Part II, The�@!������<6 Psycho�@!333333EF31 KMonty Python and the Holy Grail�@ ������H�;"- )Apocalypse Now�@ ������K�+ !Goodfellas�@!      K�NY) �Dr. Strangelove or: How I Learned to Stop Worrying and Love the Bomb�@!ffffffNBR!( %Citizen Kane�@!������O- �#' )Reservoir Dogs�@ ffffffOw�    : ���tQ/���[;���fA	 � � � g :  *�D 7Nuovo cinema Paradiso�@ ffffff:^&�/ /Central do Brasil�@ 3333335
 '�+ 1African Queen, The�@ ffffff\8#�  )Third Man, The�@!333333��&� /Great Escape, The�@ ffffff�	�5�y MBuono, il brutto, il cattivo, Il�@!      "�q 5Shichinin no samurai�	� �$�m -Some Like It Hot�@ ������-O7�a QButch Cassidy and the Sundance Kid�@ 333333�(�^ 3Singin' in the Rain�@!      �'�] 1Christmas Story, A�@ 333333%C�S Ben-Hur�@ 333333l�P !	Annie Hall�@ ffffffM2�= GBridge on the River Kwai, The�@ �������8!�: %Insider, The�@ ffffffR9�% UWallace & Gromit: The Wrong Trousers�@!      X<�# #Raging Bull�@ ������]N�" Glory�@ 333333�~�! !Sting, The�@ ffffff� � %12 Angry Men�@!333333�P� Chinatown�@ ������ XZ� Boot, Das�@!       � �%� -Deer Hunter, The�@ 333333 �
U � #Sling Blade�@ 333333"$*    B ���e8���o@����f; � � � i B          $�F -Double Indemnity�@!      �O,�D ;C'era una volta il West�@!      �(�: 3Straight Story, The�@ ������ �6�5 OTreasure of the Sierra Madre, The�@!      @8�+ Duck Soup�@ ������w��' Rebecca�@ ffffff�(� 3Todo sobre mi madre�@ ��������"�
 'Touch of Evil�@!       �"� )Paths of Glory�@!������$R"� 'Almost Famous�@!3333337��~ Ran�@!      F �&�f /On the Waterfront�@ ��������$�c +Wild Bunch, The�@ 333333�0,�^ ;Philadelphia Story, The�@ fffffft�\ High Noon�@ ffffffi"�Y 'All About Eve�@!333333$W)�G 5Arsenic and Old Lace�@ 333333��1�E EMr. Smith Goes to Washington�@ �������� �: %Sunset Blvd.�@!333333�O*�3 7Trois couleurs: Rouge�@ ffffff�4� KWallace & Gromit: A Close Shave�@ ffffff�<#�y )Cool Hand Luke�@ 333333�x Patton�@ 333333��K +Wo hu zang long�	�    U ���pP+��~M% ���Y-	 � � � U                               2� GAdventures of Robin Hood, The�@ 333333?�#� )Gold Rush, The�@ ������A � �P #City Lights�@!333333	 �3�; KWho's Afraid of Virginia Woolf?�@ ffffff	[/!� %Hustler, The�@ ffffff	�
-)�
 5Grapes of Wrath, The�@ ������	�)�	 5Sjunde inseglet, Det�@ ������	��'�v 1Dancer in the Dark�@ ������
6g#�^ )Quiet Man, The�@ 333333
�(�K 3Great Dictator, The�@ ������ �"�C )Apartment, The�@ ������O%�< /Conversation, The�@ 333333<.�6 ?Streetcar Named Desire, A�@ ffffffX�+�1 9Fucking &#197;m&#229;l�@ ffffffg
�)�. 5Die xue shuang xiong�@ ffffffw �(�+ 5Strangers on a Train�@ ������y%� -Bringing Up Baby�@ ������� �"� 'Mononoke Hime�@!      �� Rashomon�@!333333� �� Notorious�@ ffffff�#� )Searchers, The�@ �������!�M %Modern Times�@ ������� �#�H )Big Sleep, The�@ ffffff� �    I ��u?!����T0���sF$ � � � t I                   (�R 3Grande illusion, La�@!333333q�2�N GDa hong deng long gao gao gua�@ ������{"�? 'Thin Man, The�@ 333333�
(�2 3Requiem for a Dream�@!ffffff�p(�0 3Fanny och Alexander�@ ffffff���) !Strada, La�@ ��������*� 7Au revoir les enfants�@ 333333�k�y Scrooge�@ ffffff7	�,�n ;Quatre cents coups, Les�@!333333S��j Amarcord�@ ffffffX�*�e 7Bronenosets Potyomkin�@ ������bP�O !Stagecoach�@ 333333�!�a %General, The�@!ffffff�	':�W WNosferatu, eine Symphonie des Grauens�@ ffffff���V Stalag 17�@ �������O!�P %Billy Elliot�@ �������
��N Yojimbo�@!333333� �*�F 7Night at the Opera, A�@ ffffff�	��B Snatch�@ 333333��3�@ IAll Quiet on the Western Front�@ �������Z1�> EBest Years of Our Lives, The�@!      �l$�8 +His Girl Friday�@ ������� �-�6 =Night of the Hunter, The�@ ��������    ��zL!���c6���W                                                                                                                                                                                                                                         A�	 eHearts of Darkness: A Filmmaker s Apocalypse�@ ffffff�%� -Un chien andalou�@ ������/&�~ /Court Jester, The�@ ffffff	
�'�h 1To Be or Not to Be�@!      ��U Ikiru�@!������% ��M Red River�@ ������- �#�; )Hotaru no haka�@!      6	a*�  7Bride of Frankenstein�@ 333333�I#�r )Andrei Rublyov�@ ��������6�[ OVie r&#234;v&#233;e des anges, La�@ 333333�-�~ =Aguirre, der Zorn Gottes�@ 333333M^,�z ;Enfants du paradis, Les�@ ������R
(�c 3Anatomy of a Murder�@ ffffffw~+�F 9Crna macka, beli macor�@ 333333��)� 5Smultronst&#228;llet�@!      ��/�` CWitness for the Prosecution�@ ������ZO%�_ /Shadow of a Doubt�@ ������Z   \ � ���������������xog^UMD;3* ��������������uld[RH?7.&��������������zpg]SKA80(  � � � � � �         \ �[ �Z	}Yy}X-}W{	V	cvU�vT�vS	avR	WvQ	)sP	�jO �jN	dM �c	L �cKcJ �^I=^H^G �[F	[E[D �Z	CYB	UA�U@	�U?	-U>	U=	
L<L;	�K:�K9	�K8	�K7	�K6	^K5AI4	'I3I2 �?11;0#6/	6.	 �2-	,
, �,+y,*=,)-,(,'	 �+&	?+%	+$	*#	y*"	 �*!	 �*  �)	' �$ �$	"	F 	{	
	�		 �	=	t	I	�	-
	
				 �	 �	A=	+	 �		 �   O � ������������{pf\RG=3)������������}rg\QF;0%�����������}rg]RF;0$ � � � � � � �            	�+�V	�*�T�)	 �P	�(�M	�'	K�&-K�%I	�$ �D�#	 D�">	�! �8� 4�I3	�	2�-2�	"0�	�.�.�A-	��*�	 �*�I'�#'�F�		� ��+	���!��	
 �	�  ��	( ��
 ��	 ��
 ��A �� �
�' �� ��# �	� ��	 �� 	{ �	 � �~	$ �	} � �|A �{ �z	H �y	5 �x	+ �w	 �v �u1 �t' �s �r	� �q	� �p	� �o	 � �	n � �m �	l �k	� �	jO �i	� �h	� �	g �	f
 �e	 � �d	y �	c �	b	 �a$ �`t �_	� �^	� �]	M �
   V �  �&/8A �JRZdnx���� �����������",4<FPZdnx� ������������� 	 � �'/8BLV`jt~������������                      	�k	�i	�h	�g			� �	( �	�\	w	A�	j�	��	{R[E	� �	�o	��	��	|	3	6	5G"I3YCcK	 � �	c �	p �	�	8	QK	��	"	y0	{W	� �	( �	�]	w	�	A�	j�	{SL<	 � �	. �	4 �	� �	� �	 �	^L	��	1�	LBdN �l	I �	�$	�p �m	> �	\ �	� �	�+	��	��	h		u	yH	�N	��	��		�		"�		>�		�J			��		a,		Lz		��
   U �  *4>HR\dnx���� ����������� �",6@JT^hpy������ ������ ��� 
(2;EOYcmw���� � ����������                    	n	A8	2	�/	�'	�	
 � �	
�	
qM	
�l	
�	
��	
M�	
qO	
��
	 �	�`	+ 	�	
�	y�	�,(U>^H	 � �	� �	�a	��	YC	E$	� �	 �	O	�q	L~	y�	@�	��	3' �{	�'	��	"�	(�	gD	>H	�	B 	��	�z	�Z[F �v	 �	� �	^+	q	I� �s	 � �	� �	!�	��	6�	��	{�	�3	�U	��	q�6/ �\	 � �	� �		0	4	�I	��	��   L � �����������zncXMB6,"
������������xmcXMA5)�����������~sh]RF;1& � � � � � � � �        	�w �%�v)"	�u ��t	;�s$	�rH�q�p	�o �	�n ��m^�l�k	E �j@�	�i ���h��gF��f=��e�	�d��	�c��b�	�a ���`�	�_���^��]t��\E��[�
�Z �	�Yc�	�X��W	x��V)�	�Uy�	�T��	�S��R	:��Q��P	��O�		�N ���ME��L'�
	�K��J ��I��H@��G#��F�	�E ���D$��CI��B	��	�A��	�@+��?	R��>	!�	�=���<I��;	��:	���9	K�	�8�u�7	'r�6p
	�5	h�4=e�3	#d�2c	�1 �b�0$`�/\�.	
Y	�-DY�,	 �Y
   K GQ[eoy�������������)3=GQ[eoy�=�����)�������)3=GQ[emv�����������3��                                                                                                                                 	'�d	"�]	("4	!�!	;A	h�	
��	'�	>	�9	o	q�+%	�0	N�	[*	�d	��	 D �	 � �	 � �	 ��	 &�	 5	 �Q	 ��	 �	 d-	 �2	 �X	! �	!� �	!�	!
1	!��	!��	"0 �	"��	"�	"+<	"�j#60	# � �	#' �	#d �	#� �	#�		#��$ �a$ �~	$` �	$� �	$ �	$�
	$��	$��	$HA	$�5'I4' �t	' � �	'� �	'�	'9	'��	',	( � �	(5	(��	(#D	(�g	(��)sQ	)� �   L � �����������zodYMC8-" �����������wl`TH=2&�����������zocWLA6* � � � � � � � � �   �C	�<	�B�;�A;�@	J4	�?/�>	�+	�=;%�<^"�;1	�:�	�9'�8	�7��6	 �5(�4+	�3�	�2�1R�0�	�/ ��	�.��	�- ��	�,���+�	�*���)1��(-��'�	�&��	�% ���$��#	���"	��	�! ��� {��
�	� ��	���	����!�
�	�	�c�
	���{��'���		����1��		��	��	���	����	 ��	� ���t��	 ���
$��	#��	1z	� �u�	 �r�	q�	 �q�RR�O�+K� B	� �0	�~ �.�}?.	�|�+	�{�*�z	(�y		(	�xc&
   V � &0:D �NV`jt~�� ������������ �
'1;EOW_goy���� ���������� �!+5? �IQYblv� �������������              	)�j	-�f	+�X	=�W	?0O	@�A	A�	Ea�	@ �	)��	)�$	)�(	)�	)�+	+ �	+K	+4	+u	+t�	+O	+7--,)-U?-}X	-2 �	-K �	-�(	-��	-.	-W	-	��1;11 �u	1z	1�	1�)	1;	1��	1r===,*=^I	=e �	=� �	=�b	=.	=K�	=?+&	?. �	?��	?uG	?N�	?c�	?�	?3	?Fx	@� �	@� �	@{O	@�k	@��	@�	@A�AAI5A �|	A � �	A- �	A�	A�+	E� �	E� �	E  �	EwN	E';	E	p�	E�F 	F �	F� �	Fz�	F}�
   Q �   � �*4> �HPZdnx�������������",6@JR\fpz������������� *4>FOYcmw�������������                                                          	F�a	Fr<	H�)	^�#	H�	F�	Fy	H	l�	H4�	H��I	I' �	I3 �	I� �	I� �	I��	I��	I��	I�	I7	Iu	I�	J4@	J�P	J�;	J�e	J��	R� �	RR	R1	R?D	R�i	R�	R�O	R	�	RV�WvR	Ws	Wv�	W�\	W��^K6	^ �	^"<	^*�	^Z�	^�T	^�6avS	a
�	a
Y�	aN�	a�	i5z	iT	i��	i	��	i��	i��	i�W	i�tt �`	t� �	t�	t��	t��	t��	t��	t�#	t#:	t��	t/�	t�:y,+y �d	y 9	y{q	yY�	y�	y>v   K � �����������vj_SH<0$ �����������wlaUJ>4)�����������~rf[QF:." � � � � � � � � �      ��
�I�	� ��	����
t�		�	 ���t��t�	�|	�	|�y	��h	��h	��h� h�	iT�~L	�}O5	�|�5	�{�5�zi5	�y' 	�x� 	�w��v	F�u+	�t��sW	�r �q��p��o��n	���m	+��l
��k	@�	�j���iR�	�h���g	���f	��	�e��	�d��	�c ���b=��a��`�	�_ ��	�^ ���]�
�\	�	�[��	�Z	 ��	�Y ��	�X��		�Wy�	�V ��	�U�	�T��	�S		�	�R}�Q	�|	�P�|�O@{�NEw�M
q�L^�KQ	�J�M	�I G
	�H�E	�GOE	�F
E	�E	A�DR?   K � �����������uj^RF;0&�����������ynbWL@4(�����������xmaUJ?4( � � � � � � � � ��Y	��	�X��	�W��	�Vx�	�U��	�T �	�SD��R	��Q{�	�P ���O{��N�	�M�~�LFz�K+t�J	Dn	�I�a	�H�`�G	`	�FxZ	�E �Z	�D^Z	�CDI	�B�G	�A �G	�@�B�?@
�>	>	�=�8	�<�8	�;F8	�:�8	�9 �5
�81	�7 �+	�6�*	�5'*�4^*�3	"	�2�!�1!	�0 �
�/I	�. �	�- �
�,a
	�+ �	�*��	�)���(#�	�';��&I�	�%��$��#?�	�" ��!	�� I���		� ��	� ��	� ����	���	� ���t��$��$�		�:�	��	����	�	�	����-�
   M �  �%-7AKU_i �s|������������%0; �FOXbmx�� �����������"-8CNYdmv�����������                                                         	{�b
 ��\	yU
 ��E
 ��D
 �%5	yL�{	{ � �	{�	{� 	{��	{��	{h�	{�V �,,	 � �}
 �* �
 ��
 ���
 ��
 �1
 ��k
 �� � �?2 �cL
 �u
 ��Y
 ��_
 ��c
 �T�
 �P �
 �<�
 � �+' �ZD	 � �n
 �8 �
 ���
 �7>
 ���
 �e� �[
 �Y �
 �� �
 ���
 �Z�
 �	�
 �5=
 ��� �$ �*!
 �b �
 ��
 ��-
 ���
 � .
 ���
 �� 
 ��4
 ��c �)  �2. �[G	 � �
 �� �
 ���
 ��
 �_�
 �~�
 ���
 ��8 �
 � �
 �+�
 �8   K � �����������vj^RF;/$�����������uj_TI>3(�����������~sg\PD9."  � � � � � � � �       �$)��#t�
�"	j�	�!D�	� ���@���	����R�		�x��"�	�
��I��A�	� ��	���	�	��	�F���	� �	����|�w�	w�Iu
�u	�
's�	h	�	W�-W	��S�+O�I7		� �2�=.	�-.	� +�(�~ &�}"	�|
	�{�	�z�	�y�	�x�	�w:	�v�
	�u�		�t �		�s��r	�	�q� �p	���o"��n	���mi��l	��	�k���j(�	�i��	�hK�	�gK�	�f	�		�eD�	�d�	�c���b	���a	���`@��_)��^�	�] ���\�	�[ ��	�Z ��
   B< <����������� !,6ALWRbir{���~�������h]��	s*5@KVajs~�����G������                                                                                                                                                                                
 ��m
 ��e
 ��Z
 ��Y
 ��J
 ��G
 ��C
 �q �
 �D �
 � �
 � �
 � �
 �% �
 �0 �
 ��%
 ��/
 ���
 ���
 ��
 ��%
 �K'	 � �o
 ��^
 ���
 �	��
 ���		 � �^J �cM
 �� �
 �. �
 ��
 �Cw	 � �e
 ���
 �&�
 �g�
 ��	
 ���
 �
�
 ��
 ��
 �mE
 �p
 �r
 �	��
 ���
 ��
 �
 ��� �$ �*"
 �� �
 ��V
 �
�
 �5�
 ���
 �2
 �]M �jO
 ��Z
 �
f�
 ��<
 ��
 ��   K � �����������uj^SH=2'�����������{peZOC7+ 
�����������sg\PD8,  � � � � � � � � �    �o	�c�n	�_	�m']	�lcK�k	yA�j	�8	�i�4�h	F%�g	D#	�f �!	�ey	�d�	�c�	�b�	�a�	�` ��_	z	�^��	�]M��\	/�	�[���Z	��	�Y��	�X��	�W��	�VF�	�U���T^��S	n�	�R���Q ��PJ��OR��N�	�M��	�L��	�K ���J	��I��Hy�G?u	�F�r	�E �m�Dg�CY�BL�A$H	�@�D	�?�D	�> �7	�= �5�<"+�;E'�:t#�9y 	�8 ��7+	�6�5 �4
�3	�2��1!
�0		�/	�. � 
	�-��	�,���+A�	�*��	�)D�	�()��'	���&	��	�% ��	
   J � (3>IT]hs~ ������������ �!,7BMXcny������������)4=FQ\gr} ������������ �                                                               
 ��c
�$S
 �F
y�@
DV:
�z
 ��K
 �`
 �A
 �t}
 ��� �
 �G�
 �!f
 �
��
 ���	 �g
 � �
 �
� �
}R
��
	��
  � �
 6
 GI
 ��
 n/
 �?	+ �x
+� �
+
��
+8�
+]�
+�
/�\
/��
/,�
/��
/f�
D��
D�!
D#g
D��
D�
K� �
K��
K��
K��
K��
x� �
xZ�
x��
x�
xB�y*#y}Y
y� �
y�W
y��
y�i
y �
y�
q
��
�+>
�:u
���
�"�	� �p
�rF
�c
��w
�$�   K � �����������ti^SH=1%�����������zocWK@4)�����������zocXL@4* � � � � � � � � �    �:{h�9?c	�8 �_�7yY	�6 �T�5?N�4N�3=K
	�2�C	�1�B�0@A	�/A�.	A	�-+8	�,�	�+��*		�) �
��(	�
�	�'�
��&
�	�%j
�	�$+
��#	�
�	�"�
�	�!�
�	� �
p	� �
f�	�
Z�a
Y	�
X	��
K	�y
@�	�
,�
	��	��		�	��	�	�	�		�		��-	�	��	��i	��	 	�	� �	�	�	�	� �	��			��
E	p�		H	l	��	\	��	Y�	�	M�R		��		�+		�'		��	� 	O		�	���~	��}	���|	��	�{���z��y	��	�xD�	�w��	�v��	�u���t	��	�s�}	�r+}�qy{	�p�o
   K � (3>I � �T]hs~�� �������� ���#.9DOXalw���������� ���$/:EP[fq|�����������                                                  
�$R
��?
�H9
�3
��.
�-
��$
�5{
�h�
�8�
���
����K7
�	Y�
�
��
��
�Y�
��
��^
�<C
��[
� x
��Y
�#�
��]
�%�
�u �
�t
�5|
�G�
�� 
��U
�co
���
�9�K8�vU
�� �
���
�~~
���	� �q
��
��
��X
��
�x�
���
��1
��>�U@
��*
���
�	�
�E%
��
��
�
p�
���
���
� �
� �
2
��
��
`�
�


� �
6�
3
�=
��
��   J � �����������ui]QF;0$�����������ui^SG;0$ ����������}qeYOD8-! � � � � � � � � �       	���	�
�	�+��)�	�  ��	�'��~	�	�}��	�| ���{1��zi�	�yF~�xWv	�w'm�vj�u	j	�t �g		�s �e	�r+]	�q�Y	�p�Y	�o�U	�nQ�m
M		�l�E	�k�E		�j�E	�ixB	�h�A	�gMA	�f�<	�e�7		�d6	�c
4�bH4	�a�3	�`�0�_t/�^'	�] �&	�\�#	�[�	�Z ��Y �	�X ��
�W�	�V��	�U��	�T��	�S��
	�R��
	�Q ���P��O��Nt�	�Mc��L��K!��Ji�	�I��	�H��	�Gy��F!�	�ED�	�D ���C
�	�B��	�A ��	�@ �~�?F}	�>{�=y	�<�x	�;�w
   I �  � � �%0;FQ\gr}�����������!,7BMXcny������������(3>IS^it�����������                                                                         

 � �

�

�

#E

g�


 r
�~
Q�
�f
��
��
'r �
' y
'*�
's

']m
'	�
'm�
'��
+�m
+}r
+	�
+
+&
+��	5 �y
5l
5�
5��
5��
:� �
:��
:�
:��
:]�
:�l
DY �
DI�
Dn�
D��
D�)
D�x
Fv
F8�
F�
F�h
F%�
F.�	H �z
H �
H*
H�Y
H�_
H�
H.Q	M �]
M�]
MA�
MPK
M��	� �h
�� �
���
�
K�
�> 
��
��L
��[
�8o�K9
�;B
�h�
   I �  � � �
 +6ALWbmx������������&1<GR]hs~������������(1<GR]hs~�����������                                                                               
�
��
��
��"
��L
�B
�;�
�
�* �
�M �
�V �
��
��h
�`�
�
��
�c�
�i�
���
�g�K:
�� �
��W
���
���
�*�
���
�7�
��
�(6
�� �
��
�Q{
���
�b�
��|
�3�
�L�
�1�
�q;
��N�UA
��e
���
���
�E&��
�+ �
��d
��j
���
�	�
�U(�jP
�T �
��.
�w
�	\�
�Y)
��
��V	� �^
�D?
���
�A�
�PL
�0	� �i
���
�B�
���
��,
��X   J � �����������vk_SG<0$�����������ui]QF;0%�����������ymaUI=1% � � � � � � � �        	�N�a	�M �]	�L�P	�KMP	�J G	�IyG�H>�G5
	�F�#	�E
#�D(#	�C�
	�B�	�A �	�@�	�? �	�>��	�=�	�< ���;J��:t��9�	�8 ��	�7���6^��5$�	�4 ���3��2 �	�1���0y	�/ n	�.cj�- d�,	a�+^	�*[	�)�Y	�(�U	�' �K	�&�E	�%�E�$E	�#c>	�"�>	�!
>	� �>�>	�3�?3�3		� �1�',	�H*	��(		��&	�+&�"	� �	��	�+�=	�	� ��	���)��?��E�	�
O�	�	 ���y���		���� �   J � �����������zncWK?3'�����������xmbVJ>3'�����������ymaUI=1% � � � � � � � �        	��\�RV	� R�aN	��K�I	��?	�j:	�	-	�F%	�5	���	���	��	�
�	�	/�	���	����	����	��y�	���	� ��� J�	���	�~�~	�} �t	�|�p	�{�Q�z	L	�y J�x?F	�w �C�vy>		�u�:	�t;+	�s��r1�q	�p ��o	�n�	�mO
	�l5	�k ��
�j"�	�iy�	�hF�	�g(�	�f��eJ��d�	�c ��	�b��	�a��	�`��	�_H�	�^��	�]��
�\W�	�[���Z�	�YH��X �	�Wi��V{�	�U�	�T���S{�R	{		�Qcy�PFy�O
q

   F  BMXcny���7���������)4?JU`kv������������ %,0;FQ[fq|���������!��                                                                                                            
��K
��>
��,
n�+
�^
��

�#F
��`
�p|
���
�
�
��&
�?�
�3�
�k�
� �
�. �
��,
�3
�B�
�w�
�n
��n
�D@
�}s
�	�
�E�
�&
���
�?�
��
��#
��
�a
�C
���
���
���
���
���
�-�	� �r
�� �
�~�
��
�	��
�E�
��y
�z�
���
���
�
,�
���
�6�	O �j
OEG
O5}
O		�
O�

Om
j�"
j
��
j:�
j8�
j%�
n�S
no�
n/�
ye
yAk   I � ����������}qfZNB6+�����������{ocWK?3'�����������ui]QE9.# � � � � � � � � �     	�a
�	�`��	�_��	�^:�	�]��	�\��	�[��	�Z'�		�Yy�	�X ��	�W�l�VEa	�UyL	�T�6	�S�1	�R�	�Q�	�P �	�O�	�Ny 	�M��	�L5��K�	�J�	�I���HH�	�GM�	�F��	�EF�	�D�b	�C�L	�BA	�A�?	�@j8	�?�3	�>�1	�=n/	�</,	�;�(	�:�%	�9�
	�8 �
�7@ 	�6 ��	�5��	�4��	�3K��2
�	�1��	�0���/��.�	�-��	�,��	�+5��*W�	�)�	�( ��	�'�	�&���%(�	�$ ��	�#K�	�"+�	�!�z� q	�no	��j	��i	�
g	��d	��c	��^
   N � CN- �Ydo �z��"������ � � �����	*5 �@KValw������� ������& �1:EP[fq|���8��������     
��_
��I
��H
��B
�;7
��(
y� 
F�
�w
�Q
K
�5
y+
z(
yGI
y��
�8j
���
�U�
��g
�<�
���
��T
�S
��R
��t
�\�
�7�
�8�
���
��
�
��
��a
��b
��
�d
��
�* �
�7
�|Q
�a�
��[
�aN
���
���
��
�
��
�C�
���
��	 �c
�U
|�
	��
F�V
F%h
F~�
F��
F�cvV
c� �
c& �
c�
cKl
c��
c>#
cj.
cyQ
z_
z#�
�_n
�op
��
�,�
��'
�	��
���
 �   I � ����������}qeYMA5)�����������ymbWK?3'�����������vj^RF:/#  � � � � � � � �         	�*���)H�	�(���'�	�&��	�%��	�$���#^�	�"���!!�	� y�	�F��H�	��z	��w	��g	��^	��Q	�K	��9	��5	�y+	�z(	��	�
	� �	��	�H�����	�y�	�
��	�	��	���	�F�	�D��A��i�	����a��Fy	� �u�q		�~�k	�}/f	�|:]	�{�X	�z�U	�y�R	�x�?	�w �<	�v�;	�u�7�t6	�sF.	�r�-	�q�,	�pj%	�o�$	�nz#	�m�"	�l��kF	�j �	�i�	�h��	�g�	�f��	�e	�	�d/�	�c��	�b ��
   7� ���%0;EP[fq��|������������� !,7BMXcny�������������                                                                                                                                                                                                                                                                                                                      
 �^
�T
��M
	}=
��&
��
 GJ
 Jy
 R�
�
Z�
�K�
�^�
�j�	� �k
� �
�
��
�s
��
�l�
��
��M
�b
���
�R�
�U�
�u 
�MJ
��}
�E�
��7
�EH
���
�
�
��
��-
��v
�@
�(�
/?
�
��
A�		,-	UB	}Z
	2 �
	K �
	h �
	�
	AE
	��
	��
	W
		��
   C% %0;FQ\gr}����������� *5@KValw������������&1<GR]hs|�����������                                                                                                                                                       
�� �
�� �
��&
�:
�!�
��*
�2
�	M�
���
��T
��[		 �b
	�S
	|�
	-�
	��

Y �

EF

4�

>!

��

1*$
� �
�
��
/
	��

X�
��
; �
;%=
;��
;+t	� �_
��^
���
�X�
��*
�h�
��Z
��u
�	��
��
�d�
���
��%
��`
��f
��
��
�Y�
��	
��"�K;
���
�8�
���
�4i
�(
�>"
�1�
�?�
�.P
�|P
���
��{   E � ����������sg\PD8-!	�����������znbVK?3'�����������xmaVJ?4*	 � � � �                                                                        	�o�8	�n	�m ��	�l:��k��j)��i��h	��g��f-�	�e ���d'�		�c ���b{��aF�	�`��
	�_��
	�^ ��]"�	�\ ��	�[��	�Z ��	�Y ���X+��W=�	�V���Uy	�T�	�S�$	�R�$		�QH.	�P�.�O?0	�N��	�M��
	�L��
	�K��	�J ��	�I��	�H��	�G ��	�F �	�E ��	�D ��	�C ��	�B���A@�	�@y�	�?��	�>��	�=	}�<Fr	�;�q	�:DV	�9�H�8A	�7�;	�6�(	�5 �%�4("	�3��2		�1
	�0��/�	�.��	�-�	�,��	�+n�   � �j� ���                                                                                            �]'                                                                                              �]''�ytabledistributionsdistributionsCREATE TABLE distributions (idfilm integer NOT NULL REFERENCES films(id), idacteur integer NOT NULL REFERENCES acteurs(id), rang integer default NULL,  PRIMARY KEY (idfilm,idacteur))9M' indexsqlite_autoindex_distributions_1distributions   u�AtableacteursacteursCREATE TABLE acteurs (id integer NOT NULL, nom varchar(35) default NULL, PRIMARY KEY (id))�%%�MtablerealisateursrealisateursCREATE TABLE realisateurs (id integer NOT NULL, nom varchar(35) default NULL, PRIMARY KEY  (id))��utablefilmsfilmsCREATE TABLE films (id integer NOT NULL, titre varchar(70) default NULL, annee decimal(4,0) default NULL,score float default NULL, nbvotant integer default NULL, idrealisateur integer default NULL REFERENCES realisateurs(id), PRIMARY KEY  (id))    �0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       �]''�ytabledistributionsdistributionsCREATE TABLE distributions (idfilm integer NOT NULL REFERENCES films(id), idacteur integer NOT NULL REFERENCES acteurs(id), rang integer default NULL,  PRIMARY KEY (idfilm,idacteur))9M' indexsqlite_autoindex_distributions_1distributions�M�uviewFavorisFavorisCREATE VIEW Favoris AS
SELECT A.*,F.idrealisateur
FROM Acteurs A, Distributions D, Films F
WHERE A.id=D.idacteur AND D.idfilm=F.id
GROUP BY A.id, F.idrealisateur
HAVING COUNT(*)>=2