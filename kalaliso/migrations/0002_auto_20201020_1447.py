# Generated by Django 3.1 on 2020-10-20 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kalaliso', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commande_Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='photos/modele/%Y/%m/%d', verbose_name='Photo_commande')),
                ('couture', models.CharField(choices=[('BRODERIE', 'Broderie'), ('COUTURE SIMPLE', 'Couture simple'), ('COUTURE A MAIN', 'Couture a main'), ('REPARATION', 'Reparation')], default='Broderie', max_length=25)),
                ('tissu', models.CharField(choices=[('BAZIN GETZNER', 'BAZIN GETZNER'), ('BAZIN RICHE', 'BAZIN RICHE'), ('BAZIN MOYEN', 'BAZIN MOYEN'), ('WAX', 'WAX'), ('TISSU', 'TISSU'), ('LEGER', 'LEGER'), ('BRODE', 'BRODE'), ('PERCALE', 'PERCALE'), ('VOILE', 'VOILE'), ('BOGOLAN', 'BOGOLAN'), ('AUTRES', 'AUTRES')], default='BAZIN GETZNER', max_length=25)),
                ('couloir', models.CharField(choices=[('BLANCHE', 'BLANCHE'), ('ROUGE SANG', 'ROUGE SANG'), ('BLEU', 'BLEU'), ('ORANGE', 'ORANGE'), ('ROSE', 'ROSE'), ('VERT', 'VERT'), ('GRIS', 'GRIS'), ('GRIS CLAIR', 'GRIS CLAIR'), ('VIOLET', 'VIOLET'), ('MARON', 'MARON'), ('MARON CLAIR', 'MARON CLAIR'), ('TURGUOISE', 'TURGUOISE'), ('JAUNE', 'JAUNE'), ('JAUNE COUSIN', 'JAUNE COUSIN'), ('NOIR', 'NOIR'), ('BAGA', 'BAGA'), ('BAGA CLAIR', 'BAGA CLAIR'), ('DEUX TONS', 'DEUX TONS'), ('MULTICOLOR', 'MULTICOLOR')], default='BLANCHE', max_length=25)),
                ('quantite', models.PositiveSmallIntegerField()),
                ('metrage', models.FloatField()),
                ('price', models.FloatField()),
                ('avance', models.FloatField()),
                ('reliquat', models.FloatField()),
                ('remise', models.FloatField(default=0)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.RenameModel(
            old_name='ItemsDepense',
            new_name='Depense_Detail',
        ),
        migrations.RenameModel(
            old_name='Orders',
            new_name='Commande',
        ),
        migrations.DeleteModel(
            name='ItemsOrders',
        ),
        migrations.AddField(
            model_name='commande_detail',
            name='command',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='kalaliso.commande'),
        ),
        migrations.AddField(
            model_name='commande_detail',
            name='products',
            field=models.ManyToManyField(to='kalaliso.Produit', verbose_name='list_commande'),
        ),
    ]
