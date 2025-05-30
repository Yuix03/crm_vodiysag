import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "crm_vodiysag.settings")
django.setup()

from amocrm.v2 import tokens, Contact as AmoContact
from contacts.models import Contact


tokens.default_token_manager(
    client_id="47819846-de4c-4a4a-82ba-6e3e9e3ade61",
    client_secret="8xuIxU6u6JDJ4gpFj8kWu5LiMAEEOUvCgRAv4nXL8vkLICchhXabgUaaPWQCKpHW",
    subdomain="vodiysag",
    redirect_url="https://ya.ru",
    storage=tokens.FileTokensStorage(),
)

contacts = AmoContact.objects.all()

for contact in contacts:
    full_contact = AmoContact.objects.get(contact.id)
    data = full_contact._data

    name = data.get('name') or ''
    phone_number = None

    custom_fields = data.get('custom_fields_values')
    if isinstance(custom_fields, list):
        for field in custom_fields:
            if field.get('field_code') == 'PHONE':
                for value in field.get('values', []):
                    phone_number = value.get('value')
                    break
            if phone_number:
                break

    if phone_number:
        Contact.objects.update_or_create(
            phone=phone_number,
            defaults={'name': name}
        )
