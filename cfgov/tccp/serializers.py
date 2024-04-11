from rest_framework import serializers

from .fields import JSONListField
from .models import CardSurveyData


class CardSurveyDataSerializer(serializers.HyperlinkedModelSerializer):
    purchase_apr_good_max = serializers.FloatField()
    purchase_apr_good_min = serializers.FloatField()
    purchase_apr_good_rating = serializers.IntegerField()
    purchase_apr_great_max = serializers.FloatField()
    purchase_apr_great_min = serializers.FloatField()
    purchase_apr_great_rating = serializers.IntegerField()
    purchase_apr_poor_max = serializers.FloatField()
    purchase_apr_poor_min = serializers.FloatField()
    purchase_apr_poor_rating = serializers.IntegerField()

    class Meta:
        model = CardSurveyData
        fields = "__all__"
        extra_kwargs = {
            "url": {"lookup_field": "slug", "view_name": "tccp:card_detail"},
        }

    def build_standard_field(self, field_name, model_field):
        field_class, field_kwargs = super().build_standard_field(
            field_name, model_field
        )

        # Our JSONListField inherits from JSONField but also supports a
        # "choices" argument, which breaks some assumptions made by
        # django-rest-framework. This code is needed to ensure that
        # JSONListFields are serialized properly as JSON.
        if isinstance(model_field, JSONListField):
            field_kwargs.pop("encoder"),
            field_kwargs.pop("decoder")

        return field_class, field_kwargs


class CardSurveyDataListSerializer(CardSurveyDataSerializer):
    annual_fee_estimated = serializers.FloatField()
    purchase_apr_for_tier_max = serializers.FloatField()
    purchase_apr_for_tier_min = serializers.FloatField()
    purchase_apr_for_tier_rating = serializers.IntegerField()
    transfer_apr_for_tier_max = serializers.FloatField()
    transfer_apr_for_tier_min = serializers.FloatField()

    class Meta(CardSurveyDataSerializer.Meta):
        fields = [
            "annual_fee_estimated",
            "institution_name",
            "periodic_fee_type",
            "product_name",
            "purchase_apr_for_tier_max",
            "purchase_apr_for_tier_min",
            "purchase_apr_for_tier_rating",
            "requirements_for_opening",
            "rewards",
            "top_25_institution",
            "transfer_apr_for_tier_max",
            "transfer_apr_for_tier_min",
            "url",
        ]
