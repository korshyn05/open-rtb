"""De-serializers for the ad server APIs."""
from rest_framework import serializers

from ..constants import ALL_CAMPAIGN_TYPES
from ..models import Advertisement
from ..models import Publisher


class AdPlacementSerializer(serializers.Serializer):

    """
    De-serializes incoming possible ad placements for the API.

    For example, a client may suggest 3 possible placements
    and have different <div> IDs for those and have different
    priorities for them.
    """

    div_id = serializers.CharField()
    ad_type = serializers.CharField(required=True)
    priority = serializers.IntegerField(
        default=1, min_value=1, max_value=10, required=False
    )


class AdDecisionSerializer(serializers.Serializer):

    """De-serializes incoming possibilities for the ad API."""

    # Required fields
    placements = AdPlacementSerializer(many=True)
    publisher = serializers.SlugField(required=True)

    keywords = serializers.ListField(
        child=serializers.CharField(), max_length=10, required=False
    )

    # Whether this request should only consider a certain kind of ad
    campaign_types = serializers.ListField(
        child=serializers.CharField(), max_length=10, required=False
    )

    # Used to pass the actual ad viewer's data for targeting purposes
    user_ip = serializers.IPAddressField(required=False)
    user_ua = serializers.CharField(required=False)

    # Used to specify a specific ad or campaign to show (used for debugging mostly)
    force_ad = serializers.CharField(required=False)  # slug
    force_campaign = serializers.CharField(required=False)  # slug

    def validate_placements(self, placements):
        if not placements:
            raise serializers.ValidationError("At least one placement is required")

        return placements

    def validate_campaign_types(self, campaign_types):
        if campaign_types:
            for campaign_type in campaign_types:
                if campaign_type not in ALL_CAMPAIGN_TYPES:
                    raise serializers.ValidationError("Invalid campaign type")

        return campaign_types

    def validate_publisher(self, publisher_slug):
        # Resolve the publisher slug into the actual Publisher
        if publisher_slug:
            publisher = Publisher.objects.filter(slug=publisher_slug).first()
            if publisher:
                return publisher

        raise serializers.ValidationError("Invalid publisher")


class AdTrackingSerializer(serializers.Serializer):

    """A serializer for data that tracks views and clicks."""

    # Required fields
    advertisement = serializers.SlugField(required=True)
    nonce = serializers.CharField(required=True)
    url = serializers.URLField(required=True)

    # Used to pass the actual ad viewer's data for targeting purposes
    user_ip = serializers.IPAddressField(required=False)
    user_ua = serializers.CharField(required=False)

    def validate_advertisement(self, advertisement_slug):
        # Resolve the slug into the actual ad
        advertisement = Advertisement.objects.filter(slug=advertisement_slug).first()
        if not advertisement:
            raise serializers.ValidationError("Invalid advertisement")

        return advertisement