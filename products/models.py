from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
	title = models.CharField(default='例：抖音-用短视频记录美好生活', max_length=50)  	#mc+tab补全characterField
	intro = models.TextField(default='在这里写APP介绍')	  	# mt+tab键
	url   = models.CharField(default='Http://', max_length=100)
	icon  = models.ImageField(default='default_icon.png', upload_to='images/')
	image = models.ImageField(default='default_image.jpg', upload_to='images/')

	votes = models.IntegerField(default=1)
	pub_date = models.DateTimeField()
	hunter = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title

	def shout_text(self):
		return self.text[:60] + '...'	#对文本显示一部分
    #model完成之后要去admin注册,在去命令行迁移
    #此处的默认显示在admin管理界面，在网站页面显示需要去改html