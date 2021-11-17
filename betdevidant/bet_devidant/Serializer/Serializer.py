from rest_framework import serializers
from betdevidant.bet_devidant.models import Match


class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = ('team1',
                  'team2',
                  'odd1',
                  'odd2')