import csv
import io
from django import forms
from apartment.models import Apartment, Room


class CSVUploadForm(forms.Form):
    file = forms.FileField(label='CSVファイル', help_text='※拡張子csvのファイルをアップロードしてください。')

    def clean_file(self):
        file = self.cleaned_data['file']

        # ファイル名が.csvかどうかの確認
        if not file.name.endswith('.csv'):
            raise forms.ValidationError('拡張子がcsvのファイルをアップロードしてください')

        # csv.readerに渡すため、TextIOWrapperでテキストモードなファイルに変換
        csv_file = io.TextIOWrapper(file, encoding='utf-8')
        reader = csv.reader(csv_file)

        # 各行から作った保存前のモデルインスタンスを保管するリスト
        self._instances = []
        self._rent_list = []
        try:
            for row in reader:
                apartment = Apartment(name=row[0],
                                      goodNumber=row[1],
                                      age=row[2],
                                      address=row[3],
                                      appearance=row[4],
                                      )
                self._instances.append(apartment)
                self._rent_list.append(int(row[5]))

        except UnicodeDecodeError:
            raise forms.ValidationError('ファイルのエンコーディングや、正しいCSVファイルか確認ください。')

        return file

    def save(self):
        count = 0
        # Apartmentを保存後、関連するRoomを生成する。
        for apartment in self._instances:
            apartment.save()
            for i in range(5):
                number = str(i) + '01'
                room = Room(
                    apartment=apartment,
                    number=int(number),
                    isRentable=True,
                    rent=self._rent_list[count],
                    floorPlan="ワンルーム",
                    areBathAndToiletSeparated=True,
                )
                # 前半4物件は1Kに変更、後半6物件はユニットバスに変更
                if count < 4:
                    room.floorPlan = "1K"
                else:
                    room.areBathAndToiletSeparated = False
                room.save()
            count += 1
