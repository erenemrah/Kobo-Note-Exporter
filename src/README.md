# Kobo Note Exporter

A Python program for exporting highlighted notes from the Kobo Aura H2O e-book reader.

## Features

- Export all highlighted notes or notes from a specific book from the KoboReader.sqlite database.
- Save output in `.txt` or `.csv` format.

## Installation

1. Make sure Python 3 is installed.
2. Install required dependencies:
    ```sh
    pip install sqlite3
    ```
3. Keep the files in the `src` folder together.

## Usage

Run from the command line as follows:

```sh
python3 src/KoboNoteExporter.py -i <path to KoboReader.sqlite> -t <Output.txt>
python3 src/KoboNoteExporter.py -i <path to KoboReader.sqlite> -c <Output.csv>
python3 src/KoboNoteExporter.py -i <path to KoboReader.sqlite> -f "<Book Title>" -t <Output.txt>
python3 src/KoboNoteExporter.py -i <path to KoboReader.sqlite> -f "<Book Title>" -c <Output.csv>
```

### Parameters

- `-h, --help` : Show help menu.
- `-i, --input` : Path to KoboReader.sqlite file.
- `-f, --find` : Search for a specific book title.
- `-t, --txt` : Save output as a text file.
- `-c, --csv` : Save output as a CSV file.

### Examples

- Export all highlights as TXT:
  ```sh
  python3 src/KoboNoteExporter.py -i KoboReader.sqlite -t Output.txt
  ```
- Export highlights of a specific book as TXT:
  ```sh
  python3 src/KoboNoteExporter.py -i KoboReader.sqlite -f "Hamlet" -t Output.txt
  ```
- Export all highlights as CSV:
  ```sh
  python3 src/KoboNoteExporter.py -i KoboReader.sqlite -c Output.csv
  ```
- Export highlights of a specific book as CSV:
  ```sh
  python3 src/KoboNoteExporter.py -i KoboReader.sqlite -f "Hamlet" -c Output.csv
  ```

## License

This project is licensed under the [GNU GPL v3](https://www.gnu.org/licenses/gpl-3.0.html).

## Contact

For any questions: Emrah Eren

# Kobo Note Exporter

Kobo Aura H2O e-kitap okuyucusundan alınan vurgulu notları dışa aktarmak için kullanılan bir Python programıdır.

## Özellikler

- KoboReader.sqlite veritabanından tüm vurgulu notları veya belirli bir kitabın notlarını dışa aktarır.
- Çıktıyı `.txt` veya `.csv` formatında kaydedebilir.

## Kurulum

1. Python 3 yüklü olduğundan emin olun.
2. Gerekli bağımlılıkları yükleyin:
   ```sh
   pip install sqlite3
   ```
3. `src` klasöründeki dosyaları bir arada bulundurun.

## Kullanım

Komut satırından aşağıdaki gibi çalıştırabilirsiniz:

```sh
python3 src/KoboNoteExporter.py -i <KoboReader.sqlite yolu> -t <Çıktı.txt>
python3 src/KoboNoteExporter.py -i <KoboReader.sqlite yolu> -c <Çıktı.csv>
python3 src/KoboNoteExporter.py -i <KoboReader.sqlite yolu> -f "<Kitap Adı>" -t <Çıktı.txt>
python3 src/KoboNoteExporter.py -i <KoboReader.sqlite yolu> -f "<Kitap Adı>" -c <Çıktı.csv>
```

### Parametreler

- `-h, --help` : Yardım menüsünü gösterir.
- `-i, --input` : KoboReader.sqlite dosyasının yolu.
- `-f, --find` : Belirli bir kitabın adını arar.
- `-t, --txt` : Çıktıyı metin dosyası olarak kaydeder.
- `-c, --csv` : Çıktıyı CSV dosyası olarak kaydeder.

### Örnekler

- Tüm vurguları TXT olarak dışa aktar:
  ```sh
  python3 src/KoboNoteExporter.py -i KoboReader.sqlite -t Output.txt
  ```
- Belirli bir kitabın vurgularını TXT olarak dışa aktar:
  ```sh
  python3 src/KoboNoteExporter.py -i KoboReader.sqlite -f "Hamlet" -t Output.txt
  ```
- Tüm vurguları CSV olarak dışa aktar:
  ```sh
  python3 src/KoboNoteExporter.py -i KoboReader.sqlite -c Output.csv
  ```
- Belirli bir kitabın vurgularını CSV olarak dışa aktar:
  ```sh
  python3 src/KoboNoteExporter.py -i KoboReader.sqlite -f "Hamlet" -c Output.csv
  ```

## Lisans

Bu proje [GNU GPL v3](https://www.gnu.org/licenses/gpl-3.0.html) lisansı ile lisanslanmıştır.

## İletişim

Herhangi bir sorunuz için: Emrah Eren