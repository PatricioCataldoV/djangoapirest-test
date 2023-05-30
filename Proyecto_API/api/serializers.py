from rest_framework import serializers
from .models import Variables

class VarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variables
        fields = ('id', 'nombre','var1','var2','var3','var4','var5','var6','var7','var8','var9','var10','var11','var12', 'var13','var14','var15','var16','var17','var18','var19','var20','var21','var22','var23','var24','var25','var26','var27','var28','var29','var30')
        read_only_fields = ('id',)
