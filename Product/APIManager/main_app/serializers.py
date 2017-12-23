from rest_framework import serializers

MINIMUM_AGE = 0
MAXIMUM_AGE = 130

class RatingSerializer(serializers.Serializer):
    movie_id = serializers.IntegerField(min_value=0)
    rating = serializers.IntegerField(min_value=1, max_value=5, required=False)
    watched = serializers.BooleanField(required=False)

class UserSerializer(serializers.Serializer):
    age = serializers.IntegerField(min_value=MINIMUM_AGE, max_value=MAXIMUM_AGE)
    gender = serializers.CharField(allow_blank=True)
    occupation = serializers.CharField(allow_blank=True, max_length=30)

    def validate_gender(self, value):
        if value in ("Male", "Female", "Other" ,""):
            if value == "":
                return "Unknown"
            else:
                return value
        else:
            raise serializers.ValidationError("Gender must be Male, Female, Other or left blank")
