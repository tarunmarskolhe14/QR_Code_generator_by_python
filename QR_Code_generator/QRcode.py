import qrcode

# Taking UPI ID As an input
upi_id = input("Enter your UPI ID = ")

# UPI payment URL format
# upi://pay?pa=UPI_ID&pn=NAME&am=Amount&cu=CURRENCY&tn=MESSAGE

# Defining the payment URL based on the UPI ID and the payment app
# You can modify these URLs based on the payment apps you want to support

phonepe_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
paytm_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
google_pay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

# Create QR Codes for each payment URL
def generate_qr(data, filename):
    qr = qrcode.make(data)
    qr.save(filename)
    print(f"QR Code saved as {filename}")

generate_qr(phonepe_url, "phonepe_qr.png")
generate_qr(paytm_url, "paytm_qr.png")
generate_qr(google_pay_url, "google_pay_qr.png")