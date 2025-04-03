from rest_framework import serializers
from app.mainpage.models import Settings

class SettingsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Settings
        fields = ['phone_header', 'date_header', 'date_header', 'insta_url', 'face_book', 'email_footer', 'location',
                  'title_banner', 'description_banner', 'image_banner', 'title_news', 'title_scientific_degrees',
                  'title_additional_professional_education', 'title_courses', 'title_we_suggest_you_watch_it',
                  'title_journal_of_the_islamic_academy', 'title_journals_of_partner_universities', 'title_gallery',
                  'obj_date', 'title_obj', 'description_obj', 'image_obj']