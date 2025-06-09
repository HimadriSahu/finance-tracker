from rest_framework import serializers
from .models import Budget
from transactions.serializers import CategorySerializer

class BudgetSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=category.objects.all(),
        source='category',
        write_only=True
    )

    class Meta:
        model = Budget
        fields = '__all__'
        read_only_fields = ('user', 'created_at')