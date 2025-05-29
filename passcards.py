import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard


def main():
    all_passcards = Passcard.objects.all()
    active_passcard = Passcard.objects.filter(is_active=True)

    employee = all_passcards[0]

    print(
        f'employee_name: {employee.owner_name}',
        f'passcode: {employee.passcode}',
        f'created_at: {employee.created_at}',
        f'is_active: {employee.is_active}',
        sep='\n'
    )
    print()

    print('Всего пропусков', len(all_passcards))
    print('Активных пропусков', len(active_passcard))


if __name__ == '__main__':
    main()