
# PdftoWord

PdftoWord, PDF dosyalarını Word belgelerine (.docx) dönüştürmenizi sağlayan bir Python projesidir. Bu araç, PDF dosyalarındaki metinleri düzenlemek veya çıkarmak ve Word belgeleriyle çalışmayı tercih eden kullanıcılar için özellikle kullanışlıdır.

## Özellikler

- PDF dosyalarını düzenlenebilir Word belgelerine dönüştürme
- Orijinal PDF'nin düzenini ve formatını koruma
- Kullanıcı dostu komut satırı arayüzü
- Tüm platformlara destek


  
## Kullanım/Örnekler

```
1.Depoyu yerel bilgisayarınıza klonlayın:

git clone https://github.com/gulbahar-donmez/PdftoWord.git

2.Proje dizinine gidin:
cd PdftoWord

3.Sanal bir ortam oluşturun ve etkinleştirin:
python -m venv venv
source venv/bin/activate  # Windows için `venv\Scripts\activate`

4.Gerekli kütüphaneleri yükleyin
pip install pdf2docx

5.Aşağıdaki Python kodunu kullanarak bir PDF dosyasını Word belgesine dönüştürün

from pdf2docx import Converter

pdf_path = "C:\\Users\\Gulbahar-NB\\Desktop\\Yeni klasör (2)\\sample2.pdf"
docx_path = "C:\\Users\\Gulbahar-NB\\Desktop\\Yeni klasör (2)\\donusturulmus.docx"

cv = Converter(pdf_file=pdf_path)
cv.convert(docx_filename=docx_path)
cv.close()



```

  
## Kullanılan Teknolojiler

**İstemci:** Python 3.6+, pdf2docx kütüphanesi 

**ide:** PyCharm

  
## Katkı
Projeye katkıda bulunmak isterseniz, lütfen depoyu çatallayın (fork) ve değişikliklerinizle bir çekme isteği (pull request) oluşturun. Projenin kodlama standartlarına uymayı ve değişiklikleriniz için testler eklemeyi unutmayın.


  
