from rest_framework import serializers
from .models import employees

class employeeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model=employees
        fields=('user_id','name','addhar','mobile_no','image')