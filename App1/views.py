from rest_framework import status
from .models import ClientData
from django.core.mail import EmailMessage
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def add_client_data(request):
    if request.method != 'POST':
        return Response({"success": False, "message": "Method Not Allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    full_name = request.data.get('full_name')
    country = request.data.get('country')
    passport_no = request.data.get('passport_no')
    phone_number = request.data.get('phone_number')
    lost_company = request.data.get('lost_company')
    lose_amount = request.data.get('lose_amount')
    lost_year = request.data.get('lost_year')

    # التحقق من صحة البيانات
    if not all([full_name, country, passport_no, phone_number, lost_company, lose_amount, lost_year]):
        return Response({"success": False, "message": "Missing or invalid data"}, status=status.HTTP_409_CONFLICT)

    # التحقق من عدم وجود العميل مسبقًا
    if ClientData.objects.filter(passport_no=passport_no).exists():
        return Response({"success": False, "message": "Client data already exists"}, status=status.HTTP_409_CONFLICT)

    try:
        # حفظ بيانات العميل
        client_data = ClientData.objects.create(
            full_name=full_name,
            country=country,
            passport_no=passport_no,
            phone_number=phone_number,
            lost_company=lost_company,
            lose_amount=lose_amount,
            lost_year=lost_year
        )

        # إرسال البريد الإلكتروني
        send_client_data_email({
            "full_name": full_name,
            "country": country,
            "passport_no": passport_no,
            "phone_number": phone_number,
            "lost_company": lost_company,
            "lose_amount": lose_amount,
            "lost_year": lost_year
        })

        return Response({"success": True, "message": "Client data added successfully"}, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({"success": False, "message": "Server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def send_client_data_email(client_data):
    try:
        # محتوى البريد بصيغة HTML
        html_content = f"""
        <html>
        <head>
            <style>
                .container {{ font-family: Arial, sans-serif; padding: 20px; }}
                .header {{ background-color: #4CAF50; color: white; text-align: center; padding: 10px; font-size: 24px; }}
                .content {{ padding: 20px; font-size: 18px; }}
                .footer {{ background-color: #f1f1f1; text-align: center; padding: 10px; font-size: 14px; }}
                .button {{ background-color: #008CBA; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px; display: inline-block; margin-top: 20px; }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">مرحبا بك في موقعنا!</div>
                <div class="content">
                    <p><strong>الاسم الكامل:</strong> {client_data['full_name']}</p>
                    <p><strong>الدولة:</strong> {client_data['country']}</p>
                    <p><strong>رقم جواز السفر:</strong> {client_data['passport_no']}</p>
                    <p><strong>رقم الهاتف:</strong> {client_data['phone_number']}</p>
                    <p><strong>الشركة المتضررة:</strong> {client_data['lost_company']}</p>
                    <p><strong>المبلغ المفقود:</strong> ${client_data['lose_amount']}</p>
                    <p><strong>سنة الخسارة:</strong> {client_data['lost_year']}</p>
                    <a href="https://yourwebsite.com" class="button">استكشف الآن</a>
                </div>
                <div class="footer">© 2025 جميع الحقوق محفوظة</div>
            </div>
        </body>
        </html>
        """

        email = EmailMessage(
            "Test Email",
            html_content,
            settings.EMAIL_HOST_USER,
            ["alalikaram985@gmail.com"],

        )
        email.content_subtype = "html"
        email.send()

    except Exception as e:
        print(f"Email sending failed: {str(e)}") 

@api_view(['GET'])
def get_case_stats(request):
    if request.method != 'GET':
        return Response({
            "success": False,
            "message": "Method Not Allowed"
        }, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    try:
        # إجمالي عدد القضايا
        total_cases = ClientData.objects.count()
        
        unique_countries = ClientData.objects.values('country').distinct().count()
        
        return Response({
            "total_cases": total_cases,
            "unique_countries": unique_countries
        }, status=status.HTTP_200_OK)
    
    except Exception as e:
        return Response({
            "success": False,
            "message": "Server error"
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)