# passwordgenerator

TR: Bu kod, güçlü şifreler oluşturmak için bir arayüz sağlar. Arayüzde kullanıcılar şifre uzunluğunu belirleyebilir ve büyük harf, küçük harf, rakam ve özel karakter gibi farklı karakter tiplerini seçebilirler. Ayrıca, her karakterin benzersiz olmasını isteyip istemediklerini belirleyebilirler. Şifre oluşturulduğunda, oluşturulan şifre gösterilir ve şifrenin güvenliğini değerlendiren bir etiket sağlanır. Kullanıcılar ayrıca oluşturulan şifreyi panoya kopyalayabilirler.

Kod, tkinter kütüphanesini kullanarak bir GUI (Grafiksel Kullanıcı Arayüzü) oluşturur. english ve mandarin_chinese olmak üzere iki farklı dil seçeneği sunar. Kullanıcılar dil seçeneğini ComboBox kullanarak değiştirebilirler. Her dil için arayüz metinleri dil dosyasından alınır ve güncellenir.

Kodun çalışma mantığı şu adımları içerir:

Dil seçimini değiştirme işlevi: ComboBox'tan seçilen dili temel alarak arayüz metinlerini günceller.
Şifre oluşturma işlevi: Kullanıcının seçtiği kriterlere göre güçlü bir şifre oluşturur.
Şifre güvenliğini değerlendirme işlevi: Oluşturulan şifrenin gücünü belirler.
Şifreyi panoya kopyalama işlevi: Oluşturulan şifreyi panoya kopyalar.
Arayüzü oluşturma: tkinter kullanarak kullanıcı arayüzünü oluşturur.
Bu kod, güvenli şifreler oluşturmak için kullanıcı dostu bir arayüz sağlar ve çeşitli dil seçenekleri sunarak kullanıcıların tercihlerine uyum sağlar.





EN: This code provides a user-friendly interface for generating strong passwords. Users can specify the password length and select different types of characters such as uppercase letters, lowercase letters, digits, and special characters. They can also choose whether each character in the password should be unique or not. When a password is generated, it's displayed on the interface along with an evaluation of its strength. Users can also copy the generated password to the clipboard.

The code utilizes the tkinter library to create a Graphical User Interface (GUI). It offers two language options: English and Mandarin Chinese. Users can switch between languages using a ComboBox. The interface text for each language is retrieved from a language file and updated accordingly.

The logic of the code involves the following steps:

Change Language Function: Updates the interface texts based on the language selected from the ComboBox.
Generate Password Function: Creates a strong password based on the criteria selected by the user.
Evaluate Password Strength Function: Determines the strength of the generated password.
Copy Password Function: Copies the generated password to the clipboard.
Creating the Interface: Utilizes tkinter to build the user interface.
This code offers a convenient way to generate secure passwords and adapts to users' preferences by providing various language options.






