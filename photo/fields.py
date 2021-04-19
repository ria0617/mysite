import os
from PIL import Image
from django.db.models.fields.files import ImageField, ImageFieldFile

class ThumbnailImageFieldFile(ImageFieldFile):
    def _add_thumb(self, s):
        parts = s.split(".")
        parts.insert(-1, "thumb")
        if parts[-1].lower() not in ['jpeg', 'jpg']:
            parts[-1] = 'jpg'
        return ".".join(parts)
    
    @property
    def thumb_path(self):
        return self._add_thumb(self.path)
        
    @property
    def thumb_url(self):
        return self._add_thumb(self.url)

    def save(self, name, content, save=True): #파일시스템에 파일을 저장하고 생성하는 메서드
        super().save(name, content, save) #부모 ImageFieldFile클래스의 save()메서드를 호출해서 원본 이미지를 저장.

        img = Image.open(self.path)
        size = (self.field.thumb_width, self.field.thumb_height)
        img.thumbnail(size) #PIL 라이브러리의 썸네일 만드는 함수임. Image.thumbnail()이라는 함수를 이용하여 썸네일 제작.
        background = Image.new('RGB', size, (255, 255, 255))
        box = (int((size[0]- img.size[0]) / 2), int((size[1] - img.size[1]) / 2))
        background.paste(img, box)
        background.save(self.thumb_path, 'JPEG') #img와 box를 함쳐 만든 최종 썸네일을 JPEG형식으로 thumb_path 경로에 저장.

    def delete(self, save=True): #원본과 썸네일을 모두 삭제.
        if os.path.exists(self.thumb_path):
            os.remove(self.thumb_path)
        super().delete(save)
        
class ThumbnailImageField(ImageField):
    attr_class = ThumbnailImageFieldFile
    
    def __init__(self, verbose_name=None, thumb_width=250, thumb_height=250, **kwargs):
        self.thumb_width, self.thumb_height = thumb_width, thumb_height
        super().__init__(verbose_name, **kwargs)
        
