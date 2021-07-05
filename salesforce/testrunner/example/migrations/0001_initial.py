# Generated by Django 3.2.5 on 2021-07-05 13:26

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import salesforce.fields
import salesforce.testrunner.example.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChargentOrder',
            fields=[
                ('id', salesforce.fields.SalesforceAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', salesforce.fields.CharField(max_length=255)),
                ('Balance_Due', salesforce.fields.CharField(db_column='ChargentOrders__Balance_Due__c', max_length=255)),
            ],
            options={
                'db_table': 'ChargentOrders__ChargentOrder__c',
                'abstract': False,
                'managed': False,
            },
            managers=[
                ('base_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', salesforce.fields.SalesforceAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Type', salesforce.fields.CharField(choices=[('Analyst', 'Analyst'), ('Competitor', 'Competitor'), ('Customer', 'Customer'), ('Integrator', 'Integrator'), ('Investor', 'Investor'), ('Partner', 'Partner'), ('Press', 'Press'), ('Prospect', 'Prospect'), ('Reseller', 'Reseller'), ('Other', 'Other')], max_length=100, null=True)),
                ('BillingStreet', salesforce.fields.CharField(max_length=255)),
                ('BillingCity', salesforce.fields.CharField(max_length=40)),
                ('BillingState', salesforce.fields.CharField(max_length=20)),
                ('BillingPostalCode', salesforce.fields.CharField(max_length=20)),
                ('BillingCountry', salesforce.fields.CharField(max_length=40)),
                ('ShippingStreet', salesforce.fields.CharField(max_length=255)),
                ('ShippingCity', salesforce.fields.CharField(max_length=40)),
                ('ShippingState', salesforce.fields.CharField(max_length=20)),
                ('ShippingPostalCode', salesforce.fields.CharField(max_length=20)),
                ('ShippingCountry', salesforce.fields.CharField(max_length=40)),
                ('Phone', salesforce.fields.CharField(max_length=255)),
                ('Website', salesforce.fields.CharField(max_length=255)),
                ('Industry', salesforce.fields.CharField(choices=[('Agriculture', 'Agriculture'), ('Apparel', 'Apparel'), ('Banking', 'Banking'), ('Biotechnology', 'Biotechnology'), ('Chemicals', 'Chemicals'), ('Communications', 'Communications'), ('Construction', 'Construction'), ('Consulting', 'Consulting'), ('Education', 'Education'), ('Electronics', 'Electronics'), ('Energy', 'Energy'), ('Engineering', 'Engineering'), ('Entertainment', 'Entertainment'), ('Environmental', 'Environmental'), ('Finance', 'Finance'), ('Food & Beverage', 'Food & Beverage'), ('Government', 'Government'), ('Healthcare', 'Healthcare'), ('Hospitality', 'Hospitality'), ('Insurance', 'Insurance'), ('Machinery', 'Machinery'), ('Manufacturing', 'Manufacturing'), ('Media', 'Media'), ('Not For Profit', 'Not For Profit'), ('Other', 'Other'), ('Recreation', 'Recreation'), ('Retail', 'Retail'), ('Shipping', 'Shipping'), ('Technology', 'Technology'), ('Telecommunications', 'Telecommunications'), ('Transportation', 'Transportation'), ('Utilities', 'Utilities')], max_length=100)),
                ('Description', salesforce.fields.TextField()),
                ('LastModifiedDate', salesforce.fields.DateTimeField(auto_now=True)),
                ('Name', salesforce.fields.CharField(max_length=255)),
            ],
            options={
                'db_table': 'Account',
                'abstract': False,
                'managed': True,
            },
            managers=[
                ('base_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='BusinessHours',
            fields=[
                ('id', salesforce.fields.SalesforceAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', salesforce.fields.CharField(max_length=80)),
                ('IsDefault', salesforce.fields.BooleanField(default=False, verbose_name='Default Business Hours')),
                ('MondayStartTime', salesforce.fields.TimeField()),
            ],
            options={
                'verbose_name_plural': 'BusinessHours',
                'db_table': 'BusinessHours',
            },
            managers=[
                ('base_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', salesforce.fields.SalesforceAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', salesforce.fields.CharField(max_length=80)),
                ('number_sent', salesforce.fields.DecimalField(blank=True, decimal_places=0, max_digits=18, null=True, verbose_name='Num Sent')),
                ('parent', salesforce.fields.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='example.campaign')),
            ],
            options={
                'db_table': 'Campaign',
                'abstract': False,
                'managed': True,
            },
            managers=[
                ('base_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', salesforce.fields.SalesforceAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', salesforce.fields.CharField(max_length=80)),
                ('first_name', salesforce.fields.CharField(blank=True, max_length=40, null=True)),
                ('name', salesforce.fields.CharField(max_length=121, verbose_name='Full Name')),
                ('email', salesforce.fields.EmailField(blank=True, max_length=254, null=True)),
                ('email_bounced_date', salesforce.fields.DateTimeField(blank=True, null=True)),
                ('vs', salesforce.fields.DecimalField(blank=True, db_column='Vs__c', decimal_places=0, max_digits=10, null=True, unique=True)),
                ('account', salesforce.fields.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='example.account')),
            ],
            options={
                'db_table': 'Contact',
                'abstract': False,
                'managed': True,
            },
            managers=[
                ('base_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='CronTrigger',
            fields=[
                ('id', salesforce.fields.SalesforceAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PreviousFireTime', salesforce.fields.DateTimeField(blank=True, null=True, verbose_name='Previous Run Time')),
            ],
            options={
                'db_table': 'CronTrigger',
                'abstract': False,
                'managed': True,
            },
            managers=[
                ('base_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='DeletedObject',
            fields=[
                ('id', salesforce.fields.SalesforceAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'DeletedObject',
                'abstract': False,
                'managed': True,
            },
            managers=[
                ('base_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', salesforce.fields.SalesforceAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LastName', salesforce.fields.CharField(max_length=80)),
                ('FirstName', salesforce.fields.CharField(blank=True, max_length=40, null=True)),
                ('Salutation', salesforce.fields.CharField(choices=[('Mr.', 'Mr.'), ('Ms.', 'Ms.'), ('Mrs.', 'Mrs.'), ('Dr.', 'Dr.'), ('Prof.', 'Prof.')], max_length=100)),
                ('Name', salesforce.fields.CharField(max_length=121)),
                ('Title', salesforce.fields.CharField(max_length=128)),
                ('Company', salesforce.fields.CharField(max_length=255)),
                ('Street', salesforce.fields.CharField(max_length=255)),
                ('City', salesforce.fields.CharField(max_length=40)),
                ('State', salesforce.fields.CharField(max_length=20)),
                ('PostalCode', salesforce.fields.CharField(max_length=20)),
                ('Country', salesforce.fields.CharField(max_length=40)),
                ('Phone', salesforce.fields.CharField(max_length=255)),
                ('Email', salesforce.fields.CharField(max_length=100)),
                ('LeadSource', salesforce.fields.CharField(choices=[('Advertisement', 'Advertisement'), ('Employee Referral', 'Employee Referral'), ('External Referral', 'External Referral'), ('Partner', 'Partner'), ('Public Relations', 'Public Relations'), ('Seminar - Internal', 'Seminar - Internal'), ('Seminar - Partner', 'Seminar - Partner'), ('Trade Show', 'Trade Show'), ('Web', 'Web'), ('Word of mouth', 'Word of mouth'), ('Other', 'Other')], max_length=100)),
                ('Status', salesforce.fields.CharField(choices=[('Contacted', 'Contacted'), ('Open', 'Open'), ('Qualified', 'Qualified'), ('Unqualified', 'Unqualified')], max_length=100)),
                ('Industry', salesforce.fields.CharField(choices=[('Agriculture', 'Agriculture'), ('Apparel', 'Apparel'), ('Banking', 'Banking'), ('Biotechnology', 'Biotechnology'), ('Chemicals', 'Chemicals'), ('Communications', 'Communications'), ('Construction', 'Construction'), ('Consulting', 'Consulting'), ('Education', 'Education'), ('Electronics', 'Electronics'), ('Energy', 'Energy'), ('Engineering', 'Engineering'), ('Entertainment', 'Entertainment'), ('Environmental', 'Environmental'), ('Finance', 'Finance'), ('Food & Beverage', 'Food & Beverage'), ('Government', 'Government'), ('Healthcare', 'Healthcare'), ('Hospitality', 'Hospitality'), ('Insurance', 'Insurance'), ('Machinery', 'Machinery'), ('Manufacturing', 'Manufacturing'), ('Media', 'Media'), ('Not For Profit', 'Not For Profit'), ('Other', 'Other'), ('Recreation', 'Recreation'), ('Retail', 'Retail'), ('Shipping', 'Shipping'), ('Technology', 'Technology'), ('Telecommunications', 'Telecommunications'), ('Transportation', 'Transportation'), ('Utilities', 'Utilities')], max_length=100)),
                ('EmailBouncedDate', salesforce.fields.DateTimeField(blank=True, null=True)),
                ('IsDeleted', salesforce.fields.BooleanField(default=False)),
                ('is_converted', salesforce.fields.BooleanField(default=salesforce.fields.DefaultedOnCreate(), verbose_name='Converted')),
            ],
            options={
                'db_table': 'Lead',
                'abstract': False,
                'managed': True,
            },
            managers=[
                ('base_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', salesforce.fields.SalesforceAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', salesforce.fields.CharField(max_length=80)),
                ('body', salesforce.fields.TextField(null=True)),
                ('parent_id', salesforce.fields.CharField(max_length=18)),
                ('parent_type', salesforce.fields.CharField(db_column='Parent.Type', max_length=50)),
            ],
            options={
                'db_table': 'Note',
                'abstract': False,
                'managed': True,
            },
            managers=[
                ('base_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Opportunity',
            fields=[
                ('id', salesforce.fields.SalesforceAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', salesforce.fields.CharField(max_length=255)),
                ('close_date', salesforce.fields.DateField()),
                ('stage', salesforce.fields.CharField(db_column='StageName', max_length=255)),
                ('created_date', salesforce.fields.DateTimeField(auto_now_add=True)),
                ('amount', salesforce.fields.DecimalField(blank=True, decimal_places=2, max_digits=18, null=True)),
                ('probability', salesforce.fields.DecimalField(blank=True, decimal_places=0, default=salesforce.fields.DefaultedOnCreate(), max_digits=3, null=True, verbose_name='Probability (%)')),
            ],
            options={
                'db_table': 'Opportunity',
                'abstract': False,
                'managed': True,
            },
            managers=[
                ('base_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Pricebook',
            fields=[
                ('id', salesforce.fields.SalesforceAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', salesforce.fields.CharField(max_length=255)),
            ],
            options={
                'db_table': 'Pricebook2',
                'abstract': False,
                'managed': True,
            },
            managers=[
                ('base_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', salesforce.fields.SalesforceAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', salesforce.fields.CharField(max_length=255)),
            ],
            options={
                'db_table': 'Product2',
                'abstract': False,
                'managed': True,
            },
            managers=[
                ('base_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', salesforce.fields.SalesforceAutoField(auto_created=True, primary_key=True, serialize=False, sf_managed_model=True, verbose_name='ID')),
                ('name', salesforce.fields.CharField(max_length=80)),
                ('last_modified_date', salesforce.fields.DateTimeField(auto_now=True)),
                ('test_text', salesforce.fields.CharField(db_column='TestText__c', max_length=40, sf_managed=True)),
                ('test_bool', salesforce.fields.BooleanField(db_column='TestBool__c', default=False, sf_managed=True)),
            ],
            options={
                'db_table': 'django_Test__c',
            },
            managers=[
                ('base_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='TestDetail',
            fields=[
                ('id', salesforce.fields.SalesforceAutoField(auto_created=True, primary_key=True, serialize=False, sf_managed_model=True, verbose_name='ID')),
            ],
            options={
                'db_table': 'django_Test_detail__c',
                'abstract': False,
                'managed': True,
            },
            managers=[
                ('base_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', salesforce.fields.SalesforceAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', salesforce.fields.CharField(max_length=80)),
                ('Email', salesforce.fields.CharField(max_length=100)),
                ('LastName', salesforce.fields.CharField(max_length=80)),
                ('FirstName', salesforce.fields.CharField(max_length=40)),
                ('IsActive', salesforce.fields.BooleanField(default=False)),
                ('UserType', salesforce.fields.CharField(default='Standard', max_length=80)),
            ],
            options={
                'db_table': 'User',
                'abstract': False,
                'managed': True,
            },
            managers=[
                ('base_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', salesforce.fields.SalesforceAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('what', salesforce.fields.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='task_what_set', to='example.account')),
                ('who', salesforce.fields.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='example.lead')),
            ],
            options={
                'db_table': 'Task',
                'abstract': False,
                'managed': True,
            },
            managers=[
                ('base_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='PricebookEntry',
            fields=[
                ('id', salesforce.fields.SalesforceAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', salesforce.fields.CharField(max_length=255)),
                ('UseStandardPrice', salesforce.fields.BooleanField(default=False)),
                ('UnitPrice', salesforce.fields.DecimalField(decimal_places=2, max_digits=18)),
                ('Pricebook2', salesforce.fields.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='example.pricebook')),
                ('Product2', salesforce.fields.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='example.product')),
            ],
            options={
                'verbose_name_plural': 'PricebookEntries',
                'db_table': 'PricebookEntry',
                'abstract': False,
                'managed': True,
            },
            managers=[
                ('base_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', salesforce.fields.SalesforceAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', salesforce.fields.CharField(max_length=80)),
                ('division', salesforce.fields.CharField(blank=True, max_length=80)),
                ('organization_type', salesforce.fields.CharField(max_length=40, verbose_name='Edition')),
                ('instance_name', salesforce.fields.CharField(blank=True, max_length=5)),
                ('is_sandbox', salesforce.fields.BooleanField(default=False)),
                ('created_by', salesforce.fields.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='organization_createdby_set', to='example.user')),
                ('last_modified_by', salesforce.fields.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='organization_lastmodifiedby_set', to='example.user')),
            ],
            options={
                'db_table': 'Organization',
            },
            managers=[
                ('base_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='OpportunityLineItem',
            fields=[
                ('id', salesforce.fields.SalesforceAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', salesforce.fields.CharField(max_length=376, verbose_name='Opportunity Product Name')),
                ('quantity', salesforce.fields.DecimalField(decimal_places=2, max_digits=12)),
                ('total_price', salesforce.fields.DecimalField(decimal_places=2, default=salesforce.fields.DefaultedOnCreate(), max_digits=18)),
                ('unit_price', salesforce.fields.DecimalField(decimal_places=2, default=salesforce.fields.DefaultedOnCreate(), max_digits=18, verbose_name='Sales Price')),
                ('opportunity', salesforce.fields.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='example.opportunity')),
                ('pricebook_entry', salesforce.fields.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='example.pricebookentry', verbose_name='Price Book Entry ID')),
                ('product2', salesforce.fields.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='example.product', verbose_name='Product ID')),
            ],
            options={
                'db_table': 'OpportunityLineItem',
                'abstract': False,
                'managed': True,
            },
            managers=[
                ('base_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='OpportunityContactRole',
            fields=[
                ('id', salesforce.fields.SalesforceAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', salesforce.fields.CharField(blank=True, max_length=40, null=True)),
                ('contact', salesforce.fields.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='opportunity_roles', to='example.contact')),
                ('opportunity', salesforce.fields.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='contact_roles', to='example.opportunity')),
            ],
            options={
                'db_table': 'OpportunityContactRole',
                'abstract': False,
                'managed': True,
            },
            managers=[
                ('base_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='opportunity',
            name='contacts',
            field=models.ManyToManyField(related_name='opportunities', through='example.OpportunityContactRole', to='example.Contact'),
        ),
        migrations.AddField(
            model_name='lead',
            name='last_modified_by',
            field=salesforce.fields.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='lead_lastmodifiedby_set', to='example.user'),
        ),
        migrations.AddField(
            model_name='lead',
            name='owner',
            field=salesforce.fields.ForeignKey(default=salesforce.fields.DefaultedOnCreate(salesforce.testrunner.example.models.User), on_delete=django.db.models.deletion.DO_NOTHING, related_name='lead_owner_set', to='example.user'),
        ),
        migrations.AddField(
            model_name='contact',
            name='owner',
            field=salesforce.fields.ForeignKey(default=salesforce.fields.DefaultedOnCreate(salesforce.testrunner.example.models.User), on_delete=django.db.models.deletion.DO_NOTHING, related_name='contact_owner_set', to='example.user'),
        ),
        migrations.CreateModel(
            name='CampaignMember',
            fields=[
                ('id', salesforce.fields.SalesforceAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', salesforce.fields.CharField(max_length=40)),
                ('campaign', salesforce.fields.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='example.campaign')),
                ('contact', salesforce.fields.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='example.contact')),
            ],
            options={
                'db_table': 'CampaignMember',
                'abstract': False,
                'managed': True,
            },
            managers=[
                ('base_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', salesforce.fields.SalesforceAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', salesforce.fields.CharField(max_length=80)),
                ('body', salesforce.fields.TextField()),
                ('parent', salesforce.fields.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='example.test')),
            ],
            options={
                'db_table': 'Attachment',
                'abstract': False,
                'managed': True,
            },
            managers=[
                ('base_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='ApexEmailNotification',
            fields=[
                ('id', salesforce.fields.SalesforceAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', salesforce.fields.CharField(blank=True, max_length=255, unique=True, verbose_name='email')),
                ('user', salesforce.fields.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='apex_email_notification', to='example.user')),
            ],
            options={
                'db_table': 'ApexEmailNotification',
                'abstract': False,
                'managed': True,
            },
            managers=[
                ('base_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='Owner',
            field=salesforce.fields.ForeignKey(default=salesforce.fields.DefaultedOnCreate(salesforce.testrunner.example.models.User), on_delete=django.db.models.deletion.DO_NOTHING, to='example.user'),
        ),
    ]
