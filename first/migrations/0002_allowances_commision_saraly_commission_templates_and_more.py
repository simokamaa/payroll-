# Generated by Django 4.2.1 on 2023-05-22 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='allowances',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house_allowance', models.FloatField()),
                ('medical_allowance', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Commision_saraly',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('single_work', models.FloatField()),
                ('daily_work', models.FloatField()),
                ('monthly_work', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='commission_templates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('work_type', models.CharField(max_length=255)),
                ('commission_policy', models.CharField(max_length=255)),
                ('persentage_enjoyed', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='deductions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provident_fund', models.FloatField()),
                ('tax_deduction', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('middle_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=255)),
                ('Employement_id', models.IntegerField()),
                ('Email', models.EmailField(max_length=254)),
                ('phone_number', models.IntegerField()),
                ('kra_pin', models.IntegerField()),
                ('image', models.ImageField(upload_to='')),
                ('front_id_image', models.ImageField(upload_to='')),
                ('back_id_image', models.ImageField(upload_to='')),
                ('salary', models.IntegerField()),
                ('department', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Fixed_saraly',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('single_work', models.FloatField()),
                ('daily_work', models.FloatField()),
                ('monthly_work', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='job_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('department', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ManageSalary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee', models.CharField(max_length=255)),
                ('job_type', models.CharField(max_length=255)),
                ('amount', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='PayrollSummary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employeeId', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='salary_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gross_salary', models.FloatField()),
                ('deductions', models.FloatField()),
                ('net_salary', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='SelectDepartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('select_department', models.CharField(max_length=255)),
                ('select_month', models.DateField()),
            ],
        ),
    ]
