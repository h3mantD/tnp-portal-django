from django.db import models
from django.contrib import admin
# Create your models here.

def convert(lst):
    return ' '.join(lst)

class Admindata(models.Model):
    uname = models.CharField(max_length=20, blank=True, null=True)
    password = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admindata'

    def __str__(self):
        return self.password

class Logindata(models.Model):
    id = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=20,  null=True)
    lname = models.CharField(max_length=20,  null=True)
    e_mail = models.CharField(max_length=20,  null=True)
    mob_no = models.CharField(max_length=20,  null=True)
    uname = models.CharField(max_length=20,  null=True)
    password = models.CharField(max_length=20,  null=True)
    info_stat = models.CharField(max_length=10,  null=True)

    class Meta:
        managed = False
        db_table = 'logindata'

    def __str__(self):
        lst = []
        lst.extend((self.id,self.uname,self.password,self.fname,self.lname,self.e_mail,self.mob_no,self.info_stat))
        
        #return str(convert(lst))
        return self.password


class Studdata(models.Model):
    #stud_id = models.ForeignKey(Logindata, models.DO_NOTHING, db_column='id', blank=True, null=True)
    studid = models.CharField(unique=True, max_length=5, null=True)
    fname = models.CharField(max_length=20, null=True)
    lname = models.CharField(max_length=20, null=True)
    b_name = models.CharField(max_length=20, null=True)
    cyear = models.CharField(max_length=20, null=True)
    roll = models.CharField(max_length=10)
    address = models.CharField(max_length=900,  null=True)
    e_mail = models.CharField(max_length=20,  null=True)
    mob_no = models.CharField(max_length=20,  null=True)
    tenth = models.CharField(max_length=20,  null=True)
    twelth = models.CharField(max_length=20,  null=True)
    avg_marks = models.CharField(max_length=20,  null=True)
    nback = models.CharField(max_length=20,  null=True)
    add_info = models.CharField(max_length=900,  null=True)
    


    class Meta:
        managed = False
        db_table = 'studdata'


class Selectedstud(models.Model):
    #id = models.ForeignKey(Logindata, models.DO_NOTHING, db_column='id', blank=True, null=True)
    company = models.CharField(max_length=100, blank=True, null=True)
    studid = models.CharField(unique=False, max_length=5, null=True)

    class Meta:
        managed = False
        db_table = 'selectedstud'

    def __str__(self):
        return self.company

""" @admin.register(Selectedstud)
class display(admin.ModelAdmin):
    list_dis = ("id", "company") """