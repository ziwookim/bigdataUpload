# Generated by Django 3.1.4 on 2020-12-27 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('b_no', models.AutoField(db_column='b_no', primary_key=True, serialize=False)),
                ('b_title', models.CharField(db_column='b_title', max_length=255)),
                ('b_note', models.TextField(db_column='b_note')),
                ('b_writer', models.CharField(db_column='b_writer', max_length=50)),
                ('parent_no', models.IntegerField(db_column='parent_no', default=0)),
                ('b_count', models.IntegerField(db_column='b_count', default=0)),
                ('d_date', models.DateTimeField(db_column='d_date')),
            ],
            options={
                'db_table': 'board',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ExcelData',
            fields=[
                ('UPDUSERCD1', models.CharField(db_column='UPDUSERCD1', max_length=255)),
                ('SOKEY', models.CharField(db_column='SOKEY', max_length=255)),
                ('DELIVERYCD', models.CharField(db_column='DELIVERYCD', max_length=255)),
                ('ACTFLG', models.CharField(db_column='ACTFLG', max_length=255)),
                ('PICKBATCHKEY', models.CharField(db_column='PICKBATCHKEY', max_length=255)),
                ('ASSYKEY', models.CharField(db_column='ASSYKEY', max_length=255)),
                ('SOTYPE', models.CharField(db_column='SOTYPE', max_length=255)),
                ('STS', models.CharField(db_column='STS', max_length=255)),
                ('ORDERDATE', models.CharField(db_column='ORDERDATE', max_length=255)),
                ('DELIVNAME', models.DateTimeField(blank=True, db_column='DELIVNAME')),
                ('SHIPSCHDATE', models.DateTimeField(blank=True, db_column='SHIPSCHDATE')),
                ('SHIPDATE', models.DateTimeField(blank=True, db_column='SHIPDATE')),
                ('PRIORITIES', models.CharField(db_column='PRIORITIES', max_length=255)),
                ('OWNERCD', models.CharField(db_column='OWNERCD', max_length=255)),
                ('ITEMCD', models.CharField(db_column='ITEMCD', max_length=255)),
                ('EXPECTQTY1', models.CharField(db_column='EXPECTQTY1', max_length=255)),
                ('SHIPPEDQTY1', models.CharField(db_column='SHIPPEDQTY1', max_length=255)),
                ('CUSTOMERCD', models.CharField(db_column='CUSTOMERCD', max_length=255)),
                ('OWNERNM', models.CharField(db_column='OWNERNM', max_length=255)),
                ('ORDERTYPE', models.CharField(db_column='ORDERTYPE', max_length=255)),
                ('DELIVSCHDATE', models.CharField(db_column='DELIVSCHDATE', max_length=255)),
                ('DELIVDATE', models.CharField(db_column='DELIVDATE', max_length=255)),
                ('TRANSPORTPRIORITY', models.CharField(db_column='TRANSPORTPRIORITY', max_length=255)),
                ('WAREHOUSECD', models.CharField(db_column='WAREHOUSECD', max_length=255)),
                ('OTHERREFNO3', models.CharField(db_column='OTHERREFNO3', max_length=255)),
                ('WAREHOUSENM', models.CharField(db_column='WAREHOUSENM', max_length=255)),
                ('PREKEY', models.CharField(db_column='PREKEY', max_length=255)),
                ('CUSTOMERNM', models.CharField(db_column='CUSTOMERNM', max_length=255)),
                ('SHIPTOCD', models.CharField(db_column='SHIPTOCD', max_length=255)),
                ('SHIPTONM', models.CharField(db_column='SHIPTONM', max_length=255)),
                ('ADDRESS1', models.CharField(db_column='ADDRESS1', max_length=255)),
                ('ADDRESS2', models.CharField(db_column='ADDRESS2', max_length=255)),
                ('POSTNO1', models.CharField(db_column='POSTNO1', max_length=255)),
                ('POSTNO2', models.CharField(db_column='POSTNO2', max_length=255)),
                ('HPNO', models.CharField(db_column='HPNO', max_length=255)),
                ('EMAIL', models.CharField(db_column='EMAIL', max_length=255)),
                ('REFNAME', models.CharField(db_column='REFNAME', max_length=255)),
                ('ALLOCGROUP', models.CharField(db_column='ALLOCGROUP', max_length=255)),
                ('NOTES', models.CharField(db_column='NOTES', max_length=255)),
                ('OTHERREFNO1', models.CharField(db_column='OTHERREFNO1', max_length=255)),
                ('OTHERREFNO2', models.CharField(db_column='OTHERREFNO2', max_length=255)),
                ('MOVEKEY', models.CharField(db_column='MOVEKEY', max_length=255)),
                ('WBKEY', models.CharField(db_column='WBKEY', max_length=255)),
                ('ADDDATETIME', models.CharField(db_column='ADDDATETIME', max_length=255)),
                ('ADDUSERCD', models.CharField(db_column='ADDUSERCD', max_length=255)),
                ('UPDDATETIME', models.CharField(db_column='UPDDATETIME', max_length=255)),
                ('UPDUSERCD', models.CharField(db_column='UPDUSERCD', max_length=255)),
                ('TERMINALCD', models.CharField(db_column='TERMINALCD', max_length=255)),
                ('ORDERCUSTNAME', models.CharField(db_column='ORDERCUSTNAME', max_length=255)),
                ('ORDERCUSTPHONE', models.CharField(db_column='ORDERCUSTPHONE', max_length=255)),
                ('ORDERCUSTHP', models.CharField(db_column='ORDERCUSTHP', max_length=255)),
                ('PHONENO', models.CharField(db_column='PHONENO', max_length=255)),
                ('SOKEY1', models.CharField(db_column='SOKEY1', max_length=255)),
                ('SOLINENO', models.CharField(db_column='SOLINENO', max_length=255)),
                ('ORDERKEY', models.CharField(db_column='ORDERKEY', max_length=255)),
                ('ORDERLINENO', models.CharField(db_column='ORDERLINENO', max_length=255)),
                ('ITEMGROUP', models.CharField(db_column='ITEMGROUP', max_length=255)),
                ('IFITEMCD', models.CharField(db_column='IFITEMCD', max_length=255)),
                ('LOT1', models.CharField(db_column='LOT1', max_length=255)),
                ('LOT2', models.CharField(db_column='LOT2', max_length=255)),
                ('LOT3', models.CharField(db_column='LOT3', max_length=255)),
                ('LOT4', models.CharField(db_column='LOT4', max_length=255)),
                ('LOT5', models.CharField(db_column='LOT5', max_length=255)),
                ('NOSHIPPINGFLG', models.CharField(db_column='NOSHIPPINGFLG', max_length=255)),
                ('OTHERFLG', models.CharField(db_column='OTHERFLG', max_length=255)),
                ('XDOCKQTY1', models.CharField(db_column='XDOCKQTY1', max_length=255)),
                ('ALLOCQTY1', models.CharField(db_column='ALLOCQTY1', max_length=255)),
                ('PICKEDQTY1', models.CharField(db_column='PICKEDQTY1', max_length=255)),
                ('SORTEDQTY1', models.CharField(db_column='SORTEDQTY1', max_length=255)),
                ('ADJUSTQTY1', models.CharField(db_column='ADJUSTQTY1', max_length=255)),
                ('PRICE1', models.CharField(db_column='PRICE1', max_length=255)),
                ('PRICE2', models.CharField(db_column='PRICE2', max_length=255)),
                ('PRICE3', models.CharField(db_column='PRICE3', max_length=255)),
                ('NOTES1', models.CharField(db_column='NOTES1', max_length=255)),
                ('LOTRESERVEFLG', models.CharField(db_column='LOTRESERVEFLG', max_length=255)),
                ('PICKQTYERRORFLG', models.CharField(db_column='PICKQTYERRORFLG', max_length=255)),
                ('XDOCFLG', models.CharField(db_column='XDOCFLG', max_length=255)),
                ('MOVELINENO', models.CharField(db_column='MOVELINENO', max_length=255)),
                ('ASSYLINENO', models.CharField(db_column='ASSYLINENO', max_length=255)),
                ('ADDDATETIME1', models.CharField(db_column='ADDDATETIME1', max_length=255)),
                ('ADDUSERCD1', models.CharField(db_column='ADDUSERCD1', max_length=255)),
                ('UPDDATETIME1', models.CharField(db_column='UPDDATETIME1', max_length=255)),
                ('TERMINALCD1', models.CharField(db_column='TERMINALCD1', max_length=255)),
                ('SHOPITEMCD', models.CharField(db_column='SHOPITEMCD', max_length=255)),
                ('OTHERVALUE1', models.CharField(db_column='OTHERVALUE1', max_length=255)),
                ('OTHERVALUE2', models.CharField(db_column='OTHERVALUE2', max_length=255)),
                ('FAX1', models.CharField(db_column='FAX1', max_length=255)),
                ('CONFIRMQTY', models.CharField(db_column='CONFIRMQTY', max_length=255)),
                ('NAME', models.CharField(db_column='NAME', max_length=255)),
                ('CONDATE', models.DateTimeField(blank=True, db_column='CONDATE')),
                ('CRUD', models.CharField(db_column='CRUD', max_length=255)),
                ('SODAY', models.CharField(db_column='SODAY', max_length=255)),
                ('IFDATE', models.CharField(db_column='IFDATE', max_length=255)),
                ('IFSODAY', models.CharField(db_column='IFSODAY', max_length=255)),
                ('SKX_EXW2_PK', models.AutoField(db_column='SKX_EXW2_PK', primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'skx_exw2',
                'managed': False,
            },
        ),
    ]
