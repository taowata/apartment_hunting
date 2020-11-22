import csv
import io
from django import forms
from apartment.models import Apartment


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
        try:
            for row in reader:
                post = Apartment(name=row[0], goodNumber=row[1])
                self._instances.append(post)
        except UnicodeDecodeError:
            raise forms.ValidationError('ファイルのエンコーディングや、正しいCSVファイルか確認ください。')

        return file

    def save(self):
        for apartment in self._instances:
            apartment.save()