# Generated by Django 5.1 on 2025-02-05 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_alter_post_is_complete'),
    ]

    operations = [
        migrations.AddField(
            model_name='posttext',
            name='font',
            field=models.CharField(choices=[('default', '기본서체'), ('nanum_gothic', '나눔고딕'), ('nanum_myeongjo', '나눔명조'), ('bareun_gothic', '바른고딕'), ('nanum_square', '나눔스퀘어'), ('maruburi', '마루부리'), ('restart', '다시시작해'), ('bareun_hippie', '바른히피'), ('our_daughter', '우리딸손글씨')], default='nanum_gothic', max_length=20),
        ),
        migrations.AddField(
            model_name='posttext',
            name='font_size',
            field=models.IntegerField(choices=[(11, '11px'), (13, '13px'), (15, '15px'), (16, '16px'), (19, '19px'), (24, '24px'), (28, '28px'), (30, '30px'), (34, '34px'), (38, '38px')], default=15),
        ),
        migrations.AddField(
            model_name='posttext',
            name='is_bold',
            field=models.BooleanField(default=False),
        ),
    ]
