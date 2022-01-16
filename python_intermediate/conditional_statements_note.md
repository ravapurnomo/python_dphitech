CONDITIONAL STATEMENTS

1.	**WHAT AND WHY**
<br> <br>
Apa itu Conditions? | Real life use case | Mengapa Conditional Statements pad aprogramming?

Conditions adalah sebab dan akibat.
Jika ini...maka...lakukan itu....

Conditional Statements adalah bagian dari kehidupan kita sehari-hari <br>
Sebagai orang yang dapat berpikir tentang situasi, dan membuat keputusan berdasarkan apa yang kita amati. <br>
Biasanya kita mengevaluasi informasi di sekitar kita dan akhirnya memilih satu tindakan ke tindakan lainnya. <br> <br>
	“Jika cuaca baik, maka saya akan pergi jalan-jalan.” (Tersirat bahwa jika cuaca tidak baik, maka saya tidak akan pergi jalan-jalan) <br>

Conditions adalah sebuah bagian kunci dari proses penentuan keputusan untuk komputer. <br>
Komputer adalah mesin yang tidak dapat melakukan apapun tanpa kita kita mengarahkannya. <br>
Kita mengarahkan komputer menggunakan Conditional Statements. <br>
Ini dapat memberitahu komputer harus melakukan apa, dan kapan melakukannya. <br> <br>

Dalam program Python, statement if adalah bagaimana kita menunjukkan pengambilan keputusan. Hal itu memungkinkan untuk conditional execution of a statement atau grup dari statements yang berdasarkan value of  expression.
<br> <br> <br>
**2.	IF...ELIF...ELSE**
<br> <br>
Statement IF – Statement If...Else – Statement If...Elif...Else <br>
Pada dunia nyata, kita biasanya mengevaluasi informasi disekitar kita dan kemudian memilih satu tindakan atau tindakan lainnya, berdasarkan apa yang kita amati. <br> <br>
“Jika cuaca baik, maka saya akan pergi jalan-jalan.” (Tersirat bahwa jika cuaca tidak baik, maka saya tidak akan pergi jalan-jalan) <br><br>

Dalam program Python, statement if adalah bagaimana kita menunjukkan pengambilan keputusan. Hal itu memungkinkan untuk conditional execution of a statement atau grup dari statements yang berdasarkan value of expression.
<br>
<br>
<br>
<br>
**STATEMENT IF** <br>

Sintaks untuk menuliskan statement if pada Python :<br><br>
	If test expression/condition:
		Statement(s) 
<br><br>

Disini program dapat mengevaluasi ekspresi pengujian dan akan mengeksekusi hanya jika test expression/condition nya adalah True <br>

Dalam Python, body dari statement if diindikasikan oleh indentation atau lekukan pada baris baru. Body dimulai dengan lekukan atau baris baru dan tanda garis pertama di akhirnya.<br>
Python mengartikan nilai tidak nol sebagai True (bahkan nilai yang negatif). <br>
Nihil atau 0 diartikan sebagai False. <br>
String, list, dictionary, tuple, dan set yang kosong juga diartikan sebagai False.
<br> <br>

Flowchart : <br>  
<img size="150" alt="1a" src="https://user-images.githubusercontent.com/32615754/149361462-dda6abd0-94b7-4319-814a-2570b6821977.png">

<br>
Contoh : program Python mendeteksi jika (if) sebuah angka adalah genap. (tanda % memberitahu kita sisa 0 setelah dibagi 2 pastilah angka genap.) <br>

<img width="375" alt="1b" src="https://user-images.githubusercontent.com/32615754/149362282-02a1a197-f032-450f-9dbe-447688785e94.png">

<br> <br>
 
**STATEMENT IF - ELSE** <br>
Sintaks :
**	If test expression:
		Body of if
	Else:
		Body of else**

Statement if...else mengevaluasi test expression dan akan mengeksekusi body dari if hanya ketika test conditionnya adalah True. <br>
Jika conditionnya False, body dari else akan tereksekusi. Indentation atau lekukan atau baris bari digunakan untuk memisahkan blok-blok. <br>

<img width="161" alt="1C" src="https://user-images.githubusercontent.com/32615754/149362564-23a69c87-068f-407e-998e-8b01433aeeb0.png">
 <br>
Contoh : <br>

<img width="420" alt="1d" src="https://user-images.githubusercontent.com/32615754/149362622-e25729f7-6ee5-4257-97f2-5e04c1a764bd.png">
<br> <br>

**STATEMENT IF – ELIF – ELSE**
<br>
Sintaks :
	**If test expression:
		Body of if
	Elif test expression:
		Body of elif
	Else:
		Body of else**
<br

Elif adalah kependekan dari else if , memungkinkan kita untuk mengecek banyak expression. <br>
Jika condition untuk if adalah False, maka akan dicek condition dari blok elif selanjutnya, dan  begitu seterusnya. <br>
Jika semua conditions False, body dari else akan tereksekusi. <br>
Hanya satu blok diantara beberapa blok if...elif...else yang akan dieksekusi, sesuai dengan kondisi yang diberikan. 
<br> <br>
Flowchart : <br>

 <img width="161" alt="1e" src="https://user-images.githubusercontent.com/32615754/149363432-5b0e53f4-c0e8-49d8-89c5-25e3d756abc6.png">
<br>

<img width="247" alt="1f" src="https://user-images.githubusercontent.com/32615754/149363488-d60f6bae-d17e-4d6d-9e95-b550f28b6703.png">

<br>
•	Pertama, kita memberikan value 5 kepada variabel z <br>
•	Kontrol bergeser ke baris selanjutnya dimana z%2 telah dicek. 5 tidak habis dibagi 2, jadi kontrol tidak bergeser ke body dari if <br>
•	Lalu, statement elif: z%3 tereksekusi. Karena 5 tidak habis dibagi 3, maka body dari elif tidak dieksekusi <br>
•	Akhirnya, statement else dieksekusi dan kontrol bereser ke body dari kontrol statement. Statement print(“z is neither divisible by 2 nor by 3”) is executed 
<br> <br>


Poin untuk dicatat : Conditions telah dicek dari urutas atas sampai bawah. Jika condition if atau elif True, maka akan langsung dieksekusi dan tidak ada conditions selanjutnya yang akan dicek
