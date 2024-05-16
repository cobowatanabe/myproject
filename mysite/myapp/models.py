from django.utils import timezone
from django.db import models
from datetime import timedelta
# Create your models here.
import uuid  # UUIDフィールド用

class Myapp(models.Model):
    id = models.UUIDField('会員ID', primary_key=True, default=uuid.uuid4, editable=True)
    first_name = models.CharField('名前', max_length=20)
    last_name = models.CharField('姓', max_length=20)
    email = models.EmailField('メールアドレス',blank=True, null=True)
    join_date = models.DateField('入会日', auto_now_add=True)
    membership_type = models.CharField('会員種別', max_length=10, choices=(
        ('standard', 'Standard'),
        ('premium', 'Premium'),
    
    ))
    GENDER_CHOICES = (
    ('male', '男性'),
    ('female', '女性'),
    ('other', 'その他'),
    )
    gender = models.CharField('性別', max_length=10, choices=GENDER_CHOICES)
    birth_date = models.DateField('生年月日', null=True, blank=True)
    address = models.TextField('住所', null=True, blank=True)
    STATUS_CHOICES = (
    ('active', '入会'),
    ('paused', '休会'),
    ('cancelled', '退会'),
    )
    status = models.CharField('ステータス', max_length=10, choices=STATUS_CHOICES, default='active')
    
    #年齢計算
    @property
    def age(self):
        return int((timezone.now().date() - self.birth_date).days / 365.25) if self.birth_date else None
    
    expiration_date = models.DateField('継続期間', null=True, blank=True)
    def save(self, *args, **kwargs):
        # 継続期間を加入日から1年後に設定
        if not self.expiration_date: 
            self.expiration_date = self.join_date + timedelta(days=365)
        super().save(*args, **kwargs)
    photo = models.ImageField('顔写真', upload_to='member_photos/', null=True, blank=True)
    base_fee = models.DecimalField('月会費', max_digits=8, decimal_places=2)
    op1 = models.BooleanField('オプション1', default=False)
    op1_description = models.CharField('オプション1内容', max_length=200, blank=True, null=True)
    op1_fee = models.DecimalField('オプション1料金', max_digits=6, decimal_places=2, default=0)
    op2 = models.BooleanField('オプション2', default=False)
    op2_description = models.CharField('オプション2内容', max_length=200, blank=True, null=True)
    op2_fee = models.DecimalField('オプション2料金', max_digits=6, decimal_places=2, default=0)
    op3 = models.BooleanField('オプション3', default=False)
    op3_description = models.CharField('オプション3内容', max_length=200, blank=True, null=True)
    op3_fee = models.DecimalField('オプション3料金', max_digits=6, decimal_places=2, default=0)
    
    @property
    def total_fee(self):
        total = self.base_fee
        if self.op1:
            total += self.op1_fee
        if self.op2:
            total += self.op2_fee
        if self.op3:
            total += self.op3_fee
        return total

    created_at = models.DateTimeField('日付', default=timezone.now)

    def __str__(self):
        return '{0} {1}'.format(self.last_name, self.first_name)
    